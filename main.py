import random
import turtle as t

JOEY = t.Turtle()

JOEY.shape("turtle")

JOEY.color("red")

JOEY.pensize(10)

JOEY.speed(6)

DIRECTIONS = [0, 90, 180, 270]

def change_color():
    r = random.random()
    g = random.random()
    b = random.random()

    print(f"R: {r}, G: {g}, B:{b}")
    JOEY.color(r, g, b)

#Draw a square
# for i in range(4):
#     print(i)
#     joey.forward(100)
#     joey.right(90)


#Draw a dashed line


# for i in range(30):
#     if i % 2 == 0:
#         print(i)
#         joey.pendown()
#         joey.forward(10)
#     else:
#         joey.penup()
#         joey.forward(10)


#Draw shapes from 3 to 10 sides

# def draw_shape(number_of_sides):
#     angle = 360 / number_of_sides
#     print(f"Angle: {angle}")
#     for side in range(number_of_sides):
#         JOEY.forward(100)
#         JOEY.left(angle)
#
#
# for side_number in range(3, 11):
#     draw_shape(number_of_sides = side_number)
#     change_color()


#Random Walk
#Making random movements any direction
#Progress same distance
#Can choose any direction
#Different color each time it walks
#Thicker line
#Faster turtle
def random_walk():

    for steps in range(200):
        change_color()
        direction = random.choice(DIRECTIONS)
        print(direction)
        JOEY.forward(20)
        JOEY.setheading(random.choice(DIRECTIONS))



random_walk()

screen = t.Screen()
screen.exitonclick()
