import unittest
from string_calculator import AddOperation, SubtractOperation, MultiplyOperation, DivideOperation


class TestCalculatorOperations(unittest.TestCase):
    def setUp(self):
        self.adder = AddOperation()
        self.subtracter = SubtractOperation()
        self.multiplier = MultiplyOperation()
        self.divider = DivideOperation()

    # Test cases for addition
    def test_add_empty_string(self):
        self.assertEqual(self.adder.execute(""), 0)

    def test_add_single_number(self):
        self.assertEqual(self.adder.execute("5"), 5)

    def test_add_multiple_numbers(self):
        self.assertEqual(self.adder.execute("1,2,3"), 6)

    def test_add_custom_delimiter(self):
        self.assertEqual(self.adder.execute("//;\n1;2"), 3)

    def test_add_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            self.adder.execute("1,-2,3")
        self.assertEqual(
            str(context.exception), "Negative numbers not allowed: -2"
        )

    def test_add_multiple_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            self.adder.execute("1,-2,-3,4")
        self.assertEqual(
            str(context.exception), "Negative numbers not allowed: -2, -3"
        )

    # Test cases for subtraction
    def test_subtract_empty_string(self):
        self.assertEqual(self.subtracter.execute(""), 0)

    def test_subtract_single_number(self):
        self.assertEqual(self.subtracter.execute("5"), 5)

    def test_subtract_multiple_numbers(self):
        self.assertEqual(self.subtracter.execute("10,3,2"), 5)

    def test_subtract_custom_delimiter(self):
        self.assertEqual(self.subtracter.execute("//;\n10;3;2"), 5)

    def test_subtract_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            self.subtracter.execute("10,-3,-2")
        self.assertEqual(
            str(context.exception), "Negative numbers not allowed: -3, -2"
        )

    # Test cases for multiplication
    def test_multiply_empty_string(self):
        self.assertEqual(self.multiplier.execute(""), 1)

    def test_multiply_single_number(self):
        self.assertEqual(self.multiplier.execute("5"), 5)

    def test_multiply_multiple_numbers(self):
        self.assertEqual(self.multiplier.execute("2,3,4"), 24)

    def test_multiply_custom_delimiter(self):
        self.assertEqual(self.multiplier.execute("//;\n2;3;4"), 24)

    def test_multiply_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            self.multiplier.execute("2,-3,4")
        self.assertEqual(
            str(context.exception), "Negative numbers not allowed: -3"
        )

    # Test cases for division
    def test_divide_empty_string(self):
        with self.assertRaises(ValueError):
            self.divider.execute("")

    def test_divide_single_number(self):
        self.assertEqual(self.divider.execute("10"), 10)

    def test_divide_multiple_numbers(self):
        self.assertEqual(self.divider.execute("20,5,2"), 2.0)

    def test_divide_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.divider.execute("10,0")

    def test_divide_custom_delimiter(self):
        self.assertEqual(self.divider.execute("//;\n20;5;2"), 2.0)

    def test_divide_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            self.divider.execute("20,-5,2")
        self.assertEqual(
            str(context.exception), "Negative numbers not allowed: -5"
        )


if __name__ == "__main__":
    unittest.main()
