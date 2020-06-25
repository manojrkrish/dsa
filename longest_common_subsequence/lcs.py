#!/usr/bin/env python3

# program to find all longest common subsequences of sub-strings
# x(0..m-1), y(0..n-1)

def getLCS(x: str, y: str, m: int, n: int, t):
    
    # when end of the sequence reached return empty list
    if m == 0 or n == 0:
        return [""]

    # last character of x and y matches
    if x[m - 1] == y[n - 1]:
        # ignore last character of x and y and find all lcs
        # substring x[0..m-2], y[0..n-2] and store it in a list.
        lcs = getLCS(x, y, m - 1, n - 1, t)

        # append current character x[m - 1] or x[n - 1]
        # to all LCS of substring X[0..m-2] and Y[0..n-2]
        for i in range(len(lcs)):
            lcs[i] = lcs[i] + x[m - 1]

        return lcs

    # when last character of x and y doesn't match

    # if top cell of current cell has more value than the left cell,
    # then ignore current character of X and find all LCS of
    # substring y[0..m-2], y[0..n-1]
    if t[m - 1][n] > t[m][n - 1]:
        return getLCS(x, y, m - 1, n, t)
    
    # if left cell of current cell has more value than the top cell,
    # then ignore current character of Y and find all LCS of
    # substring X[0..m-1], Y[0..n-2]
    if t[m][n - 1] > t[m - 1][n]:
        return getLCS(x, y, m, n - 1, t)
    
    # if top cell has equal value to the left cell, then consider both character
    top = getLCS(x, y, m - 1, n, t)
    left = getLCS(x, y, m, n - 1, t)

    # merge two Lists and return
    return left + top


def getLookupTable(x: str, y: str):
    # Lookup table for input x - ABCBDAB, y - BDCABA
    #
    #       B, D, C, A, B, A
    #   [0, 0, 0, 0, 0, 0, 0]
    # A [0, 0, 0, 0, 1, 1, 1]
    # B [0, 1, 1, 1, 1, 2, 2]
    # C [0, 1, 1, 2, 2, 2, 2]
    # B [0, 1, 1, 2, 2, 3, 3]
    # D [0, 1, 2, 2, 2, 3, 3]
    # A [0, 1, 2, 2, 3, 3, 4]
    # B [0, 1, 2, 2, 3, 4, 4]
    
    # fill the lookup table
    lookupTable = [[ 0 for m in range(len(y) + 1)] for n in range(len(x) + 1)]
    
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i - 1] == y[j - 1]:
                # when match found, increment the match count.
                lookupTable[i][j] = lookupTable[i - 1][j - 1] + 1
            else:
                # otherwise get the max of previous counts
                lookupTable[i][j] = max(lookupTable[i - 1][j], lookupTable[i][j - 1])

    return lookupTable


def findLCS(x: str, y: str):
    # get lookup table.
    lookupTable = getLookupTable(x, y)

    # get longest common sebsequence among given two strings.
    return getLCS(x, y, len(x), len(y), lookupTable)


if __name__ == "__main__":
    x = input("Enter first string: ")
    y = input("Enter second string: ")

    print("String1 - ", x)
    print("String2 - ", y)

    # find longest common sequence
    lcs = findLCS(x, y)
    print(lcs)

