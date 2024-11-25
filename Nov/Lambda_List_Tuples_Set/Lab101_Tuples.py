# cities = ("London", "Paris", "Los Angeles", "Tokyo")
# print("Paris" in cities)
# print("Mumbai" in cities)

t = (12, 34, 56)
# t.append(12) #AttributeError: 'tuple' object has no attribute 'append'
print(t)
my_list=list(t)
my_list.append(4)
t=tuple(my_list)
print(t)
