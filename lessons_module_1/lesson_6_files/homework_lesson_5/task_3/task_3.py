"""
3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь, 
разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: 
ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные. 
Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None. 
Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):

Иванов,Иван,Иванович
Петров,Петр,Петрович

Фрагмент файла с данными о хобби (hobby.csv):

скалолазание,охота
горные лыжи
"""



from itertools import zip_longest
import json
import pandas as pd

with open("C:\Python\geek_brains\lessons_module_1\lesson_6_files\homework_lesson_5/task_3/users.csv", encoding='utf-8') as f_users:
    with open("C:\Python\geek_brains\lessons_module_1\lesson_6_files\homework_lesson_5/task_3/hobby.csv", encoding='utf-8') as f_hobby:
        users = [user.strip('\n') for user in f_users.readlines()]    # list of users
        hobbies = [hobby.strip('\n') for hobby in f_hobby.readlines()]  # hobby list

        if len(users) < len(hobbies):
            print('users less than hobbies!')
            exit(1)
        dict_data = {user: hobby for user, hobby in zip_longest(users, hobbies, fillvalue=None)}
    print(dict_data) 

with open("C:\Python\geek_brains\lessons_module_1\lesson_6_files\homework_lesson_5/task_3/data_users.json",\
     'w', encoding='utf-8') as f:

    json.dump(dict_data, f, ensure_ascii=0)




with open("C:\Python\geek_brains\lessons_module_1\lesson_6_files\homework_lesson_5/task_3/data_users.xlsx",\
     'w', encoding='utf-8') as f:
     
     data = {user: hobby.split(',') for user, hobby in dict_data.items() if hobby is not None}
     print(data)

     df = pd.DataFrame(data).fillna(0, inplace=True)
     df.to_excel(f)




