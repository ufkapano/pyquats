#!/usr/bin/python

try:
    real_types = (int, long, float)
except NameError:   # Python 3
    real_types = (int, float)
    xrange = range

import math


class Quat:
    """The class defining a quaternion."""

    def __init__(self, x=0, y=0, z=0, t=0):
        """Create a Quat instance."""
        self.q = [float(x), float(y), float(z), float(t)]

    def __str__(self):
        """Compute the string (informal) representation of the quaternion."""
        #return str(self.q)   # brzydkie
        words = []
        labels = ["1", "i", "j", "k"]
        words.append(str(self.q[0]))
        for i in range(1, 4):
            if self.q[i] >= 0:
                words.append("+")
            words.append(str(self.q[i]))
            words.append(labels[i])
        return "".join(words)

    def __repr__(self):
        """Compute the string (formal) representation of the quaternion."""
        return "Quat({}, {}, {}, {})".format(*self.q)

    def __getitem__(self, key):
        """Implement quat[key]."""
        return self.q[key]

    def _normalize(self, other):
        """Transformation an object to a quaternion."""
        if isinstance(other, real_types):
            other = Quat(other)
        elif isinstance(other, complex):
            other = Quat(other.real, other.imag)
        return other

    def __eq__(self, other):
        """Test if the quaternions are equal."""
        other = self._normalize(other)
        return all(self.q[i] == other.q[i] for i in range(4))

    def __ne__(self, other):
        """Test if the quaternions are not equal."""
        return not self == other

    def __nonzero__(self):
        """Test if the quaternion is not equal to zero."""
        return any(self.q[i] != 0 for i in range(4))

    __bool__ = __nonzero__   # Python 3

    def __pos__(self):
        """Implementation of +q."""
        return self

    def __neg__(self):
        """Implementation of -q."""
        #alist = [-item for item in self.q]
        #return Quat(*alist)
        return Quat(-self.q[0], -self.q[1], -self.q[2], -self.q[3])

    def __add__(self, other):
        """Addition of quaternions."""
        other = self._normalize(other)
        alist = [self.q[i] + other.q[i] for i in range(4)]
        return Quat(*alist)

    __radd__ = __add__

    def __sub__(self, other):
        """Subtraction of quaternions."""
        # return self + (-other)
        other = self._normalize(other)
        alist = [self.q[i] - other.q[i] for i in range(4)]
        return Quat(*alist)

    def __rsub__(self, other):
        """Subtraction of quaternions."""
        # return (-self) + other
        other = self._normalize(other)
        alist = [other.q[i] - self.q[i] for i in range(4)]
        return Quat(*alist)

    def __mul__(self, other):
        """Quaternion product."""
        other = self._normalize(other)
        a = (self.q[0] * other.q[0] - self.q[1] * other.q[1]
            - self.q[2] * other.q[2] - self.q[3] * other.q[3])
        b = (self.q[0] * other.q[1] + self.q[1] * other.q[0]
            + self.q[2] * other.q[3] - self.q[3] * other.q[2])
        c = (self.q[0] * other.q[2] - self.q[1] * other.q[3]
            + self.q[2] * other.q[0] + self.q[3] * other.q[1])
        d = (self.q[0] * other.q[3] + self.q[1] * other.q[2]
            - self.q[2] * other.q[1] + self.q[3] * other.q[0])
        return Quat(a, b, c, d)

    def __rmul__(self, other):
        """Quaternion product."""
        other = self._normalize(other)
        a = (other.q[0] * self.q[0] - other.q[1] * self.q[1]
            - other.q[2] * self.q[2] - other.q[3] * self.q[3])
        b = (other.q[0] * self.q[1] + other.q[1] * self.q[0]
            + other.q[2] * self.q[3] - other.q[3] * self.q[2])
        c = (other.q[0] * self.q[2] - other.q[1] * self.q[3]
            + other.q[2] * self.q[0] + other.q[3] * self.q[1])
        d = (other.q[0] * self.q[3] + other.q[1] * self.q[2]
            - other.q[2] * self.q[1] + other.q[3] * self.q[0])
        return Quat(a, b, c, d)

    def __abs__(self):
        """Return the norm of a quaternion (a scalar)."""
        powers = sum(item * item for item in self.q)
        return math.sqrt(powers)

    def is_unit(self):
        """Test a unit quaternion."""
        return 1.0 == sum(item * item for item in self.q)

    def conjugate(self):
        """Conjugate the quaternion."""
        return Quat(self.q[0], -self.q[1], -self.q[2], -self.q[3])

    def __invert__(self):   # ~p, return p^{-1}
        """Reciprocal of the quaternion."""
        powers = sum(item * item for item in self.q)
        return (1.0 / powers) * self.conjugate()

    def _pow1(self, n):
        """Find powers of the quaternion (inefficient)."""
        if n < 0:
            return pow(~self, -n)
        quat = Quat(1)
        while n > 0:
            quat = quat * self
            n = n - 1
        return quat

    def _pow2(self, n):
        """Find powers of the quaternion (binary exponentiation)."""
        if n == 0:
            return Quat(1)
        if n < 0:
            return pow(~self, -n)
        quat = self
        if n == 1:
            return self
        elif n == 2:
            return self * self
        else:   # binary exponentiation
            result = Quat(1)
            while True:
                if n % 2 == 1:
                    result = result * quat
                    n = n - 1  # przez ile pomnozyc
                    if n == 0:
                        break
                if n % 2 == 0:
                    quat = quat * quat
                    n = n // 2
        return result

    __pow__ = _pow2

    def __hash__(self):
        """Hashable quaternions."""
        return hash(tuple(self.q))

    def __int__(self):
        """Conversion to int is not possible."""
        raise TypeError("can't convert quat to int")

    def __long__(self):
        """Conversion to long is not possible."""
        raise TypeError("can't convert quat to long")

    def __float__(self):
        """Conversion to float is not possible."""
        raise TypeError("can't convert quat to float")

    def __complex__(self):
        """Conversion to complex is not possible."""
        raise TypeError("can't convert quat to complex")

    # method used to create a rotation Quaternion to rotate
    # any vector defined as a Quaternion
    # with respect to the vector vect theta 'radians';
    # rot_vec ma dlugosc 1 w R^3, tworzymy kwaternion jednostkowy.
    # Chyba lepiej zrobic metode klasy.
    @classmethod
    def rot_quat(cls, axis, angle):
        """From the axis-angle representation to the quat.
        The angle is in radians. The axis is a unit 3D vector."""
        if sum(x * x for x in axis) != 1.0:
            raise ValueError("not a unit vector")
        a = math.cos(angle / 2.0)
        sinus = math.sin(angle / 2.0)
        b = axis[0] * sinus
        c = axis[1] * sinus
        d = axis[2] * sinus
        return cls(a, b, c, d)

Quaternion = Quat

# EOF
