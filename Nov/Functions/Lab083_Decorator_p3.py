
def deco1(func):
    def wrapper():
        print('This is decorator1')
        func()
    return wrapper

def deco2(func):
    def wrapper():
        print('This is decorator2')
        func()
    return wrapper


@deco1
@deco2
def say_hello():
    print('hello')

say_hello()