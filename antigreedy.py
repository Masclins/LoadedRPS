import random
def antigreedyfunc(my_points, opp_points, my_loaded, opp_loaded, my_history, opp_history):
	if opp_loaded[0] > opp_loaded[1]:
		if opp_loaded[0] > opp_loaded[2]:
			return "P"
		elif opp_loaded[0] < opp_loaded[2]:
			return "R"
		else:
			return "R"
	elif opp_loaded[0] < opp_loaded[1]:
		if opp_loaded[1] > opp_loaded[2]:
			return "S"
		elif opp_loaded[1] < opp_loaded[2]:
			return "R"
		else:
			return "S"
	else:
		if opp_loaded[0] > opp_loaded[2]:
			return "P"
		elif opp_loaded[0] < opp_loaded[2]:
			return "R"
		else:
			return random.choice(["R","P","S"])		
