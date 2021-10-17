def calc_sum(number):
    fresult = [0, 0]
    for num in number:
        if int(num) % 2 == 0:
            fresult[1] += int(num)
        else:
            fresult[0] += int(num)

    return fresult


value = input("введите число без пробелов \n")

if value.isdigit():
    result = calc_sum(value)
    print(f"сумма нечетных - {result[0]}; сумма четных - {result[1]} ")
else:
    print("Введено не число")