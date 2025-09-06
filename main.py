import time
from src.problems.qbf.solvers.reactive_grasp_qbf import ReactiveGRASP_QBF, ReactiveGRASP_QFG_First_Improvement
from src.problems.qbf.solvers.grasp_qbf import GRASP_QBF, GRASP_QBF_First_Improvement


if __name__ == "__main__":
    n = 20
    instancia = f"instances/qbf/qbf0{n}"
    interations = n
    start_time = time.time()
    grasp = GRASP_QBF(alpha=0.3, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    print(f"maxVal Padrao = {cost}")
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Time Padrao = {total_time} seg")

    reactive_grasp = ReactiveGRASP_QBF(alpha_values=[0.1, 0.3, 0.5, 0.7, 0.9], iterations=interations, filename=instancia)
    best_sol_reactive = reactive_grasp.solve()
    cost_reactive = - best_sol_reactive.cost
    print(f"maxVal (Reactive) = {cost_reactive}")
    end_time_reactive = time.time()
    total_time_reactive = end_time_reactive - start_time
    print(f"Time (Reactive) = {total_time_reactive} seg")

    start_time = time.time()
    grasp_first_improvement = GRASP_QBF_First_Improvement(alpha=0.3, iterations=interations, filename=instancia)
    best_sol_first_improvement = grasp_first_improvement.solve()
    cost_first_improvement = - best_sol_first_improvement.cost
    print(f"maxVal Padrao + (First Improvement) = {cost_first_improvement}")
    end_time_first_improvement = time.time()
    total_time_first_improvement = end_time_first_improvement - start_time
    print(f"Time Padrao + (First Improvement) = {total_time_first_improvement} seg")

    start_time = time.time()
    reactive_grasp_first_improvement = ReactiveGRASP_QFG_First_Improvement(alpha_values=[0.1, 0.3, 0.5, 0.7, 0.9], iterations=interations, filename=instancia)
    best_sol_reactive_first_improvement = reactive_grasp_first_improvement.solve()
    cost_reactive_first_improvement = - best_sol_reactive_first_improvement.cost
    print(f"maxVal (Reactive First Improvement) = {cost_reactive_first_improvement}")
    end_time_reactive_first_improvement = time.time()
    total_time_reactive_first_improvement = end_time_reactive_first_improvement - start_time
    print(f"Time (Reactive First Improvement) = {total_time_reactive_first_improvement} seg")