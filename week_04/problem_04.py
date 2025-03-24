#  Guess the movie name

#  req list of movie name 
import random
movies = ["Anand","Drishyam","Nayakan","Anbe Sivan","Gol Maal","Vikram Vedha","Black Friday","Dangal","Tare Zameen par"]
def play():
    p1Name = input("Player 1! Please enter your name: ")
    p2Name = input("Player 2! Please enter your name: ")
    pointOfP1 = 0
    pointOfP2 = 0
    turn = 0
    willing = True
    while(willing):
        if turn % 2 == 0:
            # return player 1
            print(p1Name,"Your Turn")
            pickedMovie = random.choice(movies)
            qn = create_Question(pickedMovie)
            print(qn)

            not_Said = True
            while not_Said:
                letter = input("Your letter: ")
                if (is_present(letter,pickedMovie)):

                     #  unlock
                else:
                    print(letter,"Not found")
        else:
            # player 2
         turn = turn+1
play()