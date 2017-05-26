
def blodsocerfunc(my_points, opp_points, my_loaded, opp_loaded, my_history, opp_history):
    import random
    # tuned up an ready to go hopeful
    # s o c e r y
    if len(my_history) > 40 and len(set(opp_history[-30:])) == 1:
        if opp_history[-1] == "S":
            return "R"
        elif opp_history[-1] == "R":
            return "P"
        else:
            return "S"
        # against confused bots that only do one thing most of the time.
    elif len(my_history)>30 and min(opp_history.count(i) for i in "RPS")/max(opp_history.count(i) for i in "RPS") >0.8:
        return "RPS"[my_loaded.index(max(my_loaded))] # This is so if the other bot is acting errratic
                                                      # the max bonus is used for advantage
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
            return "R"
    elif len(my_history) < 15:
        if max(opp_loaded)<max(my_loaded):
            return "RPS"[len(my_history)%3]
        else:
            return "RPS"[(my_loaded.index(max(my_loaded))+len(my_history)%2)%3]
    elif len(my_history) == 15:
        if max(opp_loaded)<max(my_loaded):
            return "RPS"[(len(my_history)+1)%3]
        else:
            return "RPS"[(my_loaded.index(max(my_loaded))+ (len(my_history)%2)^1)%3]
    else:
        if max(opp_loaded)<max(my_loaded):
            return random.choice("RPS")
        else:
            return "RPS"[(my_loaded.index(max(my_loaded))+ (random.randint(0,1)))%3]
