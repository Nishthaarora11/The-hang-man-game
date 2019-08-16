
import csv
import random
stages =["_________       ",
        "|        |       ",
        "|        |      ",
        "|        |      ",
        "|        0      ",
        "|       /|\     ",
        "|        |     ",
        "|       / \     ",
        "|               "
        ]
print("\t\t\tWelcome to  game Hangman ")
print("\n\t***** How to play *******")
print("\nYou have to guess the name of the fruit, if u guess the name correct u win otherwise u loose ")
print("\t\t\t******** NOTE*********")
print("  PROTECT THE MAN FROM HANGING \n \n \t\tLIKE THIS \n")
print("\n".join(stages))
print("\n Lets begin the game\n ")


words = []
#read data from csv file
with open('fruits.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        words.extend(row)
        
        
random.shuffle(words)
answer1 = words[0]
answer = list(words[0])
display = []
used = []
guesslist = []
display.extend(answer)
used.extend(answer)

for i in range(len(display)):
    display[i]= "-"

print("You have to guess a fruit consisting of ",len(display),"characters\n ")
print(" ".join(display))
print()
count = 0
wrong = 1
#loop to guess the correct character
while count < len(answer) and wrong < len(stages):
    guess =  input(" Guess the element  ")
    guess = guess.lower()
    if guess  not in guesslist:
        guesslist.extend(guess)
        for i in range(len(answer)):
            if answer[i] == guess and guess in used :
                display[i] = guess
                count+=1
                used.remove(guess)
            continue
   
        if guess not in display :
            print("Sorry wrong guess\n ")
            print("\n".join(stages[0:wrong]))
            print("\n")
            print(" ".join(display))
            wrong +=1
            if wrong  == len(stages)-1:
                 print("Carefull if u enter 1 more wrong character u will loose\n ")
            continue
    else:
        print("\nYou already guess this character \nplease guess some different character\n")

    #display word        
    print(" ".join(display))
#to display whether u win or loose
if count == len(answer):
    print("\n well done, you guess the correct answer")
else:
    print("\n oops, you failed to find the correct answer")
    print("\n correct answer is ",answer1)
