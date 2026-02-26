from random import choice
'''
'rock' for rock
'paper' for paper
'scissors' for scissors
'''
computer = choice(['rock', 'paper', 'scissors'])
youstr = input('Enter r, p or s: ').lower()

youDict = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

if youstr not in youDict:
    print('Invalid input! Please enter r, p or s.')
    exit()

you = youDict[youstr]

print(f'You chose {you}\nComputer chose {computer}')

if you == computer:
    print('Match Drawn')

elif (you == 'rock' and computer == 'scissors') or (you == 'paper' and computer == 'rock') or (you == 'scissors' and computer == 'paper'):
    print('You Win!')
else:
    print('Computer Wins!')
