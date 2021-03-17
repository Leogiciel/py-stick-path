import unittest

import paths_worker


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(
            paths_worker.compute_paths(
                "7 7 \n"
                "A  B  C \n"
                "|  |  | \n"
                "|--|  | \n"
                "|  |--| \n"
                "|  |--| \n"
                "|  |  | \n"
                "1  2  3"
            ),
            "A2\nB1\nC3",
        )
        self.assertEqual(
            paths_worker.compute_paths(
                "22 18 \n"
                "P  Q  R  S  T  U  V  W\n"
                "|  |  |  |  |--|  |  |\n"
                "|  |  |--|  |  |  |--|\n"
                "|  |--|  |--|  |  |  |\n"
                "|--|  |--|  |  |  |--|\n"
                "|--|  |  |  |  |--|  |\n"
                "|  |--|  |  |--|  |--|\n"
                "|  |  |  |--|  |--|  |\n"
                "|--|  |  |  |--|  |  |\n"
                "|  |  |--|  |  |  |  |\n"
                "|  |  |  |--|  |  |--|\n"
                "|  |  |  |  |--|  |  |\n"
                "|--|  |  |  |  |  |  |\n"
                "|--|  |--|  |  |  |--|\n"
                "|  |--|  |  |--|  |  |\n"
                "|  |  |--|  |  |  |--|\n"
                "|--|  |--|  |  |--|  |\n"
                "1  2  3  4  5  6  7  8\n"
            ),
            "P3\nQ7\nR8\nS5\nT6\nU2\nV4\nW1",
        )


if __name__ == "__main__":
    unittest.main(exit=False)
