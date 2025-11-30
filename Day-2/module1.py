# Modules

def addition(num1, num2):
    add = num1 + num2
    return add
    
def subraction(num1, num2):
    sub = num1 - num2
    return sub

def multiplication(num1, num2):
    mul = num1 *  num2
    return mul

if __name__ == "__main__":
    print("Addition:", addition(10, 5))
    print(F"Subraction: {subraction(10, 5)}")
    print(F"Multiplication: {multiplication(10, 5) + 5}")