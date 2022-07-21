# File: SeychellesFlag.py
# Student: Crystal Le
# UT EID: CL44964
# Course Name: CS303E
# 
# Date Created: 11/23/2021
# Date Last Modified: 11/23/2021
# Description of Program: A python program using turtle methods to draw the Seychelles Flag.

myBlue   = '#003882'
myYellow = '#FCD955'
myRed = '#D72323'
myWhite = '#FFFFFF'
myGreen = '#007B3A'

import turtle

def drawBorder(flag, x, y, length, height):
    flag.penup()
    flag.goto(x,y)
    flag.pendown()
    flag.setheading(0)
    flag.forward(length)
    flag.left(90)
    flag.forward(height)
    flag.left(90)
    flag.forward(length)
    flag.left(90)
    flag.forward(height)
    
def fillInFlag(flag, x, y, length, height):
    t.fillcolor(myBlue)
    t.begin_fill()
    drawTriangle1(flag, x, y, height)
    t.end_fill()
    t.fillcolor(myYellow)
    t.begin_fill()
    drawTriangle2(flag, x, y, height)
    t.end_fill()
    t.fillcolor(myWhite)
    t.begin_fill()
    drawTriangle3(flag, x, y, length)
    t.end_fill()
    t.fillcolor(myGreen)
    t.begin_fill()
    drawTriangle4(flag, x, y, length)
    t.end_fill()
    t.fillcolor(myRed)
    t.begin_fill()
    drawQuad(flag, x, y, length, height)
    t.end_fill()
    
def drawTriangle1(flag, x, y, height):
    flag.penup()
    flag.setheading(90)
    flag.pendown()
    flag.forward(height)
    flag.right(90)
    flag.forward(200)
    flag.goto(x,y)
    
def drawTriangle2(flag, x, y, height):
    flag.penup()
    flag.setheading(90)
    flag.pendown()
    flag.goto(200, height)
    flag.right(90)
    flag.forward(200)
    flag.goto(x,y)

def drawTriangle3(flag, x, y, length):
    flag.pendown()
    flag.goto(length, 200)
    flag.right(90)
    flag.forward(100)
    flag.goto(x,y)

def drawTriangle4(flag, x, y, length):
    flag.pendown()
    flag.goto(length, 100)
    flag.right(90)
    flag.setheading(270)
    flag.forward(100)
    flag.goto(x,y)

def drawQuad(flag, x, y, length, height):
    flag.pendown()
    flag.goto(400, height)
    flag.setheading(0)
    flag.forward(200)
    flag.setheading(270)
    flag.goto(length,200)
    flag.goto(x,y)
    
t = turtle.Turtle()
t.speed(20)
t.screen.colormode(255)
drawBorder(t, 0, 0, 600, 300)
drawTriangle1(t, 0, 0, 300)
drawTriangle2(t, 0, 0, 300)
drawTriangle3(t, 0, 0, 600)
drawTriangle4(t, 0, 0, 600)
drawQuad(t, 0, 0, 600, 300)
fillInFlag(t, 0, 0, 600, 300)


