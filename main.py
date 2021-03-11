import unittest
import paths_worker


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(paths_worker.compute_paths('7 7 \nA  B  C \n|  |  | \n|--|  | \n|  |--| \n|  |--| \n|  |  | \n1  2  3'), 'A2\nB1\nC3\n')
        self.assertEqual(paths_worker.compute_paths('22 18 \nP  Q  R  S  T  U  V  W \n|  |  |  |  |--|  |  | \n|  |  |--|  |  |  |--| \n|  |--|  |--|  |  |  | \n|--|  |--|  |  |  |--| \n|--|  |  |  |  |--|  | \n|  |--|  |  |--|  |--| \n|  |  |  |--|  |--|  | \n|--|  |  |  |--|  |  | \n|  |  |--|  |  |  |  | \n|  |  |  |--|  |  |--| \n|  |  |  |  |--|  |  | \n|--|  |  |  |  |  |  | \n|--|  |--|  |  |  |--| \n|  |--|  |  |--|  |  | \n|  |  |--|  |  |  |--| \n|--|  |--|  |  |--|  | \n1  2  3  4  5  6  7  8 '), 'P3\nQ7\nR8\nS5\nT6\nU2\nV4\nW1\n')


if __name__ == '__main__':
    unittest.main()
