'''
Code from section 2.4 of Runestone's _Python Data Structures_,
with some improvements.
'''
def anagram_solution_1(s1, s2):

    if len(s1) != len(s2):
        return False

    list1 = list(s2)
    pos_1 = 0

    for i in range(len(s1)):
        found = False
        for j in range(len(list1)):
            if s1[i] == list1[j]:
                found = True
                list1[j] = None
                break
        if not found:
            return False

    return True


print(anagram_solution_1("apple", "pleap"))  # expected: True
print(anagram_solution_1("abcd", "dcba"))  # expected: True
print(anagram_solution_1("abcd", "dcda"))  # expected: False


def anagram_solution_2(s1, s2):
    a_list_1 = list(s1)
    a_list_2 = list(s2)

    a_list_1.sort()
    a_list_2.sort()

    return a_list_1 == a_list_2


print(anagram_solution_2("apple", "pleap"))  # expected: True
print(anagram_solution_2("abcd", "dcba"))  # expected: True
print(anagram_solution_2("abcd", "dcda"))  # expected: False


def anagram_solution_4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord("a")
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord("a")
        c2[pos] = c2[pos] + 1

    return c1 == c2


print(anagram_solution_4("apple", "pleap"))  # expected: True
print(anagram_solution_4("abcd", "dcba"))  # expected: True
print(anagram_solution_4("abcd", "dcda"))  # expected: False
