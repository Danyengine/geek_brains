import re
"""
stroka = input('Edit your string: ')
print('Your string is: ', stroka)
ch_lst = []
while 1:
    ch = input("What characters want you delete from your string?")
    ch_lst.append(ch)
    if not ch:
        break

new_str = re.sub(f'[{ch_lst[0]}|{ch_lst[1]}|{ch_lst[2]}]', '', stroka)
print('\n\n', new_str)
"""








"""
1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
— получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""


# 1st way is "forehead":
def parse_log():
    with open("C:/Python/geek_brains/lessons_module_1/lesson_6_files/homework_lesson_5/task_1/nginx_logs_prob.txt",\
         'r', encoding = 'utf-8') as log_file:
        log_lines = log_file.readlines()
        log_data = []
        log_data_tuple = []
        for line in log_lines:
            remote_adress = line[0: line.find(' - - ')]
            req_type = line[line.find('"') + 1: line.find('"') + 4]
            req_resourse = line[line.find('GET') + 4: line.find('HTTP') - 1]
            log_data.append((remote_adress, req_type, req_resourse))
            #log_data.extend((remote_adress, req_type, req_resourse))
            #log_data_tuple.append(tuple([ data for data in log_data[-3:] ]))

    return (log_data)


print(parse_log())
    
        

# Применим, если требуемые данные в каждой строке
# имеют одинаковый порядок распоожения
with open("C:/Python/geek_brains/lessons_module_1/lesson_6_files/homework_lesson_5/task_1/nginx_logs_prob.txt",\
     'r', encoding = 'utf-8') as log_file:
    data = []
    for line in log_file:
        splitted_line = line.split()
        data.append((splitted_line[0], splitted_line[5].replace('"',''), splitted_line[6]))
    print(data)


"""
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
"""


      
