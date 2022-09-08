class JarBar():
    def __init__(self, num):
        self.num = num

    def to_string(self):
        if not str(self.num).isdigit():
            return ""

import unittest

class Test(unittest.TestCase):
    def test_non_numbers(self):
        test1 = JarBar("nan")
        self.assertEqual(test1.to_string(), "")
    
    def test_negative_nums(self):
        test1 = JarBar(-1)
        self.assertEqual(test1.to_string(), "")

    def test_zero(self):
        test1 = JarBar(0)
        self.assertEqual(test1.to_string(), "")

    def test_positive_nums(self):
        test1 = JarBar(5)
        self.assertEqual(test1.to_string(), "1\n2\nJar\n4\nBar\n")
        
        test2 = JarBar(15)
        self.assertEqual(test2.to_string(), "1\n2\nJar\n4\nBar\nJar\n7\n8\nJar\nBar\n11\nJar\n13\n14\nJarBar")

if __name__ == '__main__':
    unittest.main()