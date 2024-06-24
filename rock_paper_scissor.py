import random as rd
ch=("rock","paper","scissors")
playing=True
while playing:
    computer=rd.choice(ch)
    player1=None
    while player1 not in ch:
        player1=input('enter a choice(rock, paper, scissors): ')
        player1.lower()
    if player1==computer:
        print("It's a tie!")
    elif player1=="rock" and computer=="scissors" or player1=="paper" and computer=="rock" or player1=="scissors" and computer=="paper":
        print("You won!")
    else:
        print('You lose!')
    print('computer choice: ',computer)
    play_again=input('you want to play again? \n enter yes or no: ')
    play_again.lower()
    if play_again=='no':
        playing=False
print("Thanks for playing!  ")