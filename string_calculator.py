# string_calculator.py

def add(numbers: str) -> int:
    if numbers == "":
        return 0
    # return sum(map(int, numbers.replace("\n", ",").split(',')))

    delimiter = ","
    if numbers.startswith("//"):
        # Extract custom delimiter
        delimiter = numbers[2:numbers.index("\n")]
        numbers = numbers[numbers.index("\n") + 1:]

    # Replace newlines with the delimiter for uniform splitting
    numbers = numbers.replace("\n", delimiter)
    num_list = numbers.split(delimiter)

    # Check for negative numbers
    negative_numbers = [num for num in num_list if int(num) < 0]
    if negative_numbers:
        raise ValueError(f"Negative numbers not allowed: {', '.join(negative_numbers)}")

    # Calculate the sum
    return sum(map(int, num_list))


