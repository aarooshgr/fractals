import sys
from turtle import *

def draw(size, n, handedness):
    if n == 0:
        forward(size)
    else:
        if handedness == "R":
            draw(size/2, n-1, "L")
            right(60)
            draw(size/2, n-1, "R")
            right(60)
            draw(size/2, n-1, "L")
        if handedness == "L":
            draw(size/2, n-1, "R")
            left(60)
            draw(size/2, n-1, "L")
            left(60)
            draw(size/2, n-1, "R")
            
def sierpinski_arrowhead(size, n, handedness):
    speed(10)
    if n%2 == 1:
        if handedness == "R":
            left(60)
        if handedness == "L":
            left(120)
    if n%2 == 0 and handedness == "L":
        left(180)
    draw(size, n, handedness)

args = sys.argv
if not(len(args) == 3 or len(args) == 4):
	print("\nUsage: python <path/to/sierpinski_arrowhead.py> <size> <n> <handedness>\nWhere the optional argument \"handedness\" is either \"L\" or \"R\"")
else:
    size = int(args[1])
    n = int(args[2])
    if len(args) == 4:
        handedness = args[3]
        if not (handedness == "R" or handedness == "L"):
            print("\nUsage: python <path/to/sierpinski_arrowhead.py> <size> <n> <handedness>\nWhere the optional argument \"handedness\" is either \"L\" or \"R\"")
    else:
        handedness = "R"
    sierpinski_arrowhead(size, n, handedness)