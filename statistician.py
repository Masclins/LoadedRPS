import random
import collections

R, P, S = moves = range(3)
move_idx = {"R": R, "P": P, "S": S}
name = "RPS"
beat = (P, S, R)
beaten = (S, R, P)

def react(_0, _1, _2, _3, _4, opp_history):
    if not opp_history:
        return random.randrange(0, 3)
    return beat[opp_history[-1]]

def anti_react(_0, _1, _2, _3, _4, opp_history):
    if not opp_history:
        return random.randrange(0, 3)
    return beaten[opp_history[-1]]

def random_max(scores):
    scores = [s + random.normalvariate(0, 1) for s in scores]
    return scores.index(max(scores))

def greedy_margin(my_points, opp_points, my_loaded, opp_loaded, my_history, opp_history):
    scores = [my_loaded[move] - opp_loaded[beat[move]] for move in moves]
    return random_max(scores)

def anti_greedy(my_points, opp_pints, my_loaded, opp_loaded, my_history, opp_history):
    scores = [-my_loaded[move] for move in moves]
    return random_max(scores)

def recent_stats(my_points, opp_points, my_loaded, opp_loaded, my_history, opp_history):
    opp_history = opp_history[-10:-1]
    counts = collections.Counter(opp_history)
    scores = [(counts[beaten[move]] + 1) * my_loaded[move] - 
              (counts[beat[move]] + 1) * opp_loaded[move] for move in moves]
    return random_max(scores)

def statisticianfunc(_0, _1, _2, _3, my_history, opp_history):
    m1 = []
    o1 = []
    my_loaded = [0] * 3
    opp_loaded = [0] * 3
    my_points = 0
    opp_points = 0
    strategies = [react, anti_react, greedy_margin, anti_greedy, recent_stats]
    strategy_scores = [0 for _ in strategies]
    for i, (mx, ox) in enumerate(zip(my_history, opp_history)):
        mx = move_idx[mx]
        ox = move_idx[ox]
        for j, strategy in enumerate(strategies):
            strategy_scores[j] *= 0.98
            move = strategy(my_points, opp_points, my_loaded, opp_loaded, m1, o1)
            if move == beat[ox]:
                strategy_scores[j] += my_loaded[move]
            elif move == beaten[ox]:
                strategy_scores[j] -= opp_loaded[ox]
        m1.append(mx)
        o1.append(ox)
        if mx == beat[ox]:
            opp_loaded[ox] += 1
            my_points += my_loaded[mx]
        elif mx == beaten[ox]:
            my_loaded[mx] += 1
            opp_points += opp_loaded[ox]
        else:
            my_loaded[mx] += 0.5
            opp_loaded[ox] += 0.5
    strategy = strategies[random_max(strategy_scores)]
    return name[strategy(my_points, opp_points, my_loaded, opp_loaded, m1, o1)]
