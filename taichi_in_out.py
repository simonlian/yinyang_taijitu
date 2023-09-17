# This is my Tai-Chi Graph
import graphlib
import turtle

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# constants
RADIUS = 200
EYE_RADIUS = 25

def move(obj, x, y):
    obj.up()
    obj.setpos(x, y)
    obj.down()


def draw_yinyan_fish(bob):
    move(bob, 0, -RADIUS)
    bob.setheading(0)
    bob.speed(0)

    bob.fillcolor("blue")
    bob.circle(RADIUS, 180)  # begin with a semi-circle

    # Draw and fill the Yin Half
    bob.begin_fill()
    bob.circle(RADIUS, 180)  # the yin-half to be filled

    bob.circle(RADIUS / 2, 180)
    bob.circle(-RADIUS / 2, 180)  # a negative radius draws the arc in clockwise direction
    bob.end_fill()

    # Draw the yin-in-yang (the yin eye)
    move(bob, 0, (RADIUS / 2 - EYE_RADIUS))
    bob.begin_fill()
    bob.circle(EYE_RADIUS)
    bob.end_fill()

    # Draw the yang-in-yin (the yang eye)
    bob.fillcolor("white")
    bob.speed(3)
    move(bob, 0, -(RADIUS / 2 - EYE_RADIUS))
    bob.begin_fill()
    bob.circle(-EYE_RADIUS)
    bob.end_fill()


# constants
POWER = 6  # 2^POWER = 64
CELL_LEN = RADIUS / POWER   # unit length of the cell
CELL_ARC = 360 / (2 ** POWER)

# Optionally display grids
def draw_separators(bob):
    # draw 64 separators
    for i in range(64):
        move(bob, 0, 0)
        bob.left(CELL_ARC)
        bob.penup()
        bob.forward(RADIUS)
        bob.pendown()
        bob.forward(RADIUS)

def draw_bagua(bob):
    move(bob, 0, -RADIUS)
    bob.speed(0)
    bob.circle(RADIUS)

    # draw 6 concentric circles
    for i in range(1, POWER + 1):
        radius = RADIUS + i * CELL_LEN
        move(bob, 0, -radius)
        bob.circle(radius)

    draw_separators(bob)

    # fill cells
    bob.speed(0)
    bob.fillcolor("blue")

    # draw cells inside-out, layer by layer
    for layer in range(POWER):
        move(bob, 0, -RADIUS - layer * CELL_LEN)
        bob.setheading(0)
        shade_unit = 2 ** layer

        # right half - plots from 0x00 - 0x1F
        for iter in range(0, 2 ** (POWER - 1), 2 * shade_unit):
            bob.begin_fill()
            bob.circle(RADIUS + (layer * CELL_LEN), shade_unit * CELL_ARC)
            bob.right(90)
            bob.forward(CELL_LEN)
            bob.right(90)
            bob.circle(-RADIUS - (layer + 1) * CELL_LEN, shade_unit * CELL_ARC)
            bob.right(90)
            bob.forward(CELL_LEN)
            bob.right(90)
            bob.end_fill()
            bob.circle(RADIUS + layer * CELL_LEN, 2 * shade_unit * CELL_ARC)

        if 5 == layer:
            # Need to skip this because MSB is NOT mirrored, but reversed
            continue

        # left half - plots from 0x20 - 0x3F
        move(bob, 0, -RADIUS - layer * CELL_LEN)
        bob.setheading(180)
        for iter in range(0, 2 ** (POWER - 1), 2 * shade_unit):
            bob.begin_fill()
            bob.circle(-RADIUS - (layer * CELL_LEN), shade_unit * CELL_ARC)
            bob.left(90)
            bob.forward(CELL_LEN)
            bob.left(90)
            bob.circle(RADIUS + (layer + 1) * CELL_LEN, shade_unit * CELL_ARC)
            bob.left(90)
            bob.forward(CELL_LEN)
            bob.left(90)
            bob.end_fill()
            bob.circle(-RADIUS - layer * CELL_LEN, 2 * shade_unit * CELL_ARC)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    scrn = turtle.Screen()
    scrn.bgcolor("white")
    scrn.title("drawing board")

    bob = turtle.Turtle()
    bob.pencolor("black")
    bob.hideturtle()        # Hide turtle cursor

    # draw the yin-yan fish
    draw_bagua(bob)
    draw_yinyan_fish(bob)

    # end drawing
    turtle.done()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Turtle in PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
