def bobwfunc(my_points, opp_points, my_loaded, opp_loaded, my_history, opp_history):
    opp_max = "PSR"
    play_opp = [max(opp_loaded), opp_max[opp_loaded.index(max(opp_loaded))]]

    self_max = "RPS"
    play_self = [max(my_loaded), self_max[my_loaded.index(max(my_loaded))]]

    if play_opp[1] == play_self[1]: return play_opp[1]
    else: return play_self[1] if play_opp[0] < play_self[0] else play_opp[1]
