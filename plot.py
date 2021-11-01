#!/usr/bin/env python3

import sys
args = sys.argv[1:]

VERSION = "0.0.2"

if "-v" in args or "--version" in args:
    print(VERSION)
    exit(0)

if "-h" in args or "--help" in args:
    print("This program allows a user to enter a x and y coordinate and plots on a graph.")
    print("Arguments are expected in the form label, value, label, value, etc.")
    exit(0)


print(f"Running {__file__}...")

cols = 17
rows = 17

points = []
for arg in args:
    li = arg.split(",")
    point = (int(li[0]), int(li[1]))
    points.append(point)

for y in range(rows//2, -(rows//2) -1, -1):
    for x in range(-(cols//2), cols//2 + 1, 1):
        currentPoint = (x,y)
        if currentPoint in points:
            print("X", end="")
        elif currentPoint == (0, 0):
            print("+", end="")
        elif x == 0:
            print("|", end="")
        elif y == 0:
            print("-", end="")
        else:
            print(" ", end="")
    print()
