import random
def greedyfunc(my_points, opp_points, my_loaded, opp_loaded, my_history, opp_history):
	if my_loaded[0] > my_loaded[1]:
		if my_loaded[0] > my_loaded[2]:
			return "R"
		elif my_loaded[0] < my_loaded[2]:
			return "S"
		else:
			return random.choice(["R","S"])
	elif my_loaded[0] < my_loaded[1]:
		if my_loaded[1] > my_loaded[2]:
			return "P"
		elif my_loaded[1] < my_loaded[2]:
			return "S"
		else:
			return random.choice(["P","S"])
	else:
		if my_loaded[0] > my_loaded[2]:
			return random.choice(["R","P"])
		elif my_loaded[0] < my_loaded[2]:
			return "S"
		else:
			return random.choice(["R","P","S"])		
