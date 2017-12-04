import math
import random 
from turtle import Turtle

# the grammar: U (up), D (down), L (left), R (right)
# generating each with an equal probability
# later, the idea should be to do a random walk, i.e. with a rotation of a particular angle
# at that point the grammar should maybe have tokens for move and for rotate

# all moves are the same length

# tokens = ["U", "D", "L", "R"]
tokens = [90, 270, 180, 0]

# l = length of path to gen
def squareWalkGen( l):
	toRet = [];
	for i in range( l):	
		toRet += [tokens[ random.randint(0, len( tokens) - 1)]]
	return toRet

def walkAndDraw( path, t, stepLen):
	t.down()

	for dir in path:
		t.setheading( dir)
		t.forward( stepLen)


def main():
	stepLen = 30
	pathLen = 100

	t = Turtle()
	t.pencolor("red")
	t.screen.bgcolor("black")

	p = squareWalkGen( pathLen)

	walkAndDraw( p, t, stepLen)
	t.hideturtle()

	input()

main()


