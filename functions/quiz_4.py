list_1 = [27, 82, 41,124]
list_2 = list_1
print(list_1 is list_2)
print(list_1 == list_2)


list_1 = [27, 82, 41,124]
list_2 = list_1[:]
print(list_1 is list_2)
print(list_1 == list_2)


list_1 = [27, 82, 41,124]
list_2 = list_1
list_2[0] = 100
print(list_1 is list_2)
print(list_1 == list_2)
