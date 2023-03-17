import unittest
import numpy as np
import scipy.optimize
import math

from fractions import Fraction

from simplex import lp_solve, Dictionary, bland, LPResult, largest_coefficient, largest_increase

class TestExample1(unittest.TestCase):
    def setUp(self):
        n = round(math.exp(math.log(100)*np.random.random(1)[0]))
        m = round(math.exp(math.log(100)*np.random.random(1)[0]))

        self.c = np.round(10*np.random.randn(n))
        self.A = np.round(10*np.random.randn(m,n))
        self.b = np.round(10*np.random.randn(m))

    def test_solve(self):
        res,D=lp_solve(self.c,self.A,self.b, pivotrule=lambda D: largest_increase(D, 0))
        scipyRes = scipy.optimize.linprog(-self.c, self.A, self.b, method="simplex")
        if res == LPResult.OPTIMAL:
            self.assertEqual(scipyRes.status, 0)
            self.assertIsNotNone(D)
            self.assertAlmostEqual(D.value(), -scipyRes.fun)
            for (a,b) in zip(list(D.basic_solution()), scipyRes.x) :
                self.assertAlmostEqual(a,b)
        if res == LPResult.UNBOUNDED:
            self.assertEqual(scipyRes.status, 3)
        if res == LPResult.INFEASIBLE:
            self.assertEqual(scipyRes.status, 2)
        

    def test_solve_float(self):
        res,D=lp_solve(self.c,self.A,self.b, dtype=np.float64, eps=0.0001, pivotrule=lambda D: largest_increase(D, 0.0001))
        scipyRes = scipy.optimize.linprog(-self.c, self.A, self.b, method="simplex")
        if res == LPResult.OPTIMAL:
            self.assertEqual(scipyRes.status, 0)
            self.assertIsNotNone(D)
            self.assertAlmostEqual(D.value(), -scipyRes.fun)
            for (a,b) in zip(list(D.basic_solution()), scipyRes.x) :
                self.assertAlmostEqual(a,b)
        if res == LPResult.UNBOUNDED:
            self.assertEqual(scipyRes.status, 3)
        if res == LPResult.INFEASIBLE:
            self.assertEqual(scipyRes.status, 2)

    def test_solve_multiple(self):
        for _ in range (100):
            self.test_solve()
            self.test_solve_float()

if __name__ == '__main__':
    unittest.main()
