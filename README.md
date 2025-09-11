# GRASP for MAX-SC-QBF Problem

This Python implementation solves the **MAX-SC-QBF** (Maximum Set Cover with Quadratic Binary Function) problem using various GRASP (Greedy Randomized Adaptive Search Procedure) metaheuristic configurations.

## Problem Description
MAX-SC-QBF combines:
- **Set Cover constraint**: All elements must be covered by at least one selected subset
- **Quadratic Binary Function maximization**: Maximize f(x) = ΣΣ a_ij·x_i·x_j

The implementation transforms this into a minimization problem (g(x) = -f(x)) to work with the GRASP framework.

## Key Features
- **10 different GRASP configurations** combining:
  - Construction methods: Standard, Reactive, Cost Perturbation
  - Local search: Best-improving vs First-improving
  - Alpha parameters: α₁=0.1 and α₂=0.3
- **Advanced techniques**:
  - Reactive GRASP with dynamic alpha adaptation
  - Cost perturbation for search diversification
  - Feasibility handling with penalty functions
- **Stopping criteria**: Maximum time (30 min) and iterations without improvement

## Usage
Run `main.py` to execute all 10 configurations on QBF instances. The code will output solution quality and execution time for each method.

## Requirements
- Python 3.11
- NumPy 2.3.2+

The implementation is based on a Java framework ported to Python with extensions for advanced metaheuristic strategies.
