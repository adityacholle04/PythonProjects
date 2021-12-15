import random
if __name__ == '__main__':
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    name = input("Enter name of Player: ")
    userChoice = int(input("Enter 1.Rock 2.Paper 3.Scissor \n"))
    if userChoice not in [1, 2, 3]:
        print("Wrong Choice, You Lose")

    compChoice = random.randint(1, 3)
    gameImg = [rock,paper,scissors]

    print(f"{name} has selected: ")
    print(gameImg[userChoice])

    print("Computer has selected:")
    print(gameImg[compChoice])

    if user == comp:
        print("Draw")
    elif (user == 1 and comp == 2) or (user == 2 and comp == 3) or (user == 3 and comp == 2):
        print("Computer Win")
    elif (user == 1 and comp == 3) or (user == 2 and comp == 1) or (user == 3 and comp == 1):
        print(f"Player {name} Win")