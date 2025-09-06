import time
from src.problems.qbf.solvers.reactive_grasp_qbf import ReactiveGRASP_QBF, ReactiveGRASP_QFG_First_Improvement
from src.problems.qbf.solvers.grasp_qbf import GRASP_QBF, GRASP_QBF_First_Improvement


if __name__ == "__main__":
    n = 400
    instancia = f"instances/qbf/qbf{n}"
    interations = 100
    alpha_1 = 0.1
    alpha_2 = 0.9
    resultados = [["name", "maxVal", "time"]]
    start_time = time.time()
    grasp = GRASP_QBF(alpha=alpha_2, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    end_time = time.time()
    total_time = end_time - start_time
    resultados.append(["GRASP QBF PADRÃO Best Improvement alfa=0.3", cost, total_time])

    start_time = time.time()
    grasp = GRASP_QBF(alpha=alpha_1, iterations=interations, filename=instancia)
    best_sol = grasp.solve()
    cost = - best_sol.cost
    resultados.append(["GRASP QBF PADRÃO Best Improvement alfa=0.1", cost, total_time])
    end_time = time.time()

    reactive_grasp = ReactiveGRASP_QBF(alpha_values=[0.1, 0.3, 0.5, 0.7, 0.9], iterations=interations, filename=instancia)
    best_sol_reactive = reactive_grasp.solve()
    cost_reactive = - best_sol_reactive.cost
    end_time_reactive = time.time()
    total_time_reactive = end_time_reactive - start_time
    resultados.append(["Reactive GRASP QBF Best Improvement", cost_reactive, total_time_reactive])

    start_time = time.time()
    grasp_first_improvement = GRASP_QBF_First_Improvement(alpha=alpha_2, iterations=interations, filename=instancia)
    best_sol_first_improvement = grasp_first_improvement.solve()
    cost_first_improvement = - best_sol_first_improvement.cost
    end_time_first_improvement = time.time()
    total_time_first_improvement = end_time_first_improvement - start_time
    resultados.append(["GRASP QBF First Improvement alfa=0.3", cost_first_improvement, total_time_first_improvement])

    start_time = time.time()
    grasp_first_improvement = GRASP_QBF_First_Improvement(alpha=alpha_1, iterations=interations, filename=instancia)
    best_sol_first_improvement = grasp_first_improvement.solve()
    cost_first_improvement = - best_sol_first_improvement.cost
    end_time_first_improvement = time.time()
    total_time_first_improvement = end_time_first_improvement - start_time
    resultados.append(["GRASP QBF First Improvement alfa=0.1", cost_first_improvement, total_time_first_improvement])

    start_time = time.time()
    reactive_grasp_first_improvement = ReactiveGRASP_QFG_First_Improvement(alpha_values=[0.1, 0.3, 0.5, 0.7, 0.9], iterations=interations, filename=instancia)
    best_sol_reactive_first_improvement = reactive_grasp_first_improvement.solve()
    cost_reactive_first_improvement = - best_sol_reactive_first_improvement.cost
    end_time_reactive_first_improvement = time.time()
    total_time_reactive_first_improvement = end_time_reactive_first_improvement - start_time
    resultados.append(["Reactive GRASP QBF First Improvement", cost_reactive_first_improvement, total_time_reactive_first_improvement])

    for resultado in resultados:
        print(f"{resultado[0]}: {resultado[1]} em {resultado[2]} segundos")
