#!/usr/bin/python

import math
from quats import Quat


def exp(x):
    """Return the exponential value e**x."""
    if isinstance(x, (int, long, float)):
        return Quat(math.exp(x))
    elif isinstance(x, complex):
        # exp(a+bJ)=exp(a)*(cos(b)+sin(b)J)
        exp_real = math.exp(x.real)
        return Quat(exp_real * math.cos(x.imag), exp_real * math.sin(x.imag))
    else:   # isinstance(x, Quat)
        quat_imag = Quat(0, x.q[1], x.q[2], x.q[3])
        v = abs(quat_imag)
        #if v < 1e4:
        #    result = quat_imag * (1.0 - v*v/6.0)
        if v == 0.0:
            result = quat_imag
        else:
            result = quat_imag * (math.sin(v) / v)
        result = result + Quat(math.cos(v))
        result = result * math.exp(x.q[0])
        return result

def sin(x):
    """Return the sine of x."""
    if isinstance(x, (int, long, float)):
        return Quat(math.sin(x))
    elif isinstance(x, complex):
        return Quat(math.sin(x.real) * math.cosh(x.imag), 
                    math.cos(x.real) * math.sinh(x.imag))
    else:   # isinstance(x, Quat)
        # sin(q)=(exp(qJ)-exp(-qJ))/(2J)
        quat = x * Quat(0, 1)
        result = exp(quat) - exp(-quat)
        result = result * Quat(0, -0.5)
        return result


def cos(x):
    """Return the cosine of x."""
    if isinstance(x, (int, long, float)):
        return Quat(math.cos(x))
    elif isinstance(x, complex):
        return Quat(math.cos(x.real) * math.cosh(x.imag), 
                    -math.sin(x.real) * math.sinh(x.imag))
    else:   # isinstance(x, Quat)
        # cos(q)=(exp(qJ)+exp(-qJ))/2
        quat = x * Quat(0, 1)
        result = exp(quat) + exp(-quat)
        result = result * Quat(0.5)
        return result

# EOF
