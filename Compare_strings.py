def strComparePermutations(str1, str2):
    """ This function takes two strings as an input. It returns True if the strings are permutations of each other,
    and False if not. A permutation is defined as containing the same characters but in a different order.

    This function has a space complexity of O(1) and time complexity of O(Nlog(N))
    """

    # If the two strings are of different lengths we can return immediately.
    if len(str1) != len(str2):
        return False

    # Sorting in python has a time complexity of O(Nlog(N))
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Comparing the sorted string will determine whether the strings are permutations of each other
    return sorted_str1 == sorted_str2

def main():
    print(strComparePermutations("string", "strngi"))
    print(strComparePermutations("string", "ingstr"))
    print(strComparePermutations("string", "notstring"))
    print(strComparePermutations("string", "strIng"))


if __name__ == '__main__':
    main()