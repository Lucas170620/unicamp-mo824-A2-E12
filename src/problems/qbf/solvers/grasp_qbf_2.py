import time
import numpy as np
from src.problems.qbf.qbf_inverse import SCQBF_Inverse
from src.metaheuristics.grasp.abstract_grasp import AbstractGRASP
from typing import List

from src.solutions.solution import Solution
from src.utils.utils import find_and_apply_first_exchange, find_and_apply_first_insertion, find_and_apply_first_removal
from src.utils.constantes import *




class CostPerturbationGRASP_QBF(AbstractGRASP[int]):
    def __init__(self, alpha: float, iterations: int, filename: str):
        super().__init__(SCQBF_Inverse(filename), alpha, iterations)
        # self.ObjFunction.A = self.cost_perturbation(self.ObjFunction.A, intensity=0.1)
    
    def makeCL(self) -> List[int]:
        return list(range(self.ObjFunction.get_domain_size()))
    
    def makeRCL(self) -> List[int]:
        return []
    
    def updateCL(self) -> None:
        pass
    
    def createEmptySol(self) -> Solution[int]:
        sol = Solution()
        sol.cost = 0.0
        return sol
    

    def solve(self) -> Solution[int]:
        self.best_sol = self.createEmptySol()
        no_improvement_counter = 0
        max_no_improvement = MAX_NO_IMPROVEMENT
        start_time = time.time()
        time_max = MAX_TIME
        A_qrq = self.ObjFunction.A
        
        while True:
            if time.time() - start_time > time_max:
                break

            self.ObjFunction.A = self.cost_perturbation(self.ObjFunction.A, intensity=0.1)
            remaining_time = time_max - (time.time() - start_time)
            self.constructiveHeuristic()

            self.ObjFunction.A = A_qrq
            remaining_time = time_max - (time.time() - start_time)
            self.localSearch()

            if self.best_sol.cost > self.sol.cost:
                self.best_sol = Solution(self.sol)
                self.best_sol.cost = self.sol.cost
                no_improvement_counter = 0
                if self.verbose:
                    print(f"(Iter.) New BestSol = {self.best_sol.cost}")
            else:
                no_improvement_counter += 1
            if no_improvement_counter >= max_no_improvement:
                if self.verbose:
                    print(f"\nStopping early at iteration  due to no improvement in the last {max_no_improvement} iterations.")
                break 
        return self.best_sol
    
    def cost_perturbation(self, base_coeffs: np.ndarray, intensity: float = 0.1) -> np.ndarray:
        perturbed = base_coeffs.copy()
        perturbation = np.random.uniform(-intensity, intensity, base_coeffs.shape)
        return perturbed * (1 + perturbation)
    
    def localSearch(self) -> Solution[int]:
        start_time = time.time()

        while True:
            if time.time() - start_time > MAX_TIME:
                break
            min_delta_cost = float('inf')
            best_cand_in = None
            best_cand_out = None
            self.updateCL()
            
            # Evaluate insertions
            for cand_in in self.CL:
                delta_cost = self.ObjFunction.evaluate_insertion_cost(cand_in, self.sol)
                if delta_cost < min_delta_cost:
                    min_delta_cost = delta_cost
                    best_cand_in = cand_in
                    best_cand_out = None
            
            # Evaluate removals
            for cand_out in self.sol:
                delta_cost = self.ObjFunction.evaluate_removal_cost(cand_out, self.sol)
                if delta_cost < min_delta_cost:
                    min_delta_cost = delta_cost
                    best_cand_in = None
                    best_cand_out = cand_out
            
            # Evaluate exchanges
            for cand_in in self.CL:
                for cand_out in self.sol:
                    delta_cost = self.ObjFunction.evaluate_exchange_cost(cand_in, cand_out, self.sol)
                    if delta_cost < min_delta_cost:
                        min_delta_cost = delta_cost
                        best_cand_in = cand_in
                        best_cand_out = cand_out
            
            if min_delta_cost < -np.nextafter(0.0, 1.0):
                if best_cand_out is not None:
                    self.sol.remove(best_cand_out)
                    self.CL.append(best_cand_out)
                if best_cand_in is not None:
                    self.sol.append(best_cand_in)
                    self.CL.remove(best_cand_in)
                self.ObjFunction.evaluate(self.sol)
            else:
                break
        
        return self.sol

class Cost_Pertubation_GRASP_QBF_First_Improvement(CostPerturbationGRASP_QBF):
    def localSearch(self) -> Solution[int]:
        start_time = time.time()

        while True:
            if time.time() - start_time > MAX_TIME:
                break
            
            if find_and_apply_first_insertion(self):
                continue
            
            if find_and_apply_first_removal(self):
                continue
            
            if find_and_apply_first_exchange(self):
                continue            
            break

        self.ObjFunction.evaluate(self.sol)
        return self.sol
