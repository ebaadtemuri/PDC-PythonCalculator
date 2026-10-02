"""Simple calculator with execution-time reporting (CLI + reusable logic)."""
import time


def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def power(a, b): return a ** b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
}


def calculate(a, op, b):
    """Run one operation and return (result, execution_time_in_seconds)."""
    if op not in OPERATIONS:
        raise ValueError(f"Unsupported operator: {op}")
    start = time.perf_counter()
    result = OPERATIONS[op](a, b)
    elapsed = time.perf_counter() - start
    return result, elapsed


def main():
    print("=== Python Calculator ===")
    print("Operators: + - * / ^   (type 'q' to quit)\n")

    while True:
        choice = input("Enter expression (e.g. 12 * 5): ").strip()
        if choice.lower() in ("q", "quit", "exit"):
            print("Goodbye!")
            break
        try:
            a, op, b = choice.split()
            result, elapsed = calculate(float(a), op, float(b))
            print(f"Result: {result}")
            print(f"Execution time: {elapsed * 1e6:.2f} microseconds\n")
        except ValueError as e:
            print(f"Invalid input: {e}. Use the format: number operator number\n")
        except ZeroDivisionError as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
