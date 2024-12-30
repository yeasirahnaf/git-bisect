def add(a,b):
    """Adds two numbers"""

def greet(name):
    return f"Greetings, {name}!"

def add(a,b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Inputs must be numbers")
        return a+b

def multiply(a, b):
    return a + b  # BUG: Should be a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def subtract(a, b):
    return b - a  # BUG: Should be a - b

def power(a, b):
    return a**b

def modulo(a, b):
    return a % b

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))
    print()
    print(add(2, 3))
    print()
    print(multiply(4, 5))
    print()
    print(divide(10, 2))
    print()
    print(subtract(10, 5))
    print()
    print(power(2,3))
    print()
    print(modulo(7,3))
    print()
    print(subtract(10,5))

if __name__ == "__main__":
    print("Add:",add(2,3))
    print("Multiply:",multiply(4,5))
    print("Divide:",divide(10,2))
    print("Subtract:",subtract(10,5))
    print("Power:",power(2,3))
    print("Modulo:",modulo(7,3))