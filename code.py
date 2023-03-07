print("-----------Welcome to the Game Rock, Paper, Scissor---------")
name1 =input("player1 enter your name:").capitalize()
user1 = input("player1 Enter your choice:").lower()
name2 =input("player2 Enter your name:").capitalize()
user2 = input("player2 Enter your choice:").lower()
if user1 == 'rock' and user2 == 'paper':
    print("winner:",name2)
elif user1 == 'scissor' and user2 == 'rock':
    print("Winner:",user2)
elif user1 == 'paper' and user2 == 'scissor':
    print("Winner:",name2)
elif user1 == 'paper' and user2 == 'rock':
    print("Winner:",name1)
elif user1 == 'rock' and user2 == 'scissor':
    print("Winner:",name1)
elif user1 == 'scissor' and user2 == 'paper':
    print("Winner:",name1)
elif user1 == user2:
    print("Draw")
else:
    ("Enter valid input---")
