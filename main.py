import time
from model import db_func as db

db.make_db()

print(
    'Hello! This is a program to train your brain. Improve your mental arithmetic, logic, memory and speed of thought')
time.sleep(2)
print('Select training direction: ')
time.sleep(2)
print('Enter 1 - to practice mental counting')
time.sleep(1)
print('Enter 2 - to train the speed of thought')
time.sleep(1)
training_direction = input('Enter the number 1 or 2: ')

if training_direction == '1':
    print('Running the math module')
elif training_direction == '2':
    print('Launch of the "speed of thought" module ')
else:
    print('Введите 1 или 2')
