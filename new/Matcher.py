#coding=utf-8
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
            setattr(typ,func.__name__,func)
            def warp(v,*args):
                return getattr(v,func.__name__)(*args)
            return warp
        return helper
    return matcher
env = {}
matcher = Match(env)
@matcher(Cons)
def length(self):
    return 1 + self.tl.length()
print( env )
@matcher(Empty)
def length(self):
    return 0
print( env )
print( length(tempList) )
@matcher(Cons)
def sum(self):
    return self.hd + self.tl.sum()
@matcher(Empty)
def sum(self):
    return 0
print( sum(tempList) )

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

#tmp = list(range(1800))
#t = list2List(tmp)
import sys
#sys.setrecursionlimit(2 ** 30)
#print( t )
#print( sum(t) )
#print( length(t) )

def Len(lst):
    if lst == []:
        return 0
    else:
        return 1 + Len(lst[1:])
#print( Len(range(10000) ) )
print( Len(list(range(10)) ) )
def test():
    frame = sys._getframe()
    print( dir(frame ) )
    frame.f_locals['a'] = 233
    print( frame.f_locals )
    while frame and frame.f_code.co_filename == Len:
        frame = frame.f_back
test()
