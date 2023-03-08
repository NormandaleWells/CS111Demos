import create_test_data

'''
Find the number of pairs of items in list a that sum to 0.
'''
def two_sum_slow(a):
    count = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] + a[j] == 0:
                count += 1
    return count


'''
Find the number of pairs of items in list a that sum to 0.
NOTE: This does work correctly if there are
duplicate items in the list.
'''
def two_sum_fast(a):
    count = 0
    nums = set()
    for num in a:
        if -num in nums:
            count += 1
        nums.add(num)
    return count


def main():
    a = create_test_data.generate_unique_list(10, 20)
    print(a)
    count_slow = two_sum_slow(a)
    count_fast = two_sum_fast(a)
    print(count_slow, count_fast)


if __name__ == "__main__":
    main()
