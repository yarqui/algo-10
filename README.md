# Task 2: Definite Integral Calculation Using Monte Carlo Method

## Objective

Estimate the definite integral of the function:

```
f(x) = x²
```

over the interval \[0, 2\] using the **Monte Carlo method**, and compare the result to the one obtained via SciPy's `quad` function.

---

## Methodology

### 1. Monte Carlo Integration

The Monte Carlo method estimates the area under a curve by averaging function values at randomly sampled points:

```python
area ≈ (b - a) * average(f(x_random))
```

Where:

- `a = 0`, `b = 2`
- `x_random` are uniform random samples in \[a, b\]
- `f(x) = x²`

### 2. SciPy Quad

The `scipy.integrate.quad` function numerically evaluates the definite integral of `f(x)`:

```python
from scipy.integrate import quad
result, error = quad(f, 0, 2)
```

---

## Results

- **Monte Carlo Estimate** (with 100,000 samples): approximately `2.67`
- **SciPy Quad Result**: `2.666666666666667 ± 2.96e-14`

---

## Conclusion

The Monte Carlo method provided a close approximation of the integral. While it is less precise than deterministic numerical methods, it is effective for large-scale simulations and multi-dimensional problems.

---
