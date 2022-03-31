import enum




"""
Task 4
Представлен список чисел. Необходимо вывести те его элементы, значения которых 
больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
Подсказка: использовать возможности python, изученные на уроке. Подумайте, 
как можно сделать оптимизацию кода по памяти, по скорости.
"""

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


# 1st way is using list.append
sort_list = []
for i in range(1, len(src)):
    if src[i] > src[i-1]:
        sort_list.append(src[i])
print(sort_list)


# 2nd way is using a function object and yield or return (if list is required)
def sort_nums(lst):
    for i in range(1, len(lst)):
        if lst[i] > lst[i-1]:
            yield lst[i]

sort_nums_var = sort_nums(src)
print(*sort_nums_var)


# 3rd way is comprehension in 1 line:
sort_nums = (src[i] for i in range(1,len(src)) if src[i] > src[i-1])
print(*sort_nums)


# 4th way is using method enumerate():
sort_nums = (x for i, x in enumerate(src) if x > src[i-1] and i != 0)
print(*sort_nums)