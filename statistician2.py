import random
import collections
import numpy as np

R, P, S = moves = range(3)
move_idx = {"R": R, "P": P, "S": S}
names = "RPS"
beat = (P, S, R)
beaten = (S, R, P)

def react(my_loaded, opp_loaded, my_history, opp_history):
    if not opp_history:
        return random.randrange(0, 3)
    counts = [0, 0, 0]
    counts[beat[opp_history[-1]]] += 1
    return counts

def random_max(scores):
    scores = [s + random.normalvariate(0, 1) for s in scores]
    return scores.index(max(scores))

def argmax(scores):
    m = max(scores)
    return [s == m for s in scores]

def greedy_margin(my_loaded, opp_loaded, my_history, opp_history):
    scores = [my_loaded[move] - opp_loaded[beat[move]] for move in moves]
    return argmax(scores)

recent_counts = None

def best_move(counts, my_loaded, opp_loaded):
    scores = [(counts[beaten[move]] + 0.5) * my_loaded[move] - 
              (counts[beat[move]] + 0.5) * opp_loaded[move] for move in moves]
    return argmax(scores)

def recent_stats(my_loaded, opp_loaded, my_history, opp_history):
    if len(opp_history) >= 10:
        recent_counts[opp_history[-10]] -= 1
    recent_counts[opp_history[-1]] += 1
    return best_move(recent_counts, my_loaded, opp_loaded)

order2_counts = None

def order2(my_loaded, opp_loaded, my_history, opp_history):
    if len(my_history) >= 2:
        base0 = 9 * my_history[-2] + 3 * opp_history[-2]
        order2_counts[base0 + opp_history[-1]] += 1
    base1 = 9 * my_history[-1] + 3 * opp_history[-1]
    counts = [order2_counts[base1 + move] for move in moves]
    return best_move(counts, my_loaded, opp_loaded)

def nash(my_loaded, opp_loaded, my_history, opp_history):
    third = 1.0 / 3
    p = np.full(3, third)
    q = np.full(3, third)
    u = np.array(my_loaded)
    v = np.array(opp_loaded)
    m0 = np.zeros(3)
    m1 = np.zeros(3)
    lr = 0.2
    for _ in range(10):
        de0 = u * np.roll(q, 1) - np.roll(v * q, 2)
        de1 = v * np.roll(p, 1) - np.roll(u * p, 2)
        m0 = 0.9 * m0 + 0.1 * de0
        m1 = 0.9 * m1 + 0.1 * de1
        p += lr * m0
        q += lr * m1
        p[p < 0] = 0
        q[q < 0] = 0
        tp, tq = np.sum(p), np.sum(q)
        if tp == 0 or tq == 0:
            return np.full(3, third)
        p /= tp
        q /= tq
        lr *= 0.9
    return p

strategies = [react, greedy_margin, recent_stats, order2, nash]

predictions = strategy_scores = mh = oh = None

def statistician2func(my_points, opp_points, my_loaded, opp_loaded, my_history, opp_history):
    global strategy_scores, history, recent_counts, mh, oh, predictions, order2_counts
    if not opp_history:
        strategy_scores = [0 for _ in strategies]
        recent_counts = collections.Counter()
        order2_counts = collections.Counter()
        mh, oh = [], []
        predictions = None
        return random.choice(names)
    my_move = move_idx[my_history[-1]]
    opp_move = move_idx[opp_history[-1]]
    if predictions is not None:
        for j, p in enumerate(predictions):
            good = beat[opp_move]
            bad = beaten[opp_move]
            strategy_scores[j] += (my_loaded[good] * p[good] - opp_loaded[opp_move] * p[bad]) / sum(p)
    mh.append(my_move)
    oh.append(opp_move)
    predictions = [strategy(my_loaded, opp_loaded, mh, oh) for strategy in strategies]
    strategy = random_max(strategy_scores)
    p = predictions[strategy]
    r = random.random()
    for i, pi in enumerate(p):
        r -= pi
        if r <= 0:
            break
    return names[i]
