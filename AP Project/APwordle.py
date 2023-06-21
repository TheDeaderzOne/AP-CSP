import turtle as trtl
import random as rand
wn = trtl.Screen()
wn.bgcolor("black") 
randomnumber0to4 = rand.randint(0,4)  
wordlist = [["T", "R", "E", "A", "D"], ["S", "T", "O", "R", "E"], ["B", "E", "R", "E", "T"], ["P", "L", "A", "I", "D"], ["M", "A", "T", "C", "H"]]
keyword = wordlist[randomnumber0to4] 
#Uses the random integer to pick one of the words listified from the wordlist to use as the answer.

alphabetlist = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] 

#a list of all the 26 letters used as the inputs for this game 

hints = ["Gadsden Flag", "Shopping", "Used by Military", "Pattern", "Title Meaning"] #list of hints used to help the user guess the word

coloredinputboxes = [] #list that eventually stores the 30 panels. 

letterturtles = [] #list that stores 30 letters that display what the user types. 

solvedletterslist = [] #list that records solved letters, whether yellow or green

userinputtedwordlist = [] #a list of the 5 letter word that the user inputs 

clog = 0 #this variable distinguishes between the 4th and 5th box position
#when clog = 0 it is considered to be the fourth box, when clog = 1 it is considered to be the fifth box both in conjunction with currentboxposiiton == 4. 


#creates the hint turtle, which gives the users hints
hint = trtl.Turtle()
hint.ht()
hint.pencolor("#4B9CD3")
hint.penup()
hint.goto(180,0)

#creates the win turtle, which displays the win message if the user wins
win = trtl.Turtle()
win.penup()
win.ht()
win.goto(-54,-250)
win.color("green")

turtlexcoordinate, turtleycoordinate = -130, 150 #these two variables are the coordinates of the panels

turtlecounter = 0 #variable that tracks the amount of turtles made

#this for loop makes the 30 panels in the game. 

for boxes in range(30):
    if turtlecounter%5 == 0 and turtlecounter != 0: #resets it so that it makes six rows of five boxes, where they form a rectangle
        turtlexcoordinate = -130
        turtleycoordinate -= 65
    #inputbox is each individual panel, which is made 30 times in this for loop. 
    inputbox = trtl.Turtle()
    inputbox.speed("fastest")
    inputbox.penup()
    inputbox.shape("square")
    inputbox.color("black")
    inputbox.pencolor("white")
    inputbox.shapesize(3)
    coloredinputboxes.append(inputbox) #appends the newly made panel into the list of panels
    coloredinputboxes[turtlecounter].goto(turtlexcoordinate, turtleycoordinate) #this takes the new panel, and puts it at specific coordinates to form the grid
    turtlexcoordinate += 65 #65 units right for box to form grid
    turtlecounter += 1

turtlexcoordinate, turtleycoordinate = -135, 133 #the coordinates at which the letters will be placed at

lettercounter = 0 #variable that tracks the amount of letters made

#this makes letter slots, which are the slots that the user can type in
for letterbox in range(30):
    if lettercounter%5 == 0 and lettercounter != 0: #resets to makes six rows of five letter slots for the user to type in. 
        turtlexcoordinate = -135
        turtleycoordinate -= 65
    #letterslot makes all the letter slots with all its characteristics 
    letterslot = trtl.Turtle()
    letterslot.ht()
    letterslot.speed("fastest")
    letterslot.penup()
    letterslot.color("black")
    letterturtles.append(letterslot) #appends the newly made letterslot into a list of these slots
    letterturtles[lettercounter].goto(turtlexcoordinate, turtleycoordinate) #puts the letterslot at a specific position
    turtlexcoordinate += 65 #65 units right for panel to form grid
    lettercounter += 1 

currentboxposition = 0 #tracks the current position of the letter slot that the user is on 
 
currentwordnumber = 1 #tracks how many words the user has inputted

antispamsystem = 1 #variable to ensure that the functions do not override each other and cause errors 

#the function below is the parent function for all the functions that occur when a certain key is pressed. 

def functionwhenkeypressed(lettermade):
    global antispamsystem
    #this "if" statement ensures that the function will not cause errors in overflow, only type 5 letter word, and not go beyond the 6th row
    if len(solvedletterslist) != 5 and antispamsystem == 1 and currentwordnumber < 7:
        global currentboxposition; global clog
        antispamsystem = 0

        letterturtles[currentboxposition].pencolor("white") 

        letterturtles[currentboxposition].clear() #makes sure the user's view will not be obstructed by previous letters

        letterturtles[currentboxposition].write(alphabetlist[lettermade], font=("Impact", 30, "normal"))
        #at the current position, it writes the letter as specified by alphabetlist[lettermade], where lettermade is an integer

        if len(userinputtedwordlist) < 5: ##if the length of the word that the user has typed is less than 5 letters, then .. 
            userinputtedwordlist.append(str(alphabetlist[lettermade])) #the letter will be appended on to the letterlist 

        else: #if the length of the word is 5 letters, then 
            userinputtedwordlist.pop() #it will pop the letter currently at the fifth spot
            userinputtedwordlist.append(str(alphabetlist[lettermade])) #and append the new letter

        if (currentboxposition+1)%5 != 0 or currentboxposition == 0:
            #if the currentboxposition is not in the 5th box for each word, then the user will be able to type on the next box, if not, then they will not move on from the box
            currentboxposition+=1
            clog = 0 
        else:
            clog = 1
        antispamsystem = 1 

#creates functions based on the above function template for each letter a - z by changing the value of lettermade

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



solvedletters = 0 #checks how many letters in the 5 letter word

#when enter or return is pressed, the checker function is activated

#the function checks if the user solved the word, and changes the color of the boxes to give the user information on their word

#yellow means that the letter is in the word but in the wrong spot, green indicates that the letter is in the correct spot, and gray means that the letter is not in the word

def yellowboxes(list, rowcounter, solvedlist, letter, box):
    if list == ["/", "/", "/", "/", "/"]:
        print("You Won") #the terminal says that the player won
        win.write("You Won", font = ("Impact", 30, "normal")) #the screen displays that the player has won 
    elif list != ["/", "/", "/", "/", "/"]:
        index = rowcounter
        for b in list:
            if solvedlist.count(b) < keyword.count(b): #if not enough letters of a specific kind have been counted as solved or yellowed in comparison to the real word, then ...
                box[index].color("#F6BE00") #the box will turn yellow
                letter[index].write(b, font = ("Impact", 30, "normal"))
                solvedlist.append(b) #the letter is appended into the solvedletterslist 

            if box[index].fillcolor() == "black": #if the colored boxes are still black after this whole process, then ... 
                box[index].color("#303030") #the boxes are turned to gray to indicate that the letter is not present in the word
                letter[index].write(b, font = ("Impact", 30, "normal"))
            index += 1
        solvedlist.clear()

def checker():
    global solvedletters; global currentboxposition; global currentwordnumber
    #the "if" condition below ensures that the word that the user inputted is actually 5 words
    if len(userinputtedwordlist) == 5:
        currentrow = (5*(currentwordnumber-1)) #tracks the current row that the user is on 
        for i in range(5): 
            if userinputtedwordlist[i] == keyword[i]:
                #if the letters do correspond, then ... 
                coloredinputboxes[i+currentrow].color("green") #the box will turn green
                letterturtles[i+currentrow].write(userinputtedwordlist[i], font = ("Impact", 30, "normal"))
                solvedletterslist.append(keyword[i]) #the letter will be put in the solvedletterslist as solved
                userinputtedwordlist[i] = "/" #and the letter will be replaced by a / in the userinputtedwordlist so that it will can't be checked by other algorithms later on
        yellowboxes(userinputtedwordlist, currentrow, solvedletterslist, letterturtles, coloredinputboxes) #function with all its parameters

        userinputtedwordlist.clear() #the user's word list is cleared to make way for the next guess

        #the hint for the specific word is written
        hint.clear()
        hint.write(hints[randomnumber0to4], font = ("Impact", 15, "normal"))

        solvedletters = 0 #the amount of solved letters is reset to prepare for the user's next word
        currentboxposition += 1 #program allows the user to move on to the next word
        currentwordnumber+=1 

#A function that acts as a backspace button. 

def deleter():
    global antispamsystem; global currentboxposition; global currentwordnumber
    if antispamsystem == 1 and currentwordnumber < 7: #make sure program will nto overflow and not beyond 6th row
        antispamsystem = 0 
        #if the user's word is one to four letters long ... 
        if 5>len(userinputtedwordlist)>=1:
            currentboxposition -= 1 #go back one box
            letterturtles[currentboxposition].clear() #clear the letter
            userinputtedwordlist.pop() # pop the letter from the user's word list

        #if the user's word is 5 letters long ... 
        if len(userinputtedwordlist) == 5:
            letterturtles[currentboxposition].clear() # clear the letter
            userinputtedwordlist.pop() # pop the letter from the word list
        antispamsystem = 1

#these wn.onkeypress functions serve to trigger the respective letter functions once the key is pressed. 

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

wn.listen() #wn.listen forces the computer to listen to key inputs on the computer 
wn.mainloop() #wn.mainloop allows the program to function