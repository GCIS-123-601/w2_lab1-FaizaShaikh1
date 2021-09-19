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
    v2=turtle.isdown()
    v3=turtle.heading()
    vx=turtle.xcor()
    vy=turtle.ycor()
    print("turtle is down?",v2)
    print("current angle: ",v3)
    print("xcor: ",vx,"ycor: ",vy)

def main():
    size=int(input("Enter the size: "))
    angle=int(input("Enter the angle: "))
    square_func(size,angle)
    print("Press enter to continue..")
    turtle_state()

def turtle_square():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

def square_func(size,angle):
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)
main()