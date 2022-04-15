import turtle
from time import sleep
from datetime import datetime

screen = turtle.Screen()
screen.setup(800, 600, startx=0, starty=100)
trtl=turtle.Turtle()
screen.bgcolor('black')
clr=['red', 'green', 'blue', 'yellow', 'purple']
trtl.pensize(5)
trtl.shape('turtle')
trtl.penup()
trtl.pencolor('violet')
m=0
#def printTime(hours, minutes, seconds):
#    print( f"{hours:02}:{minutes:02}:{seconds:02}" )

for i in range(12):
        m=m+1
        trtl.penup()
        trtl.setheading(-30*i+60)
        trtl.forward(180)
        trtl.pendown()
        trtl.forward(20)
        trtl.penup()
        trtl.forward(20)
        trtl.write(str(m),align="center",font=("Arial", 14, "bold"))
        if m==12:
          m=0
        trtl.home()


trtl.home()
trtl.setpos(0,-250)
trtl.pendown()
trtl.pensize(10)
trtl.pencolor('yellow')
trtl.circle(250 )
trtl.penup()
trtl.setpos(150, -270)
trtl.pendown()
trtl.pencolor('olive')
trtl.write('Watch Made in Gadirca_Ion', font=('Arial', 12, "normal"))
trtl.ht()


input()
