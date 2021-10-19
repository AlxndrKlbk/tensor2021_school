def calc_sum(number):
    fresult = [0, 0]
    for num in number:
        num = int(num)
        fresult[num % 2] += num

    return fresult


value = input("введите число без пробелов \n")

if value.isdigit():
    result = calc_sum(value)
    print(f"сумма четных - {result[0]}; сумма нечетных - {result[1]} ")
else:
    print("Введено не число")