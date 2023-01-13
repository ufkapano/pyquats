#!/usr/bin/env python3
#
# Results:
# math.exp(x) is 7x faster than np.exp(x).
# np.sum(np.exp(L)) is 2x faster than sum(math.exp() with for loop).

import random
import timeit
import math
import numpy as np

N = 1000000

L = [random.random()*10 for i in range(N)]

print ( "Testing sum(math.exp() with for loop)..." )
t1 = timeit.Timer(lambda: sum(math.exp(x) for x in L))
print ( "{} {}".format(N, t1.timeit(1)) )   # single run

print ( "Testing sum(np.exp() with for loop)..." )
t1 = timeit.Timer(lambda: sum(np.exp(x) for x in L))
print ( "{} {}".format(N, t1.timeit(1)) )   # single run

print ( "Testing sum(np.exp(L))..." )
t1 = timeit.Timer(lambda: sum(np.exp(L)))
print ( "{} {}".format(N, t1.timeit(1)) )   # single run

print ( "Testing np.sum(np.exp(L))..." )
t1 = timeit.Timer(lambda: np.sum(np.exp(L))) # BEST!
print ( "{} {}".format(N, t1.timeit(1)) )   # single run

# EOF
