"""
Task_1.

Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
>>> num_translate("one")
"один"
>>> num_translate("eight")
"восемь"

Если перевод сделать невозможно, вернуть None. 
Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.
"""

dict_num = {'one': 'один', 'two': 'два', 'three': 'три',
            'four': 'четыре', 'five': 'пять', 'six': 'шесть',
            'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

def num_translate(word):
    return(dict_num.get(word, None))

#print('Translate number two(2): ', num_translate('two'))
#print('Translate number seven(7): ', num_translate('seven'))
#print("If I don't translate a number: ", num_translate('Ssdsa'))


"""
task_2.

* (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
>>> num_translate_adv("One")
"Один"
>>> num_translate_adv("two")
"два"
"""


def num_translate_adv(word):
    if word.istitle():
        word = word.lower()
        result = dict_num.get(word, None).title()
    else:
        result = dict_num.get(word, None)
    return(result)

print(num_translate_adv('Two'))
print(num_translate_adv('two'))
print(num_translate_adv('Three'))
print(num_translate_adv('Four'))
print(num_translate_adv('FiVE'))
print(num_translate_adv('five'))







"""
Task_3.

Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
>>>  thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"], 
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? 
Как поступить, если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?
"""



def thesaurus(*args):
    dict_names = {}
    for name in args:
        key = name[0].title() # key = первая заглавная буква имени name 
        if key not in dict_names:
            dict_names[key] = []
        dict_names[key].append(name)
        
    return(dict_names)



def sort_dict_key(dictionary):
    # function sortes by key

    # Sorted list of tuples by 1st value(key)
    sorted_tuple = sorted(dictionary.items(), key = lambda x: x[0])
    # Conversion back to dictionary:
    dict(sorted_tuple)

    return(sorted_tuple)


dict_names = thesaurus('Nikola', 'Semen', 'Seniy', 'Fedor', 'Svetlana', 'Andrey'
               'Ivan', 'Danil', 'Anna', 'Victor', 'Alexey', 'Denis', 'Petr', 'Semen')

print('Dictionary consist the list of names:\n\n', dict_names)
print('Sorted dictionary by key:\n\n', sort_dict_key(dict_names))

# Sorting the dictionary "dict_names" by values:
print(sorted(dict_names.items(), key = lambda x: x[1]))








"""
Task_5.

 Реализовать функцию get_jokes(), возвращающую n шуток, 
 сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

        Например:

>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]

Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках 
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""

import random

# Lists of random words:
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]



def get_jokes(n, flag = 0):

    list_jokes = []

    if flag == 1 and n <= 5:
        list_nouns = []
        list_adv = []
        list_adj = []

        while (len(list_nouns) < n) or (len(list_adv) < n) or (len(list_adj) < n):

            noun = random.choice(nouns)
            if noun not in list_nouns:
                list_nouns.append(noun)

            adv = random.choice(adverbs)
            if adv not in list_adv:
                list_adv.append(adv)

            adj = random.choice(adjectives)
            if adj not in list_adj:
                list_adj.append(adj)

        for i in range(n):
            
            joke = ' '.join([list_nouns[i], list_adv[i], list_adj[i]])
            list_jokes.append(joke)

            """
            Или можно вывести с помощью zip()
            """
        #for noun, adv, adj in zip(list_nouns, list_adv, list_adj):
          #  joke = ' '.join([noun, adv, adj])
           # list_jokes.append(joke)

        """
        Если flag = False, то слова в шутках
        могут повторяться
        """

    elif not flag or n > 5: 

        for i in range(n):
            noun = random.choice(nouns)
            adv = random.choice(adverbs)
            adj = random.choice(adjectives)
            joke = ' '.join([noun, adv, adj])
            list_jokes.append(joke)

    return list_jokes

print(get_jokes(3, flag = 1))
print(get_jokes(7, 1))
print(get_jokes(4))
print(get_jokes(8))





    



    



