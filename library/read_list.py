import sys


'''
    Read from stdin until EOF, converting each token on each line
    using the given conversion function (probably int or float),
    and return a list of converted elements.
'''
def read_numbers(conversion):
    numbers = []
    for line in sys.stdin:
        tokens = line.split()
        new_nums = [conversion(s) for s in tokens]
        numbers += new_nums
    return numbers


'''
    Read integers from stdin until EOF, and return a list
    of the read integers.
'''
def read_ints():
    return read_numbers(int)


'''
    Read floats from stdin until EOF, and return a list
    of the read integers.
'''
def read_floats():
    return read_numbers(float)


def test():
    int_list = read_ints()
    print(int_list)
    # apparently, Python automatically resets stdin after EOF
    # to accept more input
    float_list = read_floats()
    print(float_list)


if __name__ == "__main__":
    test()
