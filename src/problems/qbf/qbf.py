import numpy as np
from typing import TypeVar

from src.problems.evaluator import Evaluator
from src.solutions.solution import Solution

E = TypeVar('E')

class QBF(Evaluator[int]):
    def __init__(self, filename: str):
        self.size, self.A = self.read_input(filename)
        self.variables = self.allocate_variables()
    
    def read_input(self, filename: str) -> tuple[int, np.ndarray]:
        with open(filename, 'r') as file:
            first_line = file.readline().strip()
            size = int(first_line)
            A = np.zeros((size, size))
            
            for i in range(size):
                line = file.readline().split()
                for j in range(i, size):
                    A[i, j] = float(line[j - i])
                    if j > i:
                        A[j, i] = 0.0
            
            return size, A
    
    def allocate_variables(self) -> np.ndarray:
        return np.zeros(self.size)
    
    def set_variables(self, sol: Solution[int]) -> None:
        self.reset_variables()
        for elem in sol:
            self.variables[elem] = 1.0
    
    def reset_variables(self) -> None:
        self.variables.fill(0.0)
    
    def get_domain_size(self) -> int:
        return self.size
    
    def evaluate(self, sol: Solution[int]) -> float:
        self.set_variables(sol)
        sol.cost = self.evaluateQBF()
        return sol.cost
    
    def evaluateQBF(self) -> float:
        vec_aux = np.zeros(self.size)
        for i in range(self.size):
            vec_aux[i] = np.sum(self.variables * self.A[i, :])
        return np.sum(vec_aux * self.variables)
    
    def evaluate_insertion_cost(self, elem: int, sol: Solution[int]) -> float:
        self.set_variables(sol)
        return self.evaluate_insertion_QBF(elem)
    
    def evaluate_insertion_QBF(self, i: int) -> float:
        if self.variables[i] == 1:
            return 0.0
        return self.evaluate_contribution_QBF(i)
    
    def evaluate_removal_cost(self, elem: int, sol: Solution[int]) -> float:
        self.set_variables(sol)
        return self.evaluate_removal_QBF(elem)
    
    def evaluate_removal_QBF(self, i: int) -> float:
        if self.variables[i] == 0:
            return 0.0
        return -self.evaluate_contribution_QBF(i)
    
    def evaluate_exchange_cost(self, elem_in: int, elem_out: int, sol: Solution[int]) -> float:
        self.set_variables(sol)
        return self.evaluate_exchange_QBF(elem_in, elem_out)
    
    def evaluate_exchange_QBF(self, in_val: int, out_val: int) -> float:
        if in_val == out_val:
            return 0.0
        if self.variables[in_val] == 1:
            return self.evaluate_removal_QBF(out_val)
        if self.variables[out_val] == 0:
            return self.evaluate_insertion_QBF(in_val)
        
        total = (self.evaluate_contribution_QBF(in_val) - 
                self.evaluate_contribution_QBF(out_val) - 
                (self.A[in_val, out_val] + self.A[out_val, in_val]))
        return total
    
    def evaluate_contribution_QBF(self, i: int) -> float:
        total = 0.0
        for j in range(self.size):
            if i != j:
                total += self.variables[j] * (self.A[i, j] + self.A[j, i])
        total += self.A[i, i]
        return total
    
    def print_matrix(self) -> None:
        for i in range(self.size):
            for j in range(i, self.size):
                print(self.A[i, j], end=" ")
            print()