# string_calculator.py

def add(numbers: str) -> int:
    if numbers == "":
        return 0
    # return sum(map(int, numbers.replace("\n", ",").split(',')))

    if numbers.startswith("//"):
        delimiter = numbers[2:numbers.index("\n")]
        numbers = numbers[numbers.index("\n")+1:]
        return sum(map(int, numbers.split(delimiter)))
    return sum(map(int, numbers.replace("\n", ",").split(',')))

