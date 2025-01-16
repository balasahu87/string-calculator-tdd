# string_calculator.py

def add(numbers: str) -> int:
    if numbers == "":
        return 0
    return sum(map(int, numbers.split(',')))
