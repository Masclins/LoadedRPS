import random
def nashbotfunc(my_points, opp_points, my_loaded, opp_loaded, my_history, opp_history):
    r = opp_loaded[0] * opp_loaded[2]
    p = opp_loaded[0] * opp_loaded[1]
    s = opp_loaded[1] * opp_loaded[2]
    q = random.uniform(0, r + p + s) - r
    return "R" if q < 0 else "P" if q < p else "S"
