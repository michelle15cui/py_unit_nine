import random
class Deck:
    def __init__(self):                                                                          # This code can create and initializes the class Deck and get a list of cards from the suits and values.
        self.ranks = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']                       # Pick ranks for the cards
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']                                   # Pick suits for the cards
        self.cards = [{'rank': rank, 'suit': suit} for rank in self.ranks for suit in self.suits]# combine the ranks and suits into cards.
    def shuffle(self):                                                                           # Shuffle the cards which is Deck code by using the Fisher_Yates algorith.
        number = len(self.cards)                                                                 # Get the length of the array
        for i in range(number-1, 0, -1):                                                         # Redoing the range backwards from the last number
            j = random.randint(0, i)                                                          # get a random number between 0 and the index
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]                          # Swap the current index with the new generated index.
    def final(self, num_cards):                                                                  # get a specific card from all of the cards.
        drawn_cards = self.cards[:num_cards]                                                     # get the frist card of the num_card section.
        self.cards = self.cards[num_cards:]                                                      # refreshing all of the cards by moving the drawn cards away.
        return drawn_cards
def compare_cards(players_card, computers_card):                                                 # Compare the ranks of two chosen cards.
    players_value = players_card['rank']                                                         # Define the ranks by the computer's and player's.
    computers_value = computers_card['rank']
    if players_value == computers_value:                                                         # When the number of the card equal to each other.
        return suit_value(players_card['suit']) > suit_value(computers_card['suit'])             # compare the suits when the value equals by using the suit_value function
    else:
        return players_value > computers_value                                                   # Define the only situation of the player's value is bigger than the comupter's.
def suit_value(suit):                                                                            # Define the numeric values of the suits.
    suit_values = {'Clubs': 1, 'Diamonds': 2, 'Hearts': 3, 'Spades': 4}
    return suit_values.get(suit)                                                                 # Return the numbers in when the function is comparing the cards.
def main():
    deck = Deck()                                                                                # Create a deck thing.
    deck.shuffle()                                                                               # Shuffle the whole deck of cards.
    player_score = 0                                                                             # Set the original score as 0
    computer_score = 0
    rounds = 6                                                                                   # Set the rounds to play.
    for _ in range(rounds):                                                                      # Make a loop of rounds
        player_card = deck.final(1)[0]                                                           # Get a card for player
        computer_card = deck.final(1)[0]                                                         # Get a card for computer
        print(f"Player: {player_card['rank']} of {player_card['suit']}")                         # Print the cards
        print(f"Computer: {computer_card['rank']} of {computer_card['suit']}")
        if compare_cards(player_card, computer_card):                                            # Print players win from the compare_cards function
            print("Player wins!")
            player_score += 1                                                                    # Update the score of the player.
        else:
            print("Computer wins!")
            computer_score += 1                                                                  # Update the score of the computer.
        print("")
    print("Finally:")
    print(f"Player Score: {player_score}")                                                       # Show the final score of the player and computer.
    print(f"Computer Score: {computer_score}")
    if player_score > computer_score:                                                            # SHow the winner as the player.
        print("Player wins the game!")
    elif computer_score > player_score:                                                          # Show the winner as the computer.
        print("Computer wins the game!")
    else:                                                                                        # Show that the game it's a tie.
        print("It's a tie! Let's replay!")
if __name__ == "__main__":
    main()