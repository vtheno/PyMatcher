#coding=utf-8
__all__ = ["Tail","force","matcher","Match","env"]
def Tail(func):
    def call(*args,**kw): # x
        yield func (*args,**kw)
    return call
def force(g):
    while type(g).__name__ == 'generator':
        g = next(g)
    return g

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
