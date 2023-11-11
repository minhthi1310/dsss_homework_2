import unittest
from math_quiz import get_random_number, random_operation, create_question

class TestMathGame(unittest.TestCase):

    def test_get_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operation(self):
        # TODO
          for _ in range(1000):  # Test a large number of random values
            o = random_operation()
            self.assertTrue(o == '+' or o == '-' or o =='*')
          pass

    def test_create_question(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (2,2,'*','2 * 2',4),
                (5,2,'-','5 - 2',3)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                problem, answer = create_question(num1, num2, operator)
                
                self.assertTrue(problem == expected_problem and answer == expected_answer )
            pass

if __name__ == "__main__":
    unittest.main()
