#Rebecca Glatts
#Lab B1

import turtle

def rectangle(length, width):
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(width)


def window():
    turtle.fillcolor('gold')
    turtle.begin_fill()
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.end_fill()
    turtle.forward(30)
    turtle.backward(15)
    turtle.left(90)
    turtle.forward(30)
    turtle.backward(15)
    turtle.left(90)
    turtle.backward(15)
    turtle.forward(30)
    

def main():
    turtle.title("little house")
    w = turtle.Screen()
    turtle.penup()
    turtle.goto(-200, -100)
    turtle.pendown()

    #house body
    turtle.fillcolor('#B0C4DE')
    turtle.begin_fill()
    rectangle(300, 200)
    turtle.end_fill()

    turtle.backward(200)
    turtle.left(180)

    #roof
    turtle.fillcolor('saddle brown')
    turtle.begin_fill()
    turtle.goto(-50, 200)
    turtle.goto(100, 100)
    turtle.end_fill()

    turtle.left(180)
    turtle.forward(200)
    turtle.left(270)
    turtle.forward(100)
    turtle.left(180)
    
    #door
    turtle.begin_fill()
    rectangle(30, 50)
    turtle.end_fill()
    
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()

    #window1
    window()
    
    turtle.penup()
    turtle.backward(150)
    turtle.left(90)
    turtle.backward(15)
    turtle.pendown()
    #window2
    window()
    turtle.penup()
    turtle.left(90)
    turtle.backward(100)
    
    #chimney
    turtle.fillcolor('firebrick')
    turtle.begin_fill()
    turtle.pendown()
    turtle.backward(50)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(73)
    turtle.end_fill()
   
    #downstairs windows
    turtle.penup()
    turtle.forward(160)
    turtle.pendown()


    window()
    turtle.backward(30)
    
    window()
    turtle.penup()
    turtle.left(270)
    turtle.forward(100)
    turtle.left(90)
    turtle.backward(33)
    turtle.pendown()

    window()
    turtle.backward(30)
    window()
    
    w.exitonclick()

main()

