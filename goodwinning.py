import random
def goodwinningfunc(no, yes, maybe, so, my_history, opp_history):
  if opp_history:
    me = my_history[len(my_history)-1]
    you = opp_history[len(opp_history)-1]
    if you == me:
      return goodwinningfunc(no, yes, maybe, so, my_history[:-1], opp_history[:-1])
    else:
      if me == "R":
        if you == "P":
          return "P"
        else:
          return "R"
      elif me == "P":
        if you == "S":
          return "S"
        else:
          return "R"
      else:
        if you == "R":
          return "R"
        else:
          return "P"
  else:
    return random.choice(["R","P","S"])
