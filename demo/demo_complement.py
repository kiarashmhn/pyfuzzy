#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#
# Generate plots of all available fuzzy set classes using their default values
# after processing with all available fuzzy complement classes.
# The result are some images, which you have to check by yourself.
# (They are also useful to put on the website.)
#
# Copyright (C) 2009  Rene Liebscher
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free 
# Software Foundation; either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT 
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License along with 
# this program; if not, see <http://www.gnu.org/licenses/>. 
#

__revision__ = "$Id: demo_complement.py,v 1.1 2009-08-31 20:57:49 rliebscher Exp $"

try:
    # If the package has been installed correctly, this should work:
    import Gnuplot, Gnuplot.funcutils
except ImportError:
    print "Sorry, you need Gnuplot to use this."
    import sys
    sys.exit(1)

from utils import get_classes

x_min,x_max = -1.5,+1.5

def getGnuplot():
    # A straightforward use of gnuplot.  The `debug=1' switch is used
    # in these examples so that the commands that are sent to gnuplot
    # are also output on stderr.
    g = Gnuplot.Gnuplot(debug=0)
    g(' set style fill solid 0.5 border')
    g('set style data filledcurves y1=0')
    g('set noautoscale xy')
    g('set xrange [%f:%f]' % (x_min,x_max))
    g('set yrange [-0.2:1.2]')
    g.xlabel('x')
    g.ylabel('y')
    return g

def test():
    """Plot all defined classes in fuzzy.set package"""

    import fuzzy.set
    import fuzzy.set.operations
    import fuzzy.complement

    steps = 50
    # make array in range x_min,x_max
    x = [ i*(x_max-x_min)/float(steps) + x_min for i in range(steps) ]

    objects = get_classes(fuzzy.set)
    complements = get_classes(fuzzy.complement)
    print complements

    # add demo sets
    from fuzzy.set.Polygon import Polygon
    objects["Polygon (Demo)"] = Polygon([
            (-1.2,0),
            (-1.2,1),
            (-0.8,0.3),
            (-0.3,0.2),
            (-0.2,0.4),
            (-0.1,0.0),
            (0.0,0.0),
            (0.3,1),
            (0.6,0.5),
            (0.6,0.1),
            (1.3,0.6),
        ])
    for name in sorted(objects):
        if name in ["Set", "Function","Polygon"]:
            continue
        obj = objects[name]
        print obj,name

        for name2 in sorted(complements):
            if name2 in ["Base"]:
                continue
            c = complements[name2]
            print c,name2

            obj_c = fuzzy.set.operations.complement(c,obj)

            g = getGnuplot()
            g.title(name)

            try:
                print "Plot %s ... " % name
                g("set terminal png small truecolor")
                g("set output 'complement/%s_%s.png'" % (name2,name))
                if isinstance(obj_c,fuzzy.set.Polygon.Polygon):
                    p = obj_c.points
                    if len(p) == 0:
                        continue
                    if p[0][0]>x_min:
                        p.insert(0,(x_min,p[0][1]))
                    if p[-1][0]<x_max:
                        p.append((x_max,p[-1][1]))
                    g.plot(p)
                else:
                    g.plot(Gnuplot.funcutils.compute_Data(x,obj_c))
            except:
                import traceback
                traceback.print_exc()
            #raw_input('Please press return to continue...\n')
            #g.close()
            g = None

# when executed, just run test():
if __name__ == '__main__':
    test()
