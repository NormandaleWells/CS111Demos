
def find(a, k):
    for i in range(len(a)):
        if a[i] == k:
            return k
    return -1


def power(a,b):
    result = 1
    while b != 0:
        if b % 2 != 0:
            result *= a
        a *= a
        b = b // 2
    return result


def mystery(a, k):
    if a[0] == k:
        return True
    else:
        return mystery(a[1:], k)


print(power(4,3))
print(power(3,4))

def sum(a):
    if len(a) == 0:
        return 0
    else:
        return a[0] + sum(a[1:])


print(sum([1,2,3,4,5]))
