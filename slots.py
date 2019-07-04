import sys, random
from io import StringIO

p = lambda: random.choice('♪♫♣♠♦♥◄☼☽')
x = p
y = p
z = p

[print('|'.join([x(), y(), z()]), end='\r') for i in range(8**5)]

