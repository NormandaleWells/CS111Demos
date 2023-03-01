numbers = { "one":1, "two":2, "three":3, "four":4, "five":5 }
print(numbers)
number_keys = sorted(numbers)
print(number_keys)
for num in number_keys:
    print(num, numbers[num])
