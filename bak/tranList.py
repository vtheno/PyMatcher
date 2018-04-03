#coding=utf-8
""" 
target = type("target",(object,),{"__repr__":lambda self:"_"})() 
"""
from match import match
@match
def Length(x,*xs):
    if not isinstance(x,list):
        return 1 + Length(xs)
    return Length(x) + Length(xs)
@match
def Length():
    return 0
"""
def Length(A):
    if A == []:
        return 0
    else:
        x,xs = A[0],A[1:]
        if not isinstance(x,list):
            return 1 + Length(xs)
        return Length(x) + Length(xs)
"""

"""
def toList(A):
    if A == []:
        return []
    else:
        x,xs = A[0],A[1:]
        if not isinstance(x,list):
            return [x] + toList(xs)
        return toList(x) + toList(xs)
"""
@match
def toList():
    return []
@match
def toList(x,*xs):
    if not isinstance(x,list):
        return [x] + toList(xs)
    return toList(x) + toList(xs)

class Tran(object):
    def __init__(self,B):
        self.B = toList(B)
        self.T = self.B[0]
    def __call__(self,A):
        self.T = self.B[0] if self.B else []
        if A == [] :
            return []
        else:
            x,xs = A[0],A[1:]
            if not isinstance(x,list):
                self.B = self.B[1:]
                return [self.T] + self(xs)
            return [self(x)] + self(xs)
A=[1,[2,3],[4,[5],6],7,8,9]
B=[1,2,3,4,5,6,7,8,9]
C=[[1, 2, 3, 6], [2, 3, 6], [2, [2]]]
print "A:",A
print "B:",B
print "C:",C
print "A -> B:",Tran(A)(B)
print "B -> C:",Tran(B)(C)
print "C -> A:",Tran(C)(A)
print "B -> A:",Tran(B)(A)
print "C -> B:",Tran(C)(B)
print "A -> C:",Tran(A)(C)
