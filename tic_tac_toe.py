x1y3 = "_"
x2y3 = "_"
x3y3 = "_"
x1y2 = "_"
x2y2 = "_"
x3y2 = "_"
x1y1 = " "
x2y1 = " "
x3y1 = " "

row3 = [x1y3, x2y3, x3y3]
row2 = [x1y2, x2y2, x3y2]
row1 = [x1y1, x2y1, x3y1]

game = [row1, row2, row3]

col1 = [game[0][0], game[1][0], game[2][0]]
col2 = [game[0][1], game[1][1], game[2][1]]
col3 = [game[0][2], game[1][2], game[2][2]]

diagnol1 = [game[0][0], game[1][1], game[2][2]]
diagnol2 = [game[0][2], game[1][1], game[2][0]]

import random

random_num = random.randint(1,2)
if random_num == 1:
    playerO_turn = True
    playerX_turn = False
else:
    playerX_turn = True
    playerO_turn = False

import os

def clear():
    os.system('cls')

def board():
    clear()
    print(f"""
{game[2][0]}|{game[2][1]}|{game[2][2]}
{game[1][0]}|{game[1][1]}|{game[1][2]}
{game[0][0]}|{game[0][1]}|{game[0][2]}
""")

def check_win(P):
    global col1
    global col2
    global col3
    col1 = [game[0][0], game[1][0], game[2][0]]
    col2 = [game[0][1], game[1][1], game[2][1]]
    col3 = [game[0][2], game[1][2], game[2][2]]
    if game[0] == [P, P, P] or game[1] == [P, P, P] or game[2] == [P, P, P]: 
        return P
    elif game[0][0] == P and game[1][1] == P and game[2][2] == P:
        return P
    elif game[2][0] == P and game[1][1] == P and game[0][2] == P:
        return P
    elif col1 == [P, P, P] or col2 == [P, P, P] or col3 == [P, P, P]: 
        return P
    else:
        return False

def check_tie():
    global game
    if game[0][0] != " " and game[0][1] != " " and game[0][2] != " " and game[1][0] != "_" and game[1][1] != "_" and game[1][2] != "_" and game[2][0] != "_" and game[2][1] != "_" and game[2][2] != "_":
        return True
    else:
        return False

def move_input(P):
    global game
    invalid_input = True
    while True:
        input1 = input(f"Q to quit.  What row would you like to put a {P} in: ").strip()
        if input1.lower() == "q":
            return "q"
        input2 = input("what column would you like to put your symbol in: ").strip()
        if input1.isdigit() == True and input2.isdigit() == True:
            input1 = int(input1)
            input2 = int(input2)
            if input1 > 0 and input1 <= 3 and input2 > 0 and input2 <= 3:
                input1 = "y"+str(input1)
                input2 = "x"+str(input2)
                full_input = f"{input2}{input1}"
                if full_input == "x1y1":
                    if game[0][0] == " ":
                        game[0][0] = P
                        invalid_input = False
                        return game
                elif full_input == "x2y1":
                    if game[0][1] == " ":
                        game[0][1] = P
                        return game
                elif full_input == "x3y1":
                    if game[0][2] == " ":
                        game[0][2] = P
                        invalid_input = False
                        return game
                elif full_input == "x1y2":
                    if game[1][0] == "_":
                        game[1][0] = P
                        invalid_input = False
                        return game
                elif full_input == "x2y2":
                    if game[1][1] == "_":
                        game[1][1] = P
                        invalid_input = False
                        return game
                elif full_input == "x3y2":
                    if game[1][2] == "_":
                        game[1][2] = P
                        invalid_input = False
                        return game
                elif full_input == "x1y3":
                    if game[2][0] == "_":
                        game[2][0] = P
                        invalid_input = False
                        return game
                elif full_input == "x2y3":
                    if game[2][1] == "_":
                        game[2][1] = P
                        invalid_input = False
                        return game
                elif full_input == "x3y3":
                    if game[2][2] == "_":
                        game[2][2] = P
                        invalid_input = False
                        return game
                else:
                    print("invalid input")
            else:
                print("invalid input")
        else:
            print("invalid input")
        if invalid_input == False:
            break

def play_again():
    global game
    global win
    global tie
    user = input("input y to play again: ").strip()
    if user.lower() == "y":
        game [2][2] = "_"
        game [2][1] = "_"
        game [2][0] = "_"
        game [1][2] = "_"
        game [1][1] = "_"
        game [1][0] = "_"
        game [0][2] = " "
        game [0][1] = " "
        game [0][0] = " "
        win = False
        tie = False
        return game
    else:
        return False

def check_for_lose(P):
    x = random.randint(1,3)
    y = random.randint(1,3)
    axis = f"x{x}y{y}"
    global game
    global col1
    global col2
    global col3
    global diagnol1
    global diagnol2
    diagnol1 = [game[0][0], game[1][1], game[2][2]]
    diagnol2 = [game[0][2], game[1][1], game[2][0]]
    move_found = False
    if game[0] == [P, P, " "] or game[0] == [P, " ", P] or game[0] == [" ", P, P]:
        if game[0][0] == " ":
            axis = "x1y1"
        elif game[0][1] == " ":
            axis = "x2y1"
        elif game[0][2] == " ":
            axis = "x3y1"
        move_found = True
    elif game[1] == [P, P, "_"] or game[1] == [P, "_", P] or game[1] == ["_", P, P]:
        if game[1][0] == "_":
            axis = "x1y2"
        elif game[1][1] == "_":
            axis = "x2y2"
        elif game[1][2] == "_":
            axis = "x3y2"
        move_found = True
    elif game[2] == [P, P, "_"] or game[2] == [P, "_", P] or game[2] == ["_", P, P]:
        if game[2][0] == "_":
            axis = "x1y3"
        elif game[2][1] == "_":
            axis = "x2y3"
        elif game[2][2] == "_":
            axis = "x3y3"
        move_found = True
    elif col1 == [P, P, "_"] or col1 == [P, "_", P] or col1 == [" ", P, P]:
        if game[0][0] == " ":
            axis = "x1y1"
        elif game[1][0] == "_":
            axis = "x1y2"
        elif game[2][0] == "_":
            axis = "x1y3"
        move_found = True
    elif col2 == [P, P, "_"] or col2 == [P, "_", P] or col2 == [" ", P, P]:
        if game[0][1] == " ":
            axis = "x2y1"
        elif game[1][1] == "_":
            axis = "x2y2"
        elif game[2][1] == "_":
            axis = "x2y3"
        move_found = True
    elif col3 == [P, P, "_"] or col3 == [P, "_", P] or col3 == [" ", P, P]:
        if game[0][2] == " ":
            axis = "x3y1"
        elif game[1][2] == "_":
            axis = "x3y2"
        elif game[2][2] == "_":
            axis = "x3y3"
        move_found = True
    elif diagnol1 == [P, P, "_"] or diagnol1 == [P, "_", P] or diagnol1 == [" ", P, P]:
        if game[0][0] == " ":
            axis = "x1y1"
        elif game[1][1] == "_":
            axis = "x2y2"
        elif game[2][2] == "_":
            axis = "x3y3"
        move_found = True
    elif diagnol2 == [P, P, "_"] or diagnol2 == [P, "_", P] or diagnol2 == [" ", P, P]:
        if game[0][2] == " ":
            axis = "x3y1"
        elif game[1][1] == "_":
            axis = "x2y2"
        elif game[2][0] == "_":
            axis = "x1y3"
        move_found = True
    if move_found == True:
        return axis
    else:
        return False

def easy_computer():
    global game
    chosen = False
    while True:
        x = random.randint(1,3)
        y = random.randint(1,3)
        axis = f"x{x}y{y}"
        if axis == "x1y1" and game[0][0] == " ":
            game[0][0] = "O"
            chosen = True
            return game
        elif axis == "x2y1" and game[0][1] == " ":
            game[0][1] = "O"
            chosen = True
            return game
        elif axis == "x3y1" and game[0][2] == " ":
            game[0][2] = "O"
            chosen = True
            return game
        elif axis == "x1y2" and game[1][0] == "_":
            game[1][0] = "O"
            chosen = True
            return game
        elif axis == "x2y2" and game[1][1] == "_":
            game[1][1] = "O"
            chosen = True
            return game
        elif axis == "x3y2" and game[1][2] == "_":
            game[1][2] = "O"
            chosen = True
            return game
        elif axis == "x1y3" and game[2][0] == "_":
            game[2][0] = "O"
            chosen = True
            return game
        elif axis == "x2y3" and game[2][1] == "_":
            game[2][1] = "O"
            chosen = True
            return game
        elif axis == "x3y3" and game[2][2] == "_":
            game[2][2] = "O"
            chosen = True
            return game
        else:
            tie = check_tie()
            if tie == True:
                return "tie"
            if chosen == True:
                break

def medium_computer():
    global game
    global col1
    global col2
    global col3
    global diagnol1
    global diagnol2
    diagnol1 = [game[0][0], game[1][1], game[2][2]]
    diagnol2 = [game[0][2], game[1][1], game[2][0]]
    chosen = False
    while True:
        axis = check_for_lose("X")
        axis = check_for_lose("O")
        if axis == False:
            x = random.randint(1,3)
            y = random.randint(1,3)
            axis = f"x{x}y{y}"
        if axis == "x1y1" and game[0][0] == " ":
            game[0][0] = "O"
            chosen = True
            return game
        elif axis == "x2y1" and game[0][1] == " ":
            game[0][1] = "O"
            chosen = True
            return game
        elif axis == "x3y1" and game[0][2] == " ":
            game[0][2] = "O"
            chosen = True
            return game
        elif axis == "x1y2" and game[1][0] == "_":
            game[1][0] = "O"
            chosen = True
            return game
        elif axis == "x2y2" and game[1][1] == "_":
            game[1][1] = "O"
            chosen = True
            return game
        elif axis == "x3y2" and game[1][2] == "_":
            game[1][2] = "O"
            chosen = True
            return game
        elif axis == "x1y3" and game[2][0] == "_":
            game[2][0] = "O"
            chosen = True
            return game
        elif axis == "x2y3" and game[2][1] == "_":
            game[2][1] = "O"
            chosen = True
            return game
        elif axis == "x3y3" and game[2][2] == "_":
            game[2][2] = "O"
            chosen = True
            return game
        else:
            tie = check_tie()
            if tie == True:
                return "tie"
            if chosen == True:
                break

def hard_computer():
    global game
    global col1
    global col2
    global col3
    global diagnol1
    global diagnol2
    diagnol1 = [game[0][0], game[1][1], game[2][2]]
    diagnol2 = [game[0][2], game[1][1], game[2][0]]
    while True:
        move_found = check_for_lose("O")
        if move_found == False:
            move_found = check_for_lose("X")
        if move_found == False:    
            if game[1][1] == "O":
                if game[2][2] == "_":
                    axis = "x3y3"
                if game[2][2] == "O":
                    axis = "x3y2"
            elif game[1][1] == "X":
                corner = random.randint(1,4)
                if corner == 1:
                    axis = "x1y1"
                elif corner == 2:
                    axis = "x3y1"
                elif corner == 3:
                    axis = "x1y3"
                else:
                    axis = "x3y3"
            elif game[1][1] == "_":
                axis = "x2y2"
        else:
            axis = move_found
        if axis == "x1y1" and game[0][0] == " ":
            game[0][0] = "O"
            chosen = True
            return game
        elif axis == "x2y1" and game[0][1] == " ":
            game[0][1] = "O"
            chosen = True
            return game
        elif axis == "x3y1" and game[0][2] == " ":
            game[0][2] = "O"
            chosen = True
            return game
        elif axis == "x1y2" and game[1][0] == "_":
            game[1][0] = "O"
            chosen = True
            return game
        elif axis == "x2y2" and game[1][1] == "_":
            game[1][1] = "O"
            chosen = True
            return game
        elif axis == "x3y2" and game[1][2] == "_":
            game[1][2] = "O"
            chosen = True
            return game
        elif axis == "x1y3" and game[2][0] == "_":
            game[2][0] = "O"
            chosen = True
            return game
        elif axis == "x2y3" and game[2][1] == "_":
            game[2][1] = "O"
            chosen = True
            return game
        elif axis == "x3y3" and game[2][2] == "_":
            game[2][2] = "O"
            chosen = True
            return game
        else:
            tie = check_tie()
            if tie == True:
                return "tie"
            if chosen == True:
                break

user_input = ""
tie = False
win = False

user = input("Q to quit.  Do you want to play against a computer (c) or yourself (y): ").strip()
if user.lower == "c":
    user_input = input("(e) for easy, (m) for medium, and (h) for hard mode of the computer: ").strip()
    
while True:
    if user.lower() != "y" and user.lower() != "c" and user.lower() != "q":
        user = input("Q to quit.  Do you want to play against a computer (c) or yourself (y): ").strip()
    if game == "q":
        break
    if user.lower() == "q":
        break
    elif user.lower() == "y" and win == False and tie != True:
        if tie == True or game == "tie":
            tie = True

        elif playerO_turn == True:
            game = move_input("O")
            if game == "q":
                break
            board()
            win = check_win("O")
            tie = check_tie()
            playerO_turn = False
            playerX_turn = True
        elif playerX_turn == True:
                game = move_input("X")
                if game == "q":
                    break
                board()
                win = check_win("X")
                tie = check_tie()
                playerO_turn = True
                playerX_turn = False
    elif user.lower() == "c":
        board()
        if user_input == "e" or user_input == "m" or user_input == "h":
            pass
        else:
            user_input = input("Q to quit.  (e) for easy, (m) for medium, and (h) for hard mode of the computer: ").strip()
        if user_input.lower() == "q":
                    break
        elif user_input.lower() == "e" and win == False and tie == False:
            if playerO_turn == True and win == False and tie == False:
                easy_computer()
                board()
                win = check_win("O")
                tie = check_tie()
                playerO_turn = False
                playerX_turn = True
            if playerX_turn == True and win == False and tie == False:
                game = move_input("X")
                if game == "q":
                    break
                board()
                win = check_win("X")
                tie = check_tie()
                playerO_turn = True
                playerX_turn = False
        elif user_input.lower() == "m" and win == False and tie == False:
            if playerO_turn == True and win == False and tie == False:
                medium_computer()
                board()
                win = check_win("O")
                tie = check_tie()
                playerO_turn = False
                playerX_turn = True
            if playerX_turn == True and win == False and tie == False:
                game = move_input("X")
                if game == "q":
                    break
                board()
                win = check_win("X")
                tie = check_tie()
                playerO_turn = True
                playerX_turn = False
        elif user_input.lower() == "h" and win == False and tie == False:
            if playerO_turn == True and win == False and tie == False:
                hard_computer()
                board()
                win = check_win("O")
                tie = check_tie()
                playerO_turn = False
                playerX_turn = True
            if playerX_turn == True and win == False and tie == False:
                game = move_input("X")
                if game == "q":
                    break
                board()
                win = check_win("X")
                tie = check_tie()
                playerO_turn = True
                playerX_turn = False
        else:
            print("invalid input")
            user_input = input("(e) for easy, (m) for medium, and (h) for hard mode of the computer: ").strip()
    if win != False or tie == True:
        game = play_again()
    if game == False:
        break
if user.lower() == "y" and win != False:
    print(f"player {win} wins!")
elif  user.lower() == "c" and win != False:
    if win == "O":
        print("Computer Wins!")
    else:
        print("Player Wins!")
else:
    print("Tie Game!")