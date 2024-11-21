# Create a program to sum of three number from the user input
# if user does not enter any number use number 100,200,300

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))


def sum_of_three(a=100, b=200, c=300):
    return a + b + c


result = sum_of_three(a, b, c)
print(result)


# result2=sum_of_three()
# print(result2)