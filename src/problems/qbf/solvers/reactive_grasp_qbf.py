import random
import time
import numpy as np
from typing import List
from src.problems.qbf.solvers.grasp_qbf import GRASP_QBF, GRASP_QBF_First_Improvement
from src.solutions.solution import Solution
from src.utils.constantes import *

class ReactiveGRASP_QBF(GRASP_QBF):
    def __init__(self, alpha_values: List[float], iterations: int, filename: str, reactive_update_block: int = 50):
        super().__init__(alpha_values[0], iterations, filename)
        self.alpha_values = alpha_values
        self.reactive_update_block = reactive_update_block
        self.alpha_probs = [1.0 / len(alpha_values)] * len(alpha_values)
        self.alpha_performance = [0.0] * len(alpha_values)
        self.alpha_count = [0] * len(alpha_values)
        self.best_global_value = -float('inf')
        self.penalty = 10**9  # Penalidade alta para soluções inviáveis
        self.universe = set(range(1, self.ObjFunction.size + 1))  # Universo a ser coberto

    def _is_feasible(self, sol: Solution[int]) -> bool:
        covered = set()
        for subset_idx in sol:
            covered.update(self.ObjFunction.subsets[subset_idx])
        return covered == self.universe

    def _evaluate_with_penalty(self, sol: Solution[int]) -> float:
        covered = set()
        for subset_idx in sol:
            covered.update(self.ObjFunction.subsets[subset_idx])
        uncovered = len(self.universe - covered)
        qbf_value = self.ObjFunction.evaluate(sol)
        return qbf_value - self.penalty * uncovered

    def update_alpha_probabilities(self):
        total = 0.0
        for i in range(len(self.alpha_values)):
            if self.alpha_count[i] > 0:
                self.alpha_probs[i] = self.best_global_value / (self.alpha_performance[i] / self.alpha_count[i])
            else:
                self.alpha_probs[i] = 1.0
            total += self.alpha_probs[i]
        self.alpha_probs = [p / total for p in self.alpha_probs]

    def choose_alpha(self):
        return random.choices(self.alpha_values, weights=self.alpha_probs, k=1)[0]

    def solve(self) -> Solution[int]:
        self.best_sol = self.createEmptySol()
        for i in range(self.iterations):
            self.alpha = self.choose_alpha()
            self.constructiveHeuristic()
            self.localSearch()

            # Avaliar solução com penalidades
            current_value = -self._evaluate_with_penalty(self.sol)
            idx = self.alpha_values.index(self.alpha)
            self.alpha_performance[idx] += current_value
            self.alpha_count[idx] += 1

            if current_value > self.best_global_value:
                self.best_global_value = current_value
                self.best_sol = Solution(self.sol)
                self.best_sol.cost = self.sol.cost
                if self.verbose:
                    print(f"(Iter. {i}) BestSol = {self.best_sol}")

            if i % self.reactive_update_block == 0 and i > 0:
                self.update_alpha_probabilities()
                if self.verbose:
                    print(f"Updated alpha probabilities: {list(zip(self.alpha_values, self.alpha_probs))}")

        return self.best_sol

class ReactiveGRASP_QFG_First_Improvement(GRASP_QBF_First_Improvement):
    def __init__(self, alpha_values: List[float], iterations: int, filename: str, reactive_update_block: int = 50):
        super().__init__(alpha_values[0], iterations, filename)
        self.alpha_values = alpha_values
        self.reactive_update_block = reactive_update_block
        self.alpha_probs = [1.0 / len(alpha_values)] * len(alpha_values)
        self.alpha_performance = [0.0] * len(alpha_values)
        self.alpha_count = [0] * len(alpha_values)
        self.best_global_value = -float('inf')
        self.penalty = 10**9  # Penalidade alta para soluções inviáveis
        self.universe = set(range(1, self.ObjFunction.size + 1))  # Universo a ser coberto

    def _is_feasible(self, sol: Solution[int]) -> bool:
        covered = set()
        for subset_idx in sol:
            covered.update(self.ObjFunction.subsets[subset_idx])
        return covered == self.universe

    def _evaluate_with_penalty(self, sol: Solution[int]) -> float:
        covered = set()
        for subset_idx in sol:
            covered.update(self.ObjFunction.subsets[subset_idx])
        uncovered = len(self.universe - covered)
        qbf_value = self.ObjFunction.evaluate(sol)
        return qbf_value - self.penalty * uncovered

    def update_alpha_probabilities(self):
        total = 0.0
        for i in range(len(self.alpha_values)):
            if self.alpha_count[i] > 0:
                self.alpha_probs[i] = self.best_global_value / (self.alpha_performance[i] / self.alpha_count[i])
            else:
                self.alpha_probs[i] = 1.0
            total += self.alpha_probs[i]
        self.alpha_probs = [p / total for p in self.alpha_probs]

    def choose_alpha(self):
        return random.choices(self.alpha_values, weights=self.alpha_probs, k=1)[0]

    def solve(self) -> Solution[int]:
        self.best_sol = self.createEmptySol()
        no_improvement_counter = 0
        i = 0
        max_no_improvement = MAX_NO_IMPROVEMENT
        start_time = time.time()
        time_max = MAX_TIME
        while True:
            if time.time() - start_time > time_max:
                break
            self.alpha = self.choose_alpha()
            self.constructiveHeuristic()
            self.localSearch()

            current_value = -self._evaluate_with_penalty(self.sol)
            idx = self.alpha_values.index(self.alpha)
            self.alpha_performance[idx] += current_value
            self.alpha_count[idx] += 1

            if current_value > self.best_global_value:
                self.best_global_value = current_value
                self.best_sol = Solution(self.sol)
                self.best_sol.cost = self.sol.cost
                if self.verbose:
                    print(f"(Iter. {i}) BestSol = {self.best_sol}")

            
            else:
                no_improvement_counter += 1
            if no_improvement_counter >= max_no_improvement:
                if self.verbose:
                    print(f"\nStopping early at iteration  due to no improvement in the last iterations.")
                break

            if i % self.reactive_update_block == 0 and i > 0:
                self.update_alpha_probabilities()
                if self.verbose:
                    print(f"Updated alpha probabilities: {list(zip(self.alpha_values, self.alpha_probs))}")
            i += 1
        return self.best_sol
    