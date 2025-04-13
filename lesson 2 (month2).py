low, high = 1, 100
try_count = 0
list_try_count = []

while low <= high:
    guess = (low + high) // 2
    print(f"Ваше загаданное число {guess}?")
    answer = input("Введите 'да', 'больше' или 'меньше': ").lower()

    try_count += 1
    list_try_count.append(guess)

    if answer == 'да':
        with open('result.txt', 'w') as file:
            file.write(f'Количество попыток: {try_count}\nСписок попыток: {list_try_count}\nЗагаданное число: {guess}')

        print("Даа, я угадал!")
        break
    elif answer == 'меньше':
        high = guess - 1
    elif answer == 'больше':
        low = guess + 1
    else:
        print("Пожалуйста, вводите только 'да', 'больше' или 'меньше'!")
