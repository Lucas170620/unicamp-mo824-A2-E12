import time
from src.problems.qbf.solvers.grasp_qbf_2 import Cost_Pertubation_GRASP_QBF_First_Improvement, CostPerturbationGRASP_QBF
from src.problems.qbf.solvers.reactive_grasp_qbf import ReactiveGRASP_QBF, ReactiveGRASP_QFG_First_Improvement
from src.problems.qbf.solvers.grasp_qbf import GRASP_QBF, GRASP_QBF_First_Improvement
from src.utils.constantes import *


if __name__ == "__main__":
    instancia = f"instances/a1/instancia_1_25.txt"
    interations = 20
    resultados = [["name", "maxVal", "time"]]

    # 1. PADRÃO + first-improving + α1
    start_time = time.time()
    grasp_first_improvement = GRASP_QBF_First_Improvement(alpha=ALPHA_1, iterations=interations, filename=instancia)
    best_sol_first_improvement = grasp_first_improvement.solve()
    cost_first_improvement = - best_sol_first_improvement.cost
    end_time_first_improvement = time.time()
    total_time_first_improvement = end_time_first_improvement - start_time
    resultados.append([f"1. PADRÃO + first-improving + α1", cost_first_improvement, total_time_first_improvement])
    print(f"1. PADRÃO + first-improving + α1: {cost_first_improvement} em {total_time_first_improvement} segundos")
    # 2. PADRÃO + first-improving + α2

    start_time = time.time()
    grasp_first_improvement = GRASP_QBF_First_Improvement(alpha=ALPHA_2, iterations=interations, filename=instancia)
    best_sol_first_improvement = grasp_first_improvement.solve()
    cost_first_improvement = - best_sol_first_improvement.cost
    end_time_first_improvement = time.time()
    total_time_first_improvement = end_time_first_improvement - start_time
    resultados.append([f"2. PADRÃO + first-improving + α2", cost_first_improvement, total_time_first_improvement])
    print(f"2. PADRÃO + first-improving + α2: {cost_first_improvement} em {total_time_first_improvement} segundos")
    # 3. PADRÃO + best-improving + α1
    
    start_time = time.time()
    grasp = GRASP_QBF(alpha=ALPHA_1, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    resultados.append([f"3. PADRÃO + best-improving + α1", cost, total_time])
    print(f"3. PADRÃO + best-improving + α1: {cost} em {total_time} segundos")
    # 4. PADRÃO + best-improving + α2

    start_time = time.time()
    grasp = GRASP_QBF(alpha=ALPHA_2, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    resultados.append([f"4. PADRÃO + best-improving + α2", cost, total_time])
    print(f"4. PADRÃO + best-improving + α2: {cost} em {total_time} segundos")
    # 5. REATIVE + first-improving

    start_time = time.time()
    reactive_grasp_first_improvement = ReactiveGRASP_QFG_First_Improvement(alpha_values=[0.1, 0.3, 0.5, 0.7, 0.9], iterations=interations, filename=instancia)
    best_sol_reactive_first_improvement = reactive_grasp_first_improvement.solve()
    cost_reactive_first_improvement = - best_sol_reactive_first_improvement.cost
    end_time_reactive_first_improvement = time.time()
    total_time_reactive_first_improvement = end_time_reactive_first_improvement - start_time
    resultados.append(["5. REATIVE + first-improving", cost_reactive_first_improvement, total_time_reactive_first_improvement])
    print(f"5. REATIVE + first-improving: {cost_reactive_first_improvement} em {total_time_reactive_first_improvement} segundos")

    # 6. REATIVE + best-improving

    start_time = time.time()
    reactive_grasp = ReactiveGRASP_QBF(alpha_values=[0.1, 0.3, 0.5, 0.7, 0.9], iterations=interations, filename=instancia)
    best_sol_reactive = reactive_grasp.solve()
    cost_reactive = - best_sol_reactive.cost
    end_time_reactive = time.time()
    total_time_reactive = end_time_reactive - start_time
    resultados.append(["6. REATIVE + best-improving", cost_reactive, total_time_reactive])
    print(f"6. REATIVE + best-improving: {cost_reactive} em {total_time_reactive} segundos")
    # 7. Cost perturbations + first-improving + α1
    start_time = time.time()
    grasp = Cost_Pertubation_GRASP_QBF_First_Improvement(alpha=ALPHA_1, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    resultados.append([f"7. Cost perturbations + first-improving + α1", cost, total_time])
    print(f"7. Cost perturbations + first-improving + α1: {cost} em {total_time} segundos")
     # 8. Cost perturbations + first-improving + α2
    start_time = time.time()
    grasp = Cost_Pertubation_GRASP_QBF_First_Improvement(alpha=ALPHA_2, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    resultados.append([f"8. Cost perturbations + first-improving + α2", cost, total_time])
    print(f"8. Cost perturbations + first-improving + α2: {cost} em {total_time} segundos")
   # 9. Cost perturbations + best-improving + α1
    start_time = time.time()
    grasp = CostPerturbationGRASP_QBF(alpha=ALPHA_1, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    resultados.append([f"9. Cost perturbations + best-improving + α1", cost, total_time])
    print(f"9. Cost perturbations + best-improving + α1: {cost} em {total_time} segundos")
     # 10. Cost perturbations + best-improving + α2
    start_time = time.time()
    grasp = CostPerturbationGRASP_QBF(alpha=ALPHA_2, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    resultados.append([f"10. Cost perturbations + best-improving + α2", cost, total_time])
    print(f"10. Cost perturbations + best-improving + α2: {cost} em {total_time} segundos")
   
    
    
    for resultado in resultados:
        print(f"{resultado[0]}: {resultado[1]} em {resultado[2]} segundos")
