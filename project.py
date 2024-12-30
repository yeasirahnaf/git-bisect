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
    return a - b

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

if __name__ == "__main__":
    print(add(2,3))
    print(multiply(4,5))
    print(divide(10,2))
    print(subtract(10,5))
    print(power(2,3))
    print(modulo(7,3))