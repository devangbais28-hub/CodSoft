# Simple_Calculator with Arithmetic Operations
 
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Division by zero is not possible"

calc = Calculator()

print("===== SIMPLE CALCULATOR =====")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose Operation")
print("1 for Addition")
print("2 for Subtraction")
print("3 for Multiplication")
print("4 for Division")

choice = input("Enter your choice: ")

if choice == '1':
    print("Result =", calc.add(num1, num2))

elif choice == '2':
    print("Result =", calc.subtract(num1, num2))

elif choice == '3':
    print("Result =", calc.multiply(num1, num2))

elif choice == '4':
    print("Result =", calc.divide(num1, num2))

else:
    print("Invalid Choice")