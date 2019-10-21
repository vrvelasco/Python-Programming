# Victor Velasco 8/26/19

import turtle

choice = 0
choice = int(input("Enter 1 for a Snowman\nEnter 2 for a Star\nSelection: "))

if choice == 1:
    # Turtle Properties
    turtle.bgcolor('blue')
    turtle.pencolor('white')
    turtle.pensize(5)
    turtle.fillcolor('white')

    # Movement
    turtle.penup()
    turtle.goto(0,-225)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(100)

    turtle.penup()
    turtle.goto(0,-25)
    turtle.pendown()
    turtle.circle(50)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(150, 150)
    turtle.write('Snowman! :)', font = ('Times New Roman', 20, 'bold'))
    
elif choice == 2:
    turtle.shape('turtle')
    turtle.color('green')
    turtle.pensize(8)
    turtle.forward(100)
    turtle.right (144)
    turtle.forward(100)
    turtle.right (144)
    turtle.forward(100)
    turtle.right (144)
    turtle.forward(100)
    turtle.right (144)
    turtle.forward(100)
    turtle.penup()
    turtle.goto(150, 150)
    turtle.pendown()
    turtle.write('Star! :)', font = ('Times New Roman', 20, 'bold'))
    
