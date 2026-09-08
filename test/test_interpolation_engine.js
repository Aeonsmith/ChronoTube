const assert = require('assert');

class DynamicPropertyInterpolator {
  static interpolateNumeric(v0, v1, alpha, options = {}) {
    const strategy = options.strategy || 'LINEAR';
    const t = Math.max(0, Math.min(1, alpha));
    if (v0 === v1) return v0;
    let computed;
    switch (strategy) {
      case 'STEP_HOLD':
        computed = v0;
        break;
      case 'STEP_NEXT':
        computed = t >= 1.0 ? v1 : v0;
        break;
      case 'LOGARITHMIC_GROWTH':
        if (v0 > 0 && v1 > 0) {
          const log0 = Math.log(v0);
          const log1 = Math.log(v1);
          computed = Math.exp(log0 + t * (log1 - log0));
        } else {
          computed = v0 + t * (v1 - v0);
        }
        break;
      case 'POLYNOMIAL_ACCELERATION':
        computed = v0 + Math.pow(t, 2) * (v1 - v0);
        break;
      case 'SIGMOID_S_CURVE':
        const k = options.sigmoidSteepness ?? 10;
        const sigmoidAlpha = 1 / (1 + Math.exp(-k * (t - 0.5)));
        const s0 = 1 / (1 + Math.exp(-k * (-0.5)));
        const s1 = 1 / (1 + Math.exp(-k * (0.5)));
        const normalizedSigmoid = (sigmoidAlpha - s0) / (s1 - s0);
        computed = v0 + normalizedSigmoid * (v1 - v0);
        break;
      case 'DISCRETE_BOUNDED':
        const raw = v0 + t * (v1 - v0);
        const min = options.minValue ?? -Infinity;
        const max = options.maxValue ?? Infinity;
        computed = Math.max(min, Math.min(max, raw));
        break;
      case 'LINEAR':
      default:
        computed = v0 + t * (v1 - v0);
        break;
    }
    if (options.precision !== undefined) {
      const multiplier = Math.pow(10, options.precision);
      return Math.round(computed * multiplier) / multiplier;
    }
    return Number.isInteger(v0) && Number.isInteger(v1)
      ? Math.round(computed)
      : Number(computed.toFixed(4));
  }

  static interpolateCategorical(val0, val1, alpha, options = {}) {
    const strategy = options.strategy || 'HOLD_PREVIOUS';
    const t = Math.max(0, Math.min(1, alpha));
    const threshold = options.threshold ?? 0.5;
    switch (strategy) {
      case 'SWITCH_AT_MIDPOINT':
        return t >= 0.5 ? val1 : val0;
      case 'SWITCH_AT_THRESHOLD':
        return t >= threshold ? val1 : val0;
      case 'ARRAY_SET_UNION':
        if (Array.isArray(val0) && Array.isArray(val1)) {
          return Array.from(new Set([...val0, ...val1]));
        }
        return t >= 0.5 ? val1 : val0;
      case 'ARRAY_SET_INTERSECTION':
        if (Array.isArray(val0) && Array.isArray(val1)) {
          const setB = new Set(val1);
          return val0.filter(item => setB.has(item));
        }
        return t >= 0.5 ? val1 : val0;
      case 'ARRAY_WEIGHTED_SET':
        if (Array.isArray(val0) && Array.isArray(val1)) {
          const limits = options.weightThresholds || { low: 0.3, high: 0.7 };
          if (t < limits.low) return val0;
          if (t > limits.high) return val1;
          return Array.from(new Set([...val0, ...val1]));
        }
        return t >= 0.5 ? val1 : val0;
      case 'NESTED_OBJECT_MERGE':
        if (typeof val0 === 'object' && val0 !== null && typeof val1 === 'object' && val1 !== null && !Array.isArray(val0)) {
          const merged = { ...val0 };
          for (const key of Object.keys(val1)) {
            merged[key] = t >= threshold ? val1[key] : (val0[key] ?? val1[key]);
          }
          return merged;
        }
        return t >= threshold ? val1 : val0;
      case 'HOLD_PREVIOUS':
      default:
        return val0;
    }
  }

  static resolveRecord(state0, state1, alpha, fieldRules = {}) {
    const result = {};
    const allKeys = new Set([...Object.keys(state0), ...Object.keys(state1)]);
    for (const key of allKeys) {
      const v0 = state0[key];
      const v1 = state1[key];
      const rule = fieldRules[key];
      if (v0 === undefined) { result[key] = alpha >= 0.5 ? v1 : undefined; continue; }
      if (v1 === undefined) { result[key] = alpha < 0.5 ? v0 : undefined; continue; }
      if (rule?.type === 'numeric' || (typeof v0 === 'number' && typeof v1 === 'number')) {
        result[key] = this.interpolateNumeric(v0, v1, alpha, rule?.numericOptions);
      } else if (typeof v0 === 'boolean' && typeof v1 === 'boolean') {
        result[key] = alpha >= 0.5 ? v1 : v0;
      } else {
        result[key] = this.interpolateCategorical(v0, v1, alpha, rule?.categoricalOptions);
      }
    }
    return result;
  }
}

class ChronoTubeResolutionEngine {
  static getEpochForTimestamp(targetIso) {
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

  static resolveStateAtTimestamp(entityId, snapshots, targetIso, customRules) {
    if (!snapshots || snapshots.length === 0) throw new Error(`[ChronoTube] Cannot resolve state for '${entityId}': Snapshot collection is empty.`);
    const targetMs = new Date(targetIso).getTime();
    if (isNaN(targetMs)) throw new Error(`[ChronoTube] Invalid target timestamp: ${targetIso}`);
    const timeline = [...snapshots].sort((a, b) => new Date(a.timestamp).getTime() - new Date(b.timestamp).getTime());
    const epochConfig = this.getEpochForTimestamp(targetIso);
    const activeRules = customRules || epochConfig.rules;
    const firstSnap = timeline[0];
    const lastSnap = timeline[timeline.length - 1];
    const firstMs = new Date(firstSnap.timestamp).getTime();
    const lastMs = new Date(lastSnap.timestamp).getTime();

    if (targetMs <= firstMs) {
      return {
        entityId, targetTimestamp: targetIso, isInterpolated: false, activeEpoch: epochConfig,
        boundingSnapshots: { previous: { timestamp: firstSnap.timestamp, deltaMs: firstMs - targetMs } },
        properties: { ...firstSnap.properties },
        embeddingVector: firstSnap.embeddingVector ? [...firstSnap.embeddingVector] : undefined
      };
    }
    if (targetMs >= lastMs) {
      return {
        entityId, targetTimestamp: targetIso, isInterpolated: false, activeEpoch: epochConfig,
        boundingSnapshots: { previous: { timestamp: lastSnap.timestamp, deltaMs: targetMs - lastMs } },
        properties: { ...lastSnap.properties },
        embeddingVector: lastSnap.embeddingVector ? [...lastSnap.embeddingVector] : undefined
      };
    }

    let low = 0, high = timeline.length - 1, leftIdx = 0;
    while (low <= high) {
      const mid = Math.floor((low + high) / 2);
      const midMs = new Date(timeline[mid].timestamp).getTime();
      if (midMs === targetMs) {
        return {
          entityId, targetTimestamp: targetIso, isInterpolated: false, activeEpoch: epochConfig,
          boundingSnapshots: { previous: { timestamp: timeline[mid].timestamp, deltaMs: 0 } },
          properties: { ...timeline[mid].properties },
          embeddingVector: timeline[mid].embeddingVector ? [...timeline[mid].embeddingVector] : undefined
        };
      } else if (midMs < targetMs) {
        leftIdx = mid; low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    const snap0 = timeline[leftIdx];
    const snap1 = timeline[leftIdx + 1];
    const t0 = new Date(snap0.timestamp).getTime();
    const t1 = new Date(snap1.timestamp).getTime();
    const alpha = (targetMs - t0) / (t1 - t0);

    const resolvedProps = DynamicPropertyInterpolator.resolveRecord(snap0.properties, snap1.properties, alpha, activeRules);
    let resolvedVec;
    if (snap0.embeddingVector && snap1.embeddingVector) {
      resolvedVec = this.interpolateVectorSlerp(snap0.embeddingVector, snap1.embeddingVector, alpha);
    }

    return {
      entityId, targetTimestamp: targetIso, isInterpolated: true, activeEpoch: epochConfig,
      boundingSnapshots: { previous: { timestamp: snap0.timestamp, deltaMs: targetMs - t0 }, next: { timestamp: snap1.timestamp, deltaMs: t1 - targetMs } },
      progressAlpha: Number(alpha.toFixed(4)),
      properties: resolvedProps,
      embeddingVector: resolvedVec
    };
  }

  static interpolateVectorSlerp(vecA, vecB, alpha) {
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

let passed = 0, failed = 0;

function it(name, fn) {
  try {
    fn();
    console.log('  ✔ ' + name);
    passed++;
  } catch (err) {
    console.error('  ✖ ' + name + ' -> ' + err.message);
    failed++;
  }
}

console.log('=== Running ChronoTube Repository Verification Test Suite ===\n');

console.log('Suite 1: Numeric Strategies');
it('LINEAR: Interpolates midway between values', () => {
  const res = DynamicPropertyInterpolator.interpolateNumeric(100, 200, 0.5, { strategy: 'LINEAR' });
  assert.equal(res, 150);
});

it('LOGARITHMIC_GROWTH: Models natural viral scale attenuation', () => {
  const res = DynamicPropertyInterpolator.interpolateNumeric(10000, 1000000, 0.5, { strategy: 'LOGARITHMIC_GROWTH' });
  assert.equal(res, 100000);
});

it('POLYNOMIAL_ACCELERATION: Computes quadratic acceleration curve', () => {
  const res = DynamicPropertyInterpolator.interpolateNumeric(0, 1000, 0.5, { strategy: 'POLYNOMIAL_ACCELERATION' });
  assert.equal(res, 250);
});

it('SIGMOID_S_CURVE: S-Curve rapid inflection and saturation', () => {
  const mid = DynamicPropertyInterpolator.interpolateNumeric(0, 1000, 0.5, { strategy: 'SIGMOID_S_CURVE', sigmoidSteepness: 10 });
  const early = DynamicPropertyInterpolator.interpolateNumeric(0, 1000, 0.2, { strategy: 'SIGMOID_S_CURVE', sigmoidSteepness: 10 });
  const late = DynamicPropertyInterpolator.interpolateNumeric(0, 1000, 0.8, { strategy: 'SIGMOID_S_CURVE', sigmoidSteepness: 10 });
  assert.equal(mid, 500);
  assert.ok(early < 100);
  assert.ok(late > 900);
});

it('DISCRETE_BOUNDED: Clamps to min/max and precision limits', () => {
  const res = DynamicPropertyInterpolator.interpolateNumeric(4.8, 5.2, 0.75, { strategy: 'DISCRETE_BOUNDED', minValue: 1.0, maxValue: 5.0, precision: 2 });
  assert.equal(res, 5.0);
});

it('Boundary Clamping: Keeps alpha in [0, 1]', () => {
  assert.equal(DynamicPropertyInterpolator.interpolateNumeric(10, 20, -0.5), 10);
  assert.equal(DynamicPropertyInterpolator.interpolateNumeric(10, 20, 1.5), 20);
});

console.log('\nSuite 2: Categorical & Structural Strategies');
it('HOLD_PREVIOUS: Preserves initial state', () => {
  assert.equal(DynamicPropertyInterpolator.interpolateCategorical('Initial', 'Next', 0.99, { strategy: 'HOLD_PREVIOUS' }), 'Initial');
});

it('SWITCH_AT_THRESHOLD: Switches across configurable threshold', () => {
  assert.equal(DynamicPropertyInterpolator.interpolateCategorical('A', 'B', 0.69, { strategy: 'SWITCH_AT_THRESHOLD', threshold: 0.7 }), 'A');
  assert.equal(DynamicPropertyInterpolator.interpolateCategorical('A', 'B', 0.71, { strategy: 'SWITCH_AT_THRESHOLD', threshold: 0.7 }), 'B');
});

it('ARRAY_SET_UNION: Merges distinct set elements', () => {
  const union = DynamicPropertyInterpolator.interpolateCategorical(['a', 'b'], ['b', 'c'], 0.5, { strategy: 'ARRAY_SET_UNION' });
  assert.deepEqual(union, ['a', 'b', 'c']);
});

it('ARRAY_SET_INTERSECTION: Keeps only common elements', () => {
  const inter = DynamicPropertyInterpolator.interpolateCategorical(['a', 'b'], ['b', 'c'], 0.5, { strategy: 'ARRAY_SET_INTERSECTION' });
  assert.deepEqual(inter, ['b']);
});

it('NESTED_OBJECT_MERGE: Recursively merges object properties', () => {
  const merged = DynamicPropertyInterpolator.interpolateCategorical({ x: 1, y: 2 }, { y: 20, z: 30 }, 0.6, { strategy: 'NESTED_OBJECT_MERGE', threshold: 0.5 });
  assert.deepEqual(merged, { x: 1, y: 20, z: 30 });
});

console.log('\nSuite 3: Orchestration & End-to-End Resolution');
const snapshots = [
  { timestamp: '2006-04-23T20:30:00Z', properties: { title: 'Me at the zoo', view_count: 100, star_rating: 5.0 }, embeddingVector: [1.0, 0.0, 0.0] },
  { timestamp: '2020-04-23T20:30:00Z', properties: { title: 'Me at the zoo (15th Anniv)', view_count: 90000000, star_rating: 4.88 }, embeddingVector: [0.0, 1.0, 0.0] }
];

it('Exact Match: Returns exact properties without interpolation', () => {
  const res = ChronoTubeResolutionEngine.resolveStateAtTimestamp('video:zoo', snapshots, '2006-04-23T20:30:00Z');
  assert.equal(res.isInterpolated, false);
  assert.equal(res.properties.view_count, 100);
});

it('Boundary Underflow: Handles timestamps prior to first capture', () => {
  const res = ChronoTubeResolutionEngine.resolveStateAtTimestamp('video:zoo', snapshots, '2005-01-01T00:00:00Z');
  assert.equal(res.isInterpolated, false);
  assert.equal(res.properties.view_count, 100);
});

it('Boundary Overflow: Handles timestamps after last capture', () => {
  const res = ChronoTubeResolutionEngine.resolveStateAtTimestamp('video:zoo', snapshots, '2026-01-01T00:00:00Z');
  assert.equal(res.isInterpolated, false);
  assert.equal(res.properties.view_count, 90000000);
});

it('Gap Resolution: Interpolates state and normalizes vector magnitude to 1.0', () => {
  const res = ChronoTubeResolutionEngine.resolveStateAtTimestamp('video:zoo', snapshots, '2013-04-23T20:30:00Z');
  assert.equal(res.isInterpolated, true);
  assert.equal(res.activeEpoch.epochId, 'ERA_WATCH_TIME');
  assert.ok(res.properties.view_count > 100 && res.properties.view_count < 90000000);
  const mag = Math.sqrt(res.embeddingVector.reduce((s, v) => s + v * v, 0));
  assert.ok(Math.abs(mag - 1.0) < 1e-4);
});

it('Error Handling: Throws on empty snapshots or invalid timestamp', () => {
  assert.throws(() => ChronoTubeResolutionEngine.resolveStateAtTimestamp('video:err', [], '2020-01-01T00:00:00Z'), /empty/i);
  assert.throws(() => ChronoTubeResolutionEngine.resolveStateAtTimestamp('video:err', snapshots, 'INVALID-DATE'), /invalid/i);
});

console.log(`\n=======================================================`);
console.log(`Test Results: ${passed} passed, ${failed} failed`);
console.log(`Status: ${failed === 0 ? 'SUCCESS' : 'FAILURE'}`);
console.log(`=======================================================`);
if (failed > 0) process.exit(1);