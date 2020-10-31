#!/usr/bin/env python3
# This solution grants 11/15 points.
# For subtask 5, case 3 (test 26), a wrong answer is outputted (recursion error)
# For subtask 6, case 1 (test 30), a timeout error occurs
import sys

rows = int(sys.stdin.readline(), 10)
columns = int(sys.stdin.readline(), 10)
hasReachedEnd = False
squares = {}

for i in range(rows):
    vals = sys.stdin.readline().split(" ")

    for index, val in enumerate(vals):
        squares[f"{i + 1} {index + 1}"] = int(val, 10)


def iterateSquares(multiplied, square, visited):
    global hasReachedEnd

    try:
        visited[square]
    except KeyError:
        if not hasReachedEnd and multiplied == squares[square]:
            if square == "1 1":
                hasReachedEnd = True

                return

            visited[square] = None
            dfs(square, visited)


def dfs(coords, visited={}):
    x, y = coords.split(" ")

    tuple(
        map(
            lambda square: iterateSquares(int(x, 10) * int(y, 10), square, visited),
            squares,
        ),
    )


dfs(f"{rows} {columns}")

print("yes" if hasReachedEnd else "no")