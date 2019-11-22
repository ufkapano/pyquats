#!/usr/bin/python

import unittest
import math
from quats import *


class TestQuat(unittest.TestCase):

    def setUp(self):
        self.zero = Quat()
        self.one = Quat(1)
        self.ii = Quat(0, 1, 0, 0)
        self.jj = Quat(0, 0, 1, 0)
        self.kk = Quat(0, 0, 0, 1)
        self.q1 = Quat(1, 2, 3, 4)
        self.q2 = Quat(1, 1, 1, 1)
        self.q3 = Quat(1.1, 2.2, 3.3, 4.4)
        self.q4 = Quat(-1.2, -2.3, -3.4, -4.5)
        self.c1 = 1J
        self.c2 = 1 + 2J

    def test_print(self):
        self.assertEqual(str(self.zero),"0.0+0.0i+0.0j+0.0k")
        self.assertEqual(str(self.q4),"-1.2-2.3i-3.4j-4.5k")
        self.assertEqual(repr(self.zero),"Quat(0.0, 0.0, 0.0, 0.0)")
        self.assertEqual(repr(self.q1),"Quat(1.0, 2.0, 3.0, 4.0)")
        self.assertEqual(repr(self.q4),"Quat(-1.2, -2.3, -3.4, -4.5)")

    def test_add(self):
        self.assertEqual(self.q1 + self.q2, Quat(2, 3, 4, 5))
        self.assertEqual(self.q1 + self.c1, Quat(1, 3, 3, 4))
        self.assertEqual(self.c2 + self.q2, Quat(2, 3, 1, 1))

    def test_sub(self):
        self.assertEqual(self.q1 - self.q2, Quat(0, 1, 2, 3))
        self.assertEqual(self.q1 - self.c2, Quat(0, 0, 3, 4))
        self.assertEqual(self.c2 - self.q2, Quat(0, 1, -1, -1))

    def test_mul(self):
        self.assertEqual(self.q1 * self.zero, self.zero)
        self.assertEqual(self.q1 * self.one, self.q1)
        # i*j=k, i*1=j*j=k*k=-1
        self.assertEqual(self.ii * self.jj, self.kk)
        self.assertEqual(self.jj * self.ii, Quat(0, 0, 0, -1))
        self.assertEqual(self.ii * self.ii, Quat(-1))
        self.assertEqual(self.jj * self.jj, Quat(-1))
        self.assertEqual(self.kk * self.kk, Quat(-1))
        # test complex
        self.assertEqual(self.c2 * Quat(3, 4), Quat(3, 4) * self.c2)
        self.assertEqual(self.q1 * self.c2, Quat(-3, 4, 11, -2))
        self.assertEqual(self.c2 * self.q1, Quat(-3, 4, -5, 10))

    def test_nonzero(self):
        self.assertTrue(bool(Quat(1)))
        self.assertFalse(bool(Quat()))
        self.assertEqual("a", "a" if Quat(1) else "b")
        self.assertEqual("b", "a" if Quat() else "b")

    def test_pos_neg(self):
        self.assertEqual(+self.q1, self.q1)
        self.assertEqual(-self.q1, Quat(-1, -2, -3, -4))
        self.assertEqual(self.jj * self.ii, -self.kk)
        self.assertEqual(self.ii * self.ii, -self.one)
        self.assertEqual(self.jj * self.jj, -self.one)
        self.assertEqual(self.kk * self.kk, -self.one)

    def test_conjugate(self):
        self.assertEqual(self.q1.conjugate(), Quat(1, -2, -3, -4))
        self.assertEqual(self.one.conjugate(), self.one)

    def test_invert(self):
        self.assertEqual(~self.q2, Quat(0.25, -0.25, -0.25, -0.25))
        self.assertEqual(~self.one, self.one)

    def test_abs(self):
        self.assertEqual(abs(self.zero), 0)
        self.assertEqual(abs(self.one), 1)
        self.assertEqual(abs(self.ii), 1)
        self.assertEqual(abs(self.jj), 1)
        self.assertEqual(abs(self.kk), 1)
        self.assertEqual(abs(self.q2), 2)

    def test_pow(self):
        self.assertEqual(self.q1 ** 0, self.one)
        self.assertEqual(self.q1 ** 0, 1)
        self.assertEqual(self.q1 ** 1, self.q1)
        self.assertEqual(self.q1 ** 2, self.q1 * self.q1)
        self.assertEqual(self.ii ** 4, self.one)
        self.assertEqual(self.ii ** 400, self.one)

    def test_conversion(self):
        self.assertRaises(TypeError, int, self.one)
        self.assertRaises(TypeError, long, self.one)
        self.assertRaises(TypeError, float, self.one)
        self.assertRaises(TypeError, complex, self.one)

    def test_hash(self):
        aset = set()
        aset.add(self.ii)
        aset.add(self.ii)  # ignored
        self.assertEqual(len(aset), 1)
        aset.add(self.jj)
        aset.add(self.kk)
        self.assertEqual(len(aset), 3)

    def tearDown(self): pass


class TestRotations(unittest.TestCase):

    def setUp(self):
        self.rotX180 = Quat(0, 1, 0, 0)
        self.rotY180 = Quat(0, 0, 1, 0)
        p2 = math.sqrt(0.5)
        p3 = math.sqrt(1.0 / 3.0)
        self.rotX90 = Quat(p2, p2, 0, 0)
        self.rotY90 = Quat(p2, 0, p2, 0)
        self.rotZ90 = Quat(p2, 0, 0, p2)
        self.rotZ180 = Quat(0, 0, 0, 1)
        # obrot o kat 120 stopni wokol [0,1,1,1]
        self.rot120 = Quat(0.5, 0.5, 0.5, 0.5)
        self.vec1 = [p3, p3, p3]

    def test_rot_quat(self):
        # obroty o 180 sa przemienne, ale daja inne quat
        self.assertAlmostEqual(self.rotX180 * self.rotY180, Quat(0, 0, 0, 1))
        self.assertAlmostEqual(self.rotY180 * self.rotX180, Quat(0, 0, 0, -1))
        # 90+90=180
        # assertAlmostEqual potrzebuje metody __abs__ do dzialania
        self.assertAlmostEqual(self.rotX90 * self.rotX90, self.rotX180)
        self.assertAlmostEqual(self.rotY90 * self.rotY90, self.rotY180)
        self.assertAlmostEqual(self.rotZ90 * self.rotZ90, self.rotZ180)
        # obroty o 90
        self.assertAlmostEqual(self.rotX90 * self.rotY90, self.rot120)
        self.assertAlmostEqual(self.rotY90 * self.rotZ90, self.rot120)
        self.assertAlmostEqual(self.rotZ90 * self.rotX90, self.rot120)
        self.assertAlmostEqual(self.rotY90 * self.rotX90, Quat(0.5, 0.5, 0.5, -0.5))
        self.assertAlmostEqual(self.rotZ90 * self.rotY90, Quat(0.5, -0.5, 0.5, 0.5))
        self.assertAlmostEqual(self.rotX90 * self.rotZ90, Quat(0.5, 0.5, -0.5, 0.5))
        self.assertAlmostEqual(self.rotX90, Quat.rot_quat([1, 0, 0], math.pi * 0.5))
        self.assertAlmostEqual(self.rotY90, Quat.rot_quat([0, 1, 0], math.pi * 0.5))
        self.assertAlmostEqual(self.rotZ90, Quat.rot_quat([0, 0, 1], math.pi * 0.5))
        self.assertAlmostEqual(self.rot120, Quat.rot_quat(self.vec1, math.pi * 2.0 / 3.0))

    def test_rot_vectors(self):
        # Listy nie mozna odejmowac i obliczac abs(L).
        # Potrzebna klasa Vector.
        pairs = []
        pairs.append((rotate1([10, 0, 0], self.rotZ90), [0, 10, 0]))
        pairs.append((rotate2([10, 0, 0], [0, 0, 1], math.pi * 0.5), [0, 10, 0]))
        pairs.append((rotate1([0,10, 0], self.rot120), [0, 0, 10]))
        pairs.append((rotate2([0, 10, 0], self.vec1, math.pi * 2.0 / 3.0), [0, 0, 10]))
        pairs.append((rotate3([0, 0, 10], 0, math.pi * 0.5, 0), [10, 0, 0]))
        pairs.append((rotate3([10, 0, 0], math.pi * 0.5, 0, 0), [0, 10, 0]))
        pairs.append((rotate3([10, 0, 0], math.pi * 0.5, 0, 0), [0, 10, 0]))
        # Po kolei porownuje wyniki po wspolrzednych.
        for left, right in pairs:
            self.assertAlmostEqual(left[0], right[0])
            self.assertAlmostEqual(left[1], right[1])
            self.assertAlmostEqual(left[2], right[2])

    def tearDown(self): pass

if __name__== "__main__":

    unittest.main()

# EOF
