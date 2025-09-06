import random
from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic, Optional

from src.problems.evaluator import Evaluator
from src.solutions.solution import Solution

E = TypeVar('E')


class AbstractGRASP(ABC, Generic[E]):
    verbose = False
    rng = random.Random(0)
    
    def __init__(self, obj_function: Evaluator[E], alpha: float, iterations: int):
        self.ObjFunction = obj_function
        self.alpha = alpha
        self.iterations = iterations
        self.best_cost: float = float('inf')
        self.cost: float = float('inf')
        self.best_sol: Optional[Solution[E]] = None
        self.sol: Optional[Solution[E]] = None
        self.CL: List[E] = []
        self.RCL: List[E] = []
    
    @abstractmethod
    def makeCL(self) -> List[E]:
        pass
    
    @abstractmethod
    def makeRCL(self) -> List[E]:
        pass
    
    @abstractmethod
    def updateCL(self) -> None:
        pass
    
    @abstractmethod
    def createEmptySol(self) -> Solution[E]:
        pass
    
    @abstractmethod
    def localSearch(self) -> Solution[E]:
        pass
    
    def constructiveHeuristic(self) -> Solution[E]:
        self.CL = self.makeCL()
        self.RCL = self.makeRCL()
        self.sol = self.createEmptySol()
        self.cost = float('inf')
        
        while not self.constructiveStopCriteria():
            max_cost = float('-inf')
            min_cost = float('inf')
            self.cost = self.ObjFunction.evaluate(self.sol)
            self.updateCL()
            
            for c in self.CL:
                delta_cost = self.ObjFunction.evaluate_insertion_cost(c, self.sol)
                if delta_cost < min_cost:
                    min_cost = delta_cost
                if delta_cost > max_cost:
                    max_cost = delta_cost
            
            for c in self.CL:
                delta_cost = self.ObjFunction.evaluate_insertion_cost(c, self.sol)
                if delta_cost <= min_cost + self.alpha * (max_cost - min_cost):
                    self.RCL.append(c)
            
            if self.RCL:  # Check if RCL is not empty
                in_cand = self.rng.choice(self.RCL)
                self.CL.remove(in_cand)
                self.sol.append(in_cand)
                self.ObjFunction.evaluate(self.sol)
                self.RCL.clear()
        
        return self.sol
    
    def solve(self) -> Solution[E]:
        self.best_sol = self.createEmptySol()
        
        no_improvement_counter = 0
        max_no_improvement = 5

        for i in range(self.iterations):
            self.constructiveHeuristic()
            self.localSearch()
            if self.best_sol.cost > self.sol.cost:
                self.best_sol = Solution(self.sol)
                self.best_sol.cost = self.sol.cost
                no_improvement_counter = 0
                if self.verbose:
                    print(f"(Iter. {i}) New BestSol = {self.best_sol.cost}")
            else:
                no_improvement_counter += 1
            if no_improvement_counter >= max_no_improvement:
                if self.verbose:
                    print(f"\nStopping early at iteration {i} due to no improvement in the last {max_no_improvement} iterations.")
                break 
        return self.best_sol
    
    def constructiveStopCriteria(self) -> bool:
        return not (self.cost > self.sol.cost)
