class Calculator:
    
    def __init__(self,name):
        self.name = name

    def add(self,a,b):
        sum = a + b
        print(f'output: {sum}')

    def subtract(self,a,b):
        sum = a - b
        print(f'output: {sum}')

    def multiply(self,a,b):
        sum = a * b
        print(f'output: {sum}')

    def divide(self,a,b):
        if a <= 0 or b <= 0:
            print("Number is not divisable")

        else:
            sum = a / b
            print(f'output: {sum}')

    def calculator_options(self):
        print("(a) for addition")
        print("(s) for subtraction")
        print("(m) for multiplication")
        print("(d) for division")

def calculator():

    obj = Calculator("Talha")
    obj.calculator_options()

    while True:

        try:
            user = input("Enter Here: ").lower().strip()

            if user == 'a':
                num1 = int(input("Enter your first number: "))
                num2 = int(input("Enter your second number: "))
                obj.add(num1,num2)

            elif user == 's':
                num1 = int(input("Enter your first number: "))
                num2 = int(input("Enter your second number: "))
                obj.subtract(num1,num2)

            elif user == 'm':
                num1 = int(input("Enter your first number: "))
                num2 = int(input("Enter your second number: "))
                obj.multiply(num1,num2)

            elif user == 'd':
                num1 = int(input("Enter your first number: "))
                num2 = int(input("Enter your second number: "))
                obj.divide(num1,num2)

            else:
                print("Invalid Syntax")

        except:
            print("error occured")

if __name__ == "__main__":
    calculator()