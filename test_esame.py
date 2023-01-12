import unittest
from esame import *


class MyTestCase(unittest.TestCase):
    def test_init_str(self):
        self.assertRaises(ExamException, Diff, 'Hello')

    def test_init_zero(self):
        self.assertRaises(ExamException, Diff, 0)


if __name__ == '__main__':
    unittest.main()
