import turtle as trtl
import random as rand
import time as tmr

#import leaderboard as lb
wn = trtl.Screen()
wn.bgcolor("#B5B5B5")
piecelist = []
# solveposxy = []
piecelocxy = []
solvepiececolor = []
solvelist = [1,1,1,1,1,1]
bruh = "red"
cubiesize = 1.5
inc = -120
incchange = 35
number = 1
movecounter = 0
ready = 0
counter = 1
solved = 0
solvedcounter = 1
counterinterval = 10
timerdisplay = trtl.Turtle()
timerdisplay.hideturtle()
timerdisplay.penup()
timerdisplay.goto(200,200)
movedisplay = trtl.Turtle()
movedisplay.hideturtle()
movedisplay.penup()
movedisplay.goto(0,-200)
font_setup = ("Impact", 30, "normal")
font_setup2 = ("Impact", 20, "normal")
font_setup3 = ("Helvetica", 18, "normal")
timerstart = 0
turned = 0
piececounter = 0
storedmoves = 0
storedtimes = 0
previoustimemove = trtl.Turtle()
previoustimemove.penup()
previoustimemove.goto(-200,200)
previoustimemove.pencolor("black")
# instructions = "instructions.gif"


# wn.addshape(instructions)

instructions_picture = trtl.Turtle()
# def draw_instructions(active_instructions):
#   active_instructions.shape(instructions)
#   wn.update()

# draw_instructions(instructions_picture)
instructions_picture.penup()
instructions_picture.hideturtle()
instructions_picture.goto(-290, -140)
instructions_picture.write("R = Up\n" + "T = Up Prime\n" + "B = Down\n" + "V = Down Prime\n" + "K = Right\n" + "M = Right Prime\n" + "Z = Left\n" + "A = Left Prime\n" + "J = Front\n" + "N = Front Prime\n" + "S = Back\n" + "X = Back Prime\n", font = font_setup3)



def displayer():
  global storedmoves
  global storedtimes
  previoustimemove.clear()
  previoustimemove.write("Previous Solve:\n" + str(round(storedtimes, ndigits=2)) + " seconds; " + str(storedmoves) + " moves", font=font_setup2)

def countdown():
  global timerstart
  global turned
  global storedtimes
  storedtimes = timerstart
  timerdisplay.clear()
  if turned == 1:
    timerdisplay.write(str(round(timerstart, ndigits=2)), font=font_setup)
    timerstart=0
    turned=0
    False

  if turned != 1:
    True
    timerdisplay.write(str(round(timerstart, ndigits=2)), font=font_setup)
    timerstart += .01
    timerdisplay.getscreen().ontimer(countdown, counterinterval)

    

def movewriter():
  global movecounter
  global turned
  movedisplay.clear()
  if turned == 1:
    movedisplay.write(str(movecounter) + " moves made", font=font_setup2)
    False
  if turned != 1:
    True
    movedisplay.write(str(movecounter) + " moves made", font=font_setup2)

def leftprime():
  global movecounter
  global ready
  if movecounter == 0 or ready == 1:
    ready = 0 
    movecounter+=1
    movewriter()
    counter1 = piecelocxy.index((-50,0))
    counter1loc = piecelocxy[counter1]
    counter2 = piecelocxy.index((-50,(-1*incchange)))
    counter2loc = piecelocxy[counter2]
    counter3 = piecelocxy.index((-50,(-2*incchange)))
    counter3loc = piecelocxy[counter3]
    counter4 = piecelocxy.index((-50,(-3*incchange)))
    counter4loc = piecelocxy[counter4]
    counter5 = piecelocxy.index((-50,(incchange)))
    counter5loc = piecelocxy[counter5]
    counter6 = piecelocxy.index((-50,(2*incchange)))
    counter6loc = piecelocxy[counter6]
    counter7 = piecelocxy.index((125,(-1*incchange)))
    counter7loc = piecelocxy[counter7]
    counter8 = piecelocxy.index((125,0))
    counter8loc = piecelocxy[counter8]
    rot1 = piecelocxy.index((-120,0))
    rot1loc = piecelocxy[rot1]
    rot2 = piecelocxy.index((-85,0))
    rot2loc = piecelocxy[rot2]
    rot3 = piecelocxy.index((-85,(-1*incchange)))
    rot3loc = piecelocxy[rot3]
    rot4 = piecelocxy.index((-120,(-1*incchange)))
    rot4loc = piecelocxy[rot4]
    prev1 = solvepiececolor[counter1]
    prev2 = solvepiececolor[counter2]
    prev3 = solvepiececolor[counter3]
    prev4 = solvepiececolor[counter4]
    prev5 = solvepiececolor[counter5]
    prev6 = solvepiececolor[counter6]
    prev7 = solvepiececolor[counter7]
    prev8 = solvepiececolor[counter8]
    prevrot1 = solvepiececolor[rot1]
    prevrot2 = solvepiececolor[rot2]
    prevrot3 = solvepiececolor[rot3]
    prevrot4 = solvepiececolor[rot4]

    piecelist[counter1].goto(counter6loc)
    piecelocxy[counter1] = (counter6loc)
    solvepiececolor[counter6] = prev1
    
    piecelist[counter2].goto(counter5loc)
    piecelocxy[counter2] = (counter5loc)
    solvepiececolor[counter5] = prev2
    
    piecelist[counter3].goto(counter1loc)
    piecelocxy[counter3] = (counter1loc)
    solvepiececolor[counter1] = prev3
    
    piecelist[counter4].goto(counter2loc)
    piecelocxy[counter4] = (counter2loc)
    solvepiececolor[counter2] = prev4
    
    piecelist[counter5].goto(counter7loc)
    piecelocxy[counter5] = (counter7loc)
    solvepiececolor[counter7] = prev5
    
    piecelist[counter6].goto(counter8loc)
    piecelocxy[counter6] = (counter8loc)
    solvepiececolor[counter8] = prev6
    
    piecelist[counter7].goto(counter4loc)
    piecelocxy[counter7] = (counter4loc)
    solvepiececolor[counter4] = prev7

    piecelist[counter8].goto(counter3loc)
    piecelocxy[counter8] = (counter3loc)
    solvepiececolor[counter3] = prev8
    
    piecelist[rot1].goto(rot4loc)
    piecelocxy[rot1] = (rot4loc)
    solvepiececolor[rot4] = prevrot1
    
    piecelist[rot2].goto(rot1loc)
    piecelocxy[rot2] = (rot1loc)
    solvepiececolor[rot1] = prevrot2
    
    piecelist[rot3].goto(rot2loc)
    piecelocxy[rot3] = (rot2loc)
    solvepiececolor[rot2] = prevrot3

    piecelist[rot4].goto(rot3loc)
    piecelocxy[rot4] = (rot3loc)
    solvepiececolor[rot3] = prevrot4

    global piececounter
    global counter
    counter = 1
    piececounter = 0
    for sidesolver in range (6):
      if solvepiececolor[piececounter] == solvepiececolor[piececounter+1] and solvepiececolor[piececounter] == solvepiececolor[piececounter+2] and solvepiececolor[piececounter] == solvepiececolor[piececounter+3]:
        solvelist[int(piececounter/4)] = 1
        piececounter+=4
      else: 
        solvelist[int(piececounter/4)] = 0
        piececounter+=4
      if counter == 6:
        print (solvelist)
        global turned
        if solvelist[0]+solvelist[1]+solvelist[2]+solvelist[3]+solvelist[4]+solvelist[5] == 6:
          global storedmoves
          storedmoves = movecounter
          displayer()
          movecounter = 0
          print("cube solved")
          turned=1
          tmr.sleep(3)
          movewriter()
      counter+=1
    ready = 1

def left():
  global movecounter
  global ready
  if movecounter == 0 or ready == 1:
    ready = 0 
    movecounter+=1
    movewriter()
    counter1 = piecelocxy.index((-50,0))
    counter1loc = piecelocxy[counter1]
    counter2 = piecelocxy.index((-50,(-1*incchange)))
    counter2loc = piecelocxy[counter2]
    counter3 = piecelocxy.index((-50,(-2*incchange)))
    counter3loc = piecelocxy[counter3]
    counter4 = piecelocxy.index((-50,(-3*incchange)))
    counter4loc = piecelocxy[counter4]
    counter5 = piecelocxy.index((-50,(incchange)))
    counter5loc = piecelocxy[counter5]
    counter6 = piecelocxy.index((-50,(2*incchange)))
    counter6loc = piecelocxy[counter6]
    counter7 = piecelocxy.index((125,(-1*incchange)))
    counter7loc = piecelocxy[counter7]
    counter8 = piecelocxy.index((125,0))
    counter8loc = piecelocxy[counter8]
    rot1 = piecelocxy.index((-120,0))
    rot1loc = piecelocxy[rot1]
    rot2 = piecelocxy.index((-85,0))
    rot2loc = piecelocxy[rot2]
    rot3 = piecelocxy.index((-85,(-1*incchange)))
    rot3loc = piecelocxy[rot3]
    rot4 = piecelocxy.index((-120,(-1*incchange)))
    rot4loc = piecelocxy[rot4]
    prev1 = solvepiececolor[counter1]
    prev2 = solvepiececolor[counter2]
    prev3 = solvepiececolor[counter3]
    prev4 = solvepiececolor[counter4]
    prev5 = solvepiececolor[counter5]
    prev6 = solvepiececolor[counter6]
    prev7 = solvepiececolor[counter7]
    prev8 = solvepiececolor[counter8]
    prevrot1 = solvepiececolor[rot1]
    prevrot2 = solvepiececolor[rot2]
    prevrot3 = solvepiececolor[rot3]
    prevrot4 = solvepiececolor[rot4]

    piecelist[counter1].goto(counter3loc)
    piecelocxy[counter1] = (counter3loc)
    solvepiececolor[counter3] = prev1
    
    piecelist[counter2].goto(counter4loc)
    piecelocxy[counter2] = (counter4loc)
    solvepiececolor[counter4] = prev2
    
    piecelist[counter3].goto(counter7loc)
    piecelocxy[counter3] = (counter7loc)
    solvepiececolor[counter7] = prev3
    
    piecelist[counter4].goto(counter8loc)
    piecelocxy[counter4] = (counter8loc)
    solvepiececolor[counter8] = prev4
    
    piecelist[counter5].goto(counter2loc)
    piecelocxy[counter5] = (counter2loc)
    solvepiececolor[counter2] = prev5
    
    piecelist[counter6].goto(counter1loc)
    piecelocxy[counter6] = (counter1loc)
    solvepiececolor[counter1] = prev6
    
    piecelist[counter7].goto(counter6loc)
    piecelocxy[counter7] = (counter6loc)
    solvepiececolor[counter6] = prev7

    piecelist[counter8].goto(counter5loc)
    piecelocxy[counter8] = (counter5loc)
    solvepiececolor[counter5] = prev8
    
    piecelist[rot1].goto(rot2loc)
    piecelocxy[rot1] = (rot2loc)
    solvepiececolor[rot2] = prevrot1
    
    piecelist[rot2].goto(rot3loc)
    piecelocxy[rot2] = (rot3loc)
    solvepiececolor[rot3] = prevrot2
    
    piecelist[rot3].goto(rot4loc)
    piecelocxy[rot3] = (rot4loc)
    solvepiececolor[rot4] = prevrot3

    piecelist[rot4].goto(rot1loc)
    piecelocxy[rot4] = (rot1loc)
    solvepiececolor[rot1] = prevrot4

    global piececounter
    global counter
    counter = 1
    piececounter = 0
    for sidesolver in range (6):
      if solvepiececolor[piececounter] == solvepiececolor[piececounter+1] and solvepiececolor[piececounter] == solvepiececolor[piececounter+2] and solvepiececolor[piececounter] == solvepiececolor[piececounter+3]:
        solvelist[int(piececounter/4)] = 1
        piececounter+=4
      else: 
        solvelist[int(piececounter/4)] = 0
        piececounter+=4
      if counter == 6:
        print (solvelist)
        global turned
        if solvelist[0]+solvelist[1]+solvelist[2]+solvelist[3]+solvelist[4]+solvelist[5] == 6:
          global storedmoves
          storedmoves = movecounter
          displayer()
          movecounter = 0
          print("cube solved")
          turned=1
          tmr.sleep(3)
          movewriter()
      counter+=1
    ready = 1

def rightprime():
  global movecounter
  global ready
  if movecounter == 0 or ready == 1:
    ready = 0 
    movecounter+=1
    movewriter()
    counter1 = piecelocxy.index((-15,0))
    counter1loc = piecelocxy[counter1]
    counter2 = piecelocxy.index((-15,(-1*incchange)))
    counter2loc = piecelocxy[counter2]
    counter3 = piecelocxy.index((-15,(-2*incchange)))
    counter3loc = piecelocxy[counter3]
    counter4 = piecelocxy.index((-15,(-3*incchange)))
    counter4loc = piecelocxy[counter4]
    counter5 = piecelocxy.index((-15,(incchange)))
    counter5loc = piecelocxy[counter5]
    counter6 = piecelocxy.index((-15,(2*incchange)))
    counter6loc = piecelocxy[counter6]
    counter7 = piecelocxy.index((90,(-1*incchange)))
    counter7loc = piecelocxy[counter7]
    counter8 = piecelocxy.index((90,0))
    counter8loc = piecelocxy[counter8]
    rot1 = piecelocxy.index((20,0))
    rot1loc = piecelocxy[rot1]
    rot2 = piecelocxy.index((55,0))
    rot2loc = piecelocxy[rot2]
    rot3 = piecelocxy.index((55,(-1*incchange)))
    rot3loc = piecelocxy[rot3]
    rot4 = piecelocxy.index((20,(-1*incchange)))
    rot4loc = piecelocxy[rot4]
    prev1 = solvepiececolor[counter1]
    prev2 = solvepiececolor[counter2]
    prev3 = solvepiececolor[counter3]
    prev4 = solvepiececolor[counter4]
    prev5 = solvepiececolor[counter5]
    prev6 = solvepiececolor[counter6]
    prev7 = solvepiececolor[counter7]
    prev8 = solvepiececolor[counter8]
    prevrot1 = solvepiececolor[rot1]
    prevrot2 = solvepiececolor[rot2]
    prevrot3 = solvepiececolor[rot3]
    prevrot4 = solvepiececolor[rot4]
  
    piecelist[counter1].goto(counter3loc)
    piecelocxy[counter1] = (counter3loc)
    solvepiececolor[counter3] = prev1
    piecelist[counter2].goto(counter4loc)
    piecelocxy[counter2] = (counter4loc)
    solvepiececolor[counter4] = prev2
    piecelist[counter3].goto(counter7loc)
    piecelocxy[counter3] = (counter7loc)
    solvepiececolor[counter7] = prev3
    piecelist[counter4].goto(counter8loc)
    piecelocxy[counter4] = (counter8loc)
    solvepiececolor[counter8] = prev4
    piecelist[counter5].goto(counter2loc)
    piecelocxy[counter5] = (counter2loc)
    solvepiececolor[counter2] = prev5
    piecelist[counter6].goto(counter1loc)
    piecelocxy[counter6] = (counter1loc)
    solvepiececolor[counter1] = prev6
    piecelist[counter7].goto(counter6loc)
    piecelocxy[counter7] = (counter6loc)
    solvepiececolor[counter6] = prev7
    piecelist[counter8].goto(counter5loc)
    piecelocxy[counter8] = (counter5loc)
    solvepiececolor[counter5] = prev8

    piecelist[rot1].goto(rot4loc)
    piecelocxy[rot1] = (rot4loc)
    solvepiececolor[rot4] = prevrot1

    piecelist[rot2].goto(rot1loc)
    piecelocxy[rot2] = (rot1loc)
    solvepiececolor[rot1] = prevrot2

    piecelist[rot3].goto(rot2loc)
    piecelocxy[rot3] = (rot2loc)
    solvepiececolor[rot2] = prevrot3

    piecelist[rot4].goto(rot3loc)
    piecelocxy[rot4] = (rot3loc)
    solvepiececolor[rot3] = prevrot4
    
    global piececounter
    global counter
    counter = 1
    piececounter = 0
    for sidesolver in range (6):
      if solvepiececolor[piececounter] == solvepiececolor[piececounter+1] and solvepiececolor[piececounter] == solvepiececolor[piececounter+2] and solvepiececolor[piececounter] == solvepiececolor[piececounter+3]:
        solvelist[int(piececounter/4)] = 1
        piececounter+=4
      else: 
        solvelist[int(piececounter/4)] = 0
        piececounter+=4
      if counter == 6:
        print (solvelist)
        global turned
        if solvelist[0]+solvelist[1]+solvelist[2]+solvelist[3]+solvelist[4]+solvelist[5] == 6:
          global storedmoves
          storedmoves = movecounter
          displayer()
          movecounter = 0
          print("cube solved")
          turned=1
          tmr.sleep(3)
          movewriter()
      counter+=1
    ready = 1

def right():
  global movecounter
  global ready
  if movecounter == 0 or ready == 1:
    ready = 0 
    movecounter+=1
    movewriter()
    counter1 = piecelocxy.index((-15,0))
    counter1loc = piecelocxy[counter1]
    counter2 = piecelocxy.index((-15,(-1*incchange)))
    counter2loc = piecelocxy[counter2]
    counter3 = piecelocxy.index((-15,(-2*incchange)))
    counter3loc = piecelocxy[counter3]
    counter4 = piecelocxy.index((-15,(-3*incchange)))
    counter4loc = piecelocxy[counter4]
    counter5 = piecelocxy.index((-15,(incchange)))
    counter5loc = piecelocxy[counter5]
    counter6 = piecelocxy.index((-15,(2*incchange)))
    counter6loc = piecelocxy[counter6]
    counter7 = piecelocxy.index((90,(-1*incchange)))
    counter7loc = piecelocxy[counter7]
    counter8 = piecelocxy.index((90,0))
    counter8loc = piecelocxy[counter8]
    rot1 = piecelocxy.index((20,0))
    rot1loc = piecelocxy[rot1]
    rot2 = piecelocxy.index((55,0))
    rot2loc = piecelocxy[rot2]
    rot3 = piecelocxy.index((55,(-1*incchange)))
    rot3loc = piecelocxy[rot3]
    rot4 = piecelocxy.index((20,(-1*incchange)))
    rot4loc = piecelocxy[rot4]
    prev1 = solvepiececolor[counter1]
    prev2 = solvepiececolor[counter2]
    prev3 = solvepiececolor[counter3]
    prev4 = solvepiececolor[counter4]
    prev5 = solvepiececolor[counter5]
    prev6 = solvepiececolor[counter6]
    prev7 = solvepiececolor[counter7]
    prev8 = solvepiececolor[counter8]
    prevrot1 = solvepiececolor[rot1]
    prevrot2 = solvepiececolor[rot2]
    prevrot3 = solvepiececolor[rot3]
    prevrot4 = solvepiececolor[rot4]
  
    piecelist[counter1].goto(counter6loc)
    piecelocxy[counter1] = (counter6loc)
    solvepiececolor[counter6] = prev1

    piecelist[counter2].goto(counter5loc)
    piecelocxy[counter2] = (counter5loc)
    solvepiececolor[counter5] = prev2

    piecelist[counter3].goto(counter1loc)
    piecelocxy[counter3] = (counter1loc)
    solvepiececolor[counter1] = prev3

    piecelist[counter4].goto(counter2loc)
    piecelocxy[counter4] = (counter2loc)
    solvepiececolor[counter2] = prev4

    piecelist[counter5].goto(counter7loc)
    piecelocxy[counter5] = (counter7loc)
    solvepiececolor[counter7] = prev5

    piecelist[counter6].goto(counter8loc)
    piecelocxy[counter6] = (counter8loc)
    solvepiececolor[counter8] = prev6

    piecelist[counter7].goto(counter4loc)
    piecelocxy[counter7] = (counter4loc)
    solvepiececolor[counter4] = prev7

    piecelist[counter8].goto(counter3loc)
    piecelocxy[counter8] = (counter3loc)
    solvepiececolor[counter3] = prev8

    piecelist[rot1].goto(rot2loc)
    piecelocxy[rot1] = (rot2loc)
    solvepiececolor[rot2] = prevrot1

    piecelist[rot2].goto(rot3loc)
    piecelocxy[rot2] = (rot3loc)
    solvepiececolor[rot3] = prevrot2

    piecelist[rot3].goto(rot4loc)
    piecelocxy[rot3] = (rot4loc)
    solvepiececolor[rot4] = prevrot3

    piecelist[rot4].goto(rot1loc)
    piecelocxy[rot4] = (rot1loc)
    solvepiececolor[rot1] = prevrot4

    global piececounter
    global counter
    counter = 1
    piececounter = 0

    for sidesolver in range (6):
      if solvepiececolor[piececounter] == solvepiececolor[piececounter+1] and solvepiececolor[piececounter] == solvepiececolor[piececounter+2] and solvepiececolor[piececounter] == solvepiececolor[piececounter+3]:
        solvelist[int(piececounter/4)] = 1
        piececounter+=4
      else: 
        solvelist[int(piececounter/4)] = 0
        piececounter+=4
      if counter == 6:
        print (solvelist)
        global turned
        if solvelist[0]+solvelist[1]+solvelist[2]+solvelist[3]+solvelist[4]+solvelist[5] == 6:
          global storedmoves
          storedmoves = movecounter
          displayer()
          movecounter = 0
          print("cube solved")
          turned=1
          tmr.sleep(3)
          movewriter()
      counter+=1
    ready = 1

for l in range (24):
  position = int(number-1)
  if number == 5:
    bruh = "green"
  if number == 9:
    bruh = "orange"
  if number == 13:
    bruh = "blue"
  if number == 17:
    bruh = "yellow"
  if number == 21:
    bruh = "white"
  huh = trtl.Turtle()
  piecelist.append(huh)
  piecelist[position].penup()
  piecelist[position].color(str(bruh))
  piecelist[position].pencolor("black")
  piecelist[position].shape("square")
  piecelist[position].shapesize(cubiesize)
  piecelist[position].speed("fastest")
  x = piecelist[position].xcor()
  y = piecelist[position].ycor()
  if number <= 16:
    if number%4 == 1:
      piecelist[position].goto(x+inc, y)
      inc+=incchange
    if number%4 == 2:
      piecelist[position].goto(x+inc, y)
    if number%4 == 3:
      piecelist[position].goto(x+inc-incchange, y-incchange)
    if number%4 == 0:
      piecelist[position].goto(x+inc, y-incchange)
      inc+=incchange
     
  if 21 > number >= 17:
    if number%4 == 1:
      piecelist[position].goto(x-(6*incchange)+inc, y+(2*incchange))
    if number%4 == 2:
      piecelist[position].goto(x-(5*incchange)+inc, y+(2*incchange))
    if number%4 == 3:
      piecelist[position].goto(x-(6*incchange)+inc, y+(incchange))
    if number%4 == 0:
      piecelist[position].goto(x-(5*incchange)+inc, y+(incchange))
 
  if number >= 21:
    if number%4 == 1:
      piecelist[position].goto(x-(6*incchange)+inc, y-(2*incchange))
    if number%4 == 2:
      piecelist[position].goto(x-(5*incchange)+inc, y-(2*incchange))
    if number%4 == 3:
      piecelist[position].goto(x-(6*incchange)+inc, y-(3*incchange))
    if number%4 == 0:
      piecelist[position].goto(x-(5*incchange)+inc, y-(3*incchange))
 
  x = piecelist[position].xcor()
  y = piecelist[position].ycor()
  # solveposxy.append((x, y))
  piecelocxy.append((x, y))
  solvepiececolor.append(str(bruh))
  number+=1

def upprime():
  global movecounter
  global ready
  if movecounter == 0 or ready == 1:
    ready = 0 
    movecounter+=1
    movewriter()
    counter1 = piecelocxy.index((-120,0))
    counter1loc = piecelocxy[counter1]
    counter2 = piecelocxy.index((-85,0))
    counter2loc = piecelocxy[counter2]
    counter3 = piecelocxy.index((-50,0))
    counter3loc = piecelocxy[counter3]
    counter4 = piecelocxy.index((-15,0))
    counter4loc = piecelocxy[counter4]
    counter5 = piecelocxy.index((20,0))
    counter5loc = piecelocxy[counter5]
    counter6 = piecelocxy.index((55,0))
    counter6loc = piecelocxy[counter6]
    counter7 = piecelocxy.index((90,0))
    counter7loc = piecelocxy[counter7]
    counter8 = piecelocxy.index((125,0))
    counter8loc = piecelocxy[counter8]
  
  
    rot1 = piecelocxy.index((-50,70))
    rot1loc = piecelocxy[rot1]
    rot2 = piecelocxy.index((-50,35))
    rot2loc = piecelocxy[rot2]
    rot3 = piecelocxy.index((-15,70))
    rot3loc = piecelocxy[rot3]
    rot4 = piecelocxy.index((-15,35))
    rot4loc = piecelocxy[rot4]
    prev1 = solvepiececolor[counter1]
    prev2 = solvepiececolor[counter2]
    prev3 = solvepiececolor[counter3]
    prev4 = solvepiececolor[counter4]
    prev5 = solvepiececolor[counter5]
    prev6 = solvepiececolor[counter6]
    prev7 = solvepiececolor[counter7]
    prev8 = solvepiececolor[counter8]
    prevrot1 = solvepiececolor[rot1]
    prevrot2 = solvepiececolor[rot2]
    prevrot3 = solvepiececolor[rot3]
    prevrot4 = solvepiececolor[rot4]
  
    piecelist[counter1].goto(counter3loc)
    piecelocxy[counter1] = (counter3loc)
    solvepiececolor[counter3] = prev1
  
    piecelist[counter2].goto(counter4loc)
    piecelocxy[counter2] = (counter4loc)
    solvepiececolor[counter4] = prev2

    piecelist[counter3].goto(counter5loc)
    piecelocxy[counter3] = (counter5loc)
    solvepiececolor[counter5] = prev3
  
    piecelist[counter4].goto(counter6loc)
    piecelocxy[counter4] = (counter6loc)
    solvepiececolor[counter6] = prev4
  
    piecelist[counter5].goto(counter7loc)
    piecelocxy[counter5] = (counter7loc)
    solvepiececolor[counter7] = prev5

    piecelist[counter6].goto(counter8loc)
    piecelocxy[counter6] = (counter8loc)
    solvepiececolor[counter8] = prev6
  
    piecelist[counter7].goto(counter1loc)
    piecelocxy[counter7] = (counter1loc)
    solvepiececolor[counter1] = prev7
  
    piecelist[counter8].goto(counter2loc)
    piecelocxy[counter8] = (counter2loc)
    solvepiececolor[counter2] = prev8
  
    piecelist[rot1].goto(rot2loc)
    piecelocxy[rot1] = (rot2loc)
    solvepiececolor[rot2] = prevrot1
  
    piecelist[rot2].goto(rot4loc)
    piecelocxy[rot2] = (rot4loc)
    solvepiececolor[rot4] = prevrot2

    piecelist[rot3].goto(rot1loc)
    piecelocxy[rot3] = (rot1loc)
    solvepiececolor[rot1] = prevrot3
  
    piecelist[rot4].goto(rot3loc)
    piecelocxy[rot4] = (rot3loc)
    solvepiececolor[rot3] = prevrot4
    global piececounter
    global counter
    counter = 1
    piececounter = 0

    for sidesolver in range (6):
      if solvepiececolor[piececounter] == solvepiececolor[piececounter+1] and solvepiececolor[piececounter] == solvepiececolor[piececounter+2] and solvepiececolor[piececounter] == solvepiececolor[piececounter+3]:
        solvelist[int(piececounter/4)] = 1
        piececounter+=4
      else: 
        solvelist[int(piececounter/4)] = 0
        piececounter+=4
      if counter == 6:
        print (solvelist)
        global turned
        if solvelist[0]+solvelist[1]+solvelist[2]+solvelist[3]+solvelist[4]+solvelist[5] == 6:
          global storedmoves
          storedmoves = movecounter
          displayer()
          movecounter = 0
          print("cube solved")
          turned=1
          tmr.sleep(3)
          movewriter()
      counter+=1
    ready = 1

def up():
  global movecounter
  global ready
  if movecounter == 0 or ready == 1:
    ready = 0 
    movecounter+=1
    movewriter()
    counter1 = piecelocxy.index((-120,0))
    counter1loc = piecelocxy[counter1]
    counter2 = piecelocxy.index((-85,0))
    counter2loc = piecelocxy[counter2]
    counter3 = piecelocxy.index((-50,0))
    counter3loc = piecelocxy[counter3]
    counter4 = piecelocxy.index((-15,0))
    counter4loc = piecelocxy[counter4]
    counter5 = piecelocxy.index((20,0))
    counter5loc = piecelocxy[counter5]
    counter6 = piecelocxy.index((55,0))
    counter6loc = piecelocxy[counter6]
    counter7 = piecelocxy.index((90,0))
    counter7loc = piecelocxy[counter7]
    counter8 = piecelocxy.index((125,0))
    counter8loc = piecelocxy[counter8]
  
  
    rot1 = piecelocxy.index((-50,70))
    rot1loc = piecelocxy[rot1]
    rot2 = piecelocxy.index((-50,35))
    rot2loc = piecelocxy[rot2]
    rot3 = piecelocxy.index((-15,70))
    rot3loc = piecelocxy[rot3]
    rot4 = piecelocxy.index((-15,35))
    rot4loc = piecelocxy[rot4]
    prev1 = solvepiececolor[counter1]
    prev2 = solvepiececolor[counter2]
    prev3 = solvepiececolor[counter3]
    prev4 = solvepiececolor[counter4]
    prev5 = solvepiececolor[counter5]
    prev6 = solvepiececolor[counter6]
    prev7 = solvepiececolor[counter7]
    prev8 = solvepiececolor[counter8]
    prevrot1 = solvepiececolor[rot1]
    prevrot2 = solvepiececolor[rot2]
    prevrot3 = solvepiececolor[rot3]
    prevrot4 = solvepiececolor[rot4]
  
    piecelist[counter1].goto(counter7loc)
    piecelocxy[counter1] = (counter7loc)
    solvepiececolor[counter7] = prev1
  
    piecelist[counter2].goto(counter8loc)
    piecelocxy[counter2] = (counter8loc)
    solvepiececolor[counter8] = prev2

    piecelist[counter3].goto(counter1loc)
    piecelocxy[counter3] = (counter1loc)
    solvepiececolor[counter1] = prev3
  
    piecelist[counter4].goto(counter2loc)
    piecelocxy[counter4] = (counter2loc)
    solvepiececolor[counter2] = prev4
  
    piecelist[counter5].goto(counter3loc)
    piecelocxy[counter5] = (counter3loc)
    solvepiececolor[counter3] = prev5

    piecelist[counter6].goto(counter4loc)
    piecelocxy[counter6] = (counter4loc)
    solvepiececolor[counter4] = prev6
  
    piecelist[counter7].goto(counter5loc)
    piecelocxy[counter7] = (counter5loc)
    solvepiececolor[counter5] = prev7
  
    piecelist[counter8].goto(counter6loc)
    piecelocxy[counter8] = (counter6loc)
    solvepiececolor[counter6] = prev8
  
    piecelist[rot1].goto(rot3loc)
    piecelocxy[rot1] = (rot3loc)
    solvepiececolor[rot3] = prevrot1
  
    piecelist[rot2].goto(rot1loc)
    piecelocxy[rot2] = (rot1loc)
    solvepiececolor[rot1] = prevrot2

    piecelist[rot3].goto(rot4loc)
    piecelocxy[rot3] = (rot4loc)
    solvepiececolor[rot4] = prevrot3
  
    piecelist[rot4].goto(rot2loc)
    piecelocxy[rot4] = (rot2loc)
    solvepiececolor[rot2] = prevrot4
    global piececounter
    global counter
    counter = 1
    piececounter = 0

    for sidesolver in range (6):
      if solvepiececolor[piececounter] == solvepiececolor[piececounter+1] and solvepiececolor[piececounter] == solvepiececolor[piececounter+2] and solvepiececolor[piececounter] == solvepiececolor[piececounter+3]:
        solvelist[int(piececounter/4)] = 1
        piececounter+=4
      else: 
        solvelist[int(piececounter/4)] = 0
        piececounter+=4
      if counter == 6:
        print (solvelist)
        global turned
        if solvelist[0]+solvelist[1]+solvelist[2]+solvelist[3]+solvelist[4]+solvelist[5] == 6:
          global storedmoves
          storedmoves = movecounter
          displayer()
          movecounter = 0
          print("cube solved")
          turned=1
          tmr.sleep(3)
          movewriter()
      counter+=1
    ready = 1

def back():
  global movecounter
  global ready
  if movecounter == 0 or ready == 1:
    ready = 0 
    movecounter+=1
    movewriter()
    counter1 = piecelocxy.index((-120,0))
    counter1loc = piecelocxy[counter1]
    counter2 = piecelocxy.index((-120,-35))
    counter2loc = piecelocxy[counter2]
    counter3 = piecelocxy.index((-50,70))
    counter3loc = piecelocxy[counter3]
    counter4 = piecelocxy.index((-15,70))
    counter4loc = piecelocxy[counter4]
    counter5 = piecelocxy.index((-50,-105))
    counter5loc = piecelocxy[counter5]
    counter6 = piecelocxy.index((-15,-105))
    counter6loc = piecelocxy[counter6]
    counter7 = piecelocxy.index((55,0))
    counter7loc = piecelocxy[counter7]
    counter8 = piecelocxy.index((55,-35))
    counter8loc = piecelocxy[counter8]
  
  
    rot1 = piecelocxy.index((90,0))
    rot1loc = piecelocxy[rot1]
    rot2 = piecelocxy.index((90,-35))
    rot2loc = piecelocxy[rot2]
    rot3 = piecelocxy.index((125,0))
    rot3loc = piecelocxy[rot3]
    rot4 = piecelocxy.index((125,-35))
    rot4loc = piecelocxy[rot4]


    prev1 = solvepiececolor[counter1]
    prev2 = solvepiececolor[counter2]
    prev3 = solvepiececolor[counter3]
    prev4 = solvepiececolor[counter4]
    prev5 = solvepiececolor[counter5]
    prev6 = solvepiececolor[counter6]
    prev7 = solvepiececolor[counter7]
    prev8 = solvepiececolor[counter8]
    prevrot1 = solvepiececolor[rot1]
    prevrot2 = solvepiececolor[rot2]
    prevrot3 = solvepiececolor[rot3]
    prevrot4 = solvepiececolor[rot4]
  
    piecelist[counter1].goto(counter5loc)
    piecelocxy[counter1] = (counter5loc)
    solvepiececolor[counter5] = prev1
  
    piecelist[counter2].goto(counter6loc)
    piecelocxy[counter2] = (counter6loc)
    solvepiececolor[counter6] = prev2

    piecelist[counter3].goto(counter2loc)
    piecelocxy[counter3] = (counter2loc)
    solvepiececolor[counter2] = prev3
  
    piecelist[counter4].goto(counter1loc)
    piecelocxy[counter4] = (counter1loc)
    solvepiececolor[counter1] = prev4
  
    piecelist[counter5].goto(counter8loc)
    piecelocxy[counter5] = (counter8loc)
    solvepiececolor[counter8] = prev5

    piecelist[counter6].goto(counter7loc)
    piecelocxy[counter6] = (counter7loc)
    solvepiececolor[counter7] = prev6
  
    piecelist[counter7].goto(counter3loc)
    piecelocxy[counter7] = (counter3loc)
    solvepiececolor[counter3] = prev7
  
    piecelist[counter8].goto(counter4loc)
    piecelocxy[counter8] = (counter4loc)
    solvepiececolor[counter4] = prev8
  
    piecelist[rot1].goto(rot3loc)
    piecelocxy[rot1] = (rot3loc)
    solvepiececolor[rot3] = prevrot1
  
    piecelist[rot2].goto(rot1loc)
    piecelocxy[rot2] = (rot1loc)
    solvepiececolor[rot1] = prevrot2

    piecelist[rot3].goto(rot4loc)
    piecelocxy[rot3] = (rot4loc)
    solvepiececolor[rot4] = prevrot3
  
    piecelist[rot4].goto(rot2loc)
    piecelocxy[rot4] = (rot2loc)
    solvepiececolor[rot2] = prevrot4

    global piececounter
    global counter
    counter = 1
    piececounter = 0

    for sidesolver in range (6):
      if solvepiececolor[piececounter] == solvepiececolor[piececounter+1] and solvepiececolor[piececounter] == solvepiececolor[piececounter+2] and solvepiececolor[piececounter] == solvepiececolor[piececounter+3]:
        solvelist[int(piececounter/4)] = 1
        piececounter+=4
      else: 
        solvelist[int(piececounter/4)] = 0
        piececounter+=4
      if counter == 6:
        print (solvelist)
        global turned
        if solvelist[0]+solvelist[1]+solvelist[2]+solvelist[3]+solvelist[4]+solvelist[5] == 6:
          global storedmoves
          storedmoves = movecounter
          displayer()
          movecounter = 0
          print("cube solved")
          turned=1
          tmr.sleep(3)
          movewriter()
      counter+=1
    ready = 1
  
def backprime():
  global movecounter
  global ready
  if movecounter == 0 or ready == 1:
    ready = 0 
    movecounter+=1
    movewriter()
    counter1 = piecelocxy.index((-120,0))
    counter1loc = piecelocxy[counter1]
    counter2 = piecelocxy.index((-120,-35))
    counter2loc = piecelocxy[counter2]
    counter3 = piecelocxy.index((-50,70))
    counter3loc = piecelocxy[counter3]
    counter4 = piecelocxy.index((-15,70))
    counter4loc = piecelocxy[counter4]
    counter5 = piecelocxy.index((-50,-105))
    counter5loc = piecelocxy[counter5]
    counter6 = piecelocxy.index((-15,-105))
    counter6loc = piecelocxy[counter6]
    counter7 = piecelocxy.index((55,0))
    counter7loc = piecelocxy[counter7]
    counter8 = piecelocxy.index((55,-35))
    counter8loc = piecelocxy[counter8]
  
  
    rot1 = piecelocxy.index((90,0))
    rot1loc = piecelocxy[rot1]
    rot2 = piecelocxy.index((90,-35))
    rot2loc = piecelocxy[rot2]
    rot3 = piecelocxy.index((125,0))
    rot3loc = piecelocxy[rot3]
    rot4 = piecelocxy.index((125,-35))
    rot4loc = piecelocxy[rot4]


    prev1 = solvepiececolor[counter1]
    prev2 = solvepiececolor[counter2]
    prev3 = solvepiececolor[counter3]
    prev4 = solvepiececolor[counter4]
    prev5 = solvepiececolor[counter5]
    prev6 = solvepiececolor[counter6]
    prev7 = solvepiececolor[counter7]
    prev8 = solvepiececolor[counter8]
    prevrot1 = solvepiececolor[rot1]
    prevrot2 = solvepiececolor[rot2]
    prevrot3 = solvepiececolor[rot3]
    prevrot4 = solvepiececolor[rot4]
  
    piecelist[counter1].goto(counter4loc)
    piecelocxy[counter1] = (counter4loc)
    solvepiececolor[counter4] = prev1
  
    piecelist[counter2].goto(counter3loc)
    piecelocxy[counter2] = (counter3loc)
    solvepiececolor[counter3] = prev2

    piecelist[counter3].goto(counter7loc)
    piecelocxy[counter3] = (counter7loc)
    solvepiececolor[counter7] = prev3
  
    piecelist[counter4].goto(counter8loc)
    piecelocxy[counter4] = (counter8loc)
    solvepiececolor[counter8] = prev4
  
    piecelist[counter5].goto(counter1loc)
    piecelocxy[counter5] = (counter1loc)
    solvepiececolor[counter1] = prev5

    piecelist[counter6].goto(counter2loc)
    piecelocxy[counter6] = (counter2loc)
    solvepiececolor[counter2] = prev6
  
    piecelist[counter7].goto(counter6loc)
    piecelocxy[counter7] = (counter6loc)
    solvepiececolor[counter6] = prev7
  
    piecelist[counter8].goto(counter5loc)
    piecelocxy[counter8] = (counter5loc)
    solvepiececolor[counter5] = prev8
  
    piecelist[rot1].goto(rot2loc)
    piecelocxy[rot1] = (rot2loc)
    solvepiececolor[rot2] = prevrot1
  
    piecelist[rot2].goto(rot4loc)
    piecelocxy[rot2] = (rot4loc)
    solvepiececolor[rot1] = prevrot2

    piecelist[rot3].goto(rot1loc)
    piecelocxy[rot3] = (rot1loc)
    solvepiececolor[rot1] = prevrot3
  
    piecelist[rot4].goto(rot3loc)
    piecelocxy[rot4] = (rot3loc)
    solvepiececolor[rot3] = prevrot4

    global piececounter
    global counter
    counter = 1
    piececounter = 0

    for sidesolver in range (6):
      if solvepiececolor[piececounter] == solvepiececolor[piececounter+1] and solvepiececolor[piececounter] == solvepiececolor[piececounter+2] and solvepiececolor[piececounter] == solvepiececolor[piececounter+3]:
        solvelist[int(piececounter/4)] = 1
        piececounter+=4
      else: 
        solvelist[int(piececounter/4)] = 0
        piececounter+=4
      if counter == 6:
        print (solvelist)
        global turned
        if solvelist[0]+solvelist[1]+solvelist[2]+solvelist[3]+solvelist[4]+solvelist[5] == 6:
          global storedmoves
          storedmoves = movecounter
          displayer()
          movecounter = 0
          print("cube solved")
          turned=1
          tmr.sleep(3)
          movewriter()
      counter+=1
    ready = 1

def downprime():
  global movecounter
  global ready
  if movecounter == 0 or ready == 1:
    ready = 0 
    movecounter+=1
    movewriter()
    counter1 = piecelocxy.index((-120,-35))
    counter1loc = piecelocxy[counter1]
    counter2 = piecelocxy.index((-85,-35))
    counter2loc = piecelocxy[counter2]
    counter3 = piecelocxy.index((-50,-35))
    counter3loc = piecelocxy[counter3]
    counter4 = piecelocxy.index((-15,-35))
    counter4loc = piecelocxy[counter4]
    counter5 = piecelocxy.index((20,-35))
    counter5loc = piecelocxy[counter5]
    counter6 = piecelocxy.index((55,-35))
    counter6loc = piecelocxy[counter6]
    counter7 = piecelocxy.index((90,-35))
    counter7loc = piecelocxy[counter7]
    counter8 = piecelocxy.index((125,-35))
    counter8loc = piecelocxy[counter8]
  
  
    rot1 = piecelocxy.index((-50,-70))
    rot1loc = piecelocxy[rot1]
    rot2 = piecelocxy.index((-50,-105))
    rot2loc = piecelocxy[rot2]
    rot3 = piecelocxy.index((-15,-70))
    rot3loc = piecelocxy[rot3]
    rot4 = piecelocxy.index((-15,-105))
    rot4loc = piecelocxy[rot4]
    prev1 = solvepiececolor[counter1]
    prev2 = solvepiececolor[counter2]
    prev3 = solvepiececolor[counter3]
    prev4 = solvepiececolor[counter4]
    prev5 = solvepiececolor[counter5]
    prev6 = solvepiececolor[counter6]
    prev7 = solvepiececolor[counter7]
    prev8 = solvepiececolor[counter8]
    prevrot1 = solvepiececolor[rot1]
    prevrot2 = solvepiececolor[rot2]
    prevrot3 = solvepiececolor[rot3]
    prevrot4 = solvepiececolor[rot4]
  
    piecelist[counter1].goto(counter7loc)
    piecelocxy[counter1] = (counter7loc)
    solvepiececolor[counter7] = prev1
  
    piecelist[counter2].goto(counter8loc)
    piecelocxy[counter2] = (counter8loc)
    solvepiececolor[counter8] = prev2

    piecelist[counter3].goto(counter1loc)
    piecelocxy[counter3] = (counter1loc)
    solvepiececolor[counter1] = prev3
  
    piecelist[counter4].goto(counter2loc)
    piecelocxy[counter4] = (counter2loc)
    solvepiececolor[counter2] = prev4
  
    piecelist[counter5].goto(counter3loc)
    piecelocxy[counter5] = (counter3loc)
    solvepiececolor[counter3] = prev5

    piecelist[counter6].goto(counter4loc)
    piecelocxy[counter6] = (counter4loc)
    solvepiececolor[counter4] = prev6
  
    piecelist[counter7].goto(counter5loc)
    piecelocxy[counter7] = (counter5loc)
    solvepiececolor[counter5] = prev7
  
    piecelist[counter8].goto(counter6loc)
    piecelocxy[counter8] = (counter6loc)
    solvepiececolor[counter6] = prev8
  
    piecelist[rot1].goto(rot2loc)
    piecelocxy[rot1] = (rot2loc)
    solvepiececolor[rot2] = prevrot1
  
    piecelist[rot2].goto(rot4loc)
    piecelocxy[rot2] = (rot4loc)
    solvepiececolor[rot4] = prevrot2

    piecelist[rot3].goto(rot1loc)
    piecelocxy[rot3] = (rot1loc)
    solvepiececolor[rot1] = prevrot3
  
    piecelist[rot4].goto(rot3loc)
    piecelocxy[rot4] = (rot3loc)
    solvepiececolor[rot3] = prevrot4

    global piececounter
    global counter
    counter = 1
    piececounter = 0

    for sidesolver in range (6):
      if solvepiececolor[piececounter] == solvepiececolor[piececounter+1] and solvepiececolor[piececounter] == solvepiececolor[piececounter+2] and solvepiececolor[piececounter] == solvepiececolor[piececounter+3]:
        solvelist[int(piececounter/4)] = 1
        piececounter+=4
      else: 
        solvelist[int(piececounter/4)] = 0
        piececounter+=4
      if counter == 6:
        print (solvelist)
        global turned
        if solvelist[0]+solvelist[1]+solvelist[2]+solvelist[3]+solvelist[4]+solvelist[5] == 6:
          global storedmoves
          storedmoves = movecounter
          displayer()
          movecounter = 0
          print("cube solved")
          turned=1
          tmr.sleep(3)
          movewriter()
      counter+=1
    ready = 1

def down():
  global movecounter
  global ready
  if movecounter == 0 or ready == 1:
    ready = 0 
    movecounter+=1
    movewriter()
    counter1 = piecelocxy.index((-120,-35))
    counter1loc = piecelocxy[counter1]
    counter2 = piecelocxy.index((-85,-35))
    counter2loc = piecelocxy[counter2]
    counter3 = piecelocxy.index((-50,-35))
    counter3loc = piecelocxy[counter3]
    counter4 = piecelocxy.index((-15,-35))
    counter4loc = piecelocxy[counter4]
    counter5 = piecelocxy.index((20,-35))
    counter5loc = piecelocxy[counter5]
    counter6 = piecelocxy.index((55,-35))
    counter6loc = piecelocxy[counter6]
    counter7 = piecelocxy.index((90,-35))
    counter7loc = piecelocxy[counter7]
    counter8 = piecelocxy.index((125,-35))
    counter8loc = piecelocxy[counter8]
  
    rot1 = piecelocxy.index((-50,-70))
    rot1loc = piecelocxy[rot1]
    rot2 = piecelocxy.index((-50,-105))
    rot2loc = piecelocxy[rot2]
    rot3 = piecelocxy.index((-15,-70))
    rot3loc = piecelocxy[rot3]
    rot4 = piecelocxy.index((-15,-105))
    rot4loc = piecelocxy[rot4]
    prev1 = solvepiececolor[counter1]
    prev2 = solvepiececolor[counter2]
    prev3 = solvepiececolor[counter3]
    prev4 = solvepiececolor[counter4]
    prev5 = solvepiececolor[counter5]
    prev6 = solvepiececolor[counter6]
    prev7 = solvepiececolor[counter7]
    prev8 = solvepiececolor[counter8]
    prevrot1 = solvepiececolor[rot1]
    prevrot2 = solvepiececolor[rot2]
    prevrot3 = solvepiececolor[rot3]
    prevrot4 = solvepiececolor[rot4]
  
    piecelist[counter1].goto(counter3loc)
    piecelocxy[counter1] = (counter3loc)
    solvepiececolor[counter3] = prev1
  
    piecelist[counter2].goto(counter4loc)
    piecelocxy[counter2] = (counter4loc)
    solvepiececolor[counter4] = prev2

    piecelist[counter3].goto(counter5loc)
    piecelocxy[counter3] = (counter5loc)
    solvepiececolor[counter5] = prev3
  
    piecelist[counter4].goto(counter6loc)
    piecelocxy[counter4] = (counter6loc)
    solvepiececolor[counter6] = prev4
  
    piecelist[counter5].goto(counter7loc)
    piecelocxy[counter5] = (counter7loc)
    solvepiececolor[counter7] = prev5

    piecelist[counter6].goto(counter8loc)
    piecelocxy[counter6] = (counter8loc)
    solvepiececolor[counter8] = prev6
  
    piecelist[counter7].goto(counter1loc)
    piecelocxy[counter7] = (counter1loc)
    solvepiececolor[counter1] = prev7
  
    piecelist[counter8].goto(counter2loc)
    piecelocxy[counter8] = (counter2loc)
    solvepiececolor[counter2] = prev8
  
    piecelist[rot1].goto(rot3loc)
    piecelocxy[rot1] = (rot3loc)
    solvepiececolor[rot3] = prevrot1
  
    piecelist[rot2].goto(rot1loc)
    piecelocxy[rot2] = (rot1loc)
    solvepiececolor[rot1] = prevrot2

    piecelist[rot3].goto(rot4loc)
    piecelocxy[rot3] = (rot4loc)
    solvepiececolor[rot4] = prevrot3
  
    piecelist[rot4].goto(rot2loc)
    piecelocxy[rot4] = (rot2loc)
    solvepiececolor[rot2] = prevrot4

    global piececounter
    global counter
    counter = 1
    piececounter = 0

    for sidesolver in range (6):
      if solvepiececolor[piececounter] == solvepiececolor[piececounter+1] and solvepiececolor[piececounter] == solvepiececolor[piececounter+2] and solvepiececolor[piececounter] == solvepiececolor[piececounter+3]:
        solvelist[int(piececounter/4)] = 1
        piececounter+=4
      else: 
        solvelist[int(piececounter/4)] = 0
        piececounter+=4
      if counter == 6:
        print (solvelist)
        global turned
        if solvelist[0]+solvelist[1]+solvelist[2]+solvelist[3]+solvelist[4]+solvelist[5] == 6:
          global storedmoves
          storedmoves = movecounter
          displayer()
          movecounter = 0
          print("cube solved")
          turned=1
          tmr.sleep(3)
          movewriter()
      counter+=1
    ready = 1

def front():
  global movecounter
  global ready
  if movecounter == 0 or ready == 1:
    ready = 0 
    movecounter+=1
    movewriter()
    counter1 = piecelocxy.index((-85,0))
    counter1loc = piecelocxy[counter1]
    counter2 = piecelocxy.index((-85,-35))
    counter2loc = piecelocxy[counter2]
    counter3 = piecelocxy.index((-50,35))
    counter3loc = piecelocxy[counter3]
    counter4 = piecelocxy.index((-15,35))
    counter4loc = piecelocxy[counter4]
    counter5 = piecelocxy.index((-50,-70))
    counter5loc = piecelocxy[counter5]
    counter6 = piecelocxy.index((-15,-70))
    counter6loc = piecelocxy[counter6]
    counter7 = piecelocxy.index((20,0))
    counter7loc = piecelocxy[counter7]
    counter8 = piecelocxy.index((20,-35))
    counter8loc = piecelocxy[counter8]
  
    rot1 = piecelocxy.index((-50,0))
    rot1loc = piecelocxy[rot1]
    rot2 = piecelocxy.index((-15,0))
    rot2loc = piecelocxy[rot2]
    rot3 = piecelocxy.index((-50,-35))
    rot3loc = piecelocxy[rot3]
    rot4 = piecelocxy.index((-15,-35))
    rot4loc = piecelocxy[rot4]
    prev1 = solvepiececolor[counter1]
    prev2 = solvepiececolor[counter2]
    prev3 = solvepiececolor[counter3]
    prev4 = solvepiececolor[counter4]
    prev5 = solvepiececolor[counter5]
    prev6 = solvepiececolor[counter6]
    prev7 = solvepiececolor[counter7]
    prev8 = solvepiececolor[counter8]
    prevrot1 = solvepiececolor[rot1]
    prevrot2 = solvepiececolor[rot2]
    prevrot3 = solvepiececolor[rot3]
    prevrot4 = solvepiececolor[rot4]
  
    piecelist[counter1].goto(counter4loc)
    piecelocxy[counter1] = (counter4loc)
    solvepiececolor[counter4] = prev1
  
    piecelist[counter2].goto(counter3loc)
    piecelocxy[counter2] = (counter3loc)
    solvepiececolor[counter3] = prev2

    piecelist[counter3].goto(counter7loc)
    piecelocxy[counter3] = (counter7loc)
    solvepiececolor[counter7] = prev3
  
    piecelist[counter4].goto(counter8loc)
    piecelocxy[counter4] = (counter8loc)
    solvepiececolor[counter8] = prev4
  
    piecelist[counter5].goto(counter1loc)
    piecelocxy[counter5] = (counter1loc)
    solvepiececolor[counter1] = prev5

    piecelist[counter6].goto(counter2loc)
    piecelocxy[counter6] = (counter2loc)
    solvepiececolor[counter2] = prev6
  
    piecelist[counter7].goto(counter6loc)
    piecelocxy[counter7] = (counter6loc)
    solvepiececolor[counter6] = prev7
  
    piecelist[counter8].goto(counter5loc)
    piecelocxy[counter8] = (counter5loc)
    solvepiececolor[counter5] = prev8
  
    piecelist[rot1].goto(rot2loc)
    piecelocxy[rot1] = (rot2loc)
    solvepiececolor[rot2] = prevrot1
  
    piecelist[rot2].goto(rot4loc)
    piecelocxy[rot2] = (rot4loc)
    solvepiececolor[rot4] = prevrot2

    piecelist[rot3].goto(rot1loc)
    piecelocxy[rot3] = (rot1loc)
    solvepiececolor[rot1] = prevrot3
  
    piecelist[rot4].goto(rot3loc)
    piecelocxy[rot4] = (rot3loc)
    solvepiececolor[rot3] = prevrot4

    global piececounter
    global counter
    counter = 1
    piececounter = 0

    for sidesolver in range (6):
      if solvepiececolor[piececounter] == solvepiececolor[piececounter+1] and solvepiececolor[piececounter] == solvepiececolor[piececounter+2] and solvepiececolor[piececounter] == solvepiececolor[piececounter+3]:
        solvelist[int(piececounter/4)] = 1
        piececounter+=4
      else: 
        solvelist[int(piececounter/4)] = 0
        piececounter+=4
      if counter == 6:
        print (solvelist)
        global turned
        if solvelist[0]+solvelist[1]+solvelist[2]+solvelist[3]+solvelist[4]+solvelist[5] == 6:
          global storedmoves
          storedmoves = movecounter
          displayer()
          movecounter = 0
          print("cube solved")
          turned=1
          tmr.sleep(3)
          movewriter()
      counter+=1
    ready = 1
def frontprime():
  global movecounter
  global ready
  if movecounter == 0 or ready == 1:
    ready = 0 
    movecounter+=1
    movewriter()
    counter1 = piecelocxy.index((-85,0))
    counter1loc = piecelocxy[counter1]
    counter2 = piecelocxy.index((-85,-35))
    counter2loc = piecelocxy[counter2]
    counter3 = piecelocxy.index((-50,35))
    counter3loc = piecelocxy[counter3]
    counter4 = piecelocxy.index((-15,35))
    counter4loc = piecelocxy[counter4]
    counter5 = piecelocxy.index((-50,-70))
    counter5loc = piecelocxy[counter5]
    counter6 = piecelocxy.index((-15,-70))
    counter6loc = piecelocxy[counter6]
    counter7 = piecelocxy.index((20,0))
    counter7loc = piecelocxy[counter7]
    counter8 = piecelocxy.index((20,-35))
    counter8loc = piecelocxy[counter8]
  
    rot1 = piecelocxy.index((-50,0))
    rot1loc = piecelocxy[rot1]
    rot2 = piecelocxy.index((-15,0))
    rot2loc = piecelocxy[rot2]
    rot3 = piecelocxy.index((-50,-35))
    rot3loc = piecelocxy[rot3]
    rot4 = piecelocxy.index((-15,-35))
    rot4loc = piecelocxy[rot4]
    prev1 = solvepiececolor[counter1]
    prev2 = solvepiececolor[counter2]
    prev3 = solvepiececolor[counter3]
    prev4 = solvepiececolor[counter4]
    prev5 = solvepiececolor[counter5]
    prev6 = solvepiececolor[counter6]
    prev7 = solvepiececolor[counter7]
    prev8 = solvepiececolor[counter8]
    prevrot1 = solvepiececolor[rot1]
    prevrot2 = solvepiececolor[rot2]
    prevrot3 = solvepiececolor[rot3]
    prevrot4 = solvepiececolor[rot4]
  
    piecelist[counter1].goto(counter5loc)
    piecelocxy[counter1] = (counter5loc)
    solvepiececolor[counter5] = prev1
  
    piecelist[counter2].goto(counter6loc)
    piecelocxy[counter2] = (counter6loc)
    solvepiececolor[counter6] = prev2

    piecelist[counter3].goto(counter2loc)
    piecelocxy[counter3] = (counter2loc)
    solvepiececolor[counter2] = prev3
  
    piecelist[counter4].goto(counter1loc)
    piecelocxy[counter4] = (counter1loc)
    solvepiececolor[counter1] = prev4
  
    piecelist[counter5].goto(counter8loc)
    piecelocxy[counter5] = (counter8loc)
    solvepiececolor[counter8] = prev5

    piecelist[counter6].goto(counter7loc)
    piecelocxy[counter6] = (counter7loc)
    solvepiececolor[counter7] = prev6
  
    piecelist[counter7].goto(counter3loc)
    piecelocxy[counter7] = (counter3loc)
    solvepiececolor[counter3] = prev7
  
    piecelist[counter8].goto(counter4loc)
    piecelocxy[counter8] = (counter4loc)
    solvepiececolor[counter4] = prev8
  
    piecelist[rot1].goto(rot3loc)
    piecelocxy[rot1] = (rot3loc)
    solvepiececolor[rot3] = prevrot1
  
    piecelist[rot2].goto(rot1loc)
    piecelocxy[rot2] = (rot1loc)
    solvepiececolor[rot1] = prevrot2

    piecelist[rot3].goto(rot4loc)
    piecelocxy[rot3] = (rot4loc)
    solvepiececolor[rot4] = prevrot3
  
    piecelist[rot4].goto(rot2loc)
    piecelocxy[rot4] = (rot2loc)
    solvepiececolor[rot2] = prevrot4

    global piececounter
    global counter
    counter = 1
    piececounter = 0

    for sidesolver in range (6):
      if solvepiececolor[piececounter] == solvepiececolor[piececounter+1] and solvepiececolor[piececounter] == solvepiececolor[piececounter+2] and solvepiececolor[piececounter] == solvepiececolor[piececounter+3]:
        solvelist[int(piececounter/4)] = 1
        piececounter+=4
      else: 
        solvelist[int(piececounter/4)] = 0
        piececounter+=4
      if counter == 6:
        print (solvelist)
        global turned
        if solvelist[0]+solvelist[1]+solvelist[2]+solvelist[3]+solvelist[4]+solvelist[5] == 6:
          global storedmoves
          storedmoves = movecounter
          displayer()
          movecounter = 0
          print("cube solved")
          turned=1
          tmr.sleep(3)
          movewriter()
      counter+=1
    ready = 1

wn.onkeypress(right, "k")
wn.onkeypress(rightprime, "m")
wn.onkeypress(left, "z")
wn.onkeypress(leftprime, "a")
wn.onkeypress(up, "r")
wn.onkeypress(upprime, "t")
wn.onkeypress(down, "b")
wn.onkeypress(downprime, "v")
wn.onkeypress(front, "j")
wn.onkeypress(frontprime, "n")
wn.onkeypress(back, "s")
wn.onkeypress(backprime, "x")

#create an alg to check if solved
#create a random scrambler
#create a function to recognize the solved state


# print(solveposxy)
print(solvepiececolor)

wn.ontimer(countdown, counterinterval)
wn.listen()
wn.mainloop()