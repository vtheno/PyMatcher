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
        #print( "call info:",info.v)
        argv,kwd = info.v
        #print( "argv,kwd:",argv,kwd)
        #try:
        yield func (*argv,**kwd)
        #except RuntimeError as e:
        #print( "error:",info.v,type(e))
        #yield func (*(info.v[0]),**(info.v[1]))
    return call
#sys.setrecursionlimit(7)

@Tail
def fact2(n,acc):
    if n == 1:
        return acc
    else:
        return fact2(n-1,acc*n)

@Tail
def fact1(n):
    print (n)
    if n == 1:
        return 1
    else:
        return n  *  next ( fact1(n-1) )

nj = fact1(5000)
print ( nj )
while 1 :
    try:
        nj = next(nj)
    except Exception as e:
        print (nj,e)
        break
print( "nj:", nj )

def fact3(n):
    result = 1 
    while n > 1:
        result = result * n
        n -=1
    return result

print( fact2 )
info = fact2(50000,1)
while 1:
    try:
        info = next(info)
    except:
        #print( info )
        break
#print( "info:",info )
factz = fact3(50000)
#print( "factz:",factz )
print( factz == info )

