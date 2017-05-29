import random

selection_set = ["R", "P", "S"]
selection_set.pop(random.randint(0,2))
def weightedrandomfunc(my_points, opp_points, my_loaded, opp_loaded, my_history, opp_history):
    return random.choice(selection_set)
