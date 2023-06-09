import random
import time
import turtle


# functions
def write_start():
    start_turtle = turtle.Turtle(visible=False)
    start_turtle.up()
    start_turtle.color("White")
    start_turtle.setposition(-start_turtle.getscreen().window_width() / 2 + 50,
                             start_turtle.getscreen().window_height() / 2 - 50)
    start_turtle.write("Press Here", False, font=("Verdana", 15, "normal"))
    return start_turtle


global last_x
last_x = 0
global last_y
last_y = 0


def fun_start():
    global start
    start.clear()
    timer = turtle.Turtle()
    timer.hideturtle()
    timer.color("White")
    timer.up()
    timer.setposition(-timer.getscreen().window_width() / 2 + 50, timer.getscreen().window_height() / 2 - 50)

    start_time = time.time()

    elapsed_time = 30
    count = 0
    circle_turtle = turtle.Turtle(visible=False)

    while elapsed_time - (time.time() - start_time) > 1:
        timer.clear()
        timer.write(f"You have {int(elapsed_time - (time.time() - start_time))} seconds. Your score {counter}", False,
                    font=("Verdana", 15, "normal"))

        if count % 500 == 0:
            circle_turtle.color("Yellow")
            circle_turtle.up()
            global last_x
            last_x = random.randint(-300, 300)
            global last_y
            last_y = random.randint(-300, 300)
            circle_turtle.setposition(last_x, last_y)
            circle_turtle.down()
            circle_turtle.circle(radius=10)
        elif count % 499 == 0:
            circle_turtle.clear()

        count += 1

        screen.update()

    circle_turtle.clear()
    timer.clear()
    timer.write("Game Over", False, font=("Verdana", 15, "normal"))
    time.sleep(1)
    timer.clear()

    start = write_start()


def on_click(x, y):
    global last_x
    global last_y
    global counter
    print(x, last_x, y, last_y)
    if (-450 <= x <= -325) and (350 <= y <= 380):
        fun_start()

    if (last_x - 20 <= x <= last_x + 20) and (last_y - 20 <= y <= last_y + 20):
        counter += 1


# initialize
screen = turtle.Screen()
screen.bgcolor("Black")
screen.title("Catch The Turtle Game")
screen.tracer(0)

# welcome message
welcome = turtle.Turtle(visible=False)
welcome.up()
welcome.color("Red")
welcome.setposition(- 200, 0)
welcome.write("Welcome To Catch The Turtle Game", False, font=("Verdana", 15, "normal"))
time.sleep(3)
welcome.clear()

# global variables
global start
start = write_start()
global counter
counter = 0

turtle.onscreenclick(on_click)

screen.mainloop()
