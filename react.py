import random
def reactfunc(I, do, not_, need, these, opp_history):
    if not opp_history:
        return random.choice(["R","P","S"])
    else:
        prev=opp_history[len(opp_history)-1]
        if prev == "R":
            return "P"
        if prev == "P":
            return "S"
        else:
            return "R"
