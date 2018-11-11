# -*- coding: utf-8 -*-
"""
Spyder Editor
This will be a tic tac toe game
"""
import os
from random import randint

markers = ('X', 'O', 'V', 'Z')



"""
Function to center the content.
"""
def printx(data):
    print("\t\t\t" + data + "\t\t\t")

def print_tab(data):
    print("\t" + data + "\t")

def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')
    
"""
Function to display the Logo at top.
"""
def welcome():
    print("\t" + "="*60)
    print("\t\t\tWelcome to Tic-Tac-toe world")
    print("\t" + "="*60)
    print('\n\n')

"""
Function to display the board on command line
"""
def display_board(board, light_win_boxes = []):
 
    clrscr()
    
    if len(light_win_boxes) == 3:
        for pos in light_win_boxes:
            content = board[pos]
            board[pos] = '*' + content + '*'
            
    printx("      TIC TAC BOARD\n")
    printx('\t|\t|\t')
    printx('    ' + board[7] + '\t|   ' + board[8] + '\t|   ' + board[9])
    printx('\t|\t|\t')
    printx('  ' + '-'*21)
    printx('\t|\t|\t')
    printx('    ' + board[4] + '\t|   ' + board[5] + '\t|   ' + board[6])
    printx('\t|\t|\t')
    printx('  ' + '-'*21)
    printx('\t|\t|\t')
    printx('    ' + board[1] + '\t|   ' + board[2] + '\t|   ' + board[3])
    printx('\t|\t|\t')
    printx('\n')


def is_marker_valid(marker):
    if markers.count(marker) == 1:
        return True
    else:
        print("Symbol not available. Please choose again. ")
        return False

"""
Function to take input from stdin to 
choose the marker [ X/O ]
"""
def set_markers(no_of_players):
    
    while True:
        marker1 = str(input("Choose first player marker {markers}: ".format(markers=markers))).upper()
        if is_marker_valid(marker1):
            index_of_marker = markers.index(marker1)
            if no_of_players == 1:
                while True:
                    rand_number = randint(0, len(markers) - 1)
                    if rand_number == index_of_marker:
                        continue
                    marker2 = markers[rand_number]
                    break
            elif no_of_players == 2:
                while True:
                     marker2 = str(input("Choose second player marker {markers}: ".format(markers=markers))).upper()
                     if is_marker_valid(marker2):
                         break
                     else:
                         continue
            return {'player1': marker1, 'player2': marker2}
        else:
            continue


def show_the_rivals(p1, p2):
    
    print_tab("Player 1 --> {player1}".format(player1=p1))
    print_tab("Player 2 --> {player2}".format(player2=p2))


def player_input(board):
    while True:
        player_pos = input("Where do u wanna go mate ? [1-9]: ")
        if len(player_pos) == 1 and player_pos.isdigit():
            player_pos = int(player_pos)
            if player_pos > 0 and player_pos < 10:
                if validate_input(player_pos, board) == True:
                    return player_pos
                else:
                    clrscr()
                    print("Place already occupied")
                    display_board(board)
                    continue
            else:
                 print("Only 1 to 9 are allowed")
                 continue
        else:
            print("Invalid Input.")
            continue
    

def validate_input(player_input, board):
    if board[player_input] == "":
        return True
    else:
        return False

def is_board_full(board):
    
    for i in range(1, 10):
        if board[i] != '':
            if i == 9:  
                return True
            else:
                continue
        else:
            return False


def return_keys(winner, player, win_boxes = []):
    return {'winner': winner, 'player': player, 'win_boxes': win_boxes}


def check_for_winner(board, players):
    
    if board.count(players['player1']['marker']) >= 3 or board.count(players['player2']['marker']) >= 3:
        win_conditions = {
                '789':"board[7] == board[8] == board[9]",  # across the top
                '456':"board[4] == board[5] == board[6]",  # across the middle
                '123':"board[1] == board[2] == board[3]",  # across the boardttom
                '741':"board[7] == board[4] == board[1]",  # down the left side
                '852':"board[8] == board[5] == board[2]",  # down the middle
                '963':"board[9] == board[6] == board[3]",  # down the right side
                '753':"board[7] == board[5] == board[3]",  # diagonal
                '951':"board[9] == board[5] == board[1]"   # diagonal
                }
        
        for k, v in win_conditions.items():
                i1 = int(k[0])
                i2 = int(k[1])
                i3 = int(k[2])
                check = lambda i1,i2,i3:  board[i1] == board[i2] == board[i3] != ''
                if bool(v) == True and check(i1, i2, i3) == True:
                    if board[i1] == players['player1']['marker']:
                        return return_keys(True, players['player1'], [i1, i2, i3])
                    else:
                        return return_keys(True, players['player2'], [i1, i2, i3])
                else:
                    continue
        return return_keys(False, 'None')       
    else:
        return return_keys(False, 'None')



def winner(board, who_is_the_winner, players, win_boxes):
    clrscr()
    display_board(board, win_boxes)
    if who_is_the_winner == players['player1']:
        print("Player 1: {p1} is the Winner.!!!  Hoooraayyy".format(p1=players['player1']['marker']))
    else:
        print("Player 2: {p2} is the Winner.!!!  Hoooraayyy".format(p2=players['player2']['marker']))    
         
    
def take_your_turn(board, player):
    print("Player {player} turn: ".format(player=player['marker']))
    position = player_input(board)
    board[position] = player['marker']
    display_board(board)
    
    
def switch_off(players, player):
    players[player]['turn'] = False
    return players       
    
def switch_on(players, player):
    players[player]['turn'] = True
    return players       
    
          
def prepare_the_board():
    i = 1
    players = {}
    while i <= 2:
        key = 'player' + str(i)
        players[key] = {
                    'turn': False,
                    'marker': ''
                }
        i += 1
    return players   
 

def initialize(players, markers):
    i = 1
    while i <= len(players):
        if i == 1:
            players['player' + str(i)]['turn'] = True 
        players['player' + str(i)]['marker'] = markers['player' + str(i)]
        i += 1
    show_the_rivals(players['player1']['marker'], players['player2']['marker'])    
    return players    


def main(board, no_of_players):
    
    players = prepare_the_board()
    markers = set_markers(no_of_players)
    players = initialize(players, markers)
    gameover = False
    
    while gameover != True:
        is_there_a_winner = check_for_winner(board, players)
        if is_there_a_winner['winner'] == True:
            players = switch_off(players, 'player1')
            players = switch_off(players, 'player2')
            who_is_the_winner = is_there_a_winner['player']
            winner(board, who_is_the_winner, players, is_there_a_winner['win_boxes'])
            gameover = True
        else:
            if not is_board_full(board):
                
                for player, player_config in players.items():
                    if player_config['turn'] == True:
                        take_your_turn(board, players[player])
                        players = switch_off(players, player)
                    elif player_config['turn'] == False:    
                        players = switch_on(players, player)
            else:
                no_winner()
                gameover = True


def is_number(data):
    try:
        data = int(data)
        return True
    except ValueError:
        print('Not a number.')
        return False

def is_string(data):
    try:
        data = str(data)
        return True
    except ValueError:
        print("Not a string")
        return False
    
    
"""
start_game() function -> Asks whether to start the game or exit it
P/p ->  Play
E/e ->  Exit
"""                
def start_game():
    print_tab("Are you ready to play ?")
    print_tab("--------------------")
    print_tab("Enter: ")
    print_tab("P -> Play")
    print_tab("E -> Exit")
    wrong_option_counter = 0
    
    while True:
        if wrong_option_counter > wrong_options_max_limit:
            print_tab("Too many wrong tries\n") # If too many wrong tries, recurse the function
            start_game()
        
        choice = input().upper()   # Take input whether to start or exit
        if is_string(choice):
            if choice == 'P':
                return True
            elif choice == 'E':
                return False
            else:
                print_tab("Not a right option. Type again..\n")   
                wrong_option_counter += 1 
                continue
        else:
            wrong_option_counter += 1
            continue


"""
Take input from player. Whether 
1 -> they want to play against computer
2 -> with their buddy
"""
def how_many_players():
    while True:
        no_of_players = input("How many players ? 1 [with computer] or 2: ")
        if is_number(no_of_players) and int(no_of_players) in range(1,3):
            return int(no_of_players)
        else:
            print("Only 1 or 2 players can play.")
            continue


def no_winner():
   
    print("Interesting..! No Winner yet...")
    print("Go for it again savvy's")
    
    
def game_over():
    
    print("Thank you for playing the game...")
    print("See you next time....")        


def exit_game():
    print_tab("Exiting the Game...")
    print_tab("See you next time savvy!!!")


#=================================#
#------------Start----------------#
#=================================#

# Shows the welcome top panel
welcome()

# How many wrong tries are allowed ?
wrong_options_max_limit = 5


# Start the game
if start_game() == True:
    replay = 'Y'
    while replay == 'Y':
        no_of_players = how_many_players()    # how many will play 1 or 2
        
        board = [''] * 10               # Build the board
        display_board(board)            # Display the board
        main(board, no_of_players)
        
        # After main is over. Check for play again
        replay_input = input('Want to play again savvy ? ').upper()
        if is_string(replay_input) and replay_input in ['Y', 'N']:
            replay = replay_input
        else:
            replay = 'N'
    else:
        game_over()
else:
    exit_game()