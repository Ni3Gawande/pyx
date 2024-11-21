# USer defines
# 1.They can't return -> non-return
# 2.They can return somthing
# 3.They have parameters
# 4.They don't have parameters and arguments


# 1.They can't return -> non-return
# No return and No Parameter/ Argument -NRNP

def greet():
    print("Hello")


greet()


# 2.They can return somthing
# No return type with argument/Param

def greet_by_name(name):
    print(f'Hello, {name}')


greet_by_name('Automoto')

# 3.They have parameters
# NO return with default argument

def say_hello_default(name='Automoto'):
    print("Hello",name.upper())
say_hello_default('Luci')


def multi_args(name1='Auto',name2='Moto'):
    print("Hello",name1,name2)
multi_args()
multi_args('Danger')
multi_args(name2='Suchi')
multi_args(name1='Luci')
multi_args(name1='Luci',name2='Suchi')

# 4.Arguments with return type

def sum_of_two(a,b):
    return a+b

result=sum_of_two(4,56)
print(result)