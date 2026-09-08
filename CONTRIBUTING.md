# 🤝 Contributing to ChronoTube Engine

Thank you for your interest in contributing to the **ChronoTube Engine**! Whether you are helping to improve our temporal interpolation algorithms, adding new era definitions, or fixing bugs in our archive ingestion pipelines, your contributions are welcome.

---

## 📜 Code of Conduct

We are committed to providing a welcoming, inclusive, and harassment-free environment for all contributors. Please treat everyone with respect and professional courtesy.

---

## 🛠️ Development Workflow

### 1. Prerequisites
* **Node.js**: `v18.0.0` or higher
* **Git**: `v2.30+`

### 2. Fork and Clone
```bash
# Fork the repository on GitHub, then clone your fork:
git clone https://github.com/<your-username>/ChronoTube.git
cd ChronoTube

# Install dependencies:
npm install
```

### 3. Branching Guidelines
* Create a feature branch off `main`:
  ```bash
  git checkout -b feature/new-interpolation-strategy
  # or
  git checkout -b fix/gap-resolution-edge-case
  ```

---

## 🔬 Adding New Strategies or Eras

### Adding a Numeric / Categorical Strategy
1. Define the strategy type in `interpolation_engine.ts` (`NumericStrategy` or `CategoricalStrategy`).
2. Implement the mathematical curve or state transition in `DynamicPropertyInterpolator`.
3. Add a unit test in `test/test_interpolation_engine.js`.

### Adding or Tuning an Algorithmic Era
1. Update `ChronoTubeResolutionEngine.getEpochForTimestamp()` in `temporal_resolution_engine.ts`.
2. Map epoch boundaries, priority ranking metrics, and default interpolation field rules.

---

## 🧪 Testing Your Changes

All contributions must pass the unit test suite before opening a pull request:

```bash
npm test
```

---

## 📬 Submitting a Pull Request (PR)

1. Ensure your code compiles cleanly and all tests pass.
2. Commit your changes with clear, descriptive commit messages:
   ```bash
   git commit -m "Add Weibull distribution strategy for virality decay"
   ```
3. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
4. Open a Pull Request on GitHub targeting `main`. Provide a concise summary of what was added or fixed.

---

## 🐛 Reporting Issues

If you find a bug, missing archive mapping, or edge case:
1. Check existing issues on GitHub to avoid duplicates.
2. Open a new issue providing:
   * **Target Timestamp & Entity ID** (e.g. `video:dQw4w9WgXcQ` at `2013-05-01`).
   * **Observed vs. Expected Behavior**.
   * **Steps or Code Snippet to Reproduce**.

---

## 📄 License
By contributing to ChronoTube, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).