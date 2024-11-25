set1 = {1, 2, 3}
set2 = {4, 5, 6}
my_set = set1.union(set2)
print(my_set)

set1 = {1, 2, 3,4,5}
set2 = {4, 5, 6,7,9}
my_set2=set1.intersection(set2)
print(my_set2)

my_set=set1.difference(set2)
print(my_set)
my_set=set2.difference(set1)
print(my_set)
