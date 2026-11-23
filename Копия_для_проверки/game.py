secret = 43
attempts = 0
print("Я загадал число от 1 до 100. Попробуй угадать!")
while True:
    guess = int(input("\nТвой вариант: "))
    attempts += 1
    if guess < secret:
        print("Больше!")
    elif guess > secret:
        print("Меньше!")
    else:
        print(f"Победа! Ты угадал число {secret} за {attempts} попыток.")
        break
