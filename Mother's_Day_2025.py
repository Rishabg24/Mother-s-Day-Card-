import turtle
import random

screen = turtle.Screen()
screen.bgcolor("lightpink")
screen.title("Mother's Day Card")
screen.setup(width=800, height=700)
screen.tracer(0)  

pen = turtle.Turtle()
pen.color("white")
pen.hideturtle()
pen.penup()

def write_message(text, x, y):
    pen.goto(x, y)
    pen.write(text, align="center", font=("Comic Sans MS", 50, "bold"))

# timed messages
screen.ontimer(lambda: write_message("Happy", 0, 220), 1000)
screen.ontimer(lambda: write_message("Mother's", 0, 160), 2000)
screen.ontimer(lambda: write_message("Day!", 0, 100), 3000)
screen.ontimer(lambda: write_message("Love You!", 0, -250), 5500)
screen.tracer(1)

heart = turtle.Turtle()
heart.hideturtle()
heart.color("red", "red")
heart.pensize(3)
heart.speed(3)

heart.penup()
heart.goto(0, -100)
heart.pendown()
heart.begin_fill()
heart.left(140)
heart.forward(180)
heart.circle(-90, 200)
heart.left(120)
heart.circle(-90, 200)
heart.forward(180)
heart.end_fill()

# Now that the heart is fully drawn, switch to manual updates for stars
screen.tracer(0)
screen.update()   

# 1) Star‐drawing helper
sparkle = turtle.Turtle()
sparkle.hideturtle()
sparkle.speed(0)
sparkle.color("gold")
sparkle.pensize(2)

def draw_star(x, y, size):
    sparkle.penup()
    sparkle.goto(x, y)
    sparkle.setheading(0)
    sparkle.pendown()
    for _ in range(5):
        sparkle.forward(size)
        sparkle.right(144)

# 2) Star class to track position, size, speed
class Star:
    def __init__(self):
        self.x = random.randint(-380, 380)
        self.y = random.randint(350, 700)
        self.size = random.randint(15, 25)
        self.speed = random.uniform(2, 5)

    def fall(self):
        self.y -= self.speed
        if self.y < -350:
            # reset to top
            self.y = random.randint(350, 700)
            self.x = random.randint(-380, 380)

    def show(self):
        draw_star(self.x, self.y, self.size)

# 3) Create a fleet of falling stars
stars = [Star() for _ in range(40)]

# 4) Animation loop
def animate():
    sparkle.clear()
    for s in stars:
        s.fall()
        s.show()
    screen.update()
    # call again in 50 ms
    screen.ontimer(animate, 50)

screen.ontimer(animate, 2000)

turtle.done()
