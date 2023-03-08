# binary_search(a, k)
# Return the index of a s.t. a[idx] == m
# or -1 if k is not in a.
def binary_search(a, k):
    lo = 0
    hi = len(a)
    # k may be in a[lo,hi)
    while hi - lo != 0:
        m = lo + (hi - lo) // 2
        if a[m] == k:
            return m
        elif a[m] < k:
            lo = m + 1
        else:
            hi = m
    return -1

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43]

for i in range(len(primes)):
    if binary_search(primes, primes[i]) != i:
        print("FAIL!!")

if binary_search(primes, 0) != -1:
    print("FAIL!!!")
if binary_search(primes, 44) != -1:
    print("FAIL!!!!")
if binary_search(primes, 20) != -1:
    print("FAIL!!!!!")

print("Done")
