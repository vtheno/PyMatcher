#coding=utf-8
from Tail import Tail
def force(object g):
    while type(g).__name__ == 'generator':
        g = next(g)
    return g

cpdef object setEnv(object func,object typ,object env):
    if func.__name__ not in env.keys():
        env[func.__name__] = {typ.__name__:func}
    else:
        if typ.__name__ not in env[func.__name__].keys():
            env[func.__name__][typ.__name__] = func
        else:
            raise TypeError("SetEnv error")
    return env
def Match(object Env):
    def matcher(object typ):
        def helper(object func): 
            setEnv(func,typ,Env)
            #setattr(typ,func.__name__,func)#Tail(func))
            setattr( typ,func.__name__,Tail(func) )
            def warp(v,*args):
                return getattr(v,func.__name__)(*args)
            return warp
        return helper
    return matcher
env = {}
matcher = Match(env)
