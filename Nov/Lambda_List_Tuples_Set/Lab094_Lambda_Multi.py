# write  a program to calculate even and odd

# def find_even_odd(num):
#     if num % 2 == 0:
#         print('Even')
#     else:
#         print('Odd')
#
#
# find_even_odd(5)

n=int(input("Enter the value: "))
check_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
# print(check_even_odd(5))
# print(check_even_odd(10))
print(check_even_odd(n))
