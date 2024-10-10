import random
students = ['Алексей','Дмитрий','Дарья','Анжела','Антон','Варвара']
students.sort()
classes=['Математика','Русский язык','Информатика',]
students_marks={}

for student in students:
    students_marks[student]={}
    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks[student][class_]=marks
for student in students:
    print(f'{student}{students_marks[student]}')

print('''Список команд:
        1. Добавить оценку ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Удалить оценку ученика
        5. Удалить ученика
        6. Удалить предмет 
        7. Оценки определенного ученика по определенному предмету 
        8. Изменение имени студента
        9. Изменение предмета
        10. Средняя оценка ученика по предметам
        11. Выход из программы
        .''')
while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()

    elif command == 4:
        print('4. Удалить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].remove(mark)
            print(f'Для {student} по предмету {class_} удалена  оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command ==5:
        print('5 Удалить ученика')
        student = input("Введите имя ученика: ")
        if student in students_marks.keys():
           del students_marks[student]
           print(f"студент {student} удален ")
        else:
            print("Этого ученика нету в дневнике")

    elif command ==6:
        print("6.Удалить предмет")
        class_=input("введите предмет: ")
        if class_ in classes:
            classes.remove(class_)
            print(f"предмет {class_} удален")
        else:
            print("такого предмета нету")

    elif command==7:
        print("7.оценки определенного ученика по опреденному предмету")

        student = input("введите имя Ученика: ")
        class_= input("введите предмет: ")
        if student in students_marks and class_ in classes:

            print(f'\t{class_}-{students_marks[student][class_]}')
        else:
            print("такого ученика или предмета нету")

    elif command==8:
        print("8. Изменение имени студента ")
        student=input("введите имя ученика: ")
        new_student=input("Введите новое имя :")
        if student in students_marks:
            students_marks[new_student] = students_marks[student]
            del students_marks[student]
            print(f'имя {student} изменено на {new_student}')
        else:
            print('такого ученика нету')


    elif command==9:
        print("9. Изменение предмета")
        class_=input("Введите предмет: ")
        new_class= input("Введите новый предмет: ")
        if class_ in classes:
            classes.remove(class_)
            classes.append(new_class)
            print(f'предмет {class_} изменено на {new_class}')
        else:
            print('такого предмета нету')

    elif command==10:
        print("10.Средняя оценка ученика по предметам ")
        student=input("Введите имя ученика: ")
        if student in students_marks:
                for class_ in classes:
                    marks_sum= sum(students_marks[student][class_])
                    marks_count= len(students_marks[student][class_])
                    print(f'средняя оценка по {class_}-{marks_sum//marks_count}')
        else:
            print("нету такого ученика")



    elif command == 11:
        print('11. Выход из программы')
        break
