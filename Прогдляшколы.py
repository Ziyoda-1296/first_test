def display_menu():
    print("1. Добавить ученика")
    print("2. Показать список учеников")
    print("3. Внести оценку")
    print("4. Показать средний балл ученика")
    print("5. Выйти")

def add_student(students):
    name = input("Введите имя ученика: ")
    students[name] = []
    print(f"Ученик {name} добавлен.")

def show_students(students):
    print("Список учеников:")
    for student in students:
        print(student)

def add_grade(students):
    name = input("Введите имя ученика: ")
    if name in students:
        grade = float(input("Введите оценку: "))
        students[name].append(grade)
        print(f"Оценка {grade} добавлена ученику {name}.")
    else:
        print("Ученик не найден.")

def calculate_average_grade(students):
    name = input("Введите имя ученика: ")
    if name in students:
        grades = students[name]
        if grades:
            average_grade = sum(grades) / len(grades)
            print(f"Средний балл ученика {name}: {average_grade:.2f}")
        else:
            print(f"У ученика {name} пока нет оценок.")
    else:
        print("Ученик не найден.")

def main():
    students = {}

    while True:
        display_menu()

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            add_grade(students)
        elif choice == "4":
            calculate_average_grade(students)
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите от 1 до 5.")

if __name__ == "__main__":
    main()