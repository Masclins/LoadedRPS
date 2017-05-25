def blodsocerfunc(my_points, opp_points, my_loaded, opp_loaded, my_history, opp_history):
    import random
    # s o c e r y
    if len(my_history) > 40 and len(set(opp_history)) == 1:
        if opp_history[1] == "S":
            return "R"
        elif opp_history[1] == "R":
            return "P"
        else:
            return "S"
    elif min(opp_history.count(i) for i in "RPS")/max(opp_history.count(i) for i in "RPS") >0.8 and len(my_history)>30:
        return "RPS"[my_loaded.index(max(my_loaded))]
    elif len(my_history) < 10:
        if len(my_history) > 2 and all(i == "S" for i in opp_history[1:]):
            if len(my_history) > 5: return "S"
            return "P"
        return "S" # Be careful, because scissors are SHARP
    elif len(set(opp_history[1:10])) == 1 and len(my_history) < 20:
        if opp_history[1] == "S":
            return "R"
        elif opp_history[1] == "R":
            return "R"
        else:
            return "P"
    elif len(opp_history) -  max(opp_history.count(i) for i in "RPS") < 4 and len(my_history) < 30:
        if opp_history.count("R") > max(opp_history.count(i) for i in "PS"):
            return "P"
        if opp_history.count("P") > max(opp_history.count(i) for i in "RS"):
            return "S"
        if opp_history.count("S") > max(opp_history.count(i) for i in "RP"):
            "R"
    elif len(my_history) < 15:
        if max(opp_loaded)<max(my_loaded):
            return "RPS"[my_loaded.index(max(my_loaded))+len(my_history)%2]
        else:
            return "RPS"[opp_loaded.index(max(opp_loaded))-len(my_history)%2]
    elif len(my_history) == 15:
        if max(opp_loaded)<max(my_loaded):
            return "RPS"[my_loaded.index(max(my_loaded))+ (len(my_history)%2)^1]
        else:
            return "RPS"[opp_loaded.index(max(opp_loaded)) - (len(my_history)%2)^1]
    else:
        if max(opp_loaded)<max(my_loaded):
            return "RPS"[my_loaded.index(max(my_loaded))+ (random.randint(0,1))]
        else:
            return "RPS"[opp_loaded.index(max(opp_loaded)) - (random.randint(0,1))]
