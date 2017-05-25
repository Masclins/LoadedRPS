import random
def artsychildfunc(my_points, opp_points, my_loaded, opp_loaded, my_history, opp_history):
    if len(opp_history) == 0:
            return "P"
    elif opp_history[-1] == "R":
            return "R"
    elif my_history[-1] != "P":
            return "P"
    else:
            return random.choice(["P", "S"])
