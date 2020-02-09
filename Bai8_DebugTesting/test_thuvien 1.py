from thuvien import *
import unittest
class TestMethods(unittest.TestCase):
    def runTest(self):
        self.assertEqual(tinh_tong(3,4),7)
        self.assertEqual(tinh_tong(3,6),10)
        self.assertEqual(tinh_tong(3,5),8)

def suite():
    suite = unittest.TestSuite()
    suite.addTest (TestMethods())
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run (test_suite)