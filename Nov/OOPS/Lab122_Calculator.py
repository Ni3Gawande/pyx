class Calc:
    def __init__(self):
        print("DC")

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


calculator = Calc()
a = float(input("enter the value of a: "))
b = float(input("enter the value of b: "))

outputSum = calculator.sum(a, b)
outputSub = calculator.sub(a, b)
outputMul = calculator.mul(a, b)
outputDiv = calculator.div(a, b)

print(f"Addition is {outputSum}", f"Subtraction is {outputSub}", f"Multiplication is {outputMul}",
      f"Division is {outputDiv}")
