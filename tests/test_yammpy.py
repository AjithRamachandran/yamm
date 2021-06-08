import unittest
import yammpy

NAN = float('nan')
INF = float('inf')
NINF = float('-inf')

class YammpyTests(unittest.TestCase):

    def testConstants(self):
        self.assertEqual(yammpy.pi, 3.141592653589793238462643)
        self.assertEqual(yammpy.e, 2.718281828459045235360287)
        self.assertEqual(yammpy.tau, 2*yammpy.pi)
        self.assertEqual(yammpy.phi, 1.61803398874989484820)
        self.assertEqual(yammpy.wal, 2.09455148154232659148)

    def testAcos(self):
        self.assertEqual(yammpy.acos(-1), yammpy.pi)
        self.assertEqual(yammpy.acos(0), yammpy.pi/2)
        self.assertEqual(yammpy.acos(1), 0)

    def testAcosh(self):
        self.assertEqual(yammpy.acosh(1), 0)
        self.assertEqual(yammpy.acosh(2), 1.3169578969248166)
        self.assertEqual(yammpy.acosh(INF), INF)
        self.assertTrue(yammpy.isnan(yammpy.acosh(NAN)))

    def testAsin(self):
        self.assertEqual(yammpy.asin(-1), -yammpy.pi/2)
        self.assertEqual(yammpy.asin(0), 0)
        self.assertEqual(yammpy.asin(1), yammpy.pi/2)
        self.assertTrue(yammpy.isnan(yammpy.asin(NAN)))

    def testAsinh(self):
        self.assertEqual(yammpy.asinh(0), 0)
        self.assertEqual(yammpy.asinh(1), 0.88137358701954305)
        self.assertEqual(yammpy.asinh(-1), -0.88137358701954305)
        self.assertEqual(yammpy.asinh(INF), INF)
        self.assertEqual(yammpy.asinh(NINF), NINF)
        self.assertTrue(yammpy.isnan(yammpy.asinh(NAN)))

    def testAtan(self):
        self.assertEqual(yammpy.atan(-1), -yammpy.pi/4)
        self.assertEqual(yammpy.atan(0), 0)
        self.assertEqual(yammpy.atan(1), yammpy.pi/4)
        self.assertEqual(yammpy.atan(INF), yammpy.pi/2)
        self.assertEqual(yammpy.atan(NINF), -yammpy.pi/2)
        self.assertTrue(yammpy.isnan(yammpy.atan(NAN)))

    def testAtanh(self):
        self.assertEqual(yammpy.atanh(0), 0)
        self.assertEqual(yammpy.atanh(0.5), 0.54930614433405489)
        self.assertEqual(yammpy.atanh(-0.5), -0.54930614433405489)
        self.assertTrue(yammpy.isnan(yammpy.atanh(NAN)))

    def testCbrt(self):
        self.assertEqual(yammpy.cbrt(0), 0)
        self.assertEqual(yammpy.cbrt(1), 1)
        self.assertEqual(yammpy.cbrt(27), 3)
        self.assertEqual(yammpy.cbrt(INF), INF)
        self.assertTrue(yammpy.isnan(yammpy.cbrt(NAN)))
        self.assertEqual(yammpy.cbrt(15625), 25)

    def testCeil(self):
        # self.assertEqual(int, type(yammpy.ceil(0.5)))
        self.assertEqual(yammpy.ceil(0.5), 1)
        self.assertEqual(yammpy.ceil(1.0), 1)
        self.assertEqual(yammpy.ceil(1.5), 2)
        self.assertEqual(yammpy.ceil(-0.5), 0)
        self.assertEqual(yammpy.ceil(-1.0), -1)
        self.assertEqual(yammpy.ceil(-1.5), -1)
        self.assertEqual(yammpy.ceil(0.0), 0)
        self.assertEqual(yammpy.ceil(-0.0), 0)

    def testCos(self):
        self.assertEqual(yammpy.cos(0), 1)
        self.assertEqual(yammpy.cos(yammpy.pi), -1)
        self.assertTrue(yammpy.isnan(yammpy.cos(NAN)))

    def testCosh(self):
        self.assertEqual(yammpy.cosh(0), 1)
        self.assertEqual(yammpy.cosh(2)-2*yammpy.cosh(1)**2, -1)
        self.assertEqual(yammpy.cosh(INF), INF)
        self.assertEqual(yammpy.cosh(NINF), INF)
        self.assertTrue(yammpy.isnan(yammpy.cosh(NAN)))

    def testErf(self):
        self.assertEqual(yammpy.erf(-0), -0.000000)
        self.assertEqual(yammpy.erf(INF), 1.000000)

    def testErfc(self):
        self.assertEqual(yammpy.erfc(NINF), 2.000000)
        self.assertEqual(yammpy.erfc(INF), 0.000000)

    def testExp(self):
        self.assertEqual(yammpy.exp(-1), 1/yammpy.e)
        self.assertEqual(yammpy.exp(0), 1)
        self.assertEqual(yammpy.exp(1), yammpy.e)
        self.assertEqual(yammpy.exp(INF), INF)
        self.assertEqual(yammpy.exp(NINF), 0.)
        self.assertTrue(yammpy.isnan(yammpy.exp(NAN)))

    def testExp2(self):
        self.assertEqual(yammpy.exp2(5), 32.000000)
        self.assertEqual(yammpy.exp2(0.5), 1.4142135623730951)
        self.assertEqual(yammpy.exp2(-4), 0.062500)
        self.assertEqual(yammpy.exp2(-0.9), 0.5358867312681466)
        self.assertEqual(yammpy.exp2(NINF), 0.000000)
        self.assertEqual(yammpy.exp2(1024), INF)

    def testExmp1(self):
        self.assertEqual(yammpy.expm1(1), 1.718281828459045)
        self.assertEqual(yammpy.expm1(-0), -0.000000)
        self.assertEqual(yammpy.expm1(NINF), -1.000000)
        self.assertEqual(yammpy.expm1(710), INF)

    def testFabs(self):
        self.assertEqual(yammpy.fabs(-1), 1)
        self.assertEqual(yammpy.fabs(0), 0)
        self.assertEqual(yammpy.fabs(1), 1)

    def testFloor(self):
        # self.assertEqual(int, type(yammpy.floor(0.5)))
        self.assertEqual(yammpy.floor(0.5), 0)
        self.assertEqual(yammpy.floor(1.0), 1)
        self.assertEqual(yammpy.floor(1.5), 1)
        self.assertEqual(yammpy.floor(-0.5), -1)
        self.assertEqual(yammpy.floor(-1.0), -1)
        self.assertEqual(yammpy.floor(-1.5), -2)

    def testGamma(self):
        self.assertEqual(yammpy.gamma(10), 362880.00000000006)
        self.assertEqual(yammpy.gamma(0.5), 1.772453850905516)
        self.assertEqual(yammpy.gamma(INF), INF)

    def testLgamma(self):
        self.assertEqual(yammpy.lgamma(10), 12.801827480081469)
        self.assertEqual(yammpy.lgamma(0.5), 0.5723649429247001)
        self.assertEqual(yammpy.lgamma(1), 0)
        self.assertEqual(yammpy.lgamma(INF), INF)
        self.assertEqual(yammpy.lgamma(0), INF)

    def testLog(self):
        self.assertEqual(yammpy.log(1/yammpy.e), -1)
        self.assertEqual(yammpy.log(1), 0)
        self.assertEqual(yammpy.log(yammpy.e), 1)
        self.assertEqual(yammpy.log(INF), INF)
        self.assertTrue(yammpy.isnan(yammpy.log(NAN)))

    def testLog2(self):
        self.assertEqual(yammpy.log2(1), 0.0)
        self.assertEqual(yammpy.log2(2), 1.0)
        self.assertEqual(yammpy.log2(4), 2.0)
        self.assertEqual(yammpy.log2(2**1023), 1023.0)
        self.assertTrue(yammpy.isnan(yammpy.log2(NAN)))

    def testLog10(self):
        self.assertEqual(yammpy.log10(0.1), -1)
        self.assertEqual(yammpy.log10(1), 0)
        self.assertEqual(yammpy.log10(10), 1)
        self.assertEqual(yammpy.log(INF), INF)
        self.assertTrue(yammpy.isnan(yammpy.log10(NAN)))

    def testLog1p(self):
        for n in [2, 2**90, 2**300]:
            self.assertAlmostEqual(yammpy.log1p(n), yammpy.log1p(float(n)))
        self.assertEqual(yammpy.log1p(INF), INF)

    def testLogb(self):
        self.assertEqual(yammpy.logb(0), -INF)

    def testNearbyint(self):
        self.assertEqual(yammpy.nearbyint(2.3), 2.0)
        self.assertEqual(yammpy.nearbyint(-2.3), -2.0)
        self.assertEqual(yammpy.nearbyint(2.5), 2.0)
        self.assertEqual(yammpy.nearbyint(INF), INF)

    def testSin(self):
        self.assertEqual(yammpy.sin(0), 0)
        self.assertEqual(yammpy.sin(yammpy.pi/2), 1)
        self.assertEqual(yammpy.sin(-yammpy.pi/2), -1)
        self.assertTrue(yammpy.isnan(yammpy.sin(NAN)))

    def testSinh(self):
        self.assertAlmostEqual(yammpy.sinh(0), 0)
        self.assertAlmostEqual(yammpy.sinh(1)**2-yammpy.cosh(1)**2, -1)
        self.assertAlmostEqual(yammpy.sinh(1)+yammpy.sinh(-1), 0)
        self.assertAlmostEqual(yammpy.sinh(INF), INF)
        self.assertAlmostEqual(yammpy.sinh(NINF), NINF)
        self.assertTrue(yammpy.isnan(yammpy.sinh(NAN)))

    def testTan(self):
        self.assertAlmostEqual(yammpy.tan(0), 0)
        self.assertAlmostEqual(yammpy.tan(yammpy.pi/4), 1)
        self.assertAlmostEqual(yammpy.tan(-yammpy.pi/4), -1)
        self.assertTrue(yammpy.isnan(yammpy.tan(NAN)))

    def testTanh(self):
        self.assertEqual(yammpy.tanh(0), 0)
        self.assertEqual(yammpy.tanh(INF), 1)
        self.assertEqual(yammpy.tanh(NINF), -1)
        self.assertTrue(yammpy.isnan(yammpy.tanh(NAN)))

    def testTrunc(self):
        self.assertEqual(yammpy.trunc(1), 1)
        self.assertEqual(yammpy.trunc(-1), -1)
        # self.assertEqual(type(yammpy.trunc(1)), int)
        # self.assertEqual(type(yammpy.trunc(1.5)), int)
        self.assertEqual(yammpy.trunc(1.5), 1)
        self.assertEqual(yammpy.trunc(-1.5), -1)
        self.assertEqual(yammpy.trunc(1.999999), 1)
        self.assertEqual(yammpy.trunc(-1.999999), -1)
        self.assertEqual(yammpy.trunc(-0.999999), -0)
        self.assertEqual(yammpy.trunc(-100.999), -100)

    def testAtan2(self):
        self.assertEqual(yammpy.atan2(-1, 0), -yammpy.pi/2)
        self.assertEqual(yammpy.atan2(-1, 1), -yammpy.pi/4)
        self.assertEqual(yammpy.atan2(0, 1), 0)
        self.assertEqual(yammpy.atan2(1, 1), yammpy.pi/4)
        self.assertEqual(yammpy.atan2(1, 0), yammpy.pi/2)
        self.assertEqual(yammpy.atan2(0., NINF), yammpy.pi)
        self.assertEqual(yammpy.atan2(0., -2.3), yammpy.pi)
        self.assertEqual(yammpy.atan2(0., -0.), yammpy.pi)
        self.assertEqual(yammpy.atan2(0., 0.), 0.)
        self.assertEqual(yammpy.atan2(0., 2.3), 0.)
        self.assertEqual(yammpy.atan2(0., INF), 0.)

    def testCopysign(self):
        self.assertEqual(yammpy.copysign(1, 42), 1.0)
        self.assertEqual(yammpy.copysign(0., 42), 0.0)
        self.assertEqual(yammpy.copysign(1., -42), -1.0)
        self.assertEqual(yammpy.copysign(3, 0.), 3.0)
        self.assertEqual(yammpy.copysign(4., -0.), -4.0)
        self.assertEqual(yammpy.copysign(1., 0.), 1.)
        self.assertEqual(yammpy.copysign(1., -0.), -1.)
        self.assertEqual(yammpy.copysign(INF, 0.), INF)
        self.assertEqual(yammpy.copysign(INF, -0.), NINF)
        self.assertEqual(yammpy.copysign(NINF, 0.), INF)
        self.assertEqual(yammpy.copysign(NINF, -0.), NINF)

    def testFdim(self):
        self.assertEqual(yammpy.fdim(4, 1), 3)
        self.assertEqual(yammpy.fdim(4, -1), 5)
        self.assertEqual(yammpy.fdim(8, 1), 7)
        self.assertEqual(yammpy.fdim(10, -10), 20)

    def testHypot(self):
        self.assertEqual(yammpy.hypot(12.0, 5.0), 13.0)
        self.assertEqual(yammpy.hypot(12, 5), 13)
        self.assertEqual(yammpy.hypot(0, INF), INF)
        self.assertEqual(yammpy.hypot(10, INF), INF)
        self.assertEqual(yammpy.hypot(-10, INF), INF)
        self.assertEqual(yammpy.hypot(-INF, INF), INF)
        self.assertEqual(yammpy.hypot(-INF, -INF), INF)
        self.assertEqual(yammpy.hypot(10, -INF), INF)

    def testPow(self):
        self.assertEqual(yammpy.pow(0,1), 0)
        self.assertEqual(yammpy.pow(1,0), 1)
        self.assertEqual(yammpy.pow(2,1), 2)
        self.assertEqual(yammpy.pow(2,-1), 0.5)
        self.assertEqual(yammpy.pow(INF, 1), INF)
        self.assertEqual(yammpy.pow(NINF, 1), NINF)
        self.assertEqual((yammpy.pow(1, INF)), 1.)
        self.assertEqual((yammpy.pow(1, NINF)), 1.)

    def testFmod(self):
        self.assertEqual(yammpy.fmod(10, 1), 0.0)
        self.assertEqual(yammpy.fmod(10, 0.5), 0.0)
        self.assertEqual(yammpy.fmod(10, 1.5), 1.0)
        self.assertEqual(yammpy.fmod(-10, 1), -0.0)
        self.assertEqual(yammpy.fmod(-10, 0.5), -0.0)
        self.assertEqual(yammpy.fmod(-10, 1.5), -1.0)
        self.assertTrue(yammpy.isnan(yammpy.fmod(NAN, 1.)))
        self.assertTrue(yammpy.isnan(yammpy.fmod(1., NAN)))
        self.assertTrue(yammpy.isnan(yammpy.fmod(NAN, NAN)))
        self.assertEqual(yammpy.fmod(3.0, INF), 3.0)
        self.assertEqual(yammpy.fmod(-3.0, INF), -3.0)
        self.assertEqual(yammpy.fmod(3.0, NINF), 3.0)
        self.assertEqual(yammpy.fmod(-3.0, NINF), -3.0)
        self.assertEqual(yammpy.fmod(0.0, 3.0), 0.0)
        self.assertEqual(yammpy.fmod(0.0, NINF), 0.0)

    def testRemainder(self):
        self.assertEqual(yammpy.remainder(+5.1, +3.0), -0.9000000000000004)
        self.assertEqual(yammpy.remainder(-5.1, +3.0), 0.9000000000000004)
        self.assertEqual(yammpy.remainder(+5.1, -3.0), -0.9000000000000004)
        self.assertEqual(yammpy.remainder(-5.1, -3.0), 0.9000000000000004)
        self.assertEqual(yammpy.remainder(+0.0, 1.0), 0.0)
        self.assertEqual(yammpy.remainder(-0.0, 1.0), -0.0)
        self.assertEqual(yammpy.remainder(+5.1, INF), 5.1)

    def testSqrt(self):
        self.assertEqual(yammpy.sqrt(0), 0)
        self.assertEqual(yammpy.sqrt(1), 1)
        self.assertEqual(yammpy.sqrt(4), 2)
        self.assertEqual(yammpy.sqrt(INF), INF)
        self.assertTrue(yammpy.isnan(yammpy.sqrt(NAN)))

    def testDegrees(self):
        self.assertEqual(yammpy.degrees(yammpy.pi), 180.0)
        self.assertEqual(yammpy.degrees(yammpy.pi/2), 90.0)
        self.assertEqual(yammpy.degrees(-yammpy.pi/4), -45.0)
        self.assertEqual(yammpy.degrees(0), 0)

    def testRadians(self):
        self.assertEqual(yammpy.radians(180), yammpy.pi)
        self.assertEqual(yammpy.radians(90), yammpy.pi/2)
        self.assertEqual(yammpy.radians(-45), -yammpy.pi/4)
        self.assertEqual(yammpy.radians(0), 0)

    def testSum(self):
        self.assertEqual(yammpy.sum([]), 0)
        self.assertEqual(yammpy.sum([1, 2, 3, 4, 5]), 15)
        self.assertEqual(yammpy.sum([1.0, 2.0, 3.0, 4.0, 5.0]), 15.0)
        self.assertEqual(yammpy.sum([1, 2, 3, 4.0, 5.0]), 15.0)
        self.assertEqual(yammpy.sum([1.0, 2.0, 3.0, 4, 5]), 15.0)

    def testProd(self):
        self.assertEqual(yammpy.prod([]), 1)
        self.assertEqual(yammpy.prod([1, 2, 3, 4, 5]), 120)
        self.assertEqual(yammpy.prod([1.0, 2.0, 3.0, 4.0, 5.0]), 120.0)
        self.assertEqual(yammpy.prod([1, 2, 3, 4.0, 5.0]), 120.0)
        self.assertEqual(yammpy.prod([1.0, 2.0, 3.0, 4, 5]), 120.0)

    def testIsfinite(self):
        self.assertTrue(yammpy.isfinite(0.0))
        self.assertTrue(yammpy.isfinite(-0.0))
        self.assertTrue(yammpy.isfinite(1.0))
        self.assertTrue(yammpy.isfinite(-1.0))
        self.assertFalse(yammpy.isfinite(float("nan")))
        self.assertFalse(yammpy.isfinite(float("inf")))
        self.assertFalse(yammpy.isfinite(float("-inf")))

    def testIsinf(self):
        self.assertTrue(yammpy.isinf(float("inf")))
        self.assertTrue(yammpy.isinf(float("-inf")))
        self.assertTrue(yammpy.isinf(1E400))
        self.assertTrue(yammpy.isinf(-1E400))
        self.assertFalse(yammpy.isinf(float("nan")))
        self.assertFalse(yammpy.isinf(0.))
        self.assertFalse(yammpy.isinf(1.))

    def testIsnan(self):
        self.assertTrue(yammpy.isnan(float("nan")))
        self.assertTrue(yammpy.isnan(float("-nan")))
        self.assertTrue(yammpy.isnan(float("inf") * 0.))
        self.assertFalse(yammpy.isnan(float("inf")))
        self.assertFalse(yammpy.isnan(0.))
        self.assertFalse(yammpy.isnan(1.))

    def testIsperfsqr(self):
        self.assertTrue(yammpy.isperfsqr(4))
        self.assertTrue(yammpy.isperfsqr(209764))
        self.assertTrue(yammpy.isperfsqr(616225))
        self.assertFalse(yammpy.isperfsqr(5))
        self.assertFalse(yammpy.isperfsqr(209765))

if __name__ == '__main__':
    unittest.main()
