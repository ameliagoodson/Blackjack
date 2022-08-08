import random
from art import logo
import os 

## FUNCTIONS
def clear():
   os.system('cls')

def deal():
   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
   card = random.choice(cards)
   return card

def calculate_score(user_cards, computer_cards):
   user_score = sum(user_cards)
   computer_score = sum(computer_cards)

   ## check if ace
   if 11 in user_cards and user_score > 21:
      user_cards.remove(11)
      user_cards.append(1)
      calculate_score(user_cards, computer_cards)
   if 11 in computer_cards and computer_score > 21:
      computer_cards.remove(11)
      computer_cards.append(1)
      calculate_score(user_cards, computer_cards)

   ## check if blackjack
   if user_score >= 21 or computer_score >= 21:
      print(gameover(user_score, computer_score, user_cards, computer_cards))

   print(f"Your cards: {user_cards} Your score: {user_score}\nComputer's first card: {computer_cards[0]}")

   con = input("Type y to get another card, type n to pass\n")
   
   if con == "n":
      if computer_score < 17:
         clear()
         print("The computer takes another card.")
         computer_cards.append(deal())
         calculate_score(user_cards, computer_cards)
      else:
         clear()
         gameover(user_score, computer_score, user_cards, computer_cards)
   else:
      clear()
      user_cards.append(deal())
      computer_cards.append(deal())
      calculate_score(user_cards, computer_cards)

def gameover(userS, computerS, user_cards, computer_cards):
   if userS > 21 and computerS > 21:
      print("You went over. You lose 😤")
   elif computerS > 21:
      print("Opponent went over. You win 😃") 
   elif computerS == userS:
      print("It's a draw 🙃") 
   elif userS == 21:
      print("Win with Blackjack 😎")
   elif computerS == 21:
      print("You lose, the computer got Blackjack 😤")
   elif computerS > userS and computerS < 22:
      print("You lose, the computer got a higher score 😤") 
   elif userS > computerS and userS < 22:
      print("You win, you got a higher score 😃")
   elif userS > 21:
      print("You went over, you lose 😤")
   print(f"\nYour final hand: {user_cards}, final score: {userS}")
   print(f"Computer's final hand: {computer_cards}, final score: {computerS}")
   play()

## GAME
def play():
   print(logo)
   user_cards = []
   computer_cards = []
   choice = input("Do you want to play a game of Blackjack? Type y or n\n")
   if choice == "y":
      clear()
      for player in range(2):
         user_cards.append(deal())
         computer_cards.append(deal())
   calculate_score(user_cards, computer_cards)
play()


