#coding=utf-8
# Record = dict
# tuple  = all key is inc Seq <Num>
# tuple as arguments 
record1 = {
    1:"abc",
    2:"cba"
}
Record = type("Record",(type,),{})
def record2tuple(record):
    keys = record.keys()
    values = tuple(record.values())
    typeOfvalues = map(type,values)
    print( keys,typeOfvalues,values )
    return values
def tuple2record(tupl):
    keys = range(len(tupl))
    return dict(zip(keys,tupl))
print( record2tuple( tuple2record ( record2tuple(record1) ) ) )
n
class MatchError(Exception): pass

class Switch(object):
    def __init__(self,funcs):
        self.funcList = funcs
    def __call__(self,argv):
        for func in self.funcList:
            try:
                result = apply(func,argv)
                return result
            except TypeError,e:
                continue
        raise MatchError ( "Something bug" )

def Match():
    env = {}
    def match(func):
        if func.__name__ in env.keys():
            env[func.__name__].append(func)
            print( env )
        else:
            env[func.__name__] = [func]
            print( env )
        temp = Switch(env[func.__name__])
        def helper(argv):
            return temp(argv)
        return helper
    return match

match = Match()
@match
def mSum(x,*xs):
    #print x,xs
    return x + mSum (xs)
@match
def mSum(): # this nothing in tuple 
    #print "emptyList:",emptyList
    print "Matcher!"
    return 0#emptyList
print mSum
print( mSum([1,2,3,4,5]) )

#List = type("List",(list,),{"__or__":lst,})
#Func = type("Func",(tuple,),{"__lt__":tup,})
class t(object):
    def __ror__(self,a):
        try:
            self.left = tuple(a)
        except TypeError:
            self.left = (a)
        return self
    def __gt__(self,b):
        print "b:",b
        return b(self.left)

I = t()
print 233 |I> (lambda f:f+1)
@match
def fun(x,*xs):
    return 1 + fun (xs) # |I> fun)
    
@match
def fun():
    return 0
#print [1,2] |I> fun
print fun([1,2])
print [1,2] |I> (lambda x:x)
A = any
E = all
def elem(a):
    @match
    def elemc(x,*xs):
        return True if x==a else elemc(xs)
    @match
    def elemc():
        return False
    return elemc
print elem(1)([0,2,3,4,5])
