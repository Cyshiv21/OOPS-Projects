import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop()

        
class Hand:
    def __init__(self):
        self.cards = []
        
    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        total = 0
        aces = 0
        for card in self.cards:
            if card.value.isdigit():
                total += int(card.value)
            elif card.value in [ "King", "Queen", "Jack" ]:
                total += 10
            elif card.value == "Ace":
                total += 11
                aces += 1

        while total > 21 and aces > 0:
                total -= 10
                aces -= 1

        return total
    
    def __str__(self):
        return ", ".join(str(card) for card in self.cards)
    
class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
    
    def deal_initial_cards(self):
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())
            
    def show_cards(self, reveal_dealer=False):
        print(f"\nYour cards: {self.player_hand}")
        print(f"Your total: {self.player_hand.calculate_value()}")

        if reveal_dealer:
            # show all dealer cards
            print(f"Dealer's cards: {self.dealer_hand}")
            print(f"Dealer's total: {self.dealer_hand.calculate_value()}")
        else:
            # show only first card
            print(f"Dealer's first card: {self.dealer_hand.cards[0]}")

    def play(self):
        self.deal_initial_cards()
        self.show_cards()

        # player's turn
        while True:
            choice = input("\nHit or Stand? (h/s): ").lower()
            if choice == "h":
                self.player_hand.add_card(self.deck.deal())
                self.show_cards()
                if self.player_hand.calculate_value() > 21:
                    print("You bust! Dealer wins!")
                    return
            elif choice == "s":
                break

        # dealer's turn
        while self.dealer_hand.calculate_value() < 17:
            self.dealer_hand.add_card(self.deck.deal())

        self.show_cards(reveal_dealer=True)

        # check winner
        player_total = self.player_hand.calculate_value()
        dealer_total = self.dealer_hand.calculate_value()

        if dealer_total > 21:
            print("Dealer busts! You win!")
        elif player_total > dealer_total:
            print("You win!")
        elif dealer_total > player_total:
            print("Dealer wins!")
        else:
            print("It's a tie!")

def main():
    while True:
        game = Game()
        game.play()
        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break

main()
