from fuzzy.norm.Norm import Norm

class DualOfHarmonicMean(Norm):

    def __init__(self):
        Norm.__init__(self,0) #XXX

    def __call__(self,*args):
        sum = reduce(lambda x,y:x+y, args)
        if sum == len(args): return 1.0
        product = reduce(lambda x,y:x*y, args)
        count = float(len(args))
        return (sum-count*product)/(count-sum) 