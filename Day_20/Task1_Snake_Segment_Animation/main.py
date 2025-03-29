#TODO- day1

# create a snake
#move a snake
#control a snake

#TODO- day2

# Detect collision with food
# Create Scoreboard
# Detect collision with wall
# Detect collision with tail

from turtle import Screen, Turtle
import time

screen =Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snack Game")
screen.tracer(0)

starting_position = [(0,0),(-20,0),(-40,0)]

segments = []

for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


# segment_1 = Turtle(shape="square")
# segment_1.color("white")
#
# segment_2 =Turtle(shape="square")
# segment_2.color("white")
# segment_2.goto(-20, 0)
#
# segment_3 = Turtle(shape="square")
# segment_3.color("white")
# segment_3.goto(-40, 0)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for seg in segments:
    #     seg.forward(20)

#  start= len(segment)-1, stop=0, step=-1
    for seg_num in range(len(segments)-1 ,0,-1):
       new_x = segments[seg_num - 1].xcor()
       new_y = segments[seg_num - 1].ycor()
       segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)



screen.exitonclick()


