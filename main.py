import time
from src.problems.qbf.solvers.grasp_qbf_2 import Cost_Pertubation_GRASP_QBF_First_Improvement, CostPerturbationGRASP_QBF
from src.problems.qbf.solvers.reactive_grasp_qbf import ReactiveGRASP_QBF, ReactiveGRASP_QFG_First_Improvement
from src.problems.qbf.solvers.grasp_qbf import GRASP_QBF, GRASP_QBF_First_Improvement
from src.utils.constantes import *


if __name__ == "__main__":
    instancia = f"instances/a1/instancia_1_25.txt"
    interations = 20

    print("instância:", instancia)
    print("max_no_improvement:", MAX_NO_IMPROVEMENT)
    # 7. Cost perturbations + first-improving + α1
    start_time = time.time()
    grasp = Cost_Pertubation_GRASP_QBF_First_Improvement(alpha=ALPHA_1, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    print(f"7. Cost perturbations + first-improving + α1: {cost} em {total_time} segundos")
     # 8. Cost perturbations + first-improving + α2
    start_time = time.time()
    grasp = Cost_Pertubation_GRASP_QBF_First_Improvement(alpha=ALPHA_2, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    print(f"8. Cost perturbations + first-improving + α2: {cost} em {total_time} segundos")
   # 9. Cost perturbations + best-improving + α1
    start_time = time.time()
    grasp = CostPerturbationGRASP_QBF(alpha=ALPHA_1, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    print(f"9. Cost perturbations + best-improving + α1: {cost} em {total_time} segundos")
     # 10. Cost perturbations + best-improving + α2
    start_time = time.time()
    grasp = CostPerturbationGRASP_QBF(alpha=ALPHA_2, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    print(f"10. Cost perturbations + best-improving + α2: {cost} em {total_time} segundos")
   
    instancia = f"instances/a1/instancia_2_25.txt"
    interations = 20
    print("instância:", instancia)
    print("max_no_improvement:", MAX_NO_IMPROVEMENT)
    # 7. Cost perturbations + first-improving + α1
    start_time = time.time()
    grasp = Cost_Pertubation_GRASP_QBF_First_Improvement(alpha=ALPHA_1, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    print(f"7. Cost perturbations + first-improving + α1: {cost} em {total_time} segundos")
     # 8. Cost perturbations + first-improving + α2
    start_time = time.time()
    grasp = Cost_Pertubation_GRASP_QBF_First_Improvement(alpha=ALPHA_2, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    print(f"8. Cost perturbations + first-improving + α2: {cost} em {total_time} segundos")
   # 9. Cost perturbations + best-improving + α1
    start_time = time.time()
    grasp = CostPerturbationGRASP_QBF(alpha=ALPHA_1, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    print(f"9. Cost perturbations + best-improving + α1: {cost} em {total_time} segundos")
     # 10. Cost perturbations + best-improving + α2
    start_time = time.time()
    grasp = CostPerturbationGRASP_QBF(alpha=ALPHA_2, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    print(f"10. Cost perturbations + best-improving + α2: {cost} em {total_time} segundos")
   
    instancia = f"instances/a1/instancia_3_25.txt"
    interations = 20
    print("instância:", instancia)
    print("max_no_improvement:", MAX_NO_IMPROVEMENT)
    # 7. Cost perturbations + first-improving + α1
    start_time = time.time()
    grasp = Cost_Pertubation_GRASP_QBF_First_Improvement(alpha=ALPHA_1, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    print(f"7. Cost perturbations + first-improving + α1: {cost} em {total_time} segundos")
    # 8. Cost perturbations + first-improving + α2
    start_time = time.time()
    grasp = Cost_Pertubation_GRASP_QBF_First_Improvement(alpha=ALPHA_2, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    print(f"8. Cost perturbations + first-improving + α2: {cost} em {total_time} segundos")
    # 9. Cost perturbations + best-improving + α1
    start_time = time.time()
    grasp = CostPerturbationGRASP_QBF(alpha=ALPHA_1, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    print(f"9. Cost perturbations + best-improving + α1: {cost} em {total_time} segundos")
     # 10. Cost perturbations + best-improving + α2
    start_time = time.time()
    grasp = CostPerturbationGRASP_QBF(alpha=ALPHA_2, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    print(f"10. Cost perturbations + best-improving + α2: {cost} em {total_time} segundos")


    instancia = f"instances/a1/instancia_1_100.txt"
    interations = 20
    print("instância:", instancia)
    print("max_no_improvement:", MAX_NO_IMPROVEMENT)
    # 7. Cost perturbations + first-improving + α1
    start_time = time.time()
    grasp = Cost_Pertubation_GRASP_QBF_First_Improvement(alpha=ALPHA_1, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    print(f"7. Cost perturbations + first-improving + α1: {cost} em {total_time} segundos")
     # 8. Cost perturbations + first-improving + α2
    start_time = time.time()
    grasp = Cost_Pertubation_GRASP_QBF_First_Improvement(alpha=ALPHA_2, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    print(f"8. Cost perturbations + first-improving + α2: {cost} em {total_time} segundos")
   # 9. Cost perturbations + best-improving + α1
    start_time = time.time()
    grasp = CostPerturbationGRASP_QBF(alpha=ALPHA_1, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    print(f"9. Cost perturbations + best-improving + α1: {cost} em {total_time} segundos")
     # 10. Cost perturbations + best-improving + α2
    start_time = time.time()
    grasp = CostPerturbationGRASP_QBF(alpha=ALPHA_2, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    print(f"10. Cost perturbations + best-improving + α2: {cost} em {total_time} segundos")
   
    instancia = f"instances/a1/instancia_2_100.txt"
    interations = 20
    print("instância:", instancia)
    print("max_no_improvement:", MAX_NO_IMPROVEMENT)
    # 7. Cost perturbations + first-improving + α1
    start_time = time.time()
    grasp = Cost_Pertubation_GRASP_QBF_First_Improvement(alpha=ALPHA_1, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    print(f"7. Cost perturbations + first-improving + α1: {cost} em {total_time} segundos")
     # 8. Cost perturbations + first-improving + α2
    start_time = time.time()
    grasp = Cost_Pertubation_GRASP_QBF_First_Improvement(alpha=ALPHA_2, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    print(f"8. Cost perturbations + first-improving + α2: {cost} em {total_time} segundos")
   # 9. Cost perturbations + best-improving + α1
    start_time = time.time()
    grasp = CostPerturbationGRASP_QBF(alpha=ALPHA_1, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    print(f"9. Cost perturbations + best-improving + α1: {cost} em {total_time} segundos")
     # 10. Cost perturbations + best-improving + α2
    start_time = time.time()
    grasp = CostPerturbationGRASP_QBF(alpha=ALPHA_2, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    print(f"10. Cost perturbations + best-improving + α2: {cost} em {total_time} segundos")
   
    instancia = f"instances/a1/instancia_3_100.txt"
    interations = 20
    print("instância:", instancia)
    print("max_no_improvement:", MAX_NO_IMPROVEMENT)
    # 7. Cost perturbations + first-improving + α1
    start_time = time.time()
    grasp = Cost_Pertubation_GRASP_QBF_First_Improvement(alpha=ALPHA_1, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    print(f"7. Cost perturbations + first-improving + α1: {cost} em {total_time} segundos")
    # 8. Cost perturbations + first-improving + α2
    start_time = time.time()
    grasp = Cost_Pertubation_GRASP_QBF_First_Improvement(alpha=ALPHA_2, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    print(f"8. Cost perturbations + first-improving + α2: {cost} em {total_time} segundos")
    # 9. Cost perturbations + best-improving + α1
    start_time = time.time()
    grasp = CostPerturbationGRASP_QBF(alpha=ALPHA_1, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    print(f"9. Cost perturbations + best-improving + α1: {cost} em {total_time} segundos")
     # 10. Cost perturbations + best-improving + α2
    start_time = time.time()
    grasp = CostPerturbationGRASP_QBF(alpha=ALPHA_2, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    print(f"10. Cost perturbations + best-improving + α2: {cost} em {total_time} segundos")
