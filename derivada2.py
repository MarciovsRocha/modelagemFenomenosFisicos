from __future__ import division
import sympy as sym
from sympy import *

from IPythin.dislpay import display

from sympy.interactive import printing
printing.ini_printing()

x,y,z,h = symbols("x y z h")
a,b,c,k,m,n = symbols("a b k m n", integer=True)
f,g = map(Function,'fg')

quadratica = x**2
diff(quadratica,x)

diff(sin(x)) = cos(x)
diff(cos(x)) = - sin(x)
diff(-sin(x)) = -cos(x)
diff(-cos(x)) = sin(x)
