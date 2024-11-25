my_list1 = [1, 2, 4]
my_list2 = [1, True, 'Name', 12.34]
print(my_list1)
print(len(my_list1))
print(my_list1[0])
print(my_list1[1])
print(my_list1[2])
# print(my_list1[3]) #Index out of range
my_list1[0] = 'Amit'
my_list1[1] = "tang"
my_list1[2] = 'Pang'
print(my_list1)

for i in my_list1:
    print(i)

print('______')
for item in my_list2:
    print(item, end=' ')
