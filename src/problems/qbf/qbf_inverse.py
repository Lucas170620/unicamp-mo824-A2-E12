from src.problems.qbf.qbf import QBF


class QBF_Inverse(QBF):
    def evaluateQBF(self) -> float:
        return -super().evaluateQBF()
    
    def evaluate_insertion_QBF(self, i: int) -> float:
        return -super().evaluate_insertion_QBF(i)
    
    def evaluate_removal_QBF(self, i: int) -> float:
        return -super().evaluate_removal_QBF(i)
    
    def evaluate_exchange_QBF(self, in_val: int, out_val: int) -> float:
        return -super().evaluate_exchange_QBF(in_val, out_val)
