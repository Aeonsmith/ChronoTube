export type NumericStrategy =
  | 'LINEAR'
  | 'LOGARITHMIC_GROWTH'
  | 'POLYNOMIAL_ACCELERATION'
  | 'SIGMOID_S_CURVE'
  | 'STEP_HOLD'
  | 'STEP_NEXT'
  | 'DISCRETE_BOUNDED';

export type CategoricalStrategy =
  | 'HOLD_PREVIOUS'
  | 'SWITCH_AT_MIDPOINT'
  | 'SWITCH_AT_THRESHOLD'
  | 'ARRAY_SET_UNION'
  | 'ARRAY_SET_INTERSECTION'
  | 'ARRAY_WEIGHTED_SET'
  | 'NESTED_OBJECT_MERGE';

export interface NumericInterpolationOptions {
  strategy?: NumericStrategy;
  minValue?: number;
  maxValue?: number;
  precision?: number;
  sigmoidSteepness?: number;
}

export interface CategoricalInterpolationOptions {
  strategy?: CategoricalStrategy;
  threshold?: number;
  weightThresholds?: { low: number; high: number };
}

export interface PropertyFieldRule {
  type: 'numeric' | 'categorical' | 'vector';
  numericOptions?: NumericInterpolationOptions;
  categoricalOptions?: CategoricalInterpolationOptions;
}

export class DynamicPropertyInterpolator {
  public static interpolateNumeric(
    v0: number,
    v1: number,
    alpha: number,
    options: NumericInterpolationOptions = {}
  ): number {
    const strategy = options.strategy || 'LINEAR';
    const t = Math.max(0, Math.min(1, alpha));
    if (v0 === v1) return v0;
    let computed: number;

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

  public static interpolateCategorical<T = any>(
    val0: T,
    val1: T,
    alpha: number,
    options: CategoricalInterpolationOptions = {}
  ): T {
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
          return Array.from(new Set([...val0, ...val1])) as unknown as T;
        }
        return t >= 0.5 ? val1 : val0;
      case 'ARRAY_SET_INTERSECTION':
        if (Array.isArray(val0) && Array.isArray(val1)) {
          const setB = new Set(val1);
          return val0.filter((item) => setB.has(item)) as unknown as T;
        }
        return t >= 0.5 ? val1 : val0;
      case 'ARRAY_WEIGHTED_SET':
        if (Array.isArray(val0) && Array.isArray(val1)) {
          const limits = options.weightThresholds || { low: 0.3, high: 0.7 };
          if (t < limits.low) return val0;
          if (t > limits.high) return val1;
          return Array.from(new Set([...val0, ...val1])) as unknown as T;
        }
        return t >= 0.5 ? val1 : val0;
      case 'NESTED_OBJECT_MERGE':
        if (
          typeof val0 === 'object' &&
          val0 !== null &&
          typeof val1 === 'object' &&
          val1 !== null &&
          !Array.isArray(val0)
        ) {
          const merged: Record<string, any> = { ...val0 };
          for (const key of Object.keys(val1)) {
            merged[key] = t >= threshold ? (val1 as any)[key] : (val0 as any)[key] ?? (val1 as any)[key];
          }
          return merged as unknown as T;
        }
        return t >= threshold ? val1 : val0;
      case 'HOLD_PREVIOUS':
      default:
        return val0;
    }
  }

  public static resolveRecord(
    state0: Record<string, any>,
    state1: Record<string, any>,
    alpha: number,
    fieldRules: Record<string, PropertyFieldRule>
  ): Record<string, any> {
    const result: Record<string, any> = {};
    const allKeys = new Set([...Object.keys(state0), ...Object.keys(state1)]);

    for (const key of allKeys) {
      const v0 = state0[key];
      const v1 = state1[key];
      const rule = fieldRules[key];

      if (v0 === undefined) {
        result[key] = alpha >= 0.5 ? v1 : undefined;
        continue;
      }
      if (v1 === undefined) {
        result[key] = alpha < 0.5 ? v0 : undefined;
        continue;
      }

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