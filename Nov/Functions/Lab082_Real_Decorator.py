import time


def time_decorator(func):
    def wrapper():
        start_time=time.time()
        print(start_time)
        func()
        end_time=time.time()
        print(end_time)
        print("total",end_time-start_time)

    return wrapper()


@time_decorator
def ui1():
    print("Add a function,time taken by function 1")
    time.sleep(2)

@time_decorator
def ui2():
    print("Add a function,time taken by function 2")
    time.sleep(5)
