from random import randint as Hudini
import sys


my_val = input("введите число \n")

if my_val.isdigit():
    my_val = int(my_val)
else:
    sys.exit("Введено не число")

possible_values = [1, 101]
pred_list = []
while True:
    prediction = Hudini(possible_values[0], possible_values[1])

    if prediction not in pred_list:
        pred_list.append(prediction)
    else:
        continue

    print(f"Твое число {prediction}?\n")

    command = input("Введите команду 'Больше', 'Меньше' или  'Равно'\n")
    if command.lower() == "равно":
        print(f"твое число {prediction}")
        break
    elif command.lower() == "больше":
        possible_values[0] = prediction + 1
    elif command.lower() == "меньше":
        possible_values[1] = prediction - 1

    if possible_values[0] > possible_values[1]:
        print("Кажется вы запутались и забыли ваше число")
        break

