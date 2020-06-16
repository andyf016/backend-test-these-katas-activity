import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        result = katas.add(1, 1)
        self.assertEqual(result, 2)
        # self.fail("TODO: Write add unit test")

    def test_multiply(self):
        result = katas.multiply(5, 5)
        self.assertEqual(result, 25)
        # self.fail("TODO: Write multiply unit test")

    def test_power(self):
        result = katas.power(5, 5)
        self.assertEqual(result, 3125)
        # self.fail("TODO: Write power unit test")

    def test_factorial(self):
        result = katas.factorial(5)
        self.assertEqual(result, 120)
        # self.fail("TODO: Write factorial unit test")

    def test_fibonacci(self):
        result = katas.fibonacci(10)
        self.assertEqual(result, 34)
        # self.fail("TODO: Write fibonacci unit test")


if __name__ == '__main__':
    unittest.main()
