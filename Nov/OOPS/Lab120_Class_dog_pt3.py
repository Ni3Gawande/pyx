class Dog:
    # Attribute
    name = None
    breed = None
    height = None

    def __init__(self,name,breed):
        print('PC')
        self.name=name
        self.breed=breed
    # Behaviour

    def bark(self):
        print("Barking")

    def sleep(self):
        print('sleep',self.name)

    def talk(self):
        pass


# Object Ref

chow_ref = Dog('chow','Pomi')
mow_ref = Dog('mow','german')
print(chow_ref.name)
print(mow_ref.breed)
chow_ref.sleep()
