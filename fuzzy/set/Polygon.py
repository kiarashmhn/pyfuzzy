from fuzzy.set.Set import Set

class Polygon(Set):
    """Represents a fuzzy set, which membership function
       is the shape of a polygon. For example: triangle,
       trapezoid, rectangle, or something similar."""

    # indices for coordinate tuple
    X = 0
    Y = 1
    
    def __init__(self):
        Set.__init__(self)
	self.points = []

    def __call__(self,x):
	"""Get membership of value x."""

        # first handle obvious cases	
        if self.points == []:
            return 0.0
        if len(self.points) == 1:
            return self.points[0][Polygon.Y]
        if x < self.points[0][Polygon.X]:
            return self.points[0][Polygon.Y]
        if x > self.points[-1][Polygon.X]:
            return self.points[-1][Polygon.Y]

        x0 = self.points[0][Polygon.X];
        for i in range(1,len(self.points)):
            x1 = self.points[i][Polygon.X]
            # found right interval
            if x1 < x:
                x0 = x1
                continue
            y0 = self.points[i-1][Polygon.Y]
            y1 = self.points[i][Polygon.Y]
            # interpolate value in interval
            if x1==x0:
                return y0
            return y0+(y1-y0)/(x1-x0)*(x-x0)
        return 0.0 # should never be reached
    
    # at which end do we insert or remove a point
    BEGIN = 0
    END = 1
        
    def add(self,x,y,where=END):
	"""Add a new point to the polygon.
	   The parameter where controls at which end
	   it is inserted. (The points are always sorted, but
	   if two have the same x value their order is important.
	   For example: adding a second point(y=0) in the middle
	   now           where=END        where=BEGIN 
           *--*           *--*             *  *    
               \             |              \ |\   
                \            |               \| \    
                 *           *--*             *  *    
        """
	# quick and dirty implementation
	if where == self.END:
            self.points.append((x,y))
        else:
            self.points.insert(0,(x,y))
        # use only x value for sorting
        self.points.sort(lambda x,y:cmp(x[0],y[0]))


    def remove(self,x,where=END):
	"""Remove a point from the polygon.
	   The parameter where controls at which end
	   it is removed. (The points are always sorted, but
	   if two have the same x value their order is important.
	   For example: removing the second point in the middle
	   now           where=END        where=BEGIN  
	   *--*           *--*             *      
	      |               \             \     
	      |                \             \     
	      *--*              *             *--*    
        """
	# quick and dirty implementation
        range = range(len(self.points))
	if where == self.END:
            range.reverse()
	for i in range:
            if self.points[i][X] == x:
                self.points.remove(i)
                return
        #raise Exception("Not in points list")

    def clear(self):
	"""Reset polygon to zero."""
	del self.points[:]

    def getIntervalGenerator(self):
        return self.__IntervalGenerator(self.points)

    class __IntervalGenerator(Set.IntervalGenerator):
        def __init__(self,points):
            self.points = points
            self.index = 0
        
        def nextInterval(self,prev,next):
            l = len(self.points) 
            if l==0 or self.index>=l:
                return next
            if prev is None:
                self.index = 0
            else:
                if prev == self.points[self.index][Polygon.X]:
                    self.index = self.index + 1
                if self.index >= l:
                    return next
            if next is None:
                return self.points[self.index][Polygon.X]
            else:
                return min(next,self.points[self.index][Polygon.X])

    def getCOG(self):
	"""Return center of gravity."""
	if len(self.points) <=1 :
	    #return 0.0
            raise Exception("no COG calculable: single point = constant value")
        if self.points[0][Polygon.Y] > 0 or self.points[-1][Polygon.Y] > 0:
            raise Exception("no COG calculable: end points of polygon not y=0.0")
        _Flaeche = 0.
        _Schwerpunkt = 0.
        x0 = self.points[0][Polygon.X]
        y0 = 0.
        x0_2 = x0*x0  # =x²
        x0_3 = x0_2*x0  # =x³ 
        for i in range(1,len(self.points)):
            x1 = self.points[i][Polygon.X]
            y1 = self.points[i][Polygon.Y]
            if x1<>x0: # senkrechte Anstiege haben keine Flaechen
                x1_2 = x1*x1
                x1_3 = x1_2*x1
                _Flaeche = _Flaeche+(y0+y1)/2.0*(x1-x0) # Trapezfläche
                _Schwerpunkt = ( _Schwerpunkt +   # Integral( x*f(x) ) 
                                y0/2.0*(x1_2-x0_2)+(y1-y0)/(x1-x0)*(x1_3/3.0-x0_3/3.0-x1_2*x0/2.0+x0_3/2.0))
                x0,x0_2,x0_3 = x1,x1_2,x1_3
            y0 = y1
	if _Flaeche == 0.0:
	    raise Exception("no COG calculable: polygon area is zero!")
        _Schwerpunkt = _Schwerpunkt/_Flaeche
	return _Schwerpunkt # XXX