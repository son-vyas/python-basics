import unittest
from factorial import fact

class TestFactorial(unittest.TestCase):

    def fact(self):
        res = fact(n)
        self.assertEqual(res,120)


    if __name__ == '__main__':
        unittest.main()
        
