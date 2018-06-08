print("what is the name of player 1")
player1 = raw_input()
print("what is the name of player 2")
player2 = raw_input()
print("player 1 is " + player1)
print("player 2 is " + player2)


print("player 1 please select rock, paper, scissors")
answer = raw_input()
print("player 2 please selcet rock, paper, scissors")
answer2 = raw_input()


if answer == "paper" and answer2 == "scissors" :
    print("player 2 won this battle but not war")
elif answer == "paper" and answer2 == "rock":
    print("player 1 won this battle but not this war")
elif answer == "scissors" and answer2 == "rock":
     print("player 2 won this battle but not war")
elif answer == "paper" and answer2 == "paper":
    print("no one won this battle")
elif answer == "paper" and answer2 == "rock":
    print("player 1 won the war")

    print("congratulations")
