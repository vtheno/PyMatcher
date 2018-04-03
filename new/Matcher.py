#coding=utf-8
def Tail(func):
    def init(self,v):
        self.v = v
    def toString(self):
        return "(Ref {})".format(self.v)
    Ref = type("Ref",(),{"__init__":init,"__repr__":toString})
    info = Ref( (None,None) )
    def call(*args,**kw): # 此处应该交叉引用
        info.v = (args,kw)
        argv,kwd = info.v
        yield func (*argv,**kwd)
    return call
def force(g):
    while 1:
        try:
            g = next(g)
            #print (g)
        except Exception as e:
            #print (g,e)
            return g
List = type("List",(),{})
ListValue = type("ListValue",(List,),{})
def init(self,hd,tl): 
    self.hd = hd
    self.tl = tl
def toString(self):
    if not isinstance(self.tl,Empty):
        return "[{},{}]".format(self.hd,self.tl)
    return "[{}]".format(self.hd)

ConsEnv = {"__init__":init,"__str__":toString}
Cons = type("Constructor",(ListValue,),ConsEnv)
EmptyEnv = {}
Empty = type("EmptyList",(ListValue,),EmptyEnv)
print( Cons(1,Cons(2,Cons(3,Empty))) ) # <=> [1,2,3]
tempList = Cons(1,Cons(2,Cons(3,Cons(4,Empty()))))
print( dir(tempList) )

def setEnv(func,typ,env):
    if func.__name__ not in env.keys():
        env[func.__name__] = {typ.__name__:func}
    else:
        if typ.__name__ not in env[func.__name__].keys():
            env[func.__name__][typ.__name__] = func
        else:
            raise TypeError("SetEnv error")
    return env
def Match(Env={}):
    def matcher(typ):
        def helper(func): 
            setEnv(func,typ,Env)
            setattr(typ,func.__name__,Tail(func))
            def warp(v,*args):
                return getattr(v,func.__name__)(*args)
            return warp
        return helper
    return matcher
env = {}
matcher = Match(env)
@matcher(Cons)
def length(self,acc):
    return self.tl.length(acc+1)
print( env )
@matcher(Empty)
def length(self,acc):
    return acc
print( env )
print( force(length(tempList,0) ) )
@matcher(Cons)
def sum(self,acc):
    return self.tl.sum(self.hd + acc)
@matcher(Empty)
def sum(self,acc):
    return acc
print( force( sum(tempList,0) ) )

def list2List(lst):
    def init(self,v):
        self.v = v
    Ref = type("ref",(),{"__init__":init})
    temp = Ref( Cons(lst[0],Empty()) )
    tmp = temp.v
    lst = lst[1:]
    while lst:
        rest = Cons(lst[0],Empty())
        lst = lst[1:]
        tmp.tl = rest
        tmp = tmp.tl
    return temp.v

tmp = list(range(1000))
t = list2List(tmp)
import sys
#sys.setrecursionlimit(2 ** 30)
#print( t )
#print( sum(t) )
#print( length(t) )
@Tail
def Len(lst,acc):
    #print (lst)
    if lst == []:
        return acc
    else:
        return Len(lst[1:],acc+1)

#print( force(Len(list(range(10000)),0) ) )

