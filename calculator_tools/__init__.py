# Expose selected components directly at the package level
from .arithmetic import add, subtract, multiply, divide, percentage
from .statistics import calculate_average
from .converter import celsius_to_fahrenheit, km_to_miles
from .exceptions import InvalidOperationError

__all__ = [
    'add', 'subtract', 'multiply', 'divide', 'percentage',
    'calculate_average', 'celsius_to_fahrenheit', 'km_to_miles',
    'InvalidOperationError'
]