from fuzzy.norm.Norm import Norm,NormException

class HamacherSum(Norm):

    def __init__(self):
        Norm.__init__(self,Norm.S_NORM)

    def __call__(self,*args):
        if len(args) != 2:
            raise NormException("%s is supported only for 2 parameters" % self.__class__.__name__ )
        x = float(args[0])
        y = float(args[1])
        return (x+y-2.0*x*y)/(1.0-x*y)