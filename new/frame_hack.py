#coding=utf-8
import sys
def Tail(func):
    def init(self,v):
        self.v = v
    def toString(self):
        return "(Ref {})".format(self.v)
    Ref = type("Ref",(),{"__init__":init,"__repr__":toString})
    info = Ref( (None,None) )
    def call(*args,**kw): # 此处应该交叉引用
        info.v = (args,kw)
        print( "call info:",info.v)
        argv,kwd = info.v
        #print( "argv,kwd:",argv,kwd)
        try:
            return func (*argv,**kwd)
        except RuntimeError as e:
            print( "error:",info.v,type(e))
            return func (*(info.v[0]),**(info.v[1]))
    return call

@Tail
def fact2(n,acc):
    if n == 1:
        return acc
    else:
        return fact2(n-1,acc*n)
def fact3(n):
    result = 1 
    while n > 1:
        result = result * n
        n -=1
    return result
#sys.setrecursionlimit(7)
print( fact2 )
info = fact2(500,1)
print( "info:",info )
def init(self,v):
    self.v = v
def toString(self):
    return "(Ref {})".format(self.v)
Ref = type("Ref",(),{"__init__":init,"__repr__":toString})
test = Ref ( ((2,),{}) )
fact = fact3(500)
print( "fact:",fact )
print( fact == info )

