from random import choice as Hudini
import sys


my_val = input("введите число \n")

if my_val.isdigit():
    my_val = int(my_val)
else:
    sys.exit("Введено не число")

possible_values = list(range(1, 101))
pred_list = []
while True:
    prediction = Hudini(possible_values)

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
        possible_values = possible_values[possible_values.index(prediction):]
    elif command.lower() == "меньше":
        possible_values = possible_values[:possible_values.index(prediction)]

    if len(possible_values) == 0:
        print("Кажется вы запутались и забыли ваше число")
        break

