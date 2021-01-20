import art
import random
import game_data

# Start the game by displaying logos and the two selections
    # Choose two random entries from the dictionary
    # Separate function for random choices

LENGTH = len(game_data.data)

# Compare the follower counts between the selections
def compare(a, b):
    if a > b:
        return "a"
    else:
        return "b"

def new_selections():
    entry = random.randint(0, LENGTH - 1)
    return entry

a_entry = new_selections()
b_entry = new_selections()

def win(answer, user):
    if answer == user:
        return True
    else:
        return False

# Ask user which person they think has a higher follower count
    # Make a play_game function that randomly chooses 'A' and 'B' from dictionary
def play_game(a, b):
    game = True
    points = 0


    while game:
        a_count = game_data.data[a]['follower_count']
        b_count = game_data.data[b]['follower_count']

        while a_count == b_count:
            b = new_selections()
            b_count = game_data.data[b]['follower_count']

        print(art.logo)
        print(f"Compare A: {game_data.data[a]['name']}, a {game_data.data[a]['description']}, from {game_data.data[a]['country']}")
        print(art.vs)
        print(f"Compare B: {game_data.data[b]['name']}, a {game_data.data[b]['description']}, from {game_data.data[b]['country']}")

        higher = compare(a_count, b_count)
        user_select = input("Who has more followers? Type 'A' or 'B': ").lower()

        # If user is correct they get +1 points
        # The previous 'B' selection is the new 'A' selection
        # New selection 'B' is a random choice from the dictionary but cannot be the same as 'A'
        if win(higher, user_select):
            points += 1
            print(f"Correct! Current score is {points}")
            a = b
            b = new_selections()
        else:
        # If they are wrong the game ends
            print(f"Incorrect. Game over. Final points {points}")
            game = False

play_game(a_entry, b_entry)