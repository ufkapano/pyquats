#!/usr/bin/python

import math
from quats import Quat


def exp(x):
    """Return the exponential value e**x."""
    if isinstance(x, (int, long, float)):
        return Quat(math.exp(x))
    elif isinstance(x, complex):
        # exp(a+bJ)=exp(a)*(cos(b)+sin(b)J)
        a = math.exp(x.real) * math.cos(x.imag)
        b = math.exp(x.real) * math.sin(x.imag)
        return Quat(a, b)
    else:   # isinstance(x, Quat)
        quat_imag = Quat(0, x.q[1], x.q[2], x.q[3])
        v = abs(quat_imag)
        if v == 0.0:
            result = quat_imag
        else:
            result = quat_imag * (math.sin(v) / v)
        result = result + Quat(math.cos(v))
        result = result * math.exp(x.q[0])
        return result



# EOF
