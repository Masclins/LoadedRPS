from collections import Counter
import random
def useopponentsfunc(my_points, opp_points, my_loaded, opp_loaded, my_history, opp_history):
  if opp_history:
    data = Counter(opp_history)
    return data.most_common(1)[0][0]
  else:
    return random.choice(["R","P","S"])
