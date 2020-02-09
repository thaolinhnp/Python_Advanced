from thuvien import *
import unittest
class TestMethods(unittest.TestCase):
    def test1(self):
        self.assertEqual(tinh_tong(3,4),7)
    def test2(self):
        self.assertEqual(tinh_tong(3,6),10)
    def test3(self):
        self.assertEqual(tinh_tong(3,5),8)
        
if __name__ == "__main__":
    unittest.main()