#import relevant methods
from codeSample import my_summer
#import unittest package
import unittest

#class must start with "Test"
class TestTutorial(unittest.TestCase):
    #the methods must start with "test_"
    def test_summer(self):
        self.assertEqual(1+3, my_summer(2,3))

if __name__ == '__main__':
    unittest.main(exit=False)