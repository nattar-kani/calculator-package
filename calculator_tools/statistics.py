from typing import List
from .exceptions import InvalidOperationError

def calculate_average(numbers: List[float]) -> float:
    if not isinstance(numbers, list):
        raise InvalidOperationError("Input must be a list of numbers.")
    if not numbers:
        raise InvalidOperationError("Cannot calculate average of an empty list.")
    
    for num in numbers:
        if not isinstance(num, (int, float)) or isinstance(num, bool):
            raise InvalidOperationError(f"Invalid element '{num}' in list. Expected numbers only.")
            
    return sum(numbers) / len(numbers)