import random

'''
Generate n unique numbers in the range [-m..m)
in random order.
'''
def generate_unique_list(n, m):
    a = list(range(-m, m))
    random.shuffle(a)
    return a[:n]


def test():
    a = generate_unique_list(10, 20)
    print(a)


if __name__ == "__main__":
    test()
