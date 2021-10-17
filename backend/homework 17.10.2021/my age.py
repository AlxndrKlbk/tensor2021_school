age = input("Введите ваш возраст цифрой от 0 до 100 \n")

if age.isdigit():

    if int(age[len(age) - 1]) in [0, 5, 6, 7, 8, 9]:
        print(f"{age} лет")
    elif int(age[len(age) - 1]) in [2, 3, 4]:
        print(f"{age} года")
    else:
        print(f"{age} год")
else:
    print("Введено не число")