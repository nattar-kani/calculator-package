from .exceptions import InvalidOperationError

def add(a: float, b: float) -> float:
    _validate_number(a, b)
    return a + b

def subtract(a: float, b: float) -> float:
    _validate_number(a, b)
    return a - b

def multiply(a: float, b: float) -> float:
    _validate_number(a, b)
    return a * b

def divide(a: float, b: float) -> float:
    _validate_number(a, b)
    if b == 0:
        raise InvalidOperationError("Division by zero is not allowed.")
    return a / b

def percentage(part: float, total: float) -> float:
    _validate_number(part, total)
    if total <= 0:
        raise InvalidOperationError("Total must be greater than zero for percentage calculation.")
    return (part / total) * 100

def _validate_number(*args):
    for arg in args:
        if not isinstance(arg, (int, float)) or isinstance(arg, bool):
            raise InvalidOperationError(f"Invalid input '{arg}'. Expected a real number.")