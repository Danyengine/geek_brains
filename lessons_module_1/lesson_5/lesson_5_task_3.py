"""
task 3
Есть два списка:
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors. 
Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
('Станислав', None)

### Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать, в каких ситуациях генератор даст эффект. 
"""

from itertools import zip_longest



tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

# method 1. I used zip() + generator comprehension:

# генератор, возвращающий кортежи вида (<tutor>, <klass>)
pairs = ((name, klass) for name, klass in zip(tutors, klasses))
print(*pairs, sep = ', ')

#Если в списке klasses меньше элементов, чем в списке tutors, 
# необходимо вывести последние кортежи в виде: (<tutor>, None), например: ('Станислав', None)

tutors_more = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена', 'Данил', 
    'Виктор', 'Виталий', 'Илья'
]

# apply a method itertools.zip_longest()
# itertools.zip_longest() работает пока самая длинная итерация не будет исчерпана, 
# а пропущенные элементы заполняются значением fillvalue.

pairs_zip_longest = zip_longest(tutors_more, klasses, fillvalue = None)
print(*pairs_zip_longest)
print(type(pairs_zip_longest))




# apply a key word "yield" into function:
def gen_tuples(*args):

    for i in range(len(args[0]) - len(args[1])):
        args[1].append(None)
    for name, klass in zip(args[0], args[1]):
        yield name, klass
    #yield tuple((name, klass) for name, klass in zip(args[0], args[1]))

print(type(gen_pairs))
print(next(gen_tuples(tutors_more, klasses)))
print(*gen_tuples(tutors_more, klasses))

# 3rd method is a generator comprehension = zip_longest + if condition 
gen = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses) if tutor is not None)
print(type(gen))
print(next(gen))

