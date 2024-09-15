# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:20:21 2024

@author: jackw
"""

import logic_v2_1 as logic

def main():
    
    # Configure console
    print("============================================")
    print()
    print("Match the top of the console with the thick bar above")
    print()
    print("--------------------------------------------")
    for _ in range(34):
        print()
    print("--------------------------------------------")
    print()
    
    # Card Values
    logic.card_values = {
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
    
    # Selects the number of players, creates names, generates the deck, and sets up the board
    logic.player_select()
    players = logic.create_names()
    number_of_players = logic.create_deck()
    logic.spaces_setup()
    logic.jails_setup()
    logic.homes_setup()
    player_turn_cycle = 0
    logic.positions_setup(player_turn_cycle)
    _round = 1
    rounds_to_play, turns_to_play = logic.rounds(_round)
    
    # Entire game loop
    while True:
        # Rounds loop
        while _round <= rounds_to_play:
            
            turn = 1
            player_turn_cycle = 1
            logic.positions_setup(player_turn_cycle)
            rounds_to_play, turns_to_play = logic.rounds(_round)
            
            print()
            print("--------------------------------------------")
            print(f"Round {_round}")
            print(f"Turn {turn}")
            print("Trading Stage")
            print()
            
            logic.board()
            logic.create_hands(_round)
            logic.display_hands(player_turn_cycle, "a")
            logic.trade_cards()
            
            print()
            print("--------------------------------------------")
            print()
            print()
            print()
            print()
            print()
            
            # Turns loop
            while turn <= turns_to_play:
                
                
                for player in players:
                    
                    print("--------------------------------------------")
                    print()
                    print(f"Round {_round}")
                    print(f"Turn {turn}")
                    print(f"Playing Stage: {players[player_turn_cycle - 1]}'s Turn")
                    print()
                    
                    logic.positions_setup(player_turn_cycle)
                    logic.board()
                    
                    logic.display_hands(player_turn_cycle, "o")
                    
                    print("--------------------------------------------")
                    print()
                    
                    logic.player_turn(player_turn_cycle)
                    
                    print()
                    
                    logic.positions_setup(player_turn_cycle)
                    player_turn_cycle += 1
                    
                    if player_turn_cycle > number_of_players:
                        logic.positions_setup(player_turn_cycle)
                        player_turn_cycle = 1
                        break
                    else:
                        logic.positions_setup(player_turn_cycle)
                        
                
                turn += 1
            _round += 1
        print("Time to reshuffle...")
        logic.create_deck()
        _round = 1
        rounds_to_play, turns_to_play = logic.rounds(_round)
        
       
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()