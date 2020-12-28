# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows,
# actions, and settings.


import functools


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list = [8, 2, 2, 2]
    print(functools.reduce(lambda x, y: x + y, list))
    print(functools.reduce(lambda x, y: x if x > y else y, list))
    print(functools.reduce(lambda x, y: x if x < y else y, list))
    print(functools.reduce(lambda x, y: x / y, list))
    numbers = [1, 2, 3]

    myresults = filter(lambda x: (x + 1) * 3 / 3 % 3 == 0, numbers)
    for f in myresults:
        print(f)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
