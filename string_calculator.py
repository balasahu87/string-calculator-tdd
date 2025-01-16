from abc import ABC, abstractmethod


# Abstract class for operations
class Operation(ABC):
    @abstractmethod
    def execute(self, numbers: str) -> float:
        pass


# Utility to parse input and handle negative numbers
class InputParser:
    @staticmethod
    def parse_input(numbers: str, default_delimiter: str = ",") -> list:
        if numbers == "":
            return []

        delimiter = default_delimiter
        if numbers.startswith("//"):
            delimiter = numbers[2:numbers.index("\n")]
            numbers = numbers[numbers.index("\n") + 1:]

        numbers = numbers.replace("\n", delimiter)
        num_list = list(map(int, numbers.split(delimiter)))

        # Check for negative numbers
        negative_numbers = [num for num in num_list if num < 0]
        if negative_numbers:
            raise ValueError(
                f"Negative numbers not allowed: {', '.join(map(str, negative_numbers))}"
            )

        return num_list


# Concrete operations
class AddOperation(Operation):
    def execute(self, numbers: str) -> int:
        num_list = InputParser.parse_input(numbers)
        return sum(num_list)


class SubtractOperation(Operation):
    def execute(self, numbers: str) -> int:
        num_list = InputParser.parse_input(numbers)
        if not num_list:
            return 0
        result = num_list[0]
        for num in num_list[1:]:
            result -= num
        return result


class MultiplyOperation(Operation):
    def execute(self, numbers: str) -> int:
        num_list = InputParser.parse_input(numbers)
        result = 1
        for num in num_list:
            result *= num
        return result


class DivideOperation(Operation):
    def execute(self, numbers: str) -> float:
        num_list = InputParser.parse_input(numbers)
        if not num_list:
            raise ValueError("Division requires at least one number.")
        result = num_list[0]
        for num in num_list[1:]:
            if num == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result /= num
        return result
