# Contents
- [**Overview**](#Overview)
  - [Moving](#Moving)
  - [Card Values](#Card-Values)
    - [*Get Out Cards*](#Get-Out-Cards)
    - [*Special Cards*](#Special-Cards)
  - [Rules](#Rules)
    - [*7*](#7)
    - [*Middle Space*](#Middle-Space)
- [**Files**](#Files)
  - [carbles_v2_1.py](#carbles_v2_1)
  - [logic_v2_1.py](#logic_v2_1)
  - [board_numbers.png](#board_numbers)
- [**Bugs & Implementation**](#Bugs-and-Implementation)
  - [Bugs](#Bugs)
  - [Bug Testing](#Bug-Testing)
  - [Future Imlementation](#Future-Implementation)
  
# Overview
- Carbles is a board game similar to *Sorry!* or *Trouble*, but played with playing cards and marbles.
- It is played with 4 or 6 players and in teams - partners are across from each other.
- Partners will exchange 1 card at the beginning of each round.
- Cards dealt to each player by round are: **5, 4, 4** (*4 players*) or **5, 5, 4, 4** (*6 players*), then the deck(s) get reshuffled
- A team wins once both partners have all four of their marbles in their home.

## Moving
1. A player needs to play a "get out" card to move out of their jail and onto their "get out space."
2. They will move clockwise around the board until they reach their home.
3. They will fill up their home with all four of their marbles.
4. Once their own home is filled, they will play their turn on their partners marbles (*still trading cards at the beginning of each round*).
5. Once the other partner also fills up their home, that team wins.

## Card Values
- All cards move the number of spaces as their value - with a few exceptions.
- Suits don't matter
### Get Out Cards
> - Ace
> - King
> - Joker
### Special Cards
> - Ace = 1
> - 4 = -4 (*always backwards*)
> - 7 = 7 (*can be split between marbles, anyone run over by moving is automatically sent to their jail*)
> - Jack = 11 (*can be used to swap with another marble instead*)
> - Queen = 12
> - King = 13
> - Joker = 0 (*can be used to get partner out of their jail*)

## Rules
1. If a player has a playable card, they have to play it (even if it hurts them).
2. Marble in jail, home, and on their *own* "get out space" are immortal (i.e. can't be swapped with, killed, etc.).
3. If a marble is on their *own* "get out space" they can't be passed by any other marbles (not even teammates).
4. A card has to be fully used up to be able to play it.
5. If no cards are playable, the player will choose to burn (discard) one card.
6. When moving marbles in the home, they cannot jump over each other. The front one must move up before the back one can take its place.
7. Landing on another marble sends that marble back to its jail.
8. A player cannot use a -4 to go into their home. However they can move past it, then directly into it next turn.
### 7
-  Arguably the best card in the game.
-  Can be split between marbles.
-  Once a marble is moved, it cannot be moved again.
-  The whole 7 has to be used up to be able to play it.
-  Jumping over or landing on another marble when using a 7 will automatically send that marble back to its jail.
-  Killing teammates is possible so be careful.
### Middle Space
-  The middle space can be used to bypass going around the entire board.
-  When on the middle space the player can choose any row to go down.
-  The middle space has to be landed on exactly, and cannot be used as a stepping stone.
-  It is very useful, but be careful because a marble in the middle can be hit from any angle.

# Files

## carbles_v2_1
This is the main running file and houses the outer game loop.

## logic_v2_1
This is the main logic file that defines lots of functions and runs smaller loops.

## board_numbers
All the board spaces are coded as numbers but with underscores so they can be variables (_1, _2, _3...). board_numbers shows which number corresponds to which position on the game board.

# Bugs and Implementation
- This game isn't complete and still has lots of work to do.

## Bugs
-  Lets you use a 7 into and out of middle on the same turn with the same marble.
-  When on the space right before going into home, a 7 will kill a marble on the get out space.
-  Can choose to play 7 when on the -4 space from the get out space and will break.
-  Can kill a marble on their get out space if land on them from the middle.

## Bug Testing
-  Test if a marble will die when it's on a get out space and that player takes a marble out of jail.
-  Test if a joker will burn if there are no marbles in either partners homes.

## Future Implementation
-  Ability to win...
-  Play off a partners marbles
-  6 player mode
-  Display rules/card values during a turn if someones types "rules"
-  Correctly re-display board after an input so console never shifts up/down
-  Online play so players can only see the cards in their own hand
