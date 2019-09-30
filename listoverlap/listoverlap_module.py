""" Exercise:

Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

Write a function called "listoverlap" that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:

1) Randomly generate two lists to test this
2) Write this in one line of Python """

import random

def listoverlap(list1, list2):
    tmp = []
    for i in list1:
        for j in list2:
            if i == j and i not in tmp:
                tmp.append(i)
    return tmp


def main():
    """ a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] """
    r1 = [random.randrange(1,100) for i in range(random.randrange(1,10))]
    print(r1)
    r2 = [random.randrange(1,100) for i in range(random.randrange(1,10))]
    print(r2)
    overlaps = listoverlap(r1, r2)
    print(overlaps)
    return


if __name__ == '__main__':
    main()
