# This is my Tai-Chi Graph
import graphlib
import turtle
#from PIL import Image
#from PIL import EpsImagePlugin

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# constants
SCREEN_SIZE = 1400
RADIUS = 300
EYE_RADIUS = RADIUS / 8
OUTPUT_EPS_FILE = "output.eps"
OUTPUT_PNG_FILE = "output.png"

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

    # draw cells outside-in, layer by layer
    for layer in range(POWER):
        move(bob, 0, -RADIUS - layer * CELL_LEN)
        bob.setheading(0)
        shade_unit = 2 ** (5 - layer)

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

        if 0 == layer:
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
    scrn.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
    scrn.bgcolor("white")
    scrn.title("太极八卦图")

    bob = turtle.Turtle()
    bob.pencolor("black")

    # draw the yin-yan fish
    draw_bagua(bob)
    draw_yinyan_fish(bob)
    bob.hideturtle()        # Hide turtle cursor

    # save the output to PS file
    canvas = turtle.getscreen().getcanvas()
    canvas.postscript(file = OUTPUT_EPS_FILE)

    '''
    To save the output as an image (eg. PNG), we will need PIL library and do followings:
     
      1) Import followings
         from PIL import Image
         from PIL import EpsImagePlugin
     
      2) Tell the variable below where the path of gswin64c EXE file is (if you don't want to change the system path):
         EpsImagePlugin.gs_windows_binary = r"c:\Program Files\gs\gs10.01.2\bin\gswin64c.exe" 

      Without step #2, it will fail with error "OSError: Unable to locate Ghostscript on paths"

    '''
    ##EpsImagePlugin.gs_windows_binary = r"c:\Program Files\gs\gs10.01.2\bin\gswin64c.exe"
    ##Image.open(OUTPUT_EPS_FILE).save(OUTPUT_PNG_FILE, "PNG")

    # end drawing
    turtle.done()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Turtle in PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
