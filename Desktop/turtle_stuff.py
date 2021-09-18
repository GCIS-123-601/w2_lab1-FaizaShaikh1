import turtle
def test_drive():
    turtle.forward(100)
    turtle.left(87)
    turtle.setheading(127)
    turtle.up()
    turtle.down()
    turtle.goto(50, 50)
    turtle.home()
    turtle.circle(25)

def turtle_state():
    print(turtle.isdown())
    print(turtle.heading())
    print(turtle.xcor())

def main():
    test_drive()
    print("Press enter to continue..")
    turtle_state()
main()
