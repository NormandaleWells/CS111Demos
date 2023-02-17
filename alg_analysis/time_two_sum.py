import two_sum
import create_test_data
import time
import sys


def run_one_test(test_slow, test_fast, n, m):

    a = create_test_data.generate_unique_list(n, m)

    if test_slow:
        start = time.time()
        count_slow = two_sum.two_sum_slow(a)
        end = time.time()
        time_slow = end - start

    if test_fast:
        start = time.time()
        count_fast = two_sum.two_sum_fast(a)
        end = time.time()
        time_fast = end - start

    if test_slow and test_fast and count_slow != count_fast:
        print("Error!  two_sum_slow -> {count_slow}, two_sum_fast -> {count_fast}")
        sys.exit(1)

    print(f"n = {n:6}   ", end = "")
    if test_slow:
        print(f"slow: {time_slow:10.4f}", end="")
    if test_slow and test_fast:
        print("   ", end="")
    if test_fast:
        print(f"fast: {time_fast:10.4f}", end="")
    print()


def main():
    test_slow = True
    test_fast = False
    run_one_test(test_slow, test_fast,  1000,  2000)
    run_one_test(test_slow, test_fast,  2000,  4000)
    run_one_test(test_slow, test_fast,  4000,  8000)
    run_one_test(test_slow, test_fast,  8000, 16000)
    run_one_test(test_slow, test_fast, 16000, 32000)
    run_one_test(test_slow, test_fast, 32000, 64000)


if __name__ == "__main__":
    main()
