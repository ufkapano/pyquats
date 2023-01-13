#!/usr/bin/env python3
#
# Results:
# math.sin(x) is 6x faster than np.sin(x).
# np.sum(np.sin(L)) is 2x faster than sum(math.sin() with for loop).

import random
import timeit
import math
import numpy as np

N = 1000000

L = [random.random()*10 for i in range(N)]

print ( "Testing sum(math.sin() with for loop)..." )
t1 = timeit.Timer(lambda: sum(math.sin(x) for x in L))
print ( "{} {}".format(N, t1.timeit(1)) )   # single run

print ( "Testing sum(np.sin() with for loop)..." )
t1 = timeit.Timer(lambda: sum(np.sin(x) for x in L))
print ( "{} {}".format(N, t1.timeit(1)) )   # single run

print ( "Testing sum(np.sin(L))..." )
t1 = timeit.Timer(lambda: sum(np.sin(L)))
print ( "{} {}".format(N, t1.timeit(1)) )   # single run

print ( "Testing np.sum(np.sin(L))..." )
t1 = timeit.Timer(lambda: np.sum(np.sin(L))) # BEST!
print ( "{} {}".format(N, t1.timeit(1)) )   # single run

# EOF
