import random

def choose():
    words = ["rainbow", "computer", "science", "programming", "mathematics", 
             "player", "condition", "reverse", "water", "board"]
    return random.choice(words)

def jumbled(word):
    return "".join(random.sample(word, len(word)))

def thank(pl1N, pl2N, p1, p2):
    print("\nFinal Scores:")
    print(f"{pl1N}: {p1}")
    print(f"{pl2N}: {p2}")
    print("Thanks for playing! Have a nice day!")

def play():
    pl1Name = input("Player 1, Please enter your name: ")
    pl2Name = input("Player 2, Please enter your name: ")
    
    pp1 = 0  # Player 1 score
    pp2 = 0  # Player 2 score
    turn = 0
    
    while True:
        picked_word = choose()
        qn = jumbled(picked_word)
        
        print("\nJumbled word:", qn)
        
        if turn % 2 == 0:
            print(f"{pl1Name}, it's your turn.")
            ans = input("What is on my mind? ").strip().lower()
            if ans == picked_word:
                pp1 += 1
                print(f"Correct! Your score: {pp1}")
            else:
                print(f"Better luck next time! The word was: {picked_word}")
        else:
            print(f"{pl2Name}, it's your turn.")
            ans = input("What is on my mind? ").strip().lower()
            if ans == picked_word:
                pp2 += 1
                print(f"Correct! Your score: {pp2}")
            else:
                print(f"Better luck next time! The word was: {picked_word}")

        # Ask if they want to continue
        c = input("Press 1 to continue, 0 to quit: ")
        if c == "0":
            thank(pl1Name, pl2Name, pp1, pp2)
            break
        
        turn += 1

play()
