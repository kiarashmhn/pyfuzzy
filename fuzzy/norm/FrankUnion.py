from fuzzy.norm.Norm import NormException
from fuzzy.norm.ParametricNorm import ParametricNorm
from math import log

class FrankUnion(ParametricNorm):

    def __init__(self,p=0.5):
        ParametricNorm.__init__(self,ParametricNorm.S_NORM,p)

    def __call__(self,*args):
        if len(args) != 2:
            raise NormException("%s is supported only for 2 parameters" % self.__class__.__name__ )
        p = self.p
        x = float(args[0])
        y = float(args[1])
        return 1.0-log(1.0+(pow(p,1.0-x)-1.0)*(pow(p,1.0-y)-1.0)/(p-1.0))/log(p)