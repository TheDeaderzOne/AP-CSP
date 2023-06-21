import turtle as trtl
import random as rand
import time as tmr
wn = trtl.Screen()
wn.bgcolor("black")
x = open("answers.txt", "r")
realanswerindex = rand.randint(0, 2314)
answer = 0
counter = 0
b = x.readlines()
for line in b:
  counter+=1
  if counter == realanswerindex:
    answer = str(line)
    x.close()
    break
key = list(answer)
key.pop()
keywordinletters = ""
for e in range(5):
  key[e] = key[e].upper()
  keywordinletters = keywordinletters + str(key[e])
keyword = key
alphabetlist = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
inputboxturtles = []
letterlist = []
lettersolvedlist = []
font_setup = ("Impact", 30, "normal")
userinputwordlist = []
clog = 0
smallshapesize = .000000000000000000000000000000000000001
title = trtl.Turtle()
title.ht()
title.shapesize(smallshapesize)
title.penup()
title.pencolor("#CEA65D")
title.goto(-55,200)
title.write("MECZ", font = ("Impact", 50, "normal"))
warningmessage = trtl.Turtle()
warningmessage.ht()
warningmessage.speed("fastest")
warningmessage.pu()
warningmessage.shapesize(smallshapesize)
warningmessage.pencolor("white")
warningmessage.goto(-210, 220)
warningmessage.pd()
win = trtl.Turtle()
win.ht()
win.penup()
win.shapesize(smallshapesize)
win.goto(-87,-255)
win.color("green")

turtlexcoordinate = -130; turtleycoordinate = 150
turtlecounter = 0
gray = "#555555"
for turtle in range (30):
    if turtlecounter%5 == 0 and turtlecounter != 0:
      turtlexcoordinate = -130
      turtleycoordinate -= 65
    boxturtle = trtl.Turtle()
    boxturtle.speed("fastest")
    boxturtle.penup()
    boxturtle.shape("square")
    boxturtle.color("black")
    boxturtle.pencolor(gray)
    boxturtle.shapesize(3)
    inputboxturtles.append(boxturtle)
    inputboxturtles[turtlecounter].goto(turtlexcoordinate, turtleycoordinate)
    turtlexcoordinate += 65
    turtlecounter += 1

turtlexcoordinate = -135; turtleycoordinate = 133
lettercounter = 0

for l in range (30):
    if lettercounter%5 == 0 and lettercounter != 0:
      turtlexcoordinate = -135
      turtleycoordinate -= 65
    letterturtle = trtl.Turtle()
    letterturtle.ht()
    letterturtle.speed("fastest")
    letterturtle.penup()
    letterturtle.shapesize(smallshapesize)
    letterturtle.color("black")
    letterlist.append(letterturtle)
    letterlist[lettercounter].goto(turtlexcoordinate, turtleycoordinate)
    turtlexcoordinate += 65
    lettercounter += 1

currentboxposition = 0
currentwordnumber = 1
antispamsystem = 1
def functionwhenkeypressed(lettermade):
    global antispamsystem
    if len(lettersolvedlist) != 5 and antispamsystem == 1 and currentwordnumber < 7:
        global combodeleting; global currentboxposition; global clog
        antispamsystem = 0
        combodeleting = 0
        letterlist[currentboxposition].pencolor("white")
        letterlist[currentboxposition].clear()
        letterlist[currentboxposition].write(alphabetlist[lettermade], font=font_setup)
        if len(userinputwordlist) < 5:
            userinputwordlist.append(str(alphabetlist[lettermade]))
        else:
            userinputwordlist.pop()
            userinputwordlist.append(str(alphabetlist[lettermade]))
        if (currentboxposition+1)%5 != 0 or currentboxposition == 0:
            currentboxposition+=1
            clog = 0
        else:
            clog = 1
        antispamsystem = 1
        warningmessage.clear()
def A():
    functionwhenkeypressed(lettermade=0)
def B():
    functionwhenkeypressed(lettermade=1)
def C():
    functionwhenkeypressed(lettermade=2)
def D():
    functionwhenkeypressed(lettermade=3)
def E():
    functionwhenkeypressed(lettermade=4)
def F():
    functionwhenkeypressed(lettermade=5)
def G():
    functionwhenkeypressed(lettermade=6)
def H():
    functionwhenkeypressed(lettermade=7)
def I():
    functionwhenkeypressed(lettermade=8)
def J():
    functionwhenkeypressed(lettermade=9)
def K():
    functionwhenkeypressed(lettermade=10)
def L():
    functionwhenkeypressed(lettermade=11)
def M():
    functionwhenkeypressed(lettermade=12)
def N():
    functionwhenkeypressed(lettermade=13)
def O():
    functionwhenkeypressed(lettermade=14)
def P():
    functionwhenkeypressed(lettermade=15)
def Q():
    functionwhenkeypressed(lettermade=16)
def R():
    functionwhenkeypressed(lettermade=17)
def S():
    functionwhenkeypressed(lettermade=18)
def T():
    functionwhenkeypressed(lettermade=19)
def U():
    functionwhenkeypressed(lettermade=20)
def V():
    functionwhenkeypressed(lettermade=21)
def W():
    functionwhenkeypressed(lettermade=22)
def X():
    functionwhenkeypressed(lettermade=23)
def Y():
    functionwhenkeypressed(lettermade=24)
def Z():
    functionwhenkeypressed(lettermade=25)
alreadysolved = 0
solvedletters = 0
greed = ""
solvedyes = 0
teddy = open("inputs.txt", "r")
y = teddy.readlines()
bug = 0
def checker():
    global solvedletters; global userinputwordlist; global currentboxposition; global currentwordnumber; global alreadysolved; global bug; global greed; global antispamsystem; global solvedyes
    if len(userinputwordlist) != 5 and currentwordnumber<7 and antispamsystem == 1 and solvedyes != 1:
        warningmessage.clear()
        warningmessage.write("Not enough letters", font = ("Impact", 15, "normal"))
    if currentboxposition == 4+(currentwordnumber-1)*5 and clog == 1 and currentwordnumber < 7 and antispamsystem == 1 and len(userinputwordlist) == 5:
        time1 = tmr.time()
        antispamsystem = 0
        greed = list(userinputwordlist)
        for e in range(5):
            greed[e] = greed[e].lower()
        greed.append("\n")
        bug = 0
        for line in y:
            kuh = list(line)
            if kuh == greed or ["z", "y", "m", "i", "c", "\n"] == greed:
                bug = 1
                teddy.close()
                break
        if bug == 0:
            teddy.close()
            warningmessage.write("Not in word list", font = ("Impact", 15, "normal"))
            antispamsystem = 1
        if bug == 1:
            yellow = "#D9AE3F"
            graysolve = "#303030"
            warningmessage.clear()
            global inputboxturtles; global solvedletters
            currentrow = (5*(currentwordnumber-1))
            for i in range(5):
                if userinputwordlist[i] == keyword[i]:
                    inputboxturtles[i+currentrow].color("green")
                    letterlist[i+currentrow].write(userinputwordlist[i], font = font_setup)
                    lettersolvedlist.append(keyword[i])
                    userinputwordlist[i] = "/"
            for b in range(5):
                if lettersolvedlist.count(userinputwordlist[b]) >= keyword.count(userinputwordlist[b]):
                    alreadysolved = 1
                if lettersolvedlist.count(userinputwordlist[b]) < keyword.count(userinputwordlist[b]):
                    lettersolvedlist.append(userinputwordlist[b])
                    alreadysolved = 0
                for l in range(5):
                    if userinputwordlist[b] == keyword[l] and b != l and alreadysolved == 0:
                        inputboxturtles[b+currentrow].color(yellow)
                        letterlist[b+currentrow].write(userinputwordlist[b], font = font_setup)
                if inputboxturtles[b+currentrow].fillcolor() == "black":
                    inputboxturtles[b+currentrow].color(graysolve)
                    letterlist[b+currentrow].write(userinputwordlist[b], font = font_setup)
            for a in range(5):
                if inputboxturtles[a+currentrow].fillcolor() == ("green"):
                    solvedletters += 1
            if solvedletters == 5:
                solvedyes = 1
                print("You Won")
                win.write("MECZ Achieved", font = font_setup)
            if solvedletters != 5:
                lettersolvedlist.clear()
            userinputwordlist.clear()
            greed.clear()
            solvedletters = 0
            currentboxposition += 1
            currentwordnumber+=1
            time2 = tmr.time()
            print(time2-time1)
            antispamsystem = 1
            if currentwordnumber > 6 and solvedletters != 5:
                warningmessage.write("The word was: " + keywordinletters, font = ("Impact", 15, "normal"))

def deleter():
    global antispamsystem; global combodeleting; global currentboxposition; global currentwordnumber
    if antispamsystem == 1 and currentwordnumber < 7:
        warningmessage.clear()
        antispamsystem = 0
        if currentboxposition == (currentwordnumber-1)*5:
            letterlist[currentboxposition].clear()
            userinputwordlist.clear()
        if 4+(currentwordnumber-1)*5 > currentboxposition >= 1+(currentwordnumber-1)*5 or currentboxposition == 4+(currentwordnumber-1)*5 and clog == 0 or currentboxposition == 4+(currentwordnumber-1)*5 and combodeleting != 0:
            currentboxposition -= 1
            letterlist[currentboxposition].clear()
            userinputwordlist.pop()
        if currentboxposition == 4+(currentwordnumber-1)*5 and combodeleting == 0 and clog == 1:
            letterlist[currentboxposition].clear()
            userinputwordlist.pop()
            combodeleting += 1
        antispamsystem = 1

wn.onkeypress(A, "a")
wn.onkeypress(B, "b")
wn.onkeypress(C, "c")
wn.onkeypress(D, "d")
wn.onkeypress(E, "e")
wn.onkeypress(F, "f")
wn.onkeypress(G, "g")
wn.onkeypress(H, "h")
wn.onkeypress(I, "i")
wn.onkeypress(J, "j")
wn.onkeypress(K, "k")
wn.onkeypress(L, "l")
wn.onkeypress(M, "m")
wn.onkeypress(N, "n")
wn.onkeypress(O, "o")
wn.onkeypress(P, "p")
wn.onkeypress(Q, "q")
wn.onkeypress(R, "r")
wn.onkeypress(S, "s")
wn.onkeypress(T, "t")
wn.onkeypress(U, "u")
wn.onkeypress(V, "v")
wn.onkeypress(W, "w")
wn.onkeypress(X, "x")
wn.onkeypress(Y, "y")
wn.onkeypress(Z, "z")
wn.onkeypress(checker, "Return")
wn.onkeypress(deleter, "BackSpace")
wn.listen()
wn.mainloop()