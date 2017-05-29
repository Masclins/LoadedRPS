from random import choice
def antiantigreedyfunc(my_points, opp_points, my_loaded, opp_loaded, my_history, opp_history):
    if opp_loaded[0] > opp_loaded[1] and opp_loaded[0] > opp_loaded[2]:
        return "S"
    if opp_loaded[1] > opp_loaded[0] and opp_loaded[1] > opp_loaded[2]:
        return "R"
    if opp_loaded[2] > opp_loaded[0] and opp_loaded[2] > opp_loaded[1]:
        return "P"
    else:
        return choice(["R","P","S"])
