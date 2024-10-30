from model import db_func as db
from utils import checks

db.make_db()

print(
    'Hello! This is a program to train your brain. Improve your mental arithmetic, logic, memory and speed of thought')
input('Press <Enter>')

while True:
    user_enter = checks.checking_numbers('Are you playing for the first time?',
                                         'Enter the correct value',
                                         'Enter 1 if YES first.\nEnter 2 if NO has already played\nYour answer: ')
    if user_enter == 1 or user_enter == 2: break

print('Select training direction: ')
input('Press <Enter>')
print('Enter 1 - to practice mental counting')
print('Enter 2 - to train the speed of thought')

training_direction = input('Enter the number 1 or 2: ')

if training_direction == '1':
    print('Running the math module')
elif training_direction == '2':
    print('Launch of the "speed of thought" module ')
else:
    print('Введите 1 или 2')
