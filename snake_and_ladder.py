import random

SNAKES  = {16: 6,  48: 30}
LADDERS = {3: 22,  20: 38}

WINNING_POSITION = 100


def roll_dice():
    """Return a random number between 1 and 6."""
    return random.randint(1, 6)


def apply_board_event(position):
    """
    Check if a position triggers a snake or ladder and apply the effect.

    Input  : position (int) - the cell the player just landed on
    Output : int - the final position after applying snake/ladder (or same position if none)
    """
    # Snake: player slides down from head to tail
    if position in SNAKES:
        print(f"  Oh no! A snake! Sliding down from {position} to {SNAKES[position]}.")
        return SNAKES[position]
    # Ladder: player climbs up from bottom to top
    if position in LADDERS:
        print(f"  Lucky! A ladder! Climbing up from {position} to {LADDERS[position]}.")
        return LADDERS[position]

    return position


def get_player_names():
    """
    Prompt each player to enter their name and validate that it is not empty.

    Input  : None (reads from keyboard)
    Output : list of str - a list containing the two player names [name1, name2]
    """
    players = []
    for i in range(1, 3):
        name = input(f"Enter name for Player {i}: ").strip()
        # Keep asking until the player gives a non-empty name
        while name == "":
            print("  Name cannot be empty. Please try again.")
            name = input(f"Enter name for Player {i}: ").strip()
        players.append(name)
    return players


def display_status(positions, names):
    """
    Print the current board position of both players.

    Input  : positions (list of int) - current positions of [player1, player2]
             names     (list of str) - names of [player1, player2]
    Output : None (prints to terminal)
    """
    print(f"\n  {names[0]} is at position {positions[0]}")
    print(f"  {names[1]} is at position {positions[1]}")


def play_turn(player_name, position):
    """
    Handle one complete turn: roll the dice, move the player, apply board events.

    Input  : player_name (str) - the name of the current player
             position    (int) - the player's current position before the turn
    Output : int - the player's new position after the turn
    """
    input(f"\n{player_name}'s turn - press Enter to roll the dice...")
    die = roll_dice()
    print(f"  {player_name} rolled a {die}.")

    new_position = position + die

    if new_position > WINNING_POSITION:
        print(f"  Overshoot! {player_name} stays at {position}.")
        return position
        
    print(f"  {player_name} moves from {position} to {new_position}.")
    
    # Check for snake or ladder on the new cell
    new_position = apply_board_event(new_position)
    return new_position


def check_winner(positions, names):
    """
    Check whether any player has reached exactly position 100.

    Input  : positions (list of int) - current positions of [player1, player2]
             names     (list of str) - names of [player1, player2]
    Output : str  - the winner's name if someone reached 100
             None - if nobody has won yet
    """
    for i in range(2):
        if positions[i] == WINNING_POSITION:
            return names[i]
    # No winner yet
    return None


def play_game(names):
    """
    Run the main game loop until one player wins.

    Input  : names (list of str) - names of [player1, player2]
    Output : str - the name of the winning player
    """
    # Both players start before square 1
    positions = [0, 0]
    winner = None
    turn = 0

    print("\n" + "=" * 50)
    print("  SNAKE & LADDER GAME  -  Good luck!")
    print("=" * 50)

    while winner is None:
        positions[turn] = play_turn(names[turn], positions[turn])
        display_status(positions, names)
        winner = check_winner(positions, names)
        turn   = 1 - turn

    return winner


def ask_play_again():
    """
    Ask the players whether they want to start a new game.

    Input  : None (reads from keyboard)
    Output : bool - True if players want to play again, False otherwise
    """
    answer = input("\nDo you want to play again? (y / n): ")
    while answer != "y" and answer != "n":
        print("  Please type 'y' or 'n'.")
        answer = input("Do you want to play again? (y / n): ")
    return answer == "y"


def main():
    print("=" * 50)
    print("   Welcome to Snake & Ladder (2-Player)!")
    print("=" * 50)

    names        = get_player_names()
    keep_playing = True

    while keep_playing:
        winner = play_game(names)
        print(f"\n  Congratulations {winner}! You reached 100 and won the game!")
        keep_playing = ask_play_again()

    print("\nThanks for playing! Goodbye.")


if __name__ == "__main__":
    main()
