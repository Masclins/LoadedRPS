from random import *
def f(I):
    if I==0:return "R"
    if I==1:return "P"
    return "S"
def b(I):
    if I=="R":return 0
    if I=="P":return 1
    return 2
def ensemblefunc(mp,op,ml,ol,mh,oh):
    A=[0]*3
    B=[0]*3
    if(len(oh)):
        k=b(oh[-1])
        A[k-2]+=0.84
        A[k]+=0.29
        for x in range(len(oh)):
            g=b(oh[x])
            B[g-2]+=0.82
            B[g]+=0.22
        s=sum(B)
        for x in range(len(B)):
            A[x]+=(B[x]*1.04/s)
        r=max(A)
    else:
        r=randint(0,3)
    return f(r)
