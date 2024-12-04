

class Person:
    def __init__(self):
        print("I will be called")
        self.name=input("Enter the name\n")
        self.age=input("Enter the age\n")
        self.phone=input("Enter the phone\n")
        self.occupation=input("Enter the occupation\n")


    def name_of_the_function(self):
        print(f"name is {self.name}",f"Age is {self.age}",f"phone number is {self.phone}",
              f" occuption is {self.occupation}")


person1=Person()
person1.name_of_the_function()