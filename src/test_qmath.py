#!/usr/bin/python

import unittest
import math
import cmath
import qmath
from quats import Quat


class TestQuatMath(unittest.TestCase):

    def setUp(self):
        self.c1 = 1J
        self.c2 = 1 + 2J

    def test_exp(self):
        self.assertAlmostEqual(qmath.exp(2), math.exp(2))
        self.assertAlmostEqual(qmath.exp(3.0), math.exp(3.0))
        self.assertAlmostEqual(qmath.exp(self.c1), cmath.exp(self.c1))
        self.assertAlmostEqual(qmath.exp(self.c2), cmath.exp(self.c2))
        self.assertAlmostEqual(qmath.exp(Quat(2)), math.exp(2))
        self.assertAlmostEqual(qmath.exp(Quat(0, 3)), cmath.exp(3J))
        self.assertAlmostEqual(qmath.exp(Quat(4, 5)), cmath.exp(4 + 5J))
        self.assertAlmostEqual(qmath.exp(Quat(0, math.pi)), -1.0)
        self.assertAlmostEqual(qmath.exp(Quat(0, 0, math.pi)), -1.0)
        self.assertAlmostEqual(qmath.exp(Quat(0, 0, 0, math.pi)), -1.0)
        self.assertAlmostEqual(qmath.exp(Quat(4, 0, 3)),
            math.exp(4) * Quat(math.cos(3), 0, math.sin(3)))
        self.assertAlmostEqual(qmath.exp(Quat(2, 0, 0, 3)),
            math.exp(2) * Quat(math.cos(3), 0, 0, math.sin(3)))

    def tearDown(self): pass

if __name__== "__main__":

    #unittest.main()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestQuatMath)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)

# EOF
