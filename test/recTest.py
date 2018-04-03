#coding=utf-8
from Match.cMatcher import *
print( dir() )
@Tail
def Len(lst,acc):
    if lst == []:
        return acc
    return Len(lst[1:],acc+1)

def len(lst):
    return force(Len(lst,0))

test = list(range(40000))
print ( len(test) )
