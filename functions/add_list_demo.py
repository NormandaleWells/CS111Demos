def add_list(alist):
    total = 0
    for num in alist:
        total += num
    # alist.append("george")
    return total

my_list = [7, 3, 5, 4]
sum = add_list(my_list)
print(sum)
