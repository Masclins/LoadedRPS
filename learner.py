import random
import numpy as np
def patternfunc(my_points, opp_points, my_loaded, opp_loaded, my_history, opp_history):
	if len(opp_history) <= 2:
		return ["R", "P", "S"][len(opp_history)]
	elif len(opp_history) == 3:
		return random.choice(["R","P","S"])

	nm = [[0]*3]*3
	no = [[0]*3]*3

	for (i in range(1, len(opp_history))):
		cm0 = my_history[i-1]
		co0 = opp_history[i-1]
		co1 = opp_history[i]	


 

	if len(opp_history) == 0:
		return random.choice(["R","P","S"])
	elif len(opp_history) == 1:
		if opp_history == "R":
			return "P"
		elif opp_history == "P":
			return "S"
		elif opp_history == "S":
			return "R"

	p = np.array([1/3]*3)
	c = opp_history[-1]
	for i in range(1, len(opp_history)):
		c0 = opp_history[i-1]
		c1 = opp_history[i]
		if c0 == c:
			p *= .9
			if c1 == "R":
				p[0] += .1
			elif c1 == "P":
				p[1] += .1
			elif c1 == "S":
				p[2] += .1

	idx = p.tolist().index(max(p))
	return ["P", "S", "R"][idx]	
