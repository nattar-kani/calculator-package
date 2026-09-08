from calculator_tools import (
    add, subtract, multiply, divide, percentage,
    calculate_average, celsius_to_fahrenheit, km_to_miles,
    InvalidOperationError
)

def show_menu():
    print("\n==============================")
    print("   REAL-TIME CALCULATOR TOOLS")
    print("==============================")
    print("1. Basic Arithmetic (+, -, *, /)")
    print("2. Percentage Calculation")
    print("3. Average of Numbers")
    print("4. Celsius to Fahrenheit")
    print("5. Kilometers to Miles")
    print("6. Exit")

def real_time_calculator():
    while True:
        show_menu()
        choice = input("\nSelect an option (1-6): ").strip()

        try:
            if choice == '1':
                a = float(input("Enter first number: "))
                op = input("Enter operator (+, -, *, /): ").strip()
                b = float(input("Enter second number: "))
                
                if op == '+': res = add(a, b)
                elif op == '-': res = subtract(a, b)
                elif op == '*': res = multiply(a, b)
                elif op == '/': res = divide(a, b)
                else: raise InvalidOperationError(f"Unsupported operator '{op}'")
                
                print(f"Result: {res}")

            elif choice == '2':
                part = float(input("Enter part: "))
                total = float(input("Enter total: "))
                print(f"Result: {percentage(part, total):.2f}%")

            elif choice == '3':
                raw_input = input("Enter numbers separated by spaces (e.g., 10 20 30): ")
                numbers = [float(x) for x in raw_input.split()]
                print(f"Average: {calculate_average(numbers)}")

            elif choice == '4':
                c = float(input("Enter temperature in Celsius: "))
                print(f"Result: {celsius_to_fahrenheit(c)}°F")

            elif choice == '5':
                km = float(input("Enter distance in Kilometers: "))
                print(f"Result: {km_to_miles(km):.2f} miles")

            elif choice == '6':
                print("Exiting calculator. Goodbye!")
                break
            else:
                print("Invalid choice! Please select 1-6.")

        except ValueError:
            print("Input Error: Please enter valid numbers.")
        except InvalidOperationError as e:
            print(f"Custom Error Caught: {e}")

if __name__ == "__main__":
    real_time_calculator()