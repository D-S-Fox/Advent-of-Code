# Got solution from https://github.com/fuglede/adventofcode/blob/master/2024/day04/solutions.py

from collections import defaultdict
from itertools import product
import os

# Gets scripts absolute path and changes to its directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

with open("input.txt") as f:
    ls = f.read().strip().split("\n")


boardz = defaultdict(str)
boardz |= {i + 1j * j: x for i, l in enumerate(ls) for j, x in enumerate(l)}
octdir = {i + 1j * j for (i, j) in set(product((-1, 0, 1), (-1, 0, 1))) - {(0, 0)}}

# Part 1
print(
    sum(
        [boardz[z + i * dz] for i in range(4)] == ["X", "M", "A", "S"]
        for z in list(boardz.keys())
        for dz in octdir
    )
)


# Part 2
res = 0
for z in list(boardz.keys()):
    if boardz[z] == "A":
        corners = [
            boardz[z + 1 + 1j],
            boardz[z + 1 - 1j],
            boardz[z - 1 - 1j],
            boardz[z - 1 + 1j],
        ]
        if (
            corners.count("M") == 2
            and corners.count("S") == 2
            and boardz[z - 1 - 1j] != boardz[z + 1 + 1j]
        ):
            res += 1
print(res)