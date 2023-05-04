from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet ", prompt="Which Turtle win the race ? Enter a colour:")
color = ["red","orange","yellow","green","blue","purple"]
y_position = [-70,-40,-10,20,50,80]
all_turtles =[]
for t in range(0,6):
    tinny = Turtle(shape="turtle")
    tinny.color(color[t])
    tinny.penup()
    tinny.goto(x=-230,y=y_position[t])
    all_turtles.append(tinny)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won ! The {winning_color} turtle is the winner!")
            else:
                print(f"You've Lost! The {winning_color} turtle is the race!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()