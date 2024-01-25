def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i} * {j} = {i * j}")
        print()

if __name__ == "__main__":
    try:
        size = int(input("Введите размер таблицы умножения: "))
        multiplication_table(size)
    except ValueError:
        print("Пожалуйста, введите целое число.")