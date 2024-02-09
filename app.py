# create an enum for user to choose. The three options are: rock, paper, scissors
#fix error "Enum" is not defined
#fix error "randint" is not defined
#fix error "Choice" is not defined

from random import randint
from enum import Enum
class Choice(Enum):
    rock = 1
    paper = 2
    scissors = 3    

# create a function to get the user's choice
def get_user_choice():
    print('Please choose one of the following options:')
    print('1. Rock')
    print('2. Paper')
    print('3. Scissors')
    choice = int(input('Enter your choice: '))
    #if the user's choice is not valid, ask the user to enter a valid choice
    while choice < 1 or choice > 3:
        print('Invalid choice. Please enter a valid choice.')
        choice = int(input('Enter your choice: '))
    return Choice(choice)

#create a function to get the computer's choice
def get_computer_choice():
    return Choice(randint(1, 3))

# create a function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'It\'s a tie!'
    elif user_choice == Choice.rock and computer_choice == Choice.scissors:
        return 'You win!'
    elif user_choice == Choice.paper and computer_choice == Choice.rock:
        return 'You win!'
    elif user_choice == Choice.scissors and computer_choice == Choice.paper:
        return 'You win!'
    else:
        return 'Computer wins!'

# create a function to play the game
def main():
    #while play_again is yes, play the game
    play_again = 'yes'
    while play_again.lower() == 'yes':
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print('You chose:', user_choice.name)
        print('Computer chose:', computer_choice.name)
        print(determine_winner(user_choice, computer_choice))
        # ask the user if they want to play again
        play_again = input('Do you want to play again? (yes/no): ')
    

# Using the special variable  
# __name__ 
if __name__=="__main__": 
    main() 