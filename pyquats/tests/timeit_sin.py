#!/usr/bin/env python3
#
# Results:
# math.sin(x) is 6x faster than np.sin(x).

import random
import timeit
import math
import numpy as np

N = 1000000

L = [random.random()*10 for i in range(N)]

print ( "Testing math.sin()..." )
t1 = timeit.Timer(lambda: sum(math.sin(x) for x in L))
print ( "{} {}".format(N, t1.timeit(1)) )   # single run

print ( "Testing np.sin()..." )
t1 = timeit.Timer(lambda: sum(np.sin(x) for x in L))
print ( "{} {}".format(N, t1.timeit(1)) )   # single run

# EOF
