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
    user = int(input("Enter 1.Rock 2.Paper 3.Scissor \n"))
    comp = random.randint(1, 3)

    print(f"{name} has selected: ")
    if(user == 1):
        print(rock)
    elif(user == 2):
        print(paper)
    elif(user == 3):
        print(scissors)
    else:
        print("Wrong Choice")

    print("Computer has selected:")
    if(comp == 1):
        print(rock)
    elif(comp == 2):
        print(paper)
    elif(comp == 3):
        print(scissors)
    else:
        print("Wrong Choice")


    if user == 1 and comp == 1:
        print("Draw")
    elif user == 2 and comp == 2:
        print("Draw")
    elif user == 3 and comp == 3:
        print("Draw")
    elif user == 1 and comp == 2:
        print("Computer Win")
    elif user == 1 and comp == 3:
        print(f"Player {name} Win")
    elif user == 2 and comp == 1:
        print(f"Player {name} Win")
    elif user == 2 and comp == 3:
        print("Computer Win")
    elif user == 3 and comp == 1:
        print(f"Player {name} Win")
    elif user == 3 and comp == 2:
        print("Computer Win")