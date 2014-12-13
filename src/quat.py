#!/usr/bin/python

import math

class Quat:

    def __init__(self, a=0, b=0, c=0, d=0):
        self.q = [float(a), float(b), float(c), float(d)]

    def __str__(self):
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
        #return "Quat(%s, %s, %s, %s)" % (
        #self.q[0], self.q[1], self.q[2], self.q[3])
        return "Quat(%s, %s, %s, %s)" % tuple(self.q)

    def __eq__(self, other):
        if isinstance(other, (int, long, float)):
            other = Quat(other)
        elif isinstance(other, complex):
            other = Quat(other.real, other.imag)
        return all(self.q[i] == other.q[i] for i in range(4))

    def __ne__(self, other):
        return not self == other

    def __pos__(self):
        """Implementacja +q."""
        return self

    def __neg__(self):
        """Implementacja -q."""
        return Quat(-self.q[0], -self.q[1], -self.q[2], -self.q[3])

    def __add__(self, other):
        """Addition of quaternions, q+q, q+c, c+q."""
        if isinstance(other, (int, long, float)):
            other = Quat(other)
        elif isinstance(other, complex):
            other = Quat(other.real, other.imag)
        new_quat = Quat()
        for i in range(4):
            new_quat.q[i] = self.q[i] + other.q[i]
        return new_quat

    __radd__ = __add__

    def __sub__(self, other):
        """Subtraction of quaternions, q-q, q-c."""
        if isinstance(other, (int, long, float)):
            other = Quat(other)
        elif isinstance(other, complex):
            other = Quat(other.real, other.imag)
        new_quat = Quat()
        for i in range(4):
            new_quat.q[i] = self.q[i] - other.q[i]
        return new_quat

    def __rsub__(self, other):
        """Subtraction of quaternions, c-q."""
        if isinstance(other, (int, long, float)):
            other = Quat(other)
        elif isinstance(other, complex):
            other = Quat(other.real, other.imag)
        new_quat = Quat()
        for i in range(4):
            new_quat.q[i] = other.q[i] - self.q[i]
        return new_quat

    def __mul__(self, other):
        """Quaternion product, quat*quat, quat*complex."""
        if isinstance(other, (int, long, float)):
            other = Quat(other)
        elif isinstance(other, complex):
            other = Quat(other.real, other.imag)
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
        """Quaternion product, complex*quat."""
        if isinstance(other, (int, long, float)):
            other = Quat(other)
        elif isinstance(other, complex):
            other = Quat(other.real, other.imag)
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
        """Norm of a quaternion returns an scalar."""
        powers = sum(item * item for item in self.q)
        return math.sqrt(powers)

    def conjugate(self):   # tworzy nowy quat
        """Conjugates a quaternion."""
        return Quat(self.q[0], -self.q[1], -self.q[2], -self.q[3])

    def __invert__(self):   # ~p, zwraca p^{-1}
        """Reciprocal of quaternion."""
        tmp = 1./abs(self)
        return (tmp * tmp) * self.conjugate()

    def __pow__(self, n):
        new_quat = Quat(1)
        while n > 0:
            new_quat = new_quat * self
            n = n-1
        return new_quat

    def __int__(self):
        raise TypeError("can't convert quat to int")

    def __float__(self):
        raise TypeError("can't convert quat to float")

# EOF
