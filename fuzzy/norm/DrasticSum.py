from fuzzy.norm.Norm import Norm,NormException

class DrasticSum(Norm):

    def __init__(self):
        Norm.__init__(self,Norm.S_NORM)

    def __call__(self,*args):
        if len(args) != 2:
            raise NormException("%s is supported only for 2 parameters" % self.__class__.__name__ )
        x = float(args[0])
        y = float(args[1])
        if y == 0.0: return x
        if x == 0.0: return y
        return 1.0