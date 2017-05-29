from random import choice
def somewhathungryfunc(blah, blah2, load, blah3, blah4, blah5):
    if load[0] > load[1] and load[0] < load[2] or load[0] < load[1] and load[0] > load[2]:
        return "R"
    if load[1] > load[0] and load[1] < load[2] or load[1] < load[0] and load[1] > load[2]:
        return "P"
    if load[2] > load[1] and load[2] < load[0] or load[2] < load[1] and load[2] > load[0]:
        return "S"
    else:
        return choice(["R","P","S"])
