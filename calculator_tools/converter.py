from .exceptions import InvalidOperationError

def celsius_to_fahrenheit(celsius: float) -> float:
    _validate_number(celsius)
    return (celsius * 9/5) + 32

def km_to_miles(km: float) -> float:
    _validate_number(km)
    if km < 0:
        raise InvalidOperationError("Distance cannot be negative.")
    return km * 0.621371

def _validate_number(val):
    if not isinstance(val, (int, float)) or isinstance(val, bool):
        raise InvalidOperationError(f"Invalid value '{val}'. Expected a real number.")