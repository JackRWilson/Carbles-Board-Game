# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:44:01 2024

@author: jackw
"""
_round = 1
card_values = {
"ace of hearts": 1, "ace of diamonds": 1, "ace of spades": 1, "ace of clubs": 1,
"2 of hearts": 2, "2 of diamonds": 2, "2 of spades": 2, "2 of clubs": 2,
"3 of hearts": 3, "3 of diamonds": 3, "3 of spades": 3, "3 of clubs": 3,
"4 of hearts": -4, "4 of diamonds": -4, "4 of spades": -4, "4 of clubs": -4,
"5 of hearts": 5, "5 of diamonds": 5, "5 of spades": 5, "5 of clubs": 5,
"6 of hearts": 6, "6 of diamonds": 6, "6 of spades": 6, "6 of clubs": 6,
"7 of hearts": 7, "7 of diamonds": 7, "7 of spades": 7, "7 of clubs": 7,
"8 of hearts": 8, "8 of diamonds": 8, "8 of spades": 8, "8 of clubs": 8,
"9 of hearts": 9, "9 of diamonds": 9, "9 of spades": 9, "9 of clubs": 9,
"10 of hearts": 10, "10 of diamonds": 10, "10 of spades": 10, "10 of clubs": 10,
"jack of hearts": 11, "jack of diamonds": 11, "jack of spades": 11, "jack of clubs": 11,
"queen of hearts": 12, "queen of diamonds": 12, "queen of spades": 12, "queen of clubs": 12,
"king of hearts": 13, "king of diamonds": 13, "king of spades": 13, "king of clubs": 13,
"joker": 0}


def rgb(r, g, b):
  """
  RGB text
  """
  return f"\033[38;2;{r};{g};{b}m"

# ----------------------------------------------------------------------------------------------------------------

def color(text, turn):
    """
    Creates colors for each player
    Takes a text input and a turn input (i.e. player1, player2...)
    Converts the text into that players color
    Returns the converted text
    """
    global colors
    
    red = rgb(255, 0, 0)
    blue = rgb(0, 150, 255)
    green = rgb(0, 255, 0)
    yellow = rgb(255, 255, 0)
    purple = rgb(211, 51, 255)
    orange = rgb(255, 120, 0)
    grey = rgb(105, 105, 105)
    reset = "\033[0m"
    
    colors = {"player1":red, 
              "player2":blue, 
              "player3":green, 
              "player4":yellow,
              "player5":purple,
              "player6":orange,
              "other":grey}
    
    if turn in colors:
        return f"{colors[turn]}{text}{reset}"
    else:
        print("ERROR")

# ----------------------------------------------------------------------------------------------------------------

def spaces_setup():
    """
    Creates colors based on the rgb function
    """
    global red, blue, green, yellow, purple, orange, reset
    red = rgb(255, 0, 0)
    blue = rgb(0, 150, 255)
    green = rgb(0, 255, 0)
    yellow = rgb(255, 255, 0)
    purple = rgb(211, 51, 255)
    orange = rgb(255, 120, 0)
    reset = "\033[0m"
    
    """
    Creates the all the spaces on the board represented with an o or x
    """
    global spaces, get_out
    spaces = {}
    
    for x in range(64):
        spaces[f'_{x}'] = "o"
    
    spaces['_100'] = "o"
    
    get_out = {"player1":4,
               "player2":20,
               "player3":36,
               "player4":52}
    
    for x in get_out:
        spaces[f'_{get_out[x]}'] = color("x", x)

# ----------------------------------------------------------------------------------------------------------------

def jails_setup():
    """
    Creates the jails (starting positions)
    """
    global jails
    jails = {}
    
    for x in range(-1, -17, -1):
        if x >= -4 and x <= -1:
            spaces[f'_{x}'] = f"{red}x{reset}"
        elif x >= -8 and x <= -5:
            spaces[f'_{x}'] = f"{blue}x{reset}"
        elif x >= -12 and x <= -9:
            spaces[f'_{x}'] = f"{green}x{reset}"
        elif x >= -16 and x <= -13:
            spaces[f'_{x}'] = f"{yellow}x{reset}"
        else:
            print("ERROR")

# ----------------------------------------------------------------------------------------------------------------

def homes_setup():
    """
    Creates the home where the player wants to reach to win
    """
    global homes, space_before_home
    homes = {"player1":[65, 66, 67, 68],
             "player2":[69, 70, 71, 72],
             "player3":[73, 74, 75, 76],
             "player4":[77, 78, 79, 80]}
    
    space_before_home = {"player1":2,
                         "player2":18,
                         "player3":34,
                         "player4":50}
    
    for x in range(65, 81):
        if x >= 65 and x <= 68:
            spaces[f'_{x}'] = f"{red}+{reset}"
        elif x >= 69 and x <= 72:
            spaces[f'_{x}'] = f"{blue}+{reset}"
        elif x >= 73 and x <= 76:
            spaces[f'_{x}'] = f"{green}+{reset}"
        elif x >= 77 and x <= 80:
            spaces[f'_{x}'] = f"{yellow}+{reset}"
        else:
            print("ERROR")
            
# ----------------------------------------------------------------------------------------------------------------

def positions_setup(player_turn_cycle):
    """
    Creates the positions dictionary which stores the players positions
    Default starting positions go RBGY -1 to -16
    Prints the players marble at the correct position corresponding to the dictionary
    """
    global positions, default_positions
    
    if player_turn_cycle == 0:
        positions = {"player1":{"1":-1, "2":-2, "3":-3, "4":-4}, 
                     "player2":{"1":-5, "2":-6, "3":-7, "4":-8}, 
                     "player3":{"1":-9, "2":-10, "3":-11, "4":-12}, 
                     "player4":{"1":-13, "2":-14, "3":-15, "4":-16}}
        
        default_positions = {"player1":{"1":-1, "2":-2, "3":-3, "4":-4}, 
                             "player2":{"1":-5, "2":-6, "3":-7, "4":-8}, 
                             "player3":{"1":-9, "2":-10, "3":-11, "4":-12}, 
                             "player4":{"1":-13, "2":-14, "3":-15, "4":-16}}
    
    for player in positions:
        for pos in positions[player]:
            spaces[f'_{positions[player][pos]}'] = f"{color('●',player)}"
            if player_turn_cycle != 0:
                while True:
                    try:
                        if player == order[player_turn_cycle-1]:
                            spaces[f'_{positions[player][pos]}'] = f"{color(pos,player)}"
                            break
                        else:
                            break
                    except:
                        player_turn_cycle = 1
                        continue

# ---------------------------------------------------------------------------------------------------------------- 
   
def board():  
    """
    Creates the game board
    """
    print(f"""
                  {spaces['_0']} {spaces['_1']} {spaces['_2']} {spaces['_3']} {spaces['_4']}   {spaces['_-2']} {spaces['_-4']}
                  {spaces['_63']}   {spaces['_65']}   {spaces['_5']}   {spaces['_-1']} {spaces['_-3']}
                  {spaces['_62']}   {spaces['_66']}   {spaces['_6']}
      {spaces['_-16']} {spaces['_-15']}         {spaces['_61']}   {spaces['_67']}   {spaces['_7']}
      {spaces['_-14']} {spaces['_-13']}         {spaces['_60']}   {spaces['_68']}   {spaces['_8']}
                  {spaces['_59']}       {spaces['_9']}
      {spaces['_52']} {spaces['_53']} {spaces['_54']} {spaces['_55']} {spaces['_56']} {spaces['_57']} {spaces['_58']}       {spaces['_10']} {spaces['_11']} {spaces['_12']} {spaces['_13']} {spaces['_14']} {spaces['_15']} {spaces['_16']}
      {spaces['_51']}                               {spaces['_17']}
      {spaces['_50']} {spaces['_77']} {spaces['_78']} {spaces['_79']} {spaces['_80']}       {spaces['_100']}       {spaces['_72']} {spaces['_71']} {spaces['_70']} {spaces['_69']} {spaces['_18']}
      {spaces['_49']}                               {spaces['_19']}
      {spaces['_48']} {spaces['_47']} {spaces['_46']} {spaces['_45']} {spaces['_44']} {spaces['_43']} {spaces['_42']}       {spaces['_26']} {spaces['_25']} {spaces['_24']} {spaces['_23']} {spaces['_22']} {spaces['_21']} {spaces['_20']}
                  {spaces['_41']}       {spaces['_27']}
                  {spaces['_40']}   {spaces['_76']}   {spaces['_28']}         {spaces['_-5']} {spaces['_-6']}
                  {spaces['_39']}   {spaces['_75']}   {spaces['_29']}         {spaces['_-7']} {spaces['_-8']}
                  {spaces['_38']}   {spaces['_74']}   {spaces['_30']}
            {spaces['_-11']} {spaces['_-9']}   {spaces['_37']}   {spaces['_73']}   {spaces['_31']}
            {spaces['_-12']} {spaces['_-10']}   {spaces['_36']} {spaces['_35']} {spaces['_34']} {spaces['_33']} {spaces['_32']}
    """)

# ----------------------------------------------------------------------------------------------------------------

def player_select():
    """
    Selects the number of players
    """
    global number_of_players, num_board_spaces, order
    
    player_select = True
    while player_select == True:
        try:
            number_of_players = int(input("4 or 6 Players: "))
            if number_of_players == 4:
                num_board_spaces = 63
                order = ["player1", "player2", "player3", "player4"]
                player_select = False
                continue
            elif number_of_players == 6:
                num_board_spaces = 95
                order = ["player1", "player2", "player3", "player4", "player5", "player6"]
                player_select = False
                continue
            else:
                print("Invalid Input...")
        except ValueError:
            print("Invalid Input...")
            
# ----------------------------------------------------------------------------------------------------------------
            
def create_deck():
    """
    Creates the decks
    """
    import random
    
    if number_of_players == 4:
        global deck
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        deck = [(rank + " of " + suit) for rank in ranks for suit in suits]
        deck.append("Joker")
        deck.append("Joker")
        random.shuffle(deck)
    
    elif number_of_players == 6:
        global bigdeck
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        deck1 = [(rank + " of " + suit) for rank in ranks for suit in suits]
        deck2 = [(rank + " of " + suit) for rank in ranks for suit in suits]
        deck1.append("Joker")
        deck1.append("Joker")
        deck2.append("Joker")
        deck2.append("Joker")
        random.shuffle(deck1)
        random.shuffle(deck2)
        bigdeck = deck1 + deck2
        random.shuffle(bigdeck)
    else:
        print("ERROR")

    return number_of_players
       
# ----------------------------------------------------------------------------------------------------------------

def create_names():
    """
    Creates the players
    Players must have a unique name
    If the name is unique, it gets put in the list called players
    """
    global players, players_plus_names
    
    if number_of_players == 4:
        entered_names = []
        def unique_name(player_number):
            while True:
                # User inputs a name and the first letter gets capitalized so it looks nice
                player_name_input = input(f"Player {player_number} enter your name: ")
                player_name = player_name_input.capitalize()
    
                # Checks to see if player name was already entered
                if player_name not in entered_names:
                    entered_names.append(player_name)
                    return player_name
                else:
                    print("Name already exists. Please choose a different name.")
        
        # Sets the player names as variables and puts them in a list
        player1_name = unique_name(1)
        player2_name = unique_name(2)
        player3_name = unique_name(3)
        player4_name = unique_name(4)
        players = [player1_name, player2_name, player3_name, player4_name]
        players_plus_names = {'player1':player1_name, 
                              'player2':player2_name, 
                              'player3':player3_name, 
                              'player4':player4_name}
    
    elif number_of_players == 6:
        entered_names = []
        def unique_name(player_number):
            while True:
                # User inputs a name and the first letter gets capitalized so it looks nice
                player_name_input = input(f"Player {player_number} enter your name: ")
                player_name = player_name_input.capitalize()
    
                # Checks to see if player name was already entered
                if player_name not in entered_names:
                    entered_names.append(player_name)
                    return player_name
                elif not player_name:
                    continue
                else:
                    print("Name already exists. Please choose a different name.")
        
        # Sets the player names as variables and puts them in a list
        player1_name = unique_name(1)
        player2_name = unique_name(2)
        player3_name = unique_name(3)
        player4_name = unique_name(4)
        player5_name = unique_name(5)
        player6_name = unique_name(6)
        players = [player1_name, player2_name, player3_name, player4_name, player5_name, player6_name]
        players_plus_names = {'player1':player1_name, 
                              'player2':player2_name, 
                              'player3':player3_name, 
                              'player4':player4_name, 
                              'player5':player5_name, 
                              'player6':player6_name}
    else:
        print("ERROR")
    
    return players

# ----------------------------------------------------------------------------------------------------------------

def rounds(_round):
    """
    Defines how many cards are dealt to each player depending on the round and number of players
    """
    global cards, rounds_to_play, turns_to_play
    
    if number_of_players == 4:
        cards = [5, 4, 4]
        rounds_to_play = 3
        
        if _round == 1:
            turns_to_play = 5
        else:
            turns_to_play = 4
        
    elif number_of_players == 6:
        cards = [5, 5, 4, 4]
        rounds_to_play = 4
        
        if _round == 1 or _round == 2:
            turns_to_play = 5
        else:
            turns_to_play = 4
            
    if _round > rounds_to_play:
        _round = 1
    
    return rounds_to_play, turns_to_play

# ----------------------------------------------------------------------------------------------------------------

def create_hands(_round):
    """
    Creates players hands
    """
    global hands
    
    hands = {player: [] for player in players}
    
    for x in range(cards[_round-1]):
        for player in players:
            if number_of_players == 4:
                card = deck.pop()
            elif number_of_players == 6:
                card = bigdeck.pop()
            hands[player].append(card)

# ----------------------------------------------------------------------------------------------------------------

def display_hands(player_turn_cycle, text = "a"):
    """
    Print each players hands
    Want to display just 1 hand at a time eventually
    """
    global hands, hand
    
    # Displays all hands
    if text == "a":
        for player, hand in hands.items():
            
            # Prints the players name
            print(color(player, f"player{players.index(player)+1}") + "'s hand:")
            
            # Goes through each card and shows the index and card
            for index, card in enumerate(hand, start = 1):
                
                # Converts card to lower and gets its value
                card_lower = card.lower()
                card_value = card_values.get(card_lower, "Invalid Card")
                
                valid_list = []
                # Goes through each marble and tests if the card is a valid move for that marble
                for pos in positions[order[players.index(player)]]:
                    
                    if valid_move(order[players.index(player)], pos, card_value) == True:
                        valid_list.append(True)
                    else:
                        valid_list.append(False)
                
                # If the card is valid for at least one of the marbles, will show that card as white
                if True in valid_list:
                    print(f"{index})", card)
                # Otherwise will show the card as grey  
                else:
                    print(color(f"{index}) {card}", "other"))
            print()
    
    # Displays one hand
    elif text == "o":
        # Initiates variables
        player = players[player_turn_cycle - 1]
        hand = hands[player]
       
        # Prints the players name
        print(color(player, f"player{players.index(player)+1}") + "'s hand:")
        
        # Goes through each card and shows the index and card
        for index, card in enumerate(hand, start = 1):
            
            # Converts card to lower and gets its value
            card_lower = card.lower()
            card_value = card_values.get(card_lower, "Invalid Card")
            
            valid_list = []
            # Goes through each marble and tests if the card is a valid move for that marble
            for pos in positions[order[players.index(player)]]:
                
                if valid_move(order[players.index(player)], pos, card_value) == True:
                    valid_list.append(True)
                else:
                    valid_list.append(False)
            
            # If the card is valid for at least one of the marbles, will show that card as white
            if True in valid_list:
                print(f"{index})", card)
            # Otherwise will show the card as grey  
            else:
                print(color(f"{index}) {card}", "other"))
        print()
    
# ----------------------------------------------------------------------------------------------------------------

def trade_cards():
    """
    Trades cards with partner
    """
    for player_name in players:
        while True:
            try:
                # Gets user trading card input
                user_trading_card_input = input(f"{player_name} pick a card to give your partner: ")
                
                # Make sure user input is a digit
                if not user_trading_card_input.isdigit():
                    print("Invalid input. Please choose a valid number.")
                    continue
                
                # Converts input into an integer
                user_trading_card = int(user_trading_card_input)

                if number_of_players == 4: # Partners are: 1&3, 2&4
                    # Make sure input isnt 5 or 6 depending on the round
                    if _round == 1 and user_trading_card == 6 or _round >=2 and user_trading_card == 5:
                        print("Invalid number. Please choose a valid number.")
                        continue

                    # Ensure card is in hand
                    if 1 <= user_trading_card <= len(hands[player_name]):
                        trading_card = hands[player_name].pop(user_trading_card - 1)
                        
                        # Determines partner's index based on player number
                        partner_index = (players.index(player_name) + 2) % 4
                        partner_name = players[partner_index]
                    else:
                        print("Invalid number. Please choose a valid number.")
                        continue            
                    
                elif number_of_players == 6: # Partners are: 1&4, 2&5, 3&6
                    # Make sure input isnt 5 or 6 depending on the round
                    if _round <= 2 and user_trading_card == 6 or _round <= 3 and user_trading_card == 5:
                        print("Invalid number. Please choose a valid number.")
                        continue 

                    # Ensure card is in hand
                    if 1 <= user_trading_card <= len(hands[player_name]):
                        trading_card = hands[player_name].pop(user_trading_card - 1)

                        # Determines partner's index based on player number
                        partner_index = (players.index(player_name) + 3) % 6
                        partner_name = players[partner_index]
                    else:
                        print("Invalid number. Please choose a valid number.")
                        continue

                # Add the card to the partner's hand
                hands[partner_name].append(trading_card)
                print(f"{player_name} gave {trading_card} to {partner_name}.")
                break

            except IndexError:
                print("Invalid card selection. Please choose a valid card from your hand.")

# ----------------------------------------------------------------------------------------------------------------

def replace_spaces(player, marble_input):
    """
    Replaces spaces moved with the corresponding board piece
    """
    # If a player moved from a get out position, updates that with an 'x' otherwise updates normal spaces with an 'o'
    if positions[player][marble_input] == 4:
        spaces['_4'] = color('x', 'player1')
    elif positions[player][marble_input] == 20:
        spaces['_20'] = color('x', 'player2')
    elif positions[player][marble_input] == 36:
        spaces['_36'] = color('x', 'player3')
    elif positions[player][marble_input] == 52:
        spaces['_52'] = color('x', 'player4')
    elif positions[player][marble_input] < 0:
        spaces[f'_{positions[player][marble_input]}'] = color('x', f'{player}')
    elif positions[player][marble_input] in [65, 66, 67, 68]:
        spaces[f'_{positions[player][marble_input]}'] = color('+', 'player1')
    elif positions[player][marble_input] in [69, 70, 71, 72]:
        spaces[f'_{positions[player][marble_input]}'] = color('+', 'player2')
    elif positions[player][marble_input] in [73, 74, 75, 76]:
        spaces[f'_{positions[player][marble_input]}'] = color('+', 'player3')
    elif positions[player][marble_input] in [77, 78, 79, 80]:
        spaces[f'_{positions[player][marble_input]}'] = color('+', 'player4')
    else:
        spaces[f'_{positions[player][marble_input]}'] = 'o'

# ----------------------------------------------------------------------------------------------------------------

def update_position(player, marble, player_turn_cycle, card_value, selected_card, status = "normal"):
    """
    Adds the card value to the players position
    """
    player_name = players_plus_names[player]
    moved = False
    
    # If the players plays a get out card
    if status == "out":
        positions[player][marble] = get_out[player]
        # Changes the jail spot back to an x and prints a message
        spaces[f'_{default_positions[player][marble]}'] = color('x',player)
        print(f"{player_name} played {selected_card} and got out of their jail!")
        moved = True
    
    # If the player uses a joker to get their partner out
    elif status == "partner":
        # Finds the corresponding partner
        partner = order[(order.index(player) + int(number_of_players / 2)) % number_of_players]
        # Goes through each of the partners marbles and moves the first one out
        for pos in positions[partner]:
            if positions[partner][pos] < 0:
                positions[partner][pos] = get_out[partner]
                print(f"{player_name} played {selected_card} and got {players_plus_names[partner]} out of their jail!")
                break
                moved = True
    
    # If the player plays anything else
    elif status == "normal":
        
        # Middle. Card value is subtracted by 1 when leaving middle
        middle, card_value = middle_space(player, marble, card_value, player_turn_cycle, selected_card)
        # If the player goes to the middle, skips everything else
        if middle == True:
            moved = True
            return moved
    
        # Makes a temporary list with all the positions between the current player position and where they will land
        step = 1
        in_between_list = []
        if card_value == -4:
            step = -1
        temp_mover_position = positions[player][marble]
        for x in range(abs(card_value)):
            temp_mover_position = (temp_mover_position + step) % (num_board_spaces + 1)
            in_between_list.append(temp_mover_position)

        # Home movement. Going into home and in home movement
        home = home_movement(player, marble, card_value)
        if home == True:
            moved = True
            return moved
        
        # Normal movment
        positions[player][marble] = in_between_list[-1]
        moved = True

            
    return moved
    
# ----------------------------------------------------------------------------------------------------------------

def home_movement(player, marble, card_value):
    """
    Initiates home movement
    """
    # Initiates variable
    home = False
    starting_home_position = homes[player][0] - 1
    
    # Makes a temporary list with all the positions between the current player position and where they will land
    step = 1
    if card_value == -4:
        step = -1
    in_between_list = []
    temp_mover_position = positions[player][marble]
    for x in range(abs(card_value)):
        temp_mover_position = (temp_mover_position + step) % (num_board_spaces + 1)
        in_between_list.append(temp_mover_position)
    if card_value == -4:
        return home
    
    # Checks if the marble is close to their home and that their landing position isnt the space before home (messes up validation)
    elif (space_before_home[player] in in_between_list or space_before_home[player] == positions[player][marble]) and in_between_list[-1] != space_before_home[player]:
        
        # If the player is right on top of their space before home, just assign the card value since it is right there
        if positions[player][marble] == space_before_home[player]:
            distance_in_home = card_value
        else:
            distance_in_home = len(in_between_list[in_between_list.index(space_before_home[player]) + 1:])

        # Creates a second list
        in_between_list = []
        temp_mover_position = starting_home_position
        for x in range(distance_in_home):
            temp_mover_position = (temp_mover_position + 1)
            in_between_list.append(temp_mover_position)
    
        # Home landing tracks where in the home the player will land
        home_landing = starting_home_position + distance_in_home
        positions[player][marble] = home_landing     
        home = True
    
    # Checks if the player is in their home
    elif positions[player][marble] in homes[player]:
        
        # Creates a second list
        in_between_list = []
        temp_mover_position = positions[player][marble]
        for x in range(card_value):
            temp_mover_position = (temp_mover_position + 1)
            in_between_list.append(temp_mover_position)
        
        # Home landing tracks where in the home the player will land
        home_landing = positions[player][marble] + card_value
        positions[player][marble] = home_landing        
        home = True
    
    return home

# ----------------------------------------------------------------------------------------------------------------

def middle_space(player, user_marble_input, card_value, player_turn_cycle, selected_card):
    """
    Controls going to the middle position
    
    Controls going out of the middle position
    """
    global middle_letters_pos, middle_letter_input
    
    # Initiates variables and lists
    middle = False
    middle_letters_pos = {'a':[58], 
                          'b':[10], 
                          'c':[26], 
                          'd':[42]}
    middle_letters = ['a', 'b', 'c', 'd']
    spaces_changed = []
    
    # Changes the step based on the card value
    step = 1
    if card_value == -4:
        step = -1
    
    # Creates a temporary list with the next <card value> positions
    in_between_list = []
    temp_mover_position = positions[player][user_marble_input]
    for x in range(abs(card_value)):
        temp_mover_position = (temp_mover_position + step) % (num_board_spaces + 1)
        in_between_list.append(temp_mover_position)
    
    # Creates a dictionary which has the letter and if its valid or not
    valid_lane_list = middle_lane_check(player, user_marble_input, card_value)
    for letter in valid_lane_list:
        
        # For each letter, changes a strip on the board to those letters
        for x in range(5):
            middle_letters_pos[letter].append(middle_letters_pos[letter][x] + step)
            
    try:
        # If the player is already on the middle position
        if positions[player][user_marble_input] == 100:
            for letter in middle_letters_pos:
                # If the lane is invalid, skips it
                if valid_lane_list[letter] == False:
                    continue
                for pos in middle_letters_pos[letter]:
                    
                    # Changes the strip to the corresponding letter and skips spots with players on them
                    if spaces[f'_{pos}'] != 'o':
                        continue
                    else:
                        spaces_changed.append(pos)
                        spaces[f'_{pos}'] = color(letter, "other")
            
            # Makes sure marble appears properly on the middle spot
            positions_setup(player_turn_cycle)
            
            # Shows the board
            print()
            print("--------------------------------------------")
            print()
            print()
            print()
            print()
            print()
            board()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print("--------------------------------------------")
            print()
            
            # Player selects column to go down by picking a letter
            while True:
                middle_letter_input = input("Which lane do you want to go down?: ")
                
                # Restarts if user picks an invalid letter
                if middle_letter_input not in middle_letters:
                    print("Invalid letter. Please choose a valid letter.")
                    continue
                if valid_lane_list[middle_letter_input] == False:
                    print("Invalid letter. Please choose a valid letter.")
                    continue
                
                # Sets the players position to the first spot in the row they chose
                positions[player][user_marble_input] = middle_letters_pos[middle_letter_input][0]
                
                # Lowers the card value by 1 because of the previous move off of the middle spot
                card_value = card_value - step
                
                # Changes the spaces back to the board pieces
                for pos in spaces_changed:
                    spaces[f'_{pos}'] = "o"
                
                # Changes the middle space back
                spaces['_100'] = "o"
                
                break
        
        # If the player will land directly on the middle spot
        elif (card_value != -4 and in_between_list[-1] in [11, 27, 43, 59]) or (card_value == -4 and in_between_list[-1] in [9, 25, 41, 57]):
            while True:
                try:
                    # Lets the user decide whether to go to the middle or continue on
                    middle_option_input = int(input("Middle (1) or continue (2)?: "))
                    
                    # If the player decides to go to the middle, sets their position to 100 and changes middle to True
                    if middle_option_input == 1:
                        positions[player][user_marble_input] = 100
                        middle = True
                        break
                    
                    # If the player decides to continue, breaks and doesn't do anything
                    elif middle_option_input == 2:
                        break
                    
                    # If the player doesn't pick ibe if the two options will show and error and have them try again
                    else:
                        print("Invalid number. Please choose a valid number.")
                        continue
               
                except ValueError:
                    print("Invalid number. Please choose a valid number.")
    
    # If the player plays a -4 raises an IndexError in the in_between_list[-1]
    except IndexError:
        return middle, card_value
    
    return middle, card_value

# ----------------------------------------------------------------------------------------------------------------

def joker_played(player, player_turn_cycle):
    """
    Controls Joker play
    
    Gets self or partner out
    """
    # Initiates lists
    player_jail = []
    partner_jail = []
    
    # Finds the players partner
    partner = order[(order.index(player) + int(number_of_players / 2)) % number_of_players]

    # Creates the two lists that hold the players and partners marbles that are still in jail
    for pos in positions[player]:
        if positions[player][pos] < 0:
            player_jail.append(pos)
    for pos in positions[partner]:
        if positions[partner][pos] < 0:
            partner_jail.append(pos)   

    # If the player already has all their marbles out, automatically picks partner
    if player_jail == [] and partner_jail != []:
        joker_choice = 2
    # If the partner already has all their marbles out, automaticcaly picks player
    elif player_jail != [] and partner_jail == []:
        joker_choice = 1
    # If both players have all their marbles out, will burn it
    elif player_jail == [] and partner_jail == []:
        joker_choice = 3
    # If they both still have marbles in jail, lets the player choose
    else:
        while True:
            try:
                joker_choice = int(input("Get your self out (1) or partner out (2)?: "))
                if joker_choice not in [1, 2]:
                    print("Invalid number. Please choose a valid number.")
                else:
                    break
            except ValueError:
                print("Invalid number. Please choose a valid number.")

    # 1 is get self out, 2 is get partner out, 3 is burn
    if joker_choice == 1:
        replace_spaces(player, player_jail[0])
        update_position(player, player_jail[0], player_turn_cycle, 0, "Joker", "out")
        check_collision(player, player_turn_cycle, player_jail[0])
    elif joker_choice == 2:
        replace_spaces(partner, partner_jail[0])
        update_position(player, partner_jail[0], player_turn_cycle, 0, "Joker", "partner")
        check_collision(partner, player_turn_cycle, partner_jail[0])
    elif joker_choice == 3:
        print(f"{players_plus_names[player]} burns a Joker!")

# ----------------------------------------------------------------------------------------------------------------

def jack_played(player_turn_cycle, user_marble_input):
    """
    Switches or counts out if Jack is played
    """
    player = order[player_turn_cycle-1]
    while True:
        try:
            # If the player is in their home, breaks the loop
            if positions[player][user_marble_input] > 63 and positions[player][user_marble_input] < 100:
                break
            jack_input = int(input("Switch (1) or count out 11 (2)?: "))
            print()
            print("--------------------------------------------")
            print()
            print()
            print()
            print()
            print()
            
            # Decides to switch
            if jack_input == 1:
                
                # Creates temporary dictionaryies and lists
                # Holds the player name and marble number of possible players to switch
                jack_positions = {}
                
                # Holds the letters of the possible players to switch with
                jack_letters = []
                
                # Holds all possible options for letter inputs for a switch
                jack_options = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'r']
                jack_count = 0
                for jack_player in positions:
                    
                    # Holds the marble number and which letter its assigned
                    jack_pos = {}
                    for pos in positions[jack_player]:
                        
                        # Decides which marbles are valid to switch with
                        # Marble cant be in a jail or home, and cannot be the marble initiating the switch
                        if (0 <= positions[jack_player][pos] <= 63 or positions[jack_player][pos] == 100) and positions[jack_player][pos] != positions[player][user_marble_input]: 
                            
                            # Marble cant be on their own corresponding home
                            if (jack_player == 'player1' and positions['player1'][pos] == 4) or (jack_player == 'player2' and positions['player2'][pos] == 20) or (jack_player == 'player3' and positions['player3'][pos] == 32) or (jack_player == 'player4' and positions['player4'][pos] == 52):
                                continue
                            
                            # Assigns a letter to marbles that meet the specifications
                            jack_pos[pos] = jack_options[jack_count]
                            jack_positions[jack_player] = jack_pos
                           
                            jack_letters.append(jack_options[jack_count])
                            
                            spaces[f'_{positions[jack_player][pos]}'] = color(jack_options[jack_count], jack_player)
                            jack_count += 1
                            
                # If no marble meet the specifications
                if jack_positions == {}:
                    print("No one to switch with. Counting out...")
                    break
                
                # Prints the board
                board()
                print()
                print()
                print()
                print()
                print()
                print()
                print("--------------------------------------------")
                print()
                
                while True:
                    try:
                        # Takes input of which letter to switch with
                        jack_switch = input("Which marble do you want to switch with?: ")
                        
                        # Makes sure choice is a valid option
                        if jack_switch not in jack_letters:
                            print("Invalid letter. Please choose a valid letter.")
                            continue
                        
                        # Sets swap1 to the position of the marble initiating the trade
                        swap1 = positions[player][user_marble_input]
                        
                        for jack_player in jack_positions:
                            for pos in jack_positions[jack_player]:
                                if jack_switch == jack_positions[jack_player][pos]:
                                    
                                    # Sets swap2 to the position of the player being switched with
                                    swap2 = positions[jack_player][pos]
                                    
                                    # Updates position of the marble being switched with
                                    positions[jack_player][pos] = swap1
                                    print(f"{players_plus_names[player]} switched places with {players_plus_names[jack_player]}!")
                        
                        # Updates the position of the player doing the switch
                        positions[player][user_marble_input] = swap2
                        
                        # Chances the letters of the marbles not switched with back to a marble
                        for jack_player in positions:
                            for pos in positions[jack_player]:
                                if 0 <= positions[jack_player][pos] <= 63 and positions[jack_player][pos] != positions[player][user_marble_input] and positions[jack_player][pos] not in [4, 20, 36, 52]:
                                    spaces[f'_{positions[jack_player][pos]}'] = color('●', jack_player)
                        return jack_input
                        break
                    except ValueError:
                        print("Invalid letter. Please choose a valid letter.")
                break
            
            # If a Jack is chosen to count out instead of switching, breaks the loop
            elif jack_input == 2:
                return jack_input
                break
            else:
                print("Invalid number. Please choose a valid number.")
        except ValueError:
            print("Invalid number. Please choose a valid number.")
    
# ----------------------------------------------------------------------------------------------------------------

def seven_played_skips(mover_position, player_turn_cycle, user_marble_input, seven_number_input):
    """
    Checks if any marble is run over by a player playing a seven
    """
    # Set the movers name and position as their own variables
    mover = order[player_turn_cycle-1]
    mover_name = players[player_turn_cycle-1]
    
    # Tracks the positions in a temporary list
    in_between_list = []
    temp_mover_position = mover_position
    for x in range(seven_number_input):
        temp_mover_position = (temp_mover_position + 1) % (num_board_spaces + 1)
        in_between_list.append(temp_mover_position)
    
    print("skips", in_between_list)
    
    # If the marble is in its home, get rid of the list so it can't skip over people anymore
    if mover_position in homes[mover]:
        in_between_list = []
   
    if positions[mover][user_marble_input] == 100:
        del(in_between_list[-1])
    
    print("skips2", in_between_list)
    
    # If the space before home is in the temporary list, will delete all the values after it to ensure a player on get out doesn't die by accident when a player is entering their home
    if space_before_home[mover] in in_between_list:
        del(in_between_list[in_between_list.index(space_before_home[mover]) + 1:])

    for player in positions:
        for pos in positions[player]:
            
            # If the player is the mover, skips checking them otherwise they kill themselves
            if player == mover and pos == user_marble_input:
                continue
            
            if positions[player][pos] in in_between_list:
                
                # Sets the player that got skipped name
                skipped_name = players_plus_names[player]
                
                # Displays collision message
                print(f"{mover_name} skipped over {skipped_name}")
                
                # Sets the default homes for each players
                default_homes = {'player1': -1, 'player2': -5, 'player3': -9, 'player4': -13}
                
                # Sends the players that got landed on back to their home
                if player in default_homes:
                    replace_spaces(player, pos)
                    positions[player][pos] = default_homes[player] - (int(pos) - 1)
            
# ----------------------------------------------------------------------------------------------------------------

def seven_played_split(player_turn_cycle, selected_card, card_value):
    """
    Plays out a seven
    
    If the moving player jumps over another player, the player that got jumped over get sent back to jail
    
    Also deals with splitting of the seven
    """
    # Initiates lists and variables
    seven_progress = ['1', '2', '3', '4', '5', '6', '7']
    seven_options = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    mover = order[player_turn_cycle-1]
    
    while True:
        # Initializes variables
        players_changed = {}
        seven_count = 0
        
        # For all the marbles the user has on the board, they get turned into letters
        for pos in positions[mover]:
            if positions[mover][pos] >= 0 and positions[mover][pos] not in [68, 72, 76, 80]:
                
                # Sets the marble equal to a letter
                spaces[f'_{positions[mover][pos]}'] = color(seven_options[seven_count], mover)
                players_changed[seven_options[seven_count]] = pos
                seven_count += 1
                
        # If no marbles got turned to letters, break the loop
        if players_changed == {}:
            print(f"{players_plus_names[mover]} burns {selected_card}")
            break
        
        # Print the board with the new letters
        print()
        print("--------------------------------------------")
        print()
        print()
        print()
        print()
        print()
        board()
        print()
        print()
        
        
        # Create the seven progression bar
        print("Amount of 7 left to use:")
        print()
        print(' '.join(seven_progress))
        for full_counter in range(len(seven_progress)):
            print("■", end = ' ')
        for empty_counter in range(7 - len(seven_progress)):
            print("□", end = ' ')
        print()
        print()
        print("--------------------------------------------")
        print()
        
        # Take a letter input from the user and make sure its a valid letter
        while True:
            seven_letter_input = input("Enter the letter of the marble to move: ")
            
            # Prints an error if the letter in invalid
            if seven_letter_input not in players_changed.keys():
                print("Invalid letter. Please choose a valid letter.")
                continue
            break
        
        # Take a number input from the user and make sure its a valid number
        while True:
            try:
                seven_number_input = int(input("Enter the number of spaces to move: "))
                
                # Prints an error if the number is invalid
                if seven_number_input > len(seven_progress) or seven_number_input <= 0:
                    print(f"Invalid number. Please choose a number {len(seven_progress)} or less.")
                    continue 
                
                break
            except ValueError:
                print(f"Invalid input. Please choose a number {len(seven_progress)} or less.")
                continue
        
        # Initiates mover position before position is updated
        mover_position = positions[mover][players_changed[seven_letter_input]]
        
        # Puts the corresoponding board piece back when the player moves
        replace_spaces(mover, players_changed[seven_letter_input])
        

        # Update the players positions
        if update_position(mover, players_changed[seven_letter_input], player_turn_cycle, seven_number_input, selected_card) == False:
            print(f"{players_plus_names[mover]} burns {selected_card}!")
            break
        
        positions_setup(player_turn_cycle)
        
        # Checks for skips
        if mover_position == 100:
            seven_played_skips(middle_letters_pos[middle_letter_input][0] - 1, player_turn_cycle, players_changed[seven_letter_input], seven_number_input)
        else:
            seven_played_skips(mover_position, player_turn_cycle, players_changed[seven_letter_input], seven_number_input)
        
        # Check for collisions
        check_collision(mover, player_turn_cycle, players_changed[seven_letter_input])
        
        # Updates the progress bar for the next time around
        del seven_progress[len(seven_progress) - seven_number_input:]
        
        # Breaks the loop once the seven is all used up
        if len(seven_progress) == 0:
            for pos in players_changed.values():
                spaces[f'_{positions[mover][pos]}'] = color('●', mover)
            print(f"{players_plus_names[mover]} played {selected_card} and moved {card_value} spaces!")
            break
    
# ----------------------------------------------------------------------------------------------------------------

def check_collision(mover, player_turn_cycle, user_marble_input):
    """
    Checks if the player moving collides with any players
    """
    # Set the movers name and position as their own variables
    mover_name = players_plus_names[mover]
    mover_position = positions[mover][user_marble_input]
    
    # Check if the mover is in the same position as anyone else
    for player in positions:
        for pos in positions[player]:
            if mover == player and pos == user_marble_input:
                continue
            # If the mover is in the same position as a another marble
            if mover_position == positions[player][pos]:
                collision_name = players_plus_names[player]
                
                # Displays collision message
                print(f"{mover_name} collided with {collision_name}")
                
                # Sets the default homes for each players
                default_homes = {'player1': -1, 'player2': -5, 'player3': -9, 'player4': -13}
                
                # Sends the players that got landed on back to their home
                if player in default_homes:
                    positions[player][pos] = default_homes[player] - (int(pos) - 1)
                
                positions_setup(player_turn_cycle)
            
# ----------------------------------------------------------------------------------------------------------------

def player_turn(player_turn_cycle):
    
    # Initiates variables
    player = order[player_turn_cycle - 1]
    player_name = players_plus_names[player]
    
    
    valid_list = {}
    for card in hands[player_name]:    
        
        # Converts card to lower and gets its value
        card_lower = card.lower()
        card_value = card_values.get(card_lower, "Invalid Card")
        
        temp_valid_list = {}
        # Goes through each marble and checks if it has a valid play with that marble
        for pos in positions[player]:
            
            # Appends the results to the temporary valid list
            if valid_move(player, pos, card_value) == True:
                temp_valid_list[pos] = True
            else:
                temp_valid_list[pos] = False
        
        # Appends the overall results will all 4 marbles to the bigger valid list
        valid_list[card_lower] = temp_valid_list
    
    
    # Goes through the valid list and makes sure there is at least one possible play
    burning = True
    for card in valid_list:
        if True in valid_list[card].values():            
            # If there is at least one play, sets burning to False and breaks
            burning = False
            break
        
        
    # Starts the "go back" loop
    while True:
        back = False
        while True:
            try:
                # Card selection for movement
                user_card_input = int(input(f"{player_name} choose a card: "))
    
                # Checks to see if card is in hand
                if 1 <= user_card_input <= len(hands[player_name]):
                    selected_card = hands[player_name][user_card_input - 1]
                    selected_card_lower = selected_card.lower()
                    
                    # Converts the card into its value
                    card_value = card_values.get(selected_card_lower, "Invalid Card")
                    break
                else:
                    print("Invalid number. Please choose a valid number.")
                    
            except ValueError:
                print("Invalid number. Please choose a valid number.")
        
        while True:
            try:
                # Marble selection for movement    
                user_marble_input = input(f"{player_name} choose a marble: ")
                
                # If the user enters nothing for the input, will go back to the card selection
                if user_marble_input == "":
                    back = True
                    break
                
                # Converts the marble input into an int so it can be compared
                user_marble_input = int(user_marble_input)
                if 1 <= user_marble_input <= 4:
                    user_marble_input = str(user_marble_input)
                    
                    # Burns if the player has no playable cards
                    if burning == True:
                        print(f"{player_name} burns {selected_card}!")
                        break
                    
                    # Makes sure the player plays a valid play if they have one
                    if valid_list[selected_card_lower][user_marble_input] == False and burning == False:
                        back = True
                        print("Invalid play. Please choose a valid play.")
                        break
                    
                    # Checks if marble played is in jail and an out card is played. If so moves the marble out
                    if positions[player][user_marble_input] < 0 and card_value in [13, 1]:
                        update_position(player, user_marble_input, player_turn_cycle, card_value, selected_card, "out")
                    
                    # If a Joker is played
                    elif card_value == 0:
                        joker_played(player, player_turn_cycle)
                    
                    # If the marble played is not in jail, moves the marble the corresponding spaces
                    elif positions[player][user_marble_input] >= 0:
                        
                        # If a Jack is played
                        jack_input = 0
                        if card_value == 11:
                            jack_input = jack_played(player_turn_cycle, user_marble_input)
                        
                        # If a 7 is played
                        if card_value == 7:
                            seven_played_split(player_turn_cycle, selected_card, card_value)
                            break

                        replace_spaces(player, user_marble_input)
                        
                        # If a Jack was used to switch, skips adding the value to the players positions
                        if jack_input == 1:
                            break
                        
                        # Updates players position
                        if update_position(player, user_marble_input, player_turn_cycle, card_value, selected_card) == True:
                            print(f"{players_plus_names[player]} played {selected_card} and moved {card_value} spaces!")
                        
                        # Burns if move is invalid
                        else:
                            print(f"{player_name} burns {selected_card}!")
                        
                        # Checks for a collision
                        check_collision(player, player_turn_cycle, user_marble_input)
                        
                    break
                else:
                    print("Invalid number. Please choose a valid number.")
    
            except ValueError:
                print("Invalid number. Please choose a valid number.")
        
        # If the player entered nothing for the marble input, will restart at the card selection
        if back == True:
            continue
        # If not, gets rid of the card selected and continues
        else:
            hands[player_name].pop(user_card_input - 1)
            break

# ----------------------------------------------------------------------------------------------------------------

def valid_move(player, marble, card_value):
    """
    Checks if the players move is valid or not
    """
    valid_move = True
    
    # Creates a temporary list with positions of the next <card value> positions
    in_between_list = []
    temp_mover_position = positions[player][marble]
    for x in range(card_value):
        
        # If the player is on their space before home and doesn't play a joker
        if temp_mover_position == space_before_home[player]:
            if card_value > 0:
                temp_mover_position = homes[player][0] - 1
                temp_mover_position = (temp_mover_position + 1)
        
        # If the player is in their home will just add 1 and not divide by board spaces
        elif temp_mover_position > num_board_spaces:
            temp_mover_position = (temp_mover_position + 1)
        
        # Normal player position
        else:
            temp_mover_position = (temp_mover_position + 1) % (num_board_spaces + 1)
        
        # Appends that new position to the list
        in_between_list.append(temp_mover_position)
        
    # If a Joker is played
    if card_value == 0:
        valid_joker_choice = joker_check(player)
        valid_move = valid_joker_choice
    
    # If the player is in their jail
    elif positions[player][marble] < 0:
        valid_get_out = get_out_check(player, marble, card_value) 
        valid_move = valid_get_out
    
    # If the player plays a seven
    elif card_value == 7:
        valid_seven_movement = seven_movement_check(player)
        valid_move = valid_seven_movement
    
    # If the player is in the middle
    elif positions[player][marble] == 100:
        valid_middle_movement = middle_movement_check(player, marble, card_value)
        valid_move = valid_middle_movement
    
    # If the player is in their home
    elif 63 < positions[player][marble] < 100:
        valid_home_movement = home_movement_check(player, marble, card_value)
        valid_move = valid_home_movement
    
    # If the player is anywhere normally. Validates passing get out spot and home movement
    else:
        valid_home_movement = home_movement_check(player, marble, card_value)
        valid_pass_get_out = pass_get_out_check(player, marble, card_value)

        valid_move = all([valid_home_movement,
                         valid_pass_get_out])
    
    return valid_move

# ----------------------------------------------------------------------------------------------------------------

def seven_movement_check(player):
    """
    Checks if a seven can be fully used up 
    """
    # Initiates variables
    valid_move = True
    valid = True
    seven_count = 7
    
    # Goes through each marble for the player
    for pos in positions[player]:

        # Creates a few temp variables
        temp_mover_position = positions[player][pos]                
        step = 1
        valid = True
        
        # If the marble is in the jail, skips checking that one
        if temp_mover_position < 0:
            continue

        # Keeps adding 1 to the marbles position until it is invalid or the seven is all used up
        while seven_count > 0:

            # If the player is in the middle, will validate middle movement
            if temp_mover_position == 100:
                valid_middle_movement = middle_movement_check(player, pos, step)
                
                valid = valid_middle_movement
            
            # If the player is not in the middle, will validate like normal
            else:
                valid_home_movement = home_movement_check(player, pos, step)
                valid_pass_get_out = pass_get_out_check(player, pos, step)
                
                valid = all([valid_home_movement,
                             valid_pass_get_out])
            
            if valid == False:
                break
            
            seven_count -= 1
            step += 1
    
    # If there is still value left in the seven, will set the move as invalid
    if seven_count > 0:
        valid_move = False
    
    return valid_move

# ----------------------------------------------------------------------------------------------------------------

def middle_lane_check(player, marble, card_value):
    """
    Checks which lanes from the middle are valid
    """
    # Initiates variables
    valid_lane_list = {}
    middle_letters = ['a', 'b', 'c', 'd']
    
    # Goes through each row and tests if its a valid play, then creates a dictionary with the row label and if its valid
    for row in middle_letters:
        valid_lane = middle_movement_check(player, marble, card_value, row)
        valid_lane_list[row] = valid_lane
    
    return valid_lane_list

# ----------------------------------------------------------------------------------------------------------------

def middle_movement_check(player, marble, card_value, row = 'empty'):
    """
    Checks that movement from middle is valid
    """
    # Initiates variables
    valid_move = True
    middle_letters = ['a', 'b', 'c', 'd']
    previous_position = positions[player][marble]
    
    # Sets the corners different if the player plays a -4
    if card_value == -4:
        middle_corners = [59, 11, 27, 43]
    else:
        middle_corners = [57, 9, 25, 41]
    
    # If no row was set
    if row == 'empty':
        # Goes through each corner in the list and makes sure its valid
        for x in middle_corners:

            positions[player][marble] = x
            
            valid_home_movement = home_movement_check(player, marble, card_value)
            valid_pass_get_out = pass_get_out_check(player, marble, card_value)

            valid = all([valid_home_movement, 
                         valid_pass_get_out])
            
            # If at least one of the corner rows is valid, will break and set valid_move to True
            if valid == True:
                valid_move = True
                break
            else:
                valid_move = False
        
        # Puts the player back in the middle spot
        positions[player][marble] = previous_position
    
    # If a row was specified
    else:
        # Sets the players position to the corner of the corresponding row chosen and validates card
        positions[player][marble] = middle_corners[middle_letters.index(row)]
        
        valid_home_movement = home_movement_check(player, marble, card_value)
        valid_pass_get_out = pass_get_out_check(player, marble, card_value)

        valid = all([valid_home_movement, 
                     valid_pass_get_out])
        
        # If the card is a valid play, will set valid_move to True, otherwise it will be false
        if valid == True:
            valid_move = True
        else:
            valid_move = False
        
        # Puts the player back in the middle
        positions[player][marble] = previous_position

    return valid_move

# ----------------------------------------------------------------------------------------------------------------

def home_movement_check(player, marble, card_value):
    """
    Checks if home movement is valid
    """
    # Initiates variables
    valid_move = True
    starting_home_position = homes[player][0] - 1
    
    # Makes a temporary list with all the positions between the current player position and where they will land
    in_between_list = []
    temp_mover_position = positions[player][marble]
    for x in range(card_value):
        temp_mover_position = (temp_mover_position + 1) % (num_board_spaces + 1)
        in_between_list.append(temp_mover_position)
    
    # Checks if the player plays a -4 and is in their home
    if card_value == -4 and positions[player][marble] in homes[player]:
        valid_move = False
        return valid_move
    
    # Checks if the marble is close to their home
    if space_before_home[player] in in_between_list or space_before_home[player] == positions[player][marble]:
        
        # If the player is right on top of their space before home, just assign the card value since it is right there
        if positions[player][marble] == space_before_home[player]:
            distance_in_home = card_value
        else:
            distance_in_home = len(in_between_list[in_between_list.index(space_before_home[player]) + 1:])

        # Creates a second list
        in_between_list = []
        temp_mover_position = starting_home_position
        for x in range(distance_in_home):
            temp_mover_position = (temp_mover_position + 1)
            in_between_list.append(temp_mover_position)
    
        # Home landing tracks where in the home the player will land
        home_landing = starting_home_position + distance_in_home

        if home_landing in homes[player]:
            try:
                # Goes through all the positions in the list and check if there is a player on any of them
                for y in in_between_list:
                    
                    # If there is will set move to invalid
                    if y in positions[player].values():
                        valid_move = False
            
            except IndexError:
                print("TOO FAR")
    
        # If the home landing is farther than the last spot in the home, will burn the card
        elif home_landing > homes[player][-1]:
            valid_move = False
    
    # Checks if the player is in their home
    elif positions[player][marble] in homes[player]:
        
        # Creates a second list
        in_between_list = []
        temp_mover_position = positions[player][marble]
        for x in range(card_value):
            temp_mover_position = (temp_mover_position + 1)
            in_between_list.append(temp_mover_position)

        home_landing = positions[player][marble] + card_value

        if home_landing in homes[player]:
            try:
                # Goes through all the positions in the list and check if there is a player on any of them
                for y in in_between_list:
                    
                    # If there is will set move to invalid
                    if y in positions[player].values():
                        valid_move = False
            
            except IndexError:
                print("TOO FAR")
    
        # If the home landing is farther than the last spot in the home, will burn the card
        elif home_landing > homes[player][-1]:
            valid_move = False
        
    return valid_move
 
# ----------------------------------------------------------------------------------------------------------------

def pass_get_out_check(mover, marble, card_value):
    """
    Checks if a player is trying to pass someone on their get out space
    """
    # Initiates variables
    valid_move = True
    mover_position = positions[mover][marble]
    
    # Changes the step if there is a backwards 4
    step = 1
    if card_value == -4:
        step = -1
    
    # Makes a temporary list with all the positions between the current player position and where they will land
    in_between_list = []
    temp_mover_position = mover_position
    for x in range(abs(card_value)):
        temp_mover_position = (temp_mover_position + step) % (num_board_spaces + 1)
        in_between_list.append(temp_mover_position)
        
        # If the space before home is in the list, break because they go into their home instead of trying to pass
        if temp_mover_position == space_before_home[mover]:
            break
    
    for player in get_out:
        
        # Checks if any player is on their own get out space
        if get_out[player] in positions[player].values():
            
            # Checks if the get out position is in between 
            if get_out[player] in in_between_list:
                valid_move = False
            
    return valid_move

# ----------------------------------------------------------------------------------------------------------------

def get_out_check(player, marble, card_value):
    """
    Checks if get out is valid
    """
    valid_move = True
    
    # If the player is in their jail
    if positions[player][marble] < 0:
        
        # If the card is not a get out card, will make the move invalid
        if card_value not in [1, 13]:
            valid_move = False
    
    return valid_move

# ----------------------------------------------------------------------------------------------------------------

def joker_check(player):
    """
    Checks if Joker is valid
    """
    # Initiates lists
    valid_move = True
    player_jail = []
    partner_jail = []
    
    # Finds the players partner
    partner = order[(order.index(player) + int(number_of_players / 2)) % number_of_players]

    # Creates the two lists that hold the players and partners marbles that are still in jail
    for pos in positions[player]:
        if positions[player][pos] < 0:
            player_jail.append(pos)
    for pos in positions[partner]:
        if positions[partner][pos] < 0:
            partner_jail.append(pos)   

    if player_jail == [] and partner_jail == []:
        valid_move = False
    
    return valid_move

# ----------------------------------------------------------------------------------------------------------------

'''
player_turn_cycle = 0
_round = 1
spaces_setup()
jails_setup()
homes_setup()
positions_setup(player_turn_cycle)


board()
player_select()
create_deck()
create_names()
rounds(_round)
create_hands(_round)
display_hands(player_turn_cycle, 'a')
player_turn(player_turn_cycle)
'''


