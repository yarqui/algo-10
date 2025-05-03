from typing import Callable, Tuple
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


def f(x: np.ndarray) -> np.ndarray:
    """Function to be integrated: f(x) = x^2."""
    return x**2


def monte_carlo_integrate(
    func: Callable[[np.ndarray], np.ndarray],
    bounds: Tuple[float, float],
    num_samples: int = 100_000,
) -> float:
    """Estimate the definite integral using the Monte Carlo method.

    Args:
        func: Function to integrate.
        bounds: Tuple of lower and upper limits (a, b).
        num_samples: Number of random samples.

    Returns:
        Approximated area under the curve.
    """
    a, b = bounds
    x_random: np.ndarray = np.random.uniform(a, b, num_samples)
    y_random: np.ndarray = func(x_random)
    return (b - a) * np.mean(y_random)


def compare_with_quad(
    func: Callable[[float], float], bounds: Tuple[float, float]
) -> Tuple[float, float]:
    """Compute definite integral using SciPy's quad for comparison.

    Args:
        func: Function to integrate.
        bounds: Tuple of lower and upper limits (a, b).

    Returns:
        Tuple of (integral value, estimated error).
    """
    a, b = bounds
    return integrate.quad(func, a, b)


def plot_function_and_area(
    func: Callable[[np.ndarray], np.ndarray],
    bounds: Tuple[float, float],
    x_range: Tuple[float, float] = (-0.5, 2.5),
    num_points: int = 400,
) -> None:
    """Plot the function and shade the area under the curve between given bounds."""
    a, b = bounds
    x = np.linspace(x_range[0], x_range[1], num_points)
    y = func(x)

    _, ax = plt.subplots()
    ax.plot(x, y, "r", linewidth=2, label="f(x) = x²")

    x_fill = np.linspace(a, b, num_points)
    y_fill = func(x_fill)
    ax.fill_between(x_fill, y_fill, color="gray", alpha=0.3, label="Integration area")

    ax.set_xlim(x_range)
    ax.set_ylim(0, max(y) + 0.1)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title(f"Integration of f(x) = x² from {a} to {b}")
    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.grid(True)
    ax.legend()
    plt.show()


if __name__ == "__main__":
    bounds = (0, 2)

    # Monte Carlo Integration
    monte_carlo_result = monte_carlo_integrate(f, bounds)

    # Analytical Integration with quad
    quad_result, quad_error = compare_with_quad(lambda x: x**2, bounds)

    # Output results
    print(f"Monte Carlo result: {monte_carlo_result}")
    print(f"SciPy quad result: {quad_result} ± {quad_error}")

    # Visualization
    plot_function_and_area(f, bounds)
