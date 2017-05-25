import random
def economistfunc(my_points, opp_points, my_loaded, opp_loaded, my_history, opp_history):
	if len(opp_history) == 0:
		return random.choice(["R","P","S"])
	if len(opp_history) > 9:
		opp_history = opp_history[-10:-1]
	p = [opp_history.count("R"), opp_history.count("P"), opp_history.count("S")]
	
	value = [(p[2]*my_loaded[0] - p[1]*opp_loaded[1], "R"), (p[0]*my_loaded[1] - p[2]*opp_loaded[2], "P"), (p[1]*my_loaded[2] - p[0]*opp_loaded[0], "S")]
	value.sort()
	
	if value[-1][0] > value[-2][0]:
		return value[-1][1]
	elif value[-1][0] > value[-3][0]:
		return random.choice([value[-1][1], value[-2][1]])
	else:
		return random.choice(["R","P","S"])

