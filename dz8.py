sum_func = lambda x, y: x + y

test = 123

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))


result = sum_func(num1, num2)
print(f"Сумма чисел {num1} и {num2} равна: {result}")