from random import choice
def antirepeaterfunc(my_points, opp_points, my_loaded, opp_loaded, my_history, opp_history):
    s = opp_history.count("S")
    r = opp_history.count("R")
    p = opp_history.count("P")

    if s>p and s>r:
        return "R"
    elif p>s and p>r:
        return "S"
    else:
        return "P"
