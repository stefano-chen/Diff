import unittest
from esame import *


class MyTestCase(unittest.TestCase):
    def test_init_str(self):
        self.assertRaises(ExamException, Diff, 'Hello')

    def test_init_zero(self):
        self.assertRaises(ExamException, Diff, 0)

    def test_compute_empty_list(self):
        x = Diff()
        self.assertRaises(ExamException, x.compute, [])

    def test_compute_one_element_list(self):
        x = Diff()
        self.assertRaises(ExamException, x.compute, [1])

    def test_compute_not_a_list(self):
        x = Diff()
        self.assertRaises(ExamException, x.compute, 1)

    def test_compute_list_of_str(self):
        x = Diff()
        self.assertRaises(ExamException, x.compute, [1, 1.1, 'Hello'])

    def test_compute(self):
        x = Diff()
        self.assertEqual(x.compute([2, 4, 8, 16]), [2, 4, 8])

    def test_init_negative_ratio(self):
        self.assertRaises(ExamException, Diff, -1)

    def test_compute_double_ratio(self):
        x = Diff(2)
        self.assertEqual(x.compute([2, 4, 8, 16]), [1, 2, 4])

    def test_compute_float_ratio(self):
        x = Diff(0.5)
        self.assertEqual(x.compute([2, 4, 8, 16]), [4, 8, 16])


if __name__ == '__main__':
    unittest.main()
