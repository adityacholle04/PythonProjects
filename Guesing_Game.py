import random

art = '''
  ________                                   .__                                               
 /  _____/ __ __   ____   ______ ______ _____|__| ____    ____      _________    _____   ____  
/   \  ___|  |  \_/ __ \ /  ___//  ___//  ___/  |/    \  / ___\    / ___\__  \  /     \_/ __ \ 
\    \_\  \  |  /\  ___/ \___ \ \___ \ \___ \|  |   |  \/ /_/  >  / /_/  > __ \|  Y Y  \  ___/ 
 \______  /____/  \___  >____  >____  >____  >__|___|  /\___  /   \___  (____  /__|_|  /\___  >
        \/            \/     \/     \/     \/        \//_____/   /_____/     \/      \/     \/     
                               
'''

print(art)
turns = 0
number = random.randint(1, 100)
game_over = False
mode = input("Select mode Hard or Easy :")
if mode == "Hard" or mode == "hard":
    turns = 5
else:
    turns = 10
while not game_over:
    guess = int(input("Guess for a number between 1 and 100 :"))
    if number == guess:
        print("Player Win")
        game_over = True
        continue
    elif guess > number:
        print("Too high")
    else:
        print("Too low")
    print(f"Number of attempts left {turns - 1}")
    turns -= 1
    if turns == 0:
        game_over = True
