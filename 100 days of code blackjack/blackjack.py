############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
## In case of draw dealer wins

from art import logo
import random

#cards deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#main function
def main():
  """Starting function wich executes program"""
  print(logo)
  game = input("Welcome in Blackajack! Start game? 'y' or 'n' ")
  if game.lower() == "y":
    while True:
      blackjack()
      game2 = input("Do you want to play again? 'y' or 'n' ")
      if game2.lower() != "y":
        print("Thank you for playing! See you next time")
        break
  else:
    print("See you next time")

def draw(player_cards):
  """draw fuction wich draws a card while player wants, controls if its not BUST(over21) and returns player cards back to blackjack function in case player wants to stop"""
  while True:
    draw = input("Draw a card? 'y' or 'n' ")
    if draw.lower() == "y":
      player_cards.append(random.choice(cards))
      print(f"Player cards: {''.join(f'[{item}]' for item in player_cards)}")
      if sum(player_cards) > 21 and 11 in player_cards:
        player_cards[player_cards.index(11)] = 1
        print("[11] changed to [1]")
        if sum(player_cards) > 21:
          print("\nBust!\n")
          return 0
      elif sum(player_cards) > 21:
        print("\nBust!\n")
        return 0
    else:
      print(f"\nYou have {sum(player_cards)} and your cards are: {''.join(f'[{item}]' for item in player_cards)}\n")
      return player_cards

def dealer(dealer_cards, result):
  """Dealer function evaluates situation and makes dealers turn, after dealers turn function will control who won"""
  if result == 0:
    #if player busted
    while sum(dealer_cards) < 11:
      dealer_cards.append(random.choice(cards))
      print("**Dealer draws a card**")
      print(f"Dealer cards: {''.join(f'[{item}]' for item in dealer_cards)}\n")
    else:
      print(f"Dealer won with: {''.join(f'[{item}]' for item in dealer_cards)}\n")
      
  else:
    #player still in game
    while sum(result) > sum(dealer_cards):
      dealer_cards.append(random.choice(cards))
      print("**Dealer draws a card**")
      print(f"Dealer cards: {''.join(f'[{item}]' for item in dealer_cards)}")
      if sum(dealer_cards) > 21 and 11 in dealer_cards:
        dealer_cards[dealer_cards.index(11)] = 1
        print("[11] changed to [1]")
        if sum(dealer_cards) > 21:
          print("\nDealer busted! You won!!\n")
          return
      elif sum(dealer_cards) > 21:
        print("\nDealer busted! You won!!\n")
        return
    print(f"Dealer won with {sum(dealer_cards)} and dealers cards are: {''.join(f'[{item}]' for item in dealer_cards)}\n")
    
    print("You lost :(\n")

def blackjack():
  """This is where our game comes to life :P"""
  dealer_cards = random.choices(cards, k=2)
  player_cards = random.choices(cards, k=2)
  print(f"\n{'*' * 50}\n\nDealer cards: [X][{dealer_cards[1]}]")
  print(f"Player cards: [{player_cards[0]}][{player_cards[1]}]\n")
  result = draw(player_cards)
  print("Dealers turn\n")
  dealer(dealer_cards, result)


  
  
  



if __name__ == "__main__":
    main()