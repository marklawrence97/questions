def get_missing_values(lst):
    """
    This function takes an input of a list of numbers, it then returns a list containing all the of the
    numbers that are missing in the interval of [1, 1000000]

    The time complexity is O(M) and the space complexity is O(M), where M is the max(N, 1000000).
    """

    values = set()
    missing_values = set()
    for number in lst:
        values.add(number)

    for number in range(1, 1000001):
        # Accessing a value in a set has linear time complexity, (O(1)).
        if number not in values:
            missing_values.add(number)

    return list(missing_values)


def main():
    f = open("input.txt", 'r')
    content = f.readlines()
    values = map(lambda x: int(x.split("\n")[0]), content)
    print(get_missing_values(values))

if __name__ == '__main__':
    main()
