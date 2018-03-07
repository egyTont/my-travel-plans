import turtle
def shapes():
    jimy=turtle.Turtle()
    window=turtle.Screen()
    window.bgcolor("pink")
    jimy.speed(3)
    jimy.shape("turtle")
    jimy.color("black")
    x=1
    while x<5:
        jimy.forward(100)
        jimy.right(90)
        x=x+1
    #jimy.forward(100)
    #jimy.right(90)
    #jimy.forward(100)
    #jimy.right(90)
    #jimy.forward(100)
    sara=turtle.Turtle()
    sara.circle(100)
    sara.shape("arrow")
    sara.color("pink")
    window.exitonclick()
shapes()
