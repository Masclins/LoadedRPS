def weigherfunc(my_points, opp_points, my_loaded, opp_loaded, my_history, opp_history):
    idx = {"R": 0, "P": 1, "S": 2}
    sc = [0, 0, 0]
    for i, m in enumerate(reversed(opp_history[-3:])):
        sc[idx[m]] += (1 / (1 + i))

    for i in range(3):
        sc[i] *= (opp_loaded[i] ** 2)

    return "PSR"[sc.index(max(sc))]
