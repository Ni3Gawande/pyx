my_list = [1, 2, 3]
print("Element at the index 0 -", my_list[0])
print("Element at the index 1 -", my_list[1])
print("Element at the index 2 -", my_list[2])

# Append() Add object to the end of the list
my_list.append(4)
my_list.append(7)
print(my_list)

# Extend()-Append a new lust at the end of list
my_list.extend([10, 8, 9])
print(my_list)

# Insert() -At What index you want to add
my_list.insert(1, 'Nitin')
print(my_list)
my_list.insert(0, 0)
print(my_list)
print(len(my_list))

# Remove()
my_list[1] = 'Amit'
print(my_list)
my_list.remove("Amit")
print(my_list)

print("------------------------------")
print("------------------------------")

my_copy_list = my_list.copy()
print(my_copy_list)
my_copy_list.remove('Nitin')
my_copy_list.sort()
print(my_copy_list)
