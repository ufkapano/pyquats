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

    # method used to create a rotation Quaternion to rotate
    # any vector defined as a Quaternion
    # with respect to the vector vect theta 'radians';
    # rot_vec ma dlugosc 1 w R^3, tworzymy kwaternion jednostkowy.
    # Chyba lepiej zrobic metode klasy.
    @classmethod
    def rot_quat(cls, theta, rot_vec):
        a = math.cos(theta / 2.0)
        b = rot_vec[0] * math.sin(theta / 2.0)
        c = rot_vec[1] * math.sin(theta / 2.0)
        d = rot_vec[2] * math.sin(theta / 2.0)
        return cls(a, b, c, d)

# rotates a vector or a vector defined as a Quaternion 0+xi+yj+zk 
# with respect to a Quaternion;
# vector jest z R^3, wynik tez jest z R^3, rot_quat jest jednostkowy.
def rotate1(vector, rot_quat):
    # z wektora robie kwaternion urojony
    vec_quat = Quat(0, vector[0], vector[1], vector[2])
    # obracam wektor
    vec_quat = rot_quat * vec_quat * (~rot_quat)
    # zwracamy wektor z R^3 (wycinek)
    return vec_quat.q[1:]

# rotates a vector v_to_rotate theta 'radians' with respect to v_about,
# both are vectors but it uses Quaternions
def rotate2(vector, theta, rot_vec):
    # tworze kwaternion jednostkowy dla obrotu
    rot_quat = Quat.rot_quat(theta, rot_vec)
    return rotate1(vector, rot_quat)

# chce zbudowac obrot z katow Eulera
def rotate3(vector, phi, theta, psi):
    q1 = Quat.rot_quat(phi, [0,0,1])
    q2 = Quat.rot_quat(theta, [0,1,0])
    q3 = Quat.rot_quat(psi, [0,0,1])
    rot_quat = q1 * q2 * q3
    return rotate1(vector, rot_quat)


# EOF
