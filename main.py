import time
print('Привет! Это тренажёр твоего мозга. Прокачайся в устном счёте и не только...')
time.sleep(2)
print('Выберите направление тренировки: ')
time.sleep(2)
print('Введите 1 - для тренировки устного счёта')
time.sleep(1)
print('Введите 2 - для тренировки скорости мысли')
time.sleep(1)
training_direction = input('Введите цифру 1 или 2 : ')

if training_direction == '1':
    print('Запуск математического модуля')
elif training_direction == '2':
    print('Запуск модуля "скорости мысли" ')
else:
    print('Введите 1 или 2')