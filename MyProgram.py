import sys

user1 = input("what's your name? ")
user2 = input("And your name? ")

user1_answer = input(user1 + ", do you choose rock, paper, or scissors?")
user2_answer = input(user2 + ", do you choose rock, paper, or scissors?")

def compare(a1, a2):
    if a1 == a2:
        return("It's a tie!")

    elif a1 == "rock":
        if a2 == "scissors":
            return("Rock wins!")
        else:
            return("Paper wins!")

    elif a1 == "scissors":
        if a2 == "paper":
            return("Scissors wins!")
        else:
            return("Rock wins!")

    elif a1 == "paper":
        if a2 == "rock":
            return("Paper wins!")
        else:
            return("Scissors wins!")
    else:
        return("Invalid input! Please enter rock, paper, or scissors and try again!")
        sys.exit()

print( compare(user1_answer, user2_answer) )