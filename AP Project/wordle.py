import turtle as trtl
import random as rand
import time as tmr
import array as ary
wn = trtl.Screen()
wn.bgcolor("black")
x = open("answers.txt", "r")
realanswerindex = rand.randint(1, 2315)
answer = 0; counts = 0
b = x.readlines()
for line in b:
    counts+=1
    if counts == realanswerindex:
        answer = str(line)
        x.close()
        break
keyword = list(answer.upper())
if realanswerindex != 2315:
    keyword.pop()
keywordinletters = ""
for cuh in range(5):
    keywordinletters += keyword[cuh]
alphabetlist = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
inputboxturtles = []
letterlist = []
lettersolvedlist = []
font_setup = ("Impact", 30, "normal")
userinputwordlist = []
clog = 0
title = trtl.Turtle()
title.ht()
title.penup()
title.pencolor("#CEA65D")
title.goto(-55,200)
title.write("MECZ", font = ("Impact", 50, "normal"))
warningmessage = trtl.Turtle()
warningmessage.ht()
warningmessage.speed("fastest")
warningmessage.pu()
warningmessage.pencolor("white")
warningmessage.goto(-210, 220)
warningmessage.pd()
win = trtl.Turtle()
win.ht()
win.penup()
win.goto(-87,-255)
win.color("green")

# class b:
#     def __init__(self, name, secondname, number):
#         self.firstname = name
#         self.lastname = secondname
#         self.x = number
#     def test(self):
#         print("The player's first and last name is: \n" + self.firstname , self.lastname + "\n" + "And he has successfully solved:\n" + self.x , "words")
# tst = b("Wallace", "Wei", "5")
# tst.test()

turtlexcoordinate, turtleycoordinate = -130, 150
turtlecounter = 0
for turtle in range (30):
    if turtlecounter%5 == 0 and turtlecounter != 0:
        turtlexcoordinate = -130
        turtleycoordinate -= 65
    boxturtle = trtl.Turtle()
    boxturtle.speed("fastest")
    boxturtle.penup()
    boxturtle.shape("square")
    boxturtle.color("black")
    boxturtle.pencolor("#555555")
    boxturtle.shapesize(3)
    inputboxturtles.append(boxturtle)
    inputboxturtles[turtlecounter].goto(turtlexcoordinate, turtleycoordinate)
    turtlexcoordinate += 65
    turtlecounter += 1

turtlexcoordinate, turtleycoordinate = -135, 133
lettercounter = 0

for l in range (30):
    if lettercounter%5 == 0 and lettercounter != 0:
        turtlexcoordinate = -135
        turtleycoordinate -= 65
    letterturtle = trtl.Turtle()
    letterturtle.ht()
    letterturtle.speed("fastest")
    letterturtle.penup()
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
        global currentboxposition; global clog
        antispamsystem = 0
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
greed = ""
solvedyes = 0
teddy = open("inputs.txt", "r")
y = teddy.readlines()
bug = 0

def yellowboxes(list, rowcounter, solvedlist, letter, box):
   if list == ["/", "/", "/", "/", "/"]:
       print("You Won")
       win.write("MECZ Achieved", font = ("Impact", 30, "normal"))
   else:
        index = rowcounter
        for b in list:
            if solvedlist.count(b) < keyword.count(b):
                box[index].color("#D9AE3F") 
                letter[index].write(b, font = ("Impact", 30, "normal"))
                solvedlist.append(b)
            if box[index].fillcolor() == "black":
                box[index].color("#303030") 
                letter[index].write(b, font = ("Impact", 30, "normal"))
            index += 1
        solvedlist.clear()

def checker():
    global userinputwordlist; global currentboxposition; global currentwordnumber; global bug; global greed; global antispamsystem; global solvedyes
    if len(userinputwordlist) != 5 and currentwordnumber<7 and antispamsystem == 1 and solvedyes != 1:
        warningmessage.clear()
        warningmessage.write("Not enough letters", font = ("Impact", 15, "normal"))
    if currentwordnumber < 7 and antispamsystem == 1 and len(userinputwordlist) == 5:
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
            global inputboxturtles
            currentrow = (5*(currentwordnumber-1))
            for i in range(5):
                if userinputwordlist[i] == keyword[i]:
                    inputboxturtles[i+currentrow].color("green")
                    letterlist[i+currentrow].write(keyword[i], font = font_setup)
                    lettersolvedlist.append(keyword[i])
                    userinputwordlist[i] = "/"
            yellowboxes(userinputwordlist, currentrow, lettersolvedlist, letterlist, inputboxturtles)
            userinputwordlist.clear()
            greed.clear()
            currentboxposition+=1
            currentwordnumber+=1
            antispamsystem = 1
            time2 = tmr.time()
            print(time2-time1)
            warningmessage.clear()
            if currentwordnumber > 6:
                warningmessage.write("The word was: " + keywordinletters, font = ("Impact", 15, "normal"))

def deleter():
    global antispamsystem; global currentboxposition; global currentwordnumber
    if antispamsystem == 1 and currentwordnumber < 7:
        antispamsystem = 0
        if 5>len(userinputwordlist)>=1:
            currentboxposition -= 1
            letterlist[currentboxposition].clear()
            userinputwordlist.pop()
        if len(userinputwordlist) == 5:
            letterlist[currentboxposition].clear()
            userinputwordlist.pop()
        antispamsystem = 1
        warningmessage.clear()

wn.onkeypress(A, "a")
wn.onkeypress(A, "A")
wn.onkeypress(B, "b")
wn.onkeypress(B, "B")
wn.onkeypress(C, "c")
wn.onkeypress(C, "C")
wn.onkeypress(D, "d")
wn.onkeypress(D, "D")
wn.onkeypress(E, "e")
wn.onkeypress(E, "E")
wn.onkeypress(F, "f")
wn.onkeypress(F, "F")
wn.onkeypress(G, "g")
wn.onkeypress(G, "G")
wn.onkeypress(H, "h")
wn.onkeypress(H, "H")
wn.onkeypress(I, "i")
wn.onkeypress(I, "I")
wn.onkeypress(J, "j")
wn.onkeypress(J, "J")
wn.onkeypress(K, "k")
wn.onkeypress(K, "K")
wn.onkeypress(L, "l")
wn.onkeypress(L, "L")
wn.onkeypress(M, "m")
wn.onkeypress(M, "M")
wn.onkeypress(N, "n")
wn.onkeypress(N, "N")
wn.onkeypress(O, "o")
wn.onkeypress(O, "O")
wn.onkeypress(P, "p")
wn.onkeypress(P, "P")
wn.onkeypress(Q, "q")
wn.onkeypress(Q, "Q")
wn.onkeypress(R, "r")
wn.onkeypress(R, "R")
wn.onkeypress(S, "s")
wn.onkeypress(S, "S")
wn.onkeypress(T, "t")
wn.onkeypress(T, "T")
wn.onkeypress(U, "u")
wn.onkeypress(U, "U")
wn.onkeypress(V, "v")
wn.onkeypress(V, "V")
wn.onkeypress(W, "w")
wn.onkeypress(W, "W")
wn.onkeypress(X, "x")
wn.onkeypress(X, "X")
wn.onkeypress(Y, "y")
wn.onkeypress(Y, "Y")
wn.onkeypress(Z, "z")
wn.onkeypress(Z, "Z")
wn.onkeypress(checker, "Return")
wn.onkeypress(deleter, "BackSpace")
wn.listen()
wn.mainloop()