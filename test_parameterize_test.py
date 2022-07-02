import unittest


class ReturnSumOfTwoNumbers:

    def return_sum_of_two_numbers(self, a: int, b: int):
        return a + b


class TestAddTwoNumbers(unittest.TestCase):


    def test_return_addition_of_two_numbers_withoutsubtest(self):
        ins = ReturnSumOfTwoNumbers()
        test_cases = [
            (10, 20, 30),
            (5, 10, 15),
            (85, 15, 100),
        ]
        for number1, number2, sum in test_cases:
                self.assertEqual(sum, ins.return_sum_of_two_numbers(number1, number2))

    def test_return_addition_of_two_numbers(self):
        ins = ReturnSumOfTwoNumbers()
        test_cases = [
            (10, 20, 30),
            (5, 10, 20),
            (85, 15, 100),
        ]
        for number1, number2, sum in test_cases:
            with self.subTest(f"{number1}, {number2} --> {sum}"):
                self.assertEqual(sum, ins.return_sum_of_two_numbers(number1, number2))



if __name__ == "__main__":
    unittest.main()
