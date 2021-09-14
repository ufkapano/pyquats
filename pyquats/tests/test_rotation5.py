#!/usr/bin/python
#
# Based on Vesely (1982).
#
# Conclusions
# random_unit_quat() is 5 times faster that random_quat_biax(),
# but it is unclear if the distributions are similar.

import math
import random
import timeit
from pyquats.quats import Quat
from pyquats.qtools import random_quat_biax

def random_pair():
    """Return a random pair (s1, s2), where s1^2 + s2^2 < 1."""
    while True:
        s1 = random.uniform(-1, 1)
        s2 = random.uniform(-1, 1)
        if s1 * s1 + s2 * s2 < 1:
            break
    return s1, s2

def random_unit_quat():
    """Return a random unit quat (Marsaglia, 1972)."""
    s1, s2 = random_pair()
    s3, s4 = random_pair()
    S1 = s1 * s1 + s2 * s2
    S2 = s3 * s3 + s4 * s4
    a = math.sqrt((1.0 - S1) / S2)
    return Quat(s1, s2, s3 * a, s4 * a)

#for i in range(5):
#    q = random_unit_quat()
#    print(q)
#    print(q.is_unit())
#    print("abs {}".format(abs(q)))

N = 10000

print ( "random_quat_biax()..." )
t1 = timeit.Timer(lambda: random_quat_biax())
print ( "{} {}".format(N, t1.timeit(N)) )

print ( "random_unit_quat()..." )   # over 5 times faster
t1 = timeit.Timer(lambda: random_unit_quat())
print ( "{} {}".format(N, t1.timeit(N)) )


# EOF
