# a121_catch_a_turtle.py
# leaderboard variables

#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb

# Add this function to your game code
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input("Please enter your name: ")
var = 2
score = 0
timer = 5
counter_interval  = 1000
#-----game configuration----
# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  global score
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)
#-----initialize turtle-----
spot = trtl.Turtle()
spot.color("green")
spot.pencolor("white")
spot.pensize(1.5)
spot.penup()
spot.shape("turtle")
spot.shapesize(var)
spot.right(90)
spot.forward(100)
timer_up = "False"
counter = trtl.Turtle()
score_writer = trtl.Turtle()
score_writer.penup()              
counter.penup()
score_writer.speed(50)
counter.speed(50)
spot.speed(6)
score_writer.pencolor("black")
font_setup = ("Arial", 20, "normal")
#-----game functions--------
def countdown():
    global timer
    global timer_up
    if timer <=0:
        counter.clear()
        timer_up = "True"
        score_writer.goto(150,200)
        counter.goto(-150,200)
        counter.write("Game Over", font = font_setup)
        score_writer.write("The score is: " + str(score), font=font_setup)
        spot.hideturtle()
        spot.color("white")
        manage_leaderboard()
    else:
        counter.clear()
        counter.write("Time Left: " + str(timer), font = font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)
    if 30 > timer >=20:
        spot.color("green")
        spot.pencolor("white")
    if 20 > timer >=15:
        spot.color("black")
        spot.pencolor("white")
    if 15 > timer >=10:
        spot.color("yellow")
        spot.pencolor("white")
    if 10 > timer >=5:
        spot.color("orange")
        spot.pencolor("white")
    if 5 > timer >0:
        spot.color("red")
        spot.pencolor("white")
   
   
def update_score():
    global score
    score += 1
    score_writer.write("The score is: " + str(score), font=font_setup)
def spot_clicked(x,y):
    global timer
    global var
    if var >= 0:
      var -= ((rand.randint(1,2))/100)
      spot.shapesize(var)
    if timer >= 0:
        score_writer.clear()
        newypos = rand.randint(-150,150)
        newxpos = rand.randint(-200,200)
        spot.goto(newxpos, newypos)
        score_writer.goto(150,200)
        counter.goto(-150,200)
        update_score()
        print("Spot was Clicked, and your coordinates were (y goes from -150 to 150, x goes from -200 to 200): " + str(newxpos) + ", " + str(newypos))

#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)  
wn.mainloop()