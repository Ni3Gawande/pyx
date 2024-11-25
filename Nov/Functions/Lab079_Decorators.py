def add_extra_security(func):

    def wrapper():
        print("1.Before the function is called")
        print("2.gloves and all")
        func()
        print("3.After the function is called")
        print("4.reach the destination")

    return wrapper()

@add_extra_security
def driving_scooty():
    print("Normal Function")
    print("I am driving my scooty")

