import turtle

playground = turtle.Screen()       # use nouns for objects, play is a verb

playground.bgcolor("black")
playground.screensize(250, 250)
playground.title("Turtle Keys")

tom = turtle.Turtle()              # use nouns for objects, run is a verb

tom.speed()
tom.color("white")
PIXELS_PER_1 = 30
DOT_SIZE = 5
SYS_SIZE = 20
dot_color = "red"

def drawCoordinateSys():
    tom.penup()
    tom.setposition(0, 0)

    tom.pendown()
    tom.dot(DOT_SIZE * 2, "red")

    degrees = [0, 90, 180, 270]
    for degree in degrees:
        tom.setposition((0, 0))
        tom.setheading(degree)
        tom.pendown()
        tom.forward(SYS_SIZE * PIXELS_PER_1)
        tom.penup()

    tom.setheading(90)

    tom.pendown()

    for degree in degrees:
        tom.setheading(degree)

        for x in range(-SYS_SIZE, SYS_SIZE):
            for y in range(-SYS_SIZE, SYS_SIZE):
                tom.penup()
                tom.setposition(x * PIXELS_PER_1, y * PIXELS_PER_1)
                tom.dot(DOT_SIZE, dot_color)


    # tom.right(180)
    # for i in range(SYS_SIZE):
    #     tom.penup()
    #     tom.setposition((i * PIXELS_PER_1, 0))
    #     tom.pendown()
    #
    #     for j in range(SYS_SIZE):
    #         tom.pendown()
    #         tom.dot(DOT_SIZE, dot_color)
    #         tom.penup()
    #         tom.forward(PIXELS_PER_1)

        # print(i * PIXELS_PER_1)

def drawByCommands():
    commands = [("right", 60), ("forward", 2 * PIXELS_PER_1), ("right", 60), ("forward", 2 * PIXELS_PER_1), ("right", 270)]
    repeat = 14

    tom.penup()
    tom.setposition((0, 0))
    tom.setheading(90)
    tom.pendown()

    for _ in range(repeat):
        for command, value in commands:
            if command == "right":
                tom.right(value)
            elif command == "left":
                tom.left(value)
            elif command == "forward":
                tom.forward(value)


turtle.tracer(0, 0)

drawCoordinateSys()
drawByCommands()

turtle.update()

# p = tom.pos()               # here you get the coordinates of the turtle
# tom.write(str(p), True)     # and you print a string representation on screen
# tom.penup()
#
# print(p)                    # this prints to the console

playground.exitonclick()