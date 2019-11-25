import unittest

import classCalc


class Test_calc(unittest.TestCase):

    def test_mul(self):
        print("test_mul")
        c = classCalc.Calcution(2,2,2)

        self.assertEqual(c.mul(),8)


if __name__ == "__main__":
    unittest.main()
