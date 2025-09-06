import numpy as np


TOLERANCE = np.nextafter(0.0, 1.0)

def find_and_apply_first_insertion(grasp_qbf) -> bool:
            """Tenta encontrar e aplicar o primeiro movimento de inserção que melhora a solução."""
            for cand_in in grasp_qbf.CL:
                delta_cost = grasp_qbf.ObjFunction.evaluate_insertion_cost(cand_in, grasp_qbf.sol)
                if delta_cost < -TOLERANCE:
                    grasp_qbf.sol.append(cand_in)
                    grasp_qbf.CL.remove(cand_in)
                    grasp_qbf.sol.cost += delta_cost
                    return True  # Melhora encontrada e aplicada
            return False

def find_and_apply_first_removal(grasp_qbf) -> bool:
    for cand_out in list(grasp_qbf.sol):
        delta_cost = grasp_qbf.ObjFunction.evaluate_removal_cost(cand_out, grasp_qbf.sol)
        if delta_cost < -TOLERANCE:
            grasp_qbf.sol.remove(cand_out)
            grasp_qbf.CL.append(cand_out)
            grasp_qbf.sol.cost += delta_cost
            return True  # Melhora encontrada e aplicada
    return False

def find_and_apply_first_exchange(grasp_qbf) -> bool:
    for cand_in in grasp_qbf.CL:
        for cand_out in list(grasp_qbf.sol):
            delta_cost = grasp_qbf.ObjFunction.evaluate_exchange_cost(cand_in, cand_out, grasp_qbf.sol)
            if delta_cost < -TOLERANCE:
                grasp_qbf.sol.remove(cand_out)
                grasp_qbf.CL.append(cand_out)
                grasp_qbf.sol.append(cand_in)
                grasp_qbf.CL.remove(cand_in)
                grasp_qbf.sol.cost += delta_cost
                return True
    return False