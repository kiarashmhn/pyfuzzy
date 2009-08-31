# -*- coding: iso-8859-1 -*-
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

__revision__ = "$Id: Yager.py,v 1.1 2009-08-31 21:04:20 rliebscher Exp $"

from fuzzy.complement.Base import Base
from fuzzy.utils import inf_p
import math

class Yager(Base):
    """Complement after Yager"""

    _range = [ (0.,inf_p) ]

    def __init__(self,omega=1.,*args,**keywords):
        """
        """ 
        super(Yager, self).__init__(*args,**keywords)
        self.omega = float(omega)

    def __call__(self,value):
        """calculate the complement of the value"""
        return math.pow(1. - math.pow(float(value),self.omega),1./self.omega)
