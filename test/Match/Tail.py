def Tail(func):
    def __call__(*args,**kw):
        yield func(*args,**kw)
    return __call__
