import copy

my_list = [[1,2], [3,4], [5,6]]
list_2 = copy.deepcopy(my_list)

list_2[0].append(7)
print(list_2)
print(my_list)