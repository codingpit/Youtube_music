from turtle import *
bgcolor("black")
speed(10)
color("white")
fillcolor("red")
begin_fill()
circle(250,360)
end_fill()
color("white")
penup()
goto(0,100)
pendown()
circle(150,360)
penup()
goto(-20,300)
pendown()
fillcolor("white")
right(90)
begin_fill()
for i in range(3):
    forward(100)
    left(120)
end_fill()
hideturtle()
done()