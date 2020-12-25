player1_turn = False
player2_turn = False
player2_guess = False
player1_number = input('Please keep a number between 1-100: ')

while player1_turn == False:
    try:
        player1_number = int(player1_number)
        if (player1_number >= 1 and player1_number <=100):
            player1_turn = True
        else:
            print('Please enter number between 1 and 100')
            player1_turn = False
            player1_number = input('Please keep a number between 1-100: ')
    except ValueError:
       print("That's not a number!")
       player1_number = input('Please keep a number between 1-100: ')

print("Now Change Turn, don't tell your number to Player2")

player2_number = input('Please guess a number between 1-100: ')
while player2_guess == False:
    try:
        player2_number = int(player2_number)
        if (player2_number >= 1 and player2_number <=100):
            if player2_number > player1_number:
                print('Your number is bigger than the target number, try again')
                player2_number = input('Please guess a number between 1-100: ')
            elif player2_number < player1_number:
                print('Your number is smaller than the target number, try again')
                player2_number = input('Please guess a number between 1-100: ')
            else:
                print('CONGRATULATIONS YOU NAILED IT')
                player2_guess = True
        else:
            print('Please enter number between 1 and 100')
            player2_number = input('Please guess a number between 1-100: ')
    except ValueError:
       print("That's not an number!")
       player2_number = input('Please guess a number between 1-100: ')








