import turtle as trtl
wn = trtl.Screen()
piecelist = []
ifsolve = []
solveposxy = []
piecelocxy = []
bruh = "red"
cubiesize = 1.5
inc = -180
incchange = 35
number = 1
movecounter = 0
for l in range (24):
  if number == 5:
    bruh = "green"
  if number == 9:
    bruh = "orange"
  if number == 13:
    bruh = "blue"
  if number == 17:
    bruh = "white"
  if number == 21:
    bruh = "yellow"
  huh = str(bruh)+str(number)
  huh = trtl.Turtle()
  piecelist.append(huh)
  piecelist[int(number-1)].penup()
  piecelist[int(number-1)].color(str(bruh))
  piecelist[int(number-1)].pencolor("black")
  piecelist[int(number-1)].shape("square")
  piecelist[int(number-1)].shapesize(cubiesize)
  if number%4 == 1:
    piecelist[int(number-1)].goto(piecelist[int(number-1)].xcor()+inc, piecelist[int(number-1)].ycor())
    inc+=incchange
  if number%4 == 2:
    piecelist[int(number-1)].goto(piecelist[int(number-1)].xcor()+inc, piecelist[int(number-1)].ycor())
  if number%4 == 3:
    piecelist[int(number-1)].goto(piecelist[int(number-1)].xcor()+inc-incchange, piecelist[int(number-1)].ycor()-incchange)
  if number%4 == 0:
    piecelist[int(number-1)].goto(piecelist[int(number-1)].xcor()+inc, piecelist[int(number-1)].ycor()-incchange)
    inc+=incchange
  
  ifsolve.append(1)
  x = piecelist[int(number-1)].xcor()
  y = piecelist[int(number-1)].ycor() 
  solveposxy.append((x, y))
  piecelocxy.append((x, y))
  number+=1

#create an alg to check if solved
# create a method of moving it, probably with index

print (solveposxy)

wn.listen()
wn.mainloop()