
from random import *
def f(I):
    if I==0:return "R"
    if I==1:return "P"
    return "S"
def b(I):
    if I=="R":return 0
    if I=="P":return 1
    return 2
def swapfunc(mp,op,ml,ol,mh,oh):
    A=[0]*3
    B=[0]*3
    if(len(mh)):
        r=(b(mh[-1])+randint(1,2))%3
    else:
        r=randint(0,3)
    return f(r)
