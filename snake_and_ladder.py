import random

SNAKES  = {16: 6,  48: 30}
LADDERS = {3: 22,  20: 38}

WINNING_POSITION = 100


def roll_dice():
    """Return a random number between 1 and 6."""
    return random.randint(1, 6)


def apply_board_event(position):
    """Check whether a position has a snake or ladder and return the final position."""
    if position in SNAKES:
        print(f"  Oh no! A snake! Sliding down from {position} to {SNAKES[position]}.")
        return SNAKES[position]

    if position in LADDERS:
        print(f"  Lucky! A ladder! Climbing up from {position} to {LADDERS[position]}.")
        return LADDERS[position]

    return position


def get_player_names():
    """Ask for the two players names and return them as a list."""
    players = []
    for i in range(1, 3):
        name = input(f"Enter name for Player {i}: ").strip()
        while name == "":
            print("  Name cannot be empty. Please try again.")
            name = input(f"Enter name for Player {i}: ").strip()
        players.append(name)
    return players


def display_status(positions, names):
    """Print the current board positions of both players."""
    print(f"\n  {names[0]} is at position {positions[0]}")
    print(f"  {names[1]} is at position {positions[1]}")


def play_turn(player_name, position):
    """Handle one full turn for a player and return the new position."""
    input(f"\n{player_name}'s turn - press Enter to roll the dice...")
    die = roll_dice()
    print(f"  {player_name} rolled a {die}.")

    new_position = position + die

    if new_position > WINNING_POSITION:
        print(f"  Overshoot! {player_name} stays at {position}.")
        return position

    print(f"  {player_name} moves from {position} to {new_position}.")
    new_position = apply_board_event(new_position)
    return new_position


def check_winner(positions, names):
    """Return the winner's name if someone reached 100, otherwise return None."""
    for i in range(2):
        if positions[i] == WINNING_POSITION:
            return names[i]
    return None


def play_game(names):
    """Run the main game loop and return the name of the winner."""
    positions = [0, 0]
    winner    = None
    turn      = 0

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
    """Ask the players if they want to play again. Return True or False."""
    answer = input("\nDo you want to play again? (yes / no): ").strip().lower()
    while answer not in ("yes", "no", "y", "n"):
        print("  Please type 'yes' or 'no'.")
        answer = input("Do you want to play again? (yes / no): ").strip().lower()
    return answer in ("yes", "y")


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
