import numpy as np
from src.metaheuristics.grasp.abstract_grasp import AbstractGRASP
from typing import List

from src.problems.qbf.qbf_inverse import QBF_Inverse
from src.solutions.solution import Solution




class GRASP_QBF(AbstractGRASP[int]):
    def __init__(self, alpha: float, iterations: int, filename: str):
        super().__init__(QBF_Inverse(filename), alpha, iterations)
    
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
    
    def localSearch(self) -> Solution[int]:
        while True:
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

