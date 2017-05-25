import random
def yggdrasilfunc(my_points, opp_points, my_loaded, opp_loaded, my_history, opp_history):
    cache = {}
    R = 0
    P = 1
    S = 2
    def get(turn, ml, ol):
        key = str(turn) + str(ml) + str(ol)
        if not key in cache:
            cache[key] = State(turn, ml, ol)
        return cache[key]

    def wrand(opts):
        total = sum(abs(w) for c,w in opts.items())
        while True:
            r = random.uniform(0, total)
            for c, w in opts.items():
                r -= abs(w)
                if r < 0:
                    return c
            print("error",total,r)

    class State():
        turn = 0
        ml = [1,1,1]
        ol = [1,1,1]
        val = 0
        strat = [1/3, 1/3, 1/3]
        depth = -1
        eps = 0.0001
        maxturn = 1000

        def __init__(self, turn, ml, ol):
            self.turn = turn
            self.ml = ml
            self.ol = ol
        def calcval(self, depth):
            if depth <= self.depth:
                return self.val
            if turn >= 1000:
                return 0
            a = 0
            b = -self.ol[P]
            c = self.ml[R]
            d = self.ml[P]
            e = 0
            f = -self.ol[S]
            g = -self.ol[R]
            h = self.ml[S]
            i = 0
            if depth > 0:
                a += get(self.turn+1,[self.ml[R]+1,self.ml[P],self.ml[S]],[self.ol[R]+1,self.ol[P],self.ol[S]]).calcval(depth-1)
                b += get(self.turn+1,[self.ml[R]+2,self.ml[P],self.ml[S]],[self.ol[R],self.ol[P],self.ol[S]]).calcval(depth-1)
                c += get(self.turn+1,[self.ml[R],self.ml[P],self.ml[S]],[self.ol[R],self.ol[P],self.ol[S]+2]).calcval(depth-1)
                d += get(self.turn+1,[self.ml[R],self.ml[P],self.ml[S]],[self.ol[R]+2,self.ol[P],self.ol[S]]).calcval(depth-1)
                e += get(self.turn+1,[self.ml[R],self.ml[P]+1,self.ml[S]],[self.ol[R],self.ol[P]+1,self.ol[S]]).calcval(depth-1)
                f += get(self.turn+1,[self.ml[R],self.ml[P]+2,self.ml[S]],[self.ol[R],self.ol[P],self.ol[S]]).calcval(depth-1)
                g += get(self.turn+1,[self.ml[R],self.ml[P],self.ml[S]+2],[self.ol[R],self.ol[P],self.ol[S]]).calcval(depth-1)
                h += get(self.turn+1,[self.ml[R],self.ml[P],self.ml[S]],[self.ol[R],self.ol[P]+2,self.ol[S]]).calcval(depth-1)
                i += get(self.turn+1,[self.ml[R],self.ml[P],self.ml[S]+1],[self.ol[R],self.ol[P],self.ol[S]+1]).calcval(depth-1)
            self.val = -9223372036854775808
            for pr in range(0,11):
                for pp in range(0,11-pr):
                    ps = 10-pr-pp
                    thisval = min([pr*a+pp*d+ps*g,pr*b+pp*e+ps*h,pr*b+pp*f+ps*i])
                    if thisval > self.val:
                        self.strat = [pr,pp,ps]
                        self.val = thisval
            self.val /= 10


            if depth == 0:
                self.val *= min(self.val, self.maxturn - self.turn)
            return self.val

    turn = len(my_history)
    teststate = get(turn, [x * 2 for x in my_loaded], [x * 2 for x in opp_loaded])
    teststate.calcval(1)
    return wrand({"R":teststate.strat[R],"P":teststate.strat[P],"S":teststate.strat[S]})
