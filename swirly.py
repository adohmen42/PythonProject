import turtle
myTurtle = turtle.Turtle() 
myTurtle.shape("turtle")

prevNum = 0
currNum = 1
fibNums = [prevNum, currNum ] 
myTurtle.color("green")
for i in range(5):
    nextNum = prevNum + currNum
    prevNum = currNum
    currNum = nextNum
    fibNums.append(currNum )

for x in fibNums:    
    print(x)
    myTurtle.right(22)
    myTurtle.forward(x / 2)
