import time
from src.problems.qbf.solvers.reactive_grasp_qbf import ReactiveGRASP_QBF
from src.problems.qbf.solvers.grasp_qbf import GRASP_QBF


if __name__ == "__main__":
    instancia = "instances/qbf/qbf020"
    start_time = time.time()
    grasp = GRASP_QBF(alpha=0.3, iterations=100, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    print(f"maxVal (Reactive) = {cost}")
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Time (Reactive) = {total_time} seg")

    reactive_grasp = ReactiveGRASP_QBF(alpha_values=[0.1, 0.3, 0.5, 0.7, 0.9], iterations=100, filename=instancia)
    best_sol_reactive = reactive_grasp.solve()
    cost_reactive = - best_sol_reactive.cost
    print(f"maxVal (Reactive) = {cost_reactive}")
    end_time_reactive = time.time()
    total_time_reactive = end_time_reactive - start_time
    print(f"Time (Reactive) = {total_time_reactive} seg")
