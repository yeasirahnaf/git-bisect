def greet(name):
    return f"Greetings, {name}!"

def add(a, b):
    return a + b

def multiply(a, b):
    return a + b  # BUG: Should be a * b

def divide(a, b):
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