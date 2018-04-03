#coding=utf-8
def force(g):
    while type(g).__name__ == 'generator':
        g = next(g)
    return g
def Tail(func):
    def call(*args,**kw):
        yield func(*args,**kw)
    return call
@Tail
def tail_fact(n,acc):
    if n == 0 :
        return acc
    else:
        return tail_fact(n-1,acc*n)

def fact(n):
    return force(tail_fact(n,1))

fact1 = fact(500)
print( fact1 )
