class Person:
    # Attribute
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None

    # Behaviour

    def talk(self):  # Arg with no retun
        print('I can talk')

    def sleep(self):
        print("I can sleep")

Amit=Person()
Amit.talk()