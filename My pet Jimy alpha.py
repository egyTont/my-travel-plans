import turtle
def shapes():
    window=turtle.Screen()
    window.bgcolor("pink")
#This is a squear
    jimy=turtle.Turtle()
    jimy.speed(3)
    jimy.shape("turtle")
    jimy.color("black")
    x=1
    while x<5:
        jimy.forward(100)
        jimy.right(90)
        x=x+1
#This is a circle
    sara=turtle.Turtle()
    sara.circle(100)
    sara.shape("arrow")
    sara.color("pink")
#This is a Tringle
    brad=turtle.Turtle()
    brad.shape("classic")
    brad.color("blue")
    f=1
    while f<4:
        brad.forward(100)
        brad.left(120)
        f=f+1
    window.exitonclick()
shapes()
