pb_global=12

def my_function():
    pb_a=10
    print(pb_a)
    print(pb_global)

# print(pb_a) cannot print as it is defined inside function
print(pb_global)
my_function()