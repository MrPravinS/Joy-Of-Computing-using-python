import random

def choose():
    word=["rainbow","computer","science","programming","mathematics","player","condition","reverse","water","board"]
    pick = random.choice(word)
    return pick

def jumbled(word):
   jumble = "".join(random.sample(word,len(word)))
   return jumble

def thank(pl1N,pl2N,p1,p2):
    print("Your score is : ",p1)
    print("Your score is : ",p2)
    print("Thanks for playing")
    print("Have a nice day")
    

def play():
    pl1Name = input("Player 1, Please enter your name")
    pl2Name = input("Player 2, Please enter your Name")
    pp1 = 0
    pp2 = 0
    turn = 0
    while(1):
        #computers task 
        picked_word = choose()
        
        #create question
        qn = jumbled(picked_word)
        #player 1
        print(qn)
        if turn % 2 == 0:
            print(pl1Name,"Your turn. ")
            ans = input("What is on my mind")
            if ans == picked_word:
                pp1 = pp1 + 1
                print("Your score is: ",pp1)
            else:
                print("Better luck next time i thought :", picked_word)
                c = int(input("Press 1 to Continue and 0 to quit : "))
            if c == 0:
                thank(pl1Name,pl2Name,pp1,pp2)
                break
            #player 2
        else:
            print(pl2Name,"Your turn. ")
            ans = input("What is on my mind")
            if ans == picked_word:
                pp2 = pp2 + 1
                print("Your score is: ",pp2)
            else:
                print("Better luck next time i thought :", picked_word)
                c = int(input("Press 1 to Continue and 0 to quit : "))
            if c == 0:
                thank(pl1Name,pl2Name,pp1,pp2)
                break
        turn = turn + 1
play()