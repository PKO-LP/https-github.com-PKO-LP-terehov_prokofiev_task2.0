VERSION = "0.1.1"
secret = 43
attempts = 0
print(f"Угадай число")
print("Я загадал число от 1 до 100. Попробуй угадать!")
while True:
    guess = int(input("\nТвой вариант: "))
    attempts += 1
    if guess == 67:
        print("Пасхалко!❤️❤️ Нашёл секретный код, но загаданное число меньше :)")
    elif guess < secret:
        print("Больше!")
    elif guess > secret:
        print("Меньше!")
    else:
        print(f"Победа! Ты угадал число {secret} за {attempts} попыток.")
        break
