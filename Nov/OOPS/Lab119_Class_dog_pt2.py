class Dog:
    # Attribute
    name = 'Tommy'
    breed = None
    height = None

    def __init__(self):
        print('I been called')
    # Behaviour

    def bark(self):
        print("Barking")

    def sleep(self):
        print('sleep')

    def talk(self):
        pass


# Object Ref

chow_ref = Dog()
mow_ref = Dog()
print(chow_ref.name)
