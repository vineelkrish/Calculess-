import math

def get_input():
    """Function to take input from the user."""
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

def Add(a, b):
    pass

def Sub(a, b):
    pass

def Mul(a, b):
    pass  

def Div(a, b):
    pass


def calculator():
    print("\nWelcome to the Team Calculator!")
    a, b = get_input()  # Taking input for `a` and `b`
    print(f"Values received: a = {a}, b = {b}")
    print(f"Addition of {a} and {b} is {Add(a,b)}")
    print(f"Subtraction of {a} and {b} is {Sub(a,b)}")
    print(f"Subtraction of {a} and {b} is {Mul(a,b)}")
    print(f"Division of {a} and {b} is {Div(a,b)}")
    

    

if __name__ == "__main__":
    calculator()