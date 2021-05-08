#!/usr/bin/python

import math
import random
from pyquats.quats import Quat
#from pyquats.numpyquats import Quat

# Rotates a vector with respect to a quat.
# The vector is from R^3, the result is from R^3, rot_quat is a unit quat.
def rotate1(vector, unit_quat):
    """Return the rotated vector (rot_quat used)."""
    # From a vector to a quaternion.
    vec_quat = Quat(0, vector[0], vector[1], vector[2])
    # Rotate a vector.
    vec_quat = unit_quat * vec_quat * (~unit_quat)
    # Return a vector from R^3.
    return vec_quat.q[1:]

# Rotates a vector angle 'radians' with respect to axis,
# both are vectors but it uses quaternions.
def rotate2(vector, axis, angle):
    """Return the rotated vector (axis and angle used)."""
    # Make a unit quat.
    unit_quat = Quat.rot_quat(axis, angle)
    return rotate1(vector, unit_quat)

def rotate3(vector, phi, theta, psi):
    """Return the rotated vector (Euler angles used)."""
    unit_quat = Quat.from_eulers(phi, theta, psi)
    return rotate1(vector, unit_quat)

def random_quat_uniax():
    """Return a random rotation quat for uniaxial molecules."""
    phi = random.uniform(0, 2*math.pi)
    ct = random.uniform(-1, 1)
    theta = math.acos(ct)   # mozna tez -ct
    quat = Quat.from_eulers(phi, theta, 0)
    return quat

def random_quat_biax():
    """Return a random rotation quat for biaxial molecules."""
    phi = random.uniform(0, 2*math.pi)
    ct = random.uniform(-1, 1)
    theta = math.acos(ct)   # mozna tez -ct
    psi = random.uniform(0, 2*math.pi)
    quat = Quat.from_eulers(phi, theta, psi)
    return quat

# EOF
