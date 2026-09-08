# 🪐 ChronoTube Engine: Multi-Dimensional YouTube Time-Machine & Digital Archaeology OS

[![ChronoTube Engine CI](https://github.com/Aeonsmith/ChronoTube/actions/workflows/ci.yml/badge.svg)](https://github.com/Aeonsmith/ChronoTube/actions/workflows/ci.yml)
[![GitHub Release](https://img.shields.io/github/v/release/Aeonsmith/ChronoTube?color=blue&label=Release)](https://github.com/Aeonsmith/ChronoTube/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests: 16 Passing](https://img.shields.io/badge/Tests-16%20Passing-success.svg)](TEST_RESULTS.md)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.x-blue.svg)](https://www.typescriptlang.org/)
[![Node.js](https://img.shields.io/badge/Node.js-18%2B-green.svg)](https://nodejs.org/)

The **ChronoTube Engine** is an interactive, spatial, and semantic simulation operating system for web archaeology, temporal graph querying, and counterfactual internet culture exploration across YouTube history (2005–2026+).

---

## ⚡ Quick Reference: Terminal Commands Guide

When opening the **ChronoTube** desktop shortcut or launching the terminal in this directory, here are the primary commands you can run:

| Command | Action | Description |
| :--- | :--- | :--- |
| `launch.bat` / Desktop Icon | **Launch Visual App** | Opens the interactive ChronoTube Time-Machine Desktop GUI application. |
| `python app.py` | **Direct GUI Run** | Launches the CustomTkinter visual application with interactive time-scrubber and era simulator. |
| `npm test` | **Run Test Suite** | Executes all 16 automated tests verifying mathematical curves (Linear, Logarithmic, Sigmoid S-Curve), categorical shifts, vector slerp normalization, and gap resolution. |
| `node test/test_interpolation_engine.js` | **Direct Test Run** | Runs the unit test harness directly with Node.js without package manager wrappers. |
| `node test/test_plugin_and_sandbox.js` | **Plugin & Sandbox Tests** | Verifies modular plugin hooks, custom shell rendering, and sandboxed simulation engine. |
| `code .` | **Open in VS Code** | Launches Visual Studio Code with the full project tree open. |
| `git status` | **Check Git Status** | Inspects current branch, modified files, and staging status. |
| `git log --oneline -n 5` | **Recent History** | Displays the latest commits and releases. |
| `ls` / `dir` | **List Files** | Lists all engines (`temporal_resolution_engine.ts`, `interpolation_engine.ts`), tests, and docs. |

### Quick Smoke Test via Node.js
To test the engine resolution headlessly from the command line:
```bash
node -e "const { ChronoTubeResolutionEngine } = require('./dist/temporal_resolution_engine.js'); console.log('✅ ChronoTube Engine is ready.');"
```

---

## 🎯 Overview & Purpose

The **ChronoTube Engine** transforms historical internet archive snapshots into a continuous, interactive, and explorable universe.

Traditional archives like the Wayback Machine capture websites as disconnected, static HTML pages with frequent gaps (such as missing media or unindexed months in 2023). ChronoTube solves this by:
1. **Bridging Archive Gaps**: Dynamically interpolating missing metrics (views, ratings, comments, and semantic embeddings) between recorded captures using domain-specific growth curves.
2. **Reconstructing Historic Ecosystems**: Restoring era-accurate interfaces, recommendation algorithms, and social response graphs (from early 2006 Flash 5-star ratings to modern 2026 neural vector feeds).
3. **Powering In-Situ & Counterfactual Exploration**: Allowing digital historians and creators to scrub through time, explore cultural topologies in a 3D galaxy view, or simulate how content would propagate if uploaded in a past era.

---

## 🏛️ 1. System Architecture

The ChronoTube Engine uses an event-sourced temporal property graph combined with interval-validity models and continuous numerical/categorical interpolation.

```
+-----------------------------------------------------------------------------------+
|                                PRESENTATION LAYER                                 |
|                                                                                   |
|  [ 🪐 WebGL 3D Galaxy ]    [ 📜 Multi-Scale Scrubber ]   [ 🕸️ Force Graph View ]   |
|  [ 📺 Retro UI Shells ]    [ ⚡ WASM Ruffle / Codecs ]    [ 🧪 Time Sandbox IDE ]   |
+----------------------------------------^------------------------------------------+
                                         | JSON-RPC / GraphQL-Temporal
+----------------------------------------v------------------------------------------+
|                              CHRONOTUBE CORE ENGINE                               |
|                                                                                   |
|  +---------------------------------+   +----------------------------------------+ |
|  |       Temporal State Router     |   |      Algorithmic Epoch Simulator       | |
|  | - Snapshot delta interpolation  |   | - 2005–2009: 5-Star / Direct Views     | |
|  | - Memento datetime resolver     |   | - 2010–2015: Watch-Time Accumulators   | |
|  | - Dynamic skin & layout binding |   | - 2016–2021: Retention & Dislikes CTR  | |
|  +----------------^----------------+   | - 2022–2026+: Neural Multimodal Vectors| |
|                   |                    +-------------------^--------------------+ |
|  +----------------v----------------------------------------v--------------------+ |
|  |                     Unified Temporal Execution Engine                        | |
|  | - Traversal planning across time branches   - Spherical Vector Slerp Engine  | |
|  | - Graph entity reconstruction               - Cross-Platform Identity Graph  | |
|  +-------------------------------------^----------------------------------------+ |
+----------------------------------------+------------------------------------------+
                                         | Internal Storage Interface
+----------------------------------------v------------------------------------------+
|                               PERSISTENCE & GRAPH LAYER                           |
|                                                                                   |
|  +------------------------------+  +----------------------+  +------------------+ |
|  |  Temporal Property Graph DB  |  | Vector Semantic DB   |  | Metadata Index   | |
|  |  (Nodes/Edges with [t_s,t_e])|  | (HNSW 1536-dim per t)|  | (RocksDB / CDX)  | |
|  +------------------------------+  +----------------------+  +------------------+ |
+----------------------------------------^------------------------------------------+
                                         | Ingestion & Normalization Pipeline
+----------------------------------------v------------------------------------------+
|                              INGESTION & ARCHIVE LAYER                            |
|                                                                                   |
|  [ Wayback CDX API ]    [ TubeUp / IA S3 ]    [ Google+ WARC Dumps ]              |
|  [ Filmot Subtitle DB ] [ Archivarix Echo ]   [ Live Snapshot Fallbacks ]         |
+-----------------------------------------------------------------------------------+
```

---

## 🧮 2. Interpolation Strategy Matrix

When querying between discontinuous snapshots, the engine applies domain-specific mathematical functions:

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

## ⚙️ 3. Installation & Setup Instructions

### 3.1 Prerequisites
Ensure the following tools are installed on your system:
* **Node.js**: `v18.0.0` or later (LTS recommended)
* **Git**: `v2.30+`
* **npm** or **pnpm**

### 3.2 Installation Steps

```bash
# 1. Clone the repository
git clone https://github.com/Aeonsmith/ChronoTube.git
cd ChronoTube

# 2. Install project dependencies
npm install

# 3. (Optional) Build TypeScript source to JavaScript
npm run build
```

---

## 🚀 4. Usage Instructions & Examples

### 4.1 Programmatic Point-in-Time Resolution (TypeScript / Node.js)

```typescript
import { ChronoTubeResolutionEngine, TemporalSnapshot } from './temporal_resolution_engine';

// Define historical captures
const snapshots: TemporalSnapshot[] = [
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

// Resolve state during an unrecorded period (e.g. 2013-06-15)
const resolvedState = ChronoTubeResolutionEngine.resolveStateAtTimestamp(
  'video:me_at_the_zoo',
  snapshots,
  '2013-06-15T12:00:00Z'
);

console.log(resolvedState);
```

### 4.2 Querying via ChronoCypher

```cypher
// Query viral video responses and recommendation links at a specific historical point
MATCH (v:TemporalNode {id: "video:evolution_of_dance"})
      <-[r:VIDEO_RESPONSE_TO AT TIME "2007-06-15T12:00:00Z"]-(resp:TemporalNode)
RETURN resp.id, resp.properties.title, resp.properties.view_count
ORDER BY resp.properties.view_count DESC
LIMIT 10;
```

---

## 🧩 5. Modular Plugin Architecture (`plugin_system.ts`)

The ChronoTube OS provides an extensible lifecycle hook framework allowing researchers to mount custom UI reconstructors, algorithmic inspectors, and cross-platform timelines.

### 5.1 Plugin Lifecycle Interface
```typescript
export interface ChronoTubePlugin {
  readonly id: string;
  readonly name: string;
  readonly version: string;
  readonly category: 'UI_RECONSTRUCTION' | 'ALGORITHM_ANALYSIS' | 'PROVENANCE_INTEGRITY' | 'CROSS_PLATFORM_GRAPH';
  
  initialize?(context: PluginContext): Promise<void> | void;
  onEpochChange?(newEpoch: AlgorithmicEpochConfig, timestamp: string): void;
  onStateResolve?<T>(resolvedState: ResolvedTemporalState<T>): ResolvedTemporalState<T> | void;
  renderCustomShell?(resolvedState: ResolvedTemporalState<any>, timestamp: string): ReconstructedShellView | null;
  verifyProvenance?(entityId: string, timestamp: string): ProvenanceAuditRecord | null;
}
```

### 5.2 How to Author a Custom Plugin
```typescript
import { ChronoTubePlugin, ReconstructedShellView, ChronoTubePluginRegistry } from './plugin_system';
import { ResolvedTemporalState } from './temporal_resolution_engine';

export class Custom2008AnnotationsPlugin implements ChronoTubePlugin {
  public readonly id = 'plugin.custom.2008-annotations';
  public readonly name = '2008 Interactive Annotations Overlay';
  public readonly version = '1.0.0';
  public readonly category = 'UI_RECONSTRUCTION';

  public renderCustomShell(state: ResolvedTemporalState<any>, timestamp: string): ReconstructedShellView | null {
    const year = new Date(timestamp).getUTCFullYear();
    if (year !== 2008) return null;

    return {
      eraName: '2008 Annotations & Speech Bubble Era',
      playerType: 'FLASH_FLV',
      resolution: '480x360',
      bitrateKbps: 450,
      ratingSystem: '5_STAR_DISCRETE',
      uiTheme: {
        primaryBg: '#FFFFFF',
        accentColor: '#CC181E',
        subscribeStyle: 'YELLOW_BUTTON'
      },
      sidebarModules: ['Interactive Note Bubbles', 'Spotlight Annotations', 'Video Responses']
    };
  }
}

// Registering the plugin:
const registry = new ChronoTubePluginRegistry();
registry.register(new Custom2008AnnotationsPlugin());
```

### 5.3 Mounted Built-in Plugins
1. **`plugin.reconstruct.2006-homepage`**: Reconstructs the 2006 Flash 8 layout, yellow subscribe buttons, and featured video carousels.
2. **`plugin.reconstruct.2010-cosmic`**: Reconstitutes the Cosmic Panda dark player frame, watch-time recommendation cards, and Google+ discussion threads.
3. **`plugin.algo.shift-explorer`**: Injects era-specific algorithm regime metadata (Keyword ➔ Watch Time ➔ Retention CTR ➔ 1536-dim HNSW).
4. **`plugin.timeline.vine-tiktok-bridge`**: Connects video responses with Vine loops and modern vertical Shorts shelves.
5. **`plugin.provenance.wayback-verifier`**: Verifies Memento and Wayback Machine CDX cryptographic hashes.

---

## 🧪 6. Sandboxed Playback & Counterfactual Publishing (`sandboxed_playback_engine.ts`)

Allows historians to run **in-situ simulations** and test hypothetical "What-If" publishing experiments under historical platform constraints.

* **Strict Provenance Watermarking**: All counterfactual artifacts carry an immutable `✦ SYNTHETIC SIMULATION ARTIFACT // PROVENANCE: EXP-SIM-YYYY-XXXXXXXX // NOT A HISTORICAL CANONICAL CAPTURE ✦` header.
* **Virtualized Codec Emulation**:
  * *2005–2009*: Sorenson Spark FLV (320x240 @ 15fps, 300kbps) with 3.5 Mbps DSL buffering latency (3,800ms stall).
  * *2010–2015*: H.264 / AVC 720p/1080p HTML5 with watch-time accumulation modeling.
  * *2022–2026+*: AV1 4K 60fps HDR spatial audio with 1536-dim HNSW neural vector clustering.

---

## 🧪 7. Testing & Verification

Run the full 23-suite automated test matrix covering numerical curves, structural mergers, vector slerp normalization, plugin lifecycle hooks, and sandboxed simulation:

```bash
# Execute full test suite
npm test
```

## 🤝 Contributing

We welcome contributions from developers, mathematicians, data archivists, and internet historians! Please review our [Contribution Guidelines (CONTRIBUTING.md)](CONTRIBUTING.md) to learn about our development workflow, coding standards, and pull request process.

---
---

## 📄 License
Distributed under the **MIT License**. Created for digital preservation, web archaeology, and media research.