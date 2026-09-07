import {
  DynamicPropertyInterpolator,
  PropertyFieldRule
} from './interpolation_engine';

export interface TemporalSnapshot<T = Record<string, any>> {
  timestamp: string;
  properties: T;
  embeddingVector?: number[];
}

export interface AlgorithmicEpochConfig {
  epochId: string;
  name: string;
  metricPriority: 'STAR_RATINGS' | 'RAW_VIEWS' | 'WATCH_TIME' | 'RETENTION_CTR' | 'MULTIMODAL_VECTOR';
  rules: Record<string, PropertyFieldRule>;
}

export interface ResolvedTemporalState<T = Record<string, any>> {
  entityId: string;
  targetTimestamp: string;
  isInterpolated: boolean;
  activeEpoch: {
    epochId: string;
    name: string;
    metricPriority: string;
  };
  boundingSnapshots: {
    previous: { timestamp: string; deltaMs: number };
    next?: { timestamp: string; deltaMs: number };
  };
  progressAlpha?: number;
  properties: T;
  embeddingVector?: number[];
}

export class ChronoTubeResolutionEngine {
  public static getEpochForTimestamp(targetIso: string): AlgorithmicEpochConfig {
    const year = new Date(targetIso).getUTCFullYear();

    if (year <= 2009) {
      return {
        epochId: 'ERA_5STAR_VIEWS',
        name: 'Early Web 1.0 / Flash / 5-Star Ratings Era',
        metricPriority: 'STAR_RATINGS',
        rules: {
          view_count: { type: 'numeric', numericOptions: { strategy: 'LOGARITHMIC_GROWTH' } },
          star_rating: { type: 'numeric', numericOptions: { strategy: 'DISCRETE_BOUNDED', minValue: 1.0, maxValue: 5.0, precision: 2 } },
          title: { type: 'categorical', categoricalOptions: { strategy: 'HOLD_PREVIOUS' } },
          tags: { type: 'categorical', categoricalOptions: { strategy: 'ARRAY_SET_UNION' } }
        }
      };
    } else if (year <= 2015) {
      return {
        epochId: 'ERA_WATCH_TIME',
        name: 'Watch Time & Daily Gaming / Vlogger Boom',
        metricPriority: 'WATCH_TIME',
        rules: {
          view_count: { type: 'numeric', numericOptions: { strategy: 'SIGMOID_S_CURVE', sigmoidSteepness: 8 } },
          likes: { type: 'numeric', numericOptions: { strategy: 'LINEAR' } },
          dislikes: { type: 'numeric', numericOptions: { strategy: 'LINEAR' } },
          tags: { type: 'categorical', categoricalOptions: { strategy: 'ARRAY_WEIGHTED_SET' } }
        }
      };
    } else if (year <= 2021) {
      return {
        epochId: 'ERA_RETENTION_CTR',
        name: 'Algorithmic Optimization & Public Dislikes Era',
        metricPriority: 'RETENTION_CTR',
        rules: {
          view_count: { type: 'numeric', numericOptions: { strategy: 'LOGARITHMIC_GROWTH' } },
          likes: { type: 'numeric', numericOptions: { strategy: 'LINEAR' } },
          dislikes: { type: 'numeric', numericOptions: { strategy: 'LINEAR' } }
        }
      };
    } else {
      return {
        epochId: 'ERA_NEURAL_SHORTS',
        name: 'Neural Recommendation & Shorts / Multimodal Era',
        metricPriority: 'MULTIMODAL_VECTOR',
        rules: {
          view_count: { type: 'numeric', numericOptions: { strategy: 'LOGARITHMIC_GROWTH' } },
          likes: { type: 'numeric', numericOptions: { strategy: 'LINEAR' } }
        }
      };
    }
  }

  public static resolveStateAtTimestamp<T extends Record<string, any>>(
    entityId: string,
    snapshots: TemporalSnapshot<T>[],
    targetIso: string,
    customRules?: Record<string, PropertyFieldRule>
  ): ResolvedTemporalState<T> {
    if (!snapshots || snapshots.length === 0) {
      throw new Error(`[ChronoTube] Cannot resolve state for '${entityId}': Snapshot collection is empty.`);
    }

    const targetMs = new Date(targetIso).getTime();
    if (isNaN(targetMs)) {
      throw new Error(`[ChronoTube] Invalid target timestamp: ${targetIso}`);
    }

    const timeline = [...snapshots].sort(
      (a, b) => new Date(a.timestamp).getTime() - new Date(b.timestamp).getTime()
    );

    const epochConfig = this.getEpochForTimestamp(targetIso);
    const activeRules = customRules || epochConfig.rules;

    const firstSnap = timeline[0];
    const lastSnap = timeline[timeline.length - 1];
    const firstMs = new Date(firstSnap.timestamp).getTime();
    const lastMs = new Date(lastSnap.timestamp).getTime();

    if (targetMs <= firstMs) {
      return {
        entityId,
        targetTimestamp: targetIso,
        isInterpolated: false,
        activeEpoch: {
          epochId: epochConfig.epochId,
          name: epochConfig.name,
          metricPriority: epochConfig.metricPriority
        },
        boundingSnapshots: { previous: { timestamp: firstSnap.timestamp, deltaMs: firstMs - targetMs } },
        properties: { ...firstSnap.properties },
        embeddingVector: firstSnap.embeddingVector ? [...firstSnap.embeddingVector] : undefined
      };
    }

    if (targetMs >= lastMs) {
      return {
        entityId,
        targetTimestamp: targetIso,
        isInterpolated: false,
        activeEpoch: {
          epochId: epochConfig.epochId,
          name: epochConfig.name,
          metricPriority: epochConfig.metricPriority
        },
        boundingSnapshots: { previous: { timestamp: lastSnap.timestamp, deltaMs: targetMs - lastMs } },
        properties: { ...lastSnap.properties },
        embeddingVector: lastSnap.embeddingVector ? [...lastSnap.embeddingVector] : undefined
      };
    }

    let low = 0;
    let high = timeline.length - 1;
    let leftIdx = 0;

    while (low <= high) {
      const mid = Math.floor((low + high) / 2);
      const midMs = new Date(timeline[mid].timestamp).getTime();

      if (midMs === targetMs) {
        const match = timeline[mid];
        return {
          entityId,
          targetTimestamp: targetIso,
          isInterpolated: false,
          activeEpoch: {
            epochId: epochConfig.epochId,
            name: epochConfig.name,
            metricPriority: epochConfig.metricPriority
          },
          boundingSnapshots: { previous: { timestamp: match.timestamp, deltaMs: 0 } },
          properties: { ...match.properties },
          embeddingVector: match.embeddingVector ? [...match.embeddingVector] : undefined
        };
      } else if (midMs < targetMs) {
        leftIdx = mid;
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    const snap0 = timeline[leftIdx];
    const snap1 = timeline[leftIdx + 1];
    const t0 = new Date(snap0.timestamp).getTime();
    const t1 = new Date(snap1.timestamp).getTime();
    const alpha = (targetMs - t0) / (t1 - t0);

    const resolvedProps = DynamicPropertyInterpolator.resolveRecord(
      snap0.properties,
      snap1.properties,
      alpha,
      activeRules
    ) as T;

    let resolvedVec: number[] | undefined;
    if (snap0.embeddingVector && snap1.embeddingVector) {
      resolvedVec = this.interpolateVectorSlerp(snap0.embeddingVector, snap1.embeddingVector, alpha);
    }

    return {
      entityId,
      targetTimestamp: targetIso,
      isInterpolated: true,
      activeEpoch: {
        epochId: epochConfig.epochId,
        name: epochConfig.name,
        metricPriority: epochConfig.metricPriority
      },
      boundingSnapshots: {
        previous: { timestamp: snap0.timestamp, deltaMs: targetMs - t0 },
        next: { timestamp: snap1.timestamp, deltaMs: t1 - targetMs }
      },
      progressAlpha: Number(alpha.toFixed(4)),
      properties: resolvedProps,
      embeddingVector: resolvedVec
    };
  }

  private static interpolateVectorSlerp(vecA: number[], vecB: number[], alpha: number): number[] {
    if (vecA.length !== vecB.length) return vecA;

    let dot = 0;
    for (let i = 0; i < vecA.length; i++) dot += vecA[i] * vecB[i];
    dot = Math.max(-1, Math.min(1, dot));

    const theta = Math.acos(dot) * alpha;
    const relVec = new Array(vecA.length);
    for (let i = 0; i < vecA.length; i++) relVec[i] = vecB[i] - vecA[i] * dot;

    let relNorm = 0;
    for (let i = 0; i < relVec.length; i++) relNorm += relVec[i] * relVec[i];
    relNorm = Math.sqrt(relNorm);

    if (relNorm > 0) {
      for (let i = 0; i < relVec.length; i++) relVec[i] /= relNorm;
    }

    const out = new Array(vecA.length);
    for (let i = 0; i < vecA.length; i++) {
      out[i] = vecA[i] * Math.cos(theta) + relVec[i] * Math.sin(theta);
    }
    return out;
  }
}