#!/usr/bin/env python

try:
    # If the package has been installed correctly, this should work:
    import Gnuplot, Gnuplot.funcutils, Gnuplot.PlotItems
except ImportError:
    print "Sorry, you need Gnuplot to use this."
    import sys
    sys.exit(1)

def makePlotItem(points,title):
    # extend polygon so its is in [0:60]
    points.insert(0,(0,points[0][1]))
    points.append((60,points[-1][1]))
    l=[]
    for i in points:
	l.append(list(i))
    return Gnuplot.PlotItems.Data(l,inline=1,title=title, with="linespoints")

def plotPlotItems(items,title,filename):
    g = Gnuplot.Gnuplot()
    g.clear
    g('set data style lines')
    g('set noautoscale xy')
    g('set xrange [0:60]')
    g('set yrange [-0.2:1.2]')
#    g("set zeroaxis")
    g("set terminal png small color")
    g("set title '%s'" % title)
    g("set output 'merge/%s.png'" % filename)
    apply(g.plot,items)
    g("set terminal x11")
    g("set output")

def main():
    import fuzzy
    import fuzzy.System
    import fuzzy.Variable
    import fuzzy.OutputVariableCOG
    import fuzzy.Adjective
    import fuzzy.Rule
    import fuzzy.operator
    import fuzzy.operator.Input
    import fuzzy.norm
    import fuzzy.norm.Min
    import fuzzy.norm.Max
    import fuzzy.norm.AlgebraicProduct
    import fuzzy.norm.AlgebraicSum
    import fuzzy.set
    import fuzzy.set.Polygon
    import fuzzy.set.Trapez
    import fuzzy.set.Function
    import fuzzy.set.SFunction
    import fuzzy.set.ZFunction
    import fuzzy.set.PiFunction

    from fuzzy.set.Set import norm,merge

    a_set = fuzzy.set.PiFunction.PiFunction(a=30.,delta=20.)
    b_set = fuzzy.set.ZFunction.ZFunction(a=21.,delta=10.)
    c_set = fuzzy.set.SFunction.SFunction(a=42.,delta=15.)

    # Graphische Darstellung
    l_a=[]
    l_b=[]
    l_c=[]
    l_05=[]
    for i in range(0,61):
    	l_a.append([i,a_set(i)])
	l_b.append([i,b_set(i)])
	l_c.append([i,c_set(i)])
	l_05.append([i,0.5]) 
    p_a= Gnuplot.PlotItems.Data(l_a,inline=1,title="a: Pi a=30, delta=20", with="lines")
    p_b= Gnuplot.PlotItems.Data(l_b,inline=1,title="b: Z  a=21, delta=10", with="lines")
    p_c= Gnuplot.PlotItems.Data(l_c,inline=1,title="c: S  a=42, delta=15", with="lines")
    p_05= Gnuplot.PlotItems.Data(l_05,inline=1,title="constant value 0.5", with="lines")

    # test norm of in_set2 with different norm and 0.5
    p = norm(fuzzy.norm.Min.Min(),a_set,0.5)
    plotPlotItems([makePlotItem(p.points,"Min(a,0.5)"),p_a,p_05],"Min(a,0.5)","Min_a_0.5")
    p = norm(fuzzy.norm.Max.Max(),a_set,0.5)
    plotPlotItems([makePlotItem(p.points,"Max(a,0.5)"),p_a,p_05],"Max(a,0.5)","Max_a_0.5")
    p = norm(fuzzy.norm.AlgebraicProduct.AlgebraicProduct(),a_set,0.5)
    plotPlotItems([makePlotItem(p.points,"AlgebraicProduct(a,0.5)"),p_a,p_05],"AlgebraicProduct(a,0.5)","AlgebraicProduct_a_0.5")
    p = norm(fuzzy.norm.AlgebraicSum.AlgebraicSum(),a_set,0.5)
    plotPlotItems([makePlotItem(p.points,"AlgebraicSum(a,0.5)"),p_a,p_05],"AlgebraicSum(a,0.5)","AlgebraicSum_a_0.5")
    
    # test merge of a_set and b_set with different norms
    p = merge(fuzzy.norm.Min.Min(),a_set,b_set)
    plotPlotItems([makePlotItem(p.points,"Min(a,b)"),p_a,p_b],"Min(a,b)","Min_a_b")
    p = merge(fuzzy.norm.Max.Max(),a_set,b_set)
    plotPlotItems([makePlotItem(p.points,"Max(a,b)"),p_a,p_b],"Max(a,b)","Max_a_b")
    p = merge(fuzzy.norm.AlgebraicProduct.AlgebraicProduct(),a_set,b_set)
    plotPlotItems([makePlotItem(p.points,"AlgebraicProduct(a,b)"),p_a,p_b],"AlgebraicProduct(a,b)","AlgebraicProduct_a_b")
    p = merge(fuzzy.norm.AlgebraicSum.AlgebraicSum(),a_set,b_set)
    plotPlotItems([makePlotItem(p.points,"AlgebraicSum(a,b)"),p_a,p_b],"AlgebraicSum(a,b)","AlgebraicSum_a_b")

    p = merge(fuzzy.norm.AlgebraicProduct.AlgebraicProduct(),a_set,a_set)
    plotPlotItems([makePlotItem(p.points,"AlgebraicProduct(a,a)"),p_a],"AlgebraicProduct(a,a)","AlgebraicProduct_a_a")
    p = merge(fuzzy.norm.AlgebraicSum.AlgebraicSum(),a_set,a_set)
    plotPlotItems([makePlotItem(p.points,"AlgebraicSum(a,a)"),p_a],"AlgebraicSum(a,a)","AlgebraicSum_a_a")


    p = merge(fuzzy.norm.AlgebraicSum.AlgebraicSum(),c_set,merge(fuzzy.norm.AlgebraicProduct.AlgebraicProduct(),a_set,b_set))
    plotPlotItems([makePlotItem(p.points,"AlgebraicSum(c,AlgebraicProduct(a,b))"),p_a,p_b,p_c],"AlgebraicSum(c,AlgebraicProduct(a,b))","AlgebraicSum_c_AlgebraicProduct_a_b")

# when executed, just run main():
if __name__ == '__main__':
    main()
