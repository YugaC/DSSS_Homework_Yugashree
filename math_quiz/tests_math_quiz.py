import unittest
from math_quiz import random_integer_generate, random_operator_generate, calc


class TestMathGame(unittest.TestCase):

    def test_random_integer_generate(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer_generate(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator_generate(self):
        
        operators = {'+', '-', '*'}
        for _ in range(1000):
            rand_operator = random_operator_generate()
            self.assertIn(rand_operator, operators)
        

    def test_calc(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (9, 1, '-', '9 - 1', 8),
                (7, 4, '*', '7 * 4', 28),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                
                result_problem, result_answer = calc(num1, num2, operator)
                self.assertEqual(result_problem, expected_problem)
                self.assertEqual(result_answer, expected_answer)

                #if __name__ == "__main__":
    #unittest.main()
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMathGame))