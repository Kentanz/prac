def varArgs(*args):
       print(args)

varArgs()
varArgs(1)
varArgs(1,2)
varArgs(1,2,3)


def varKwargs(**kwargs):
    print(kwargs)
varKwargs()
varKwargs(a=1)
varKwargs(a=1,b=2)
varKwargs(a=1,b=2,x=3)
