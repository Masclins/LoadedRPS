import random
def copycatfunc(I,dont,care,about,these,enmoves):
    if not enmoves:
        return random.choice(["R","P","S"])
    else:
        return enmoves[len(enmoves)-1]
