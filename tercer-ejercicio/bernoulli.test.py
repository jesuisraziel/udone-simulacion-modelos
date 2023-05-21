import unittest
from bernoulli import * 

class BernoulliTest(unittest.TestCase):
    def testProbability(self):
       p = 1/6
       success = bernoulli_probability(1,p)
       failure = bernoulli_probability(0,p)
       self.assertAlmostEqual(p, success)
       self.assertAlmostEqual(1-p, failure)

    def testMean(self):
        p = 1/6
        mean = bernoulli_mean(p)
        self.assertEqual(p,mean)

    def testVariance(self):
       p = 1/6
       q = 1-p
       variance = bernoulli_variance(p)
       self.assertAlmostEqual(variance, p*q) 

if __name__ == '__main__':
    unittest.main()
