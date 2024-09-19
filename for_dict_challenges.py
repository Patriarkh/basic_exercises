# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

names_students = {}
for student in students:
    name = student['first_name']
    if name in names_students:
        names_students[name] += 1
    else:
        names_students[name] = 1

for name, count in names_students.items():
    print(f"{name}: {count}")



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
studentss = {}

for student in students:
    name = student['first_name']
    if name in studentss:
        studentss[name] += 1
    else:
        studentss[name] = 1

most_common_names = max(studentss, key=studentss.get)


print("Самое частое имя среди учеников: ", most_common_names)



# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for class_index, school_students in enumerate(school_students, 1):
    class_name_counts = {} 

   
    for student in school_students:
        name = student['first_name']  
        if name in class_name_counts:
            class_name_counts[name] += 1
        else:
            class_name_counts[name] = 1

   
    most_common_name = max(class_name_counts, key=class_name_counts.get)

   
    print(f"Самое частое имя в классе {class_index}: {most_common_name}")




# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

boys = {}
girls = {}

for guys in school:
    boys_count = 0
    girls_count = 0
    for student in guys['students']:
        if is_male[student['first_name']]:
            boys_count += 1
        else:
            girls_count += 1
    print(f"Класс {guys['class']}: девочки {girls_count}, мальчики {boys_count}")
    


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

boys_in_classes = {}
girls_in_classes = {}

for class_info in school:
    class_name = class_info['class']
    boys_count = 0
    girls_count = 0
    for student in class_info['students']:
        if is_male[student['first_name']]:
            boys_count += 1
        else:
            girls_count += 1
    boys_in_classes[class_name] = boys_count
    girls_in_classes[class_name] = girls_count


max_boys_class = max(boys_in_classes, key=boys_in_classes.get)
max_girls_class = max(girls_in_classes, key=girls_in_classes.get)

print(f"Больше всего мальчиков в классе {max_boys_class}")
print(f"Больше всего девочек в классе {max_girls_class}")



