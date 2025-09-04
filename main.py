

import time
import numpy as np
from src.problems.qbf.solvers.grasp_qbf import GRASP_QBF
from src.problems.qbf.solvers.reactive_grasp_qbf import ReactiveGRASP_QBF


if __name__ == "__main__":
    instancia = "instances/qbf/qbf020"
    start_time = time.time()
    reactive_grasp = ReactiveGRASP_QBF([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], 1000, instancia, reactive_update_block=50)
    best_sol_reactive = reactive_grasp.solve()
    print(f"maxVal (Reactive) = {best_sol_reactive}")
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Time (Reactive) = {total_time} seg")
    