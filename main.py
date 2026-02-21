import random
from colorama import init, Fore, Back
init(autoreset=False)

while True:
    game_size = int(input(Back.GREEN + "Enter grid size: "))

    game_field = []

    for i in range(game_size):
        game_field.append(["_"] * game_size)


    for row in game_field:
        print(row)

    current_player = "X"
    game_is_on = True


    while game_is_on:
        if current_player == "X":
            x = int(input(Back.BLUE + "Enter X: "))
            y = int(input(Back.YELLOW +"Enter Y: "))
        elif current_player == "0":
            print(Back.BLUE + "-"*20)
            x = random.randint(0, game_size - 1)
            y = random.randint(0, game_size - 1)
        if 0 <= x < game_size and 0 <= y < game_size:
            if game_field[x][y] == "_":
                game_field[x][y] = current_player
            else:
                print("Cell is already occupied")
                continue
        else:
            print("Wrong coords")
            continue

        # for i in range(game_size):
        #         if game_field[i][0] == current_player and game_field[i][1] == current_player and game_field[i][2] == current_player:
        #             print("You won")
        #             game_is_on = False
                    
        # for i in range(game_size):
        #         if game_field[0][i] == current_player and game_field[1][i] == current_player and game_field[2][i] == current_player:
        #             print("You won")
        #             game_is_on = False

        # rows
        for i in range(game_size):
            if all(game_field[i][j] == current_player for j in range(game_size)):
                print("You won")
                game_is_on = False
                break

        # columns
        for j in range(game_size):
            if all(game_field[i][j] == current_player for i in range(game_size)):
                print("You won")
                game_is_on = False
                break
        
        

        # 00 11 22
        need_to_win = 0
        for i in range(game_size): # 0 1 2
            if game_field[i][i] == current_player:
                need_to_win += 1
        if need_to_win == game_size:
            print("You won")
            game_is_on = False
        
        # 20 11 02                  0 1 2   2 1 0 
        need_to_win = 0
        for i in range(game_size): # 0 1 2
            if game_field[game_size - i - 1][i] == current_player:
                need_to_win += 1
        if need_to_win == game_size:
            print("You won")
            game_is_on = False

        for row in game_field:
            print(row)
        
        if current_player == "X":
            current_player = "0"
        elif current_player == "0":
            current_player = "X"
        

    answer = input("Do you want to play again? (y): ")
    if answer != "y":
        break
    else:
        continue