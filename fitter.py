import random
import numpy as np
def fitterfunc(my_points, opp_points, my_loaded, opp_loaded, my_history, opp_history):
	t = len(opp_history)
	RPS = ["R","P","S"]
	if t <= 2:
		return RPS[t]
	elif t == 3:
		return random.choice(RPS)

	def n(c): return RPS.index(c)

	total_me = np.zeros(shape=(3,3))
	total_opp= np.zeros(shape=(3,3))
	p_me = np.array([[1/3]*3]*3)
	p_opp = np.array([[1/3]*3]*3)

	for i in range(1, t):
		total_me[n(my_history[i-1]), n(opp_history[i])] += 1
		total_opp[n(opp_history[i-1]), n(opp_history[i])] += 1
	for i in range(3):
		if np.sum(total_me[i,:]) != 0:
			p_me[i,:] = total_me[i,:] / np.sum(total_me[i,:])
		if np.sum(total_opp[i,:]) != 0:
			p_opp[i,:] = total_opp[i,:] / np.sum(total_opp[i,:])

	error_me = 0
	error_opp = 0

	for i in range(1, t):
		diff = 1 - p_me[n(my_history[i-1]), n(opp_history[i])]
		error_me += diff * diff
		diff = 1 - p_opp[n(opp_history[i-1]), n(opp_history[i])]
		error_opp += diff * diff
	
	if error_me < error_opp:
		p = p_me[n(my_history[-1]),:]
	else:
		p = p_opp[n(opp_history[-1]),:]


# From here, right now I weight values, though not 100% is the best idea, I leave the alternative in case I'd feel like changing it
	value = [(p[2]*my_loaded[0] - p[1]*opp_loaded[1], "R"), (p[0]*my_loaded[1] - p[2]*opp_loaded[2], "P"), (p[1]*my_loaded[2] - p[0]*opp_loaded[0], "S")]
	value.sort()

	if value[-1][0] > value[-2][0]:
		return value[-1][1]
	elif value[-1][0] > value[-3][0]:
 		return random.choice([value[-1][1], value[-2][1]])
	else:
		return random.choice(RPS)

#	idx = p.tolist().index(max(p))
#	return ["P", "S", "R"][idx]	
