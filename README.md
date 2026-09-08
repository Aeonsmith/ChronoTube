# ðŸª ChronoTube Engine: Multi-Dimensional YouTube Time-Machine & Digital Archaeology OS

[![ChronoTube Engine CI](https://github.com/Aeonsmith/ChronoTube/actions/workflows/ci.yml/badge.svg)](https://github.com/Aeonsmith/ChronoTube/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.x-blue.svg)](https://www.typescriptlang.org/)
[![Node.js](https://img.shields.io/badge/Node.js-18%2B-green.svg)](https://nodejs.org/)

The **ChronoTube Engine** is an interactive, spatial, and semantic simulation operating system for web archaeology, temporal graph querying, and counterfactual internet culture exploration across YouTube history (2005â€“2026+).

---

## ðŸ›ï¸ 1. System Architecture

The ChronoTube Engine uses an event-sourced temporal property graph combined with interval-validity models and continuous numerical/categorical interpolation.

```
+â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€+
|                                PRESENTATION LAYER                                 |
|                                                                                   |
|  [ ðŸª WebGL 3D Galaxy ]    [ ðŸ“œ Multi-Scale Scrubber ]   [ ðŸ•¸ï¸ Force Graph View ]   |
|  [ ðŸ“º Retro UI Shells ]    [ âš¡ WASM Ruffle / Codecs ]    [ ðŸ§ª Time Sandbox IDE ]   |
+â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–²â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€+
                                         â”‚ JSON-RPC / GraphQL-Temporal
+â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€+
|                              CHRONOTUBE CORE ENGINE                               |
|                                                                                   |
|  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”   â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” |
|  |       Temporal State Router     |   |      Algorithmic Epoch Simulator       | |
|  | - Snapshot delta interpolation  |   | - 2005â€“2009: 5-Star / Direct Views     | |
|  | - Memento datetime resolver     |   | - 2010â€“2015: Watch-Time Accumulators   | |
|  | - Dynamic skin & layout binding |   | - 2016â€“2021: Retention & Dislikes CTR  | |
|  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–²â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜   | - 2022â€“2026+: Neural Multimodal Vectors| |
|                   â”‚                    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–²â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ |
|  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” |
|  |                     Unified Temporal Execution Engine                        | |
|  | - Traversal planning across time branches   - Spherical Vector Slerp Engine  | |
|  | - Graph entity reconstruction               - Cross-Platform Identity Graph  | |
|  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–²â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ |
+â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€+
                                         â”‚ Internal Storage Interface
+â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€+
|                               PERSISTENCE & GRAPH LAYER                           |
|                                                                                   |
|  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” |
|  |  Temporal Property Graph DB  |  | Vector Semantic DB   |  | Metadata Index   | |
|  |  (Nodes/Edges with [t_s,t_e])|  | (HNSW 1536-dim per t)|  | (RocksDB / CDX)  | |
|  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ |
+â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–²â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€+
                                         â”‚ Ingestion & Normalization Pipeline
+â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€+
|                              INGESTION & ARCHIVE LAYER                            |
|                                                                                   |
|  [ Wayback CDX API ]    [ TubeUp / IA S3 ]    [ Google+ WARC Dumps ]              |
|  [ Filmot Subtitle DB ] [ Archivarix Echo ]   [ Live Snapshot Fallbacks ]         |
+â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€+
```

---

## ðŸ§® 2. Interpolation Strategy Matrix

When querying between discontinuous snapshots (such as archive gaps in 2023), the engine applies domain-specific mathematical functions:

| Strategy Name | Category | Mathematical Function | Best Use Case |
| :--- | :--- | :--- | :--- |
| `LINEAR` | Numeric | $v(t) = v_0 + t(v_1 - v_0)$ | Steady metrics (Likes, Subscriptions) |
| `LOGARITHMIC_GROWTH` | Numeric | $v(t) = \exp(\ln v_0 + t(\ln v_1 - \ln v_0))$ | Views post-viral decay |
| `POLYNOMIAL_ACCELERATION` | Numeric | $v(t) = v_0 + t^2(v_1 - v_0)$ | Viral liftoff curves |
| `SIGMOID_S_CURVE` | Numeric | $v(t) = v_0 + \sigma(k(t - 0.5))(v_1 - v_0)$ | Algorithmic explosion to saturation |
| `DISCRETE_BOUNDED` | Numeric | $\text{clamp}(\text{round}(v(t), p), \text{min}, \text{max})$ | Star ratings ($1.00 - 5.00$) |
| `HOLD_PREVIOUS` | Categorical | $S(t) = S_0$ | Titles, Upload IDs |
| `SWITCH_AT_THRESHOLD` | Categorical | $S(t) = t \ge \theta ? S_1 : S_0$ | UI Re-designs, Policy switches |
| `ARRAY_SET_UNION` | Structural | $A(t) = A_0 \cup A_1$ | Metadata tags, Category markers |
| `NESTED_OBJECT_MERGE` | Structural | Recursive property override | Complex component configs |
| `SPHERICAL_SLERP` | Vector | $\frac{\sin((1-t)\theta)}{\sin\theta}\vec{v_0} + \frac{\sin(t\theta)}{\sin\theta}\vec{v_1}$ | Semantic embeddings ($\|\vec{v}\| = 1$) |

---

## ðŸš€ 3. Installation & Quick Start

### Prerequisites
* **Node.js**: `v18.0.0` or higher
* **npm** or **pnpm**

```bash
# 1. Clone repository
git clone https://github.com/chronotube/engine.git
cd engine

# 2. Install dependencies
npm install

# 3. Seed historical metadata and archive indices
npm run seed -- --sources=wayback,archive_team,filmot

# 4. Start the interactive server & 3D Galaxy Engine
npm run dev
```

---

## ðŸ’» 4. Usage Examples

### 4.1 Basic Point-in-Time Temporal Resolution
```typescript
import { ChronoTubeResolutionEngine, TemporalSnapshot } from './temporal_resolution_engine';

const videoTimeline: TemporalSnapshot[] = [
  {
    timestamp: '2006-04-23T20:30:00Z',
    properties: {
      title: 'Me at the zoo',
      view_count: 100,
      star_rating: 5.0,
      tags: ['zoo', 'jawed']
    },
    embeddingVector: [1.0, 0.0, 0.0]
  },
  {
    timestamp: '2020-04-23T20:30:00Z',
    properties: {
      title: 'Me at the zoo (15th Anniversary)',
      view_count: 90_000_000,
      star_rating: 4.88,
      tags: ['zoo', 'jawed', 'historic']
    },
    embeddingVector: [0.0, 1.0, 0.0]
  }
];

// Query exact state inside historical gap (June 2013)
const state = ChronoTubeResolutionEngine.resolveStateAtTimestamp(
  'video:me_at_the_zoo',
  videoTimeline,
  '2013-06-15T12:00:00Z'
);

console.log(state);
```

### 4.2 Querying via ChronoCypher (GraphQL / Cypher)
```cypher
// Find all video responses to viral anchors in 2007
MATCH (root:TemporalNode {id: "video:evolution_of_dance"})
      <-[:VIDEO_RESPONSE_TO AT TIME "2007-06-15T12:00:00Z"]-(resp:TemporalNode)
RETURN resp.id, resp.properties.title, resp.properties.view_count
ORDER BY resp.properties.view_count DESC
LIMIT 10;
```

---

## ðŸ§ª 5. Testing & Verification

Run the built-in test suite covering all mathematical curves and gap resolution edge cases:

```bash
npm test
```

---

## ðŸ“„ License
MIT License. Created for digital preservation, web archaeology, and media research.