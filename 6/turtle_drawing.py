import turtle

playground = turtle.Screen()       # use nouns for objects, play is a verb

playground.bgcolor("black")
playground.screensize(250, 250)
playground.title("Turtle Keys")

tom = turtle.Turtle()              # use nouns for objects, run is a verb

tom.hideturtle()
tom.speed()
tom.color("white")
PIXELS_PER_1 = 25
DOT_SIZE = 5
SYS_SIZE = 20
dot_color = "red"
rounding = 5


commands = [("right", 60), ("forward", 2), ("right", 60), ("forward", 2), ("right", 270)]
repeat = 14


class Vec2:
    def __init__(self, x: float | int, y: float | int):
        self.x = x
        self.y = y

    def scale(self, multiplier: float | int) -> tuple[float | int]:
        self.x_scaled = self.x * multiplier
        self.y_scaled = self.y * multiplier
        return self.x_scaled, self.y_scaled


def drawCoordinateSys() -> list[Vec2, ...]:
    int_coords = []

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

                int_coords.append(Vec2(x, y))

    return int_coords


def calculateVerticesCoords() -> list[Vec2, ...]:
    vertices_coords = list()

    tom.penup()
    tom.setposition((0, 0))
    tom.setheading(90)

    for _ in range(repeat):
        for command, value in commands:
            if command == "right":
                tom.right(value)
            elif command == "left":
                tom.left(value)
            elif command == "forward":
                coords = Vec2(*tom.position())
                if not ((coords.x, coords.y) in vertices_coords):
                    vertices_coords.append(coords)

                tom.forward(value)


    return vertices_coords


def drawByCommands():
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
                tom.forward(value * PIXELS_PER_1)

                # vertices_int_coords.append(tom_pos)


def drawByVerticesCoords(vertices_coords):
    tom.penup()
    tom.setposition((0, 0))
    tom.pendown()
    for coords in vertices_coords:
        x_scaled, y_scaled = coords.x * PIXELS_PER_1, coords.y * PIXELS_PER_1
        tom.goto((x_scaled, y_scaled))


def calculateLineParams(vertex_1: Vec2, vertex_2: Vec2):
    k = (vertex_2.y - vertex_1.y) / (vertex_2.x - vertex_1.x)
    b = vertex_1.y - k * vertex_1.x
    return k, b


def findMultiplier(x, y, k, b):
    if y > k * x + b:
        return 1  # above
    elif y < k * x + b:
        return -1  # under
    elif y == k * x + b:
        return 0  # at


def defineTwoSets(all_dots_coords: list[Vec2, ...], x, k, b) -> tuple[set, set]:
    set_1 = set()
    set_2 = set()
    for dot_coords in all_dots_coords:
        if dot_coords.y > k * x + b:
            set_1.add((dot_coords.x, dot_coords.y))
        elif dot_coords.y < k * x + b:
            set_2.add((dot_coords.x, dot_coords.y))

    return set_1, set_2

def solve(vertices_coords: list[Vec2, ...], all_dots_coords: list[Vec2, ...]):

    all_dots_coords_set = set()
    for dot_coords in all_dots_coords:
        all_dots_coords_set.add((dot_coords.x, dot_coords.y))

    all_sets_1 = all_dots_coords_set
    for i in range(len(vertices_coords) - 1):
        params = calculateLineParams(vertices_coords[i], vertices_coords[i + 1])
        set_1, set_2 = defineTwoSets(all_dots_coords, vertices_coords[i].x, *params) # надо учитывать то, где находится следующая линия и в зависимости от этого менять условия в defineTwoSets

        all_sets_1 = all_sets_1.intersection(set_2)

    # print(all_sets_1)
    print(len(all_dots_coords_set))
    print(len(all_sets_1))

turtle.tracer(0, 0)

sys_int_coords = drawCoordinateSys()
vertices_int_coords: list[Vec2, ...] = calculateVerticesCoords()
# drawByCommands()
drawByVerticesCoords(vertices_int_coords)

solve(vertices_int_coords, sys_int_coords)
#print([coords for coords in vertices_int_coords])

turtle.update()

# p = tom.pos()               # here you get the coordinates of the turtle
# tom.write(str(p), True)     # and you print a string representation on screen
# tom.penup()
#
# print(p)                    # this prints to the console

playground.exitonclick()