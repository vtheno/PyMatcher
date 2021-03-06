#coding=utf-8
from Match.cMatcher import *
List = type("List",(),{})
ListValue = type("ListValue",(List,),{})
def init(self,hd,tl): 
    self.hd = hd
    self.tl = tl
def toString(self):
    if not isinstance(self.tl,Empty):
        return "[{},{}]".format(self.hd,self.tl)
    return "[{}]".format(self.hd)
ConsEnv = {"__init__":init,}#"__str__":toString}
Cons = type("Constructor",(ListValue,),ConsEnv)
EmptyEnv = {}
Empty = type("EmptyList",(ListValue,),EmptyEnv)
print( Cons(1,Cons(2,Cons(3,Empty))) ) # <=> [1,2,3]
tempList = Cons(1,Cons(2,Cons(3,Cons(4,Empty()))))
#print( dir(tempList) )
@matcher(Cons)
def length(self,acc):
    return self.tl.length( acc+1 )
@matcher(Empty)
def length(self,acc):
    return acc

def mLength(s):
    return force(s.length(0))

print( force( Empty().length(0) ) )
print( force(tempList.length(0)) )
print( mLength(tempList) )

@matcher(Cons)
def sum(self,acc):
    return self.tl.sum(self.hd + acc)
@matcher(Empty)
def sum(self,acc):
    return acc
def mSum(s):
    return force( s.sum(0) )
print( force( sum(tempList,0) ) )
print( force( tempList.sum(0) ) )
print( mSum(tempList) )
@matcher(Cons)
def elem(self,element,acc):
    if element == self.hd:
        return True
    else:
        return self.tl.elem(element,acc)
@matcher(Empty)
def elem(self,element,acc):
    return acc
def mElem(s,element):
    return force( s.elem(element,False) )
print( force( elem(tempList,2,False) ) )
print( force( tempList.elem(2,False) ) )
print( mElem( tempList , 2) )
@matcher(Cons)
def foldl(self,func,acc):
    return self.tl.foldl(func,func(self.hd,acc))
@matcher(Empty)
def foldl(self,func,acc):
    return acc

def mFoldl(func,acc,s):
    return force(s.foldl(func,acc))
print ( tempList )
print( force (foldl( tempList,lambda x,y:x+y,0 ) ) )
print( force (tempList.foldl(lambda x,y:x+y,0)) )
print( mFoldl(lambda x,y:x+y,0,tempList))

