print(bool(0))
print(bool(1))
print(bool(-1))
print()

print(bool(0.0))
print(bool(0.0000000000001))
print(bool(-0.0))
print()

print(bool([]))
print(bool([1]))
print(bool([[]]))
print()

print(bool(""))
print(bool("xyzzy"))
print(bool("0"))
print(bool("False"))

my_list = []

if len(my_list) != 0:
    pass
if my_list:
    pass
else:
    
