import numpy as np
import random

def nashfunc(my_points, opp_points, my_loaded, opp_loaded, my_history, opp_history):
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
            return random.choice("RPS")
        p /= tp
        q /= tq
        lr *= 0.9
    r = random.random()
    for i, pi in enumerate(p):
        r -= pi
        if r <= 0:
            break
    return "RPS"[i]
