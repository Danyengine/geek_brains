"""
Task 5
Представлен список чисел. Определить элементы списка, не имеющие повторений. 
Сформировать из этих элементов список с сохранением порядка их следования 
в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
"""

# 1st way
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
src_copy = src[:]
sort_list = []
for i in range(len(src_copy)):

    while src_copy != []:
  
        elem = src_copy.pop(i)

        if elem not in src_copy:
            sort_list.append(elem)
        else:
            while elem in src_copy:
                src_copy.remove(elem)
                
print(sort_list)
print(len(src_copy))



# 2nd way:
unic_numbers = [num for num in src if src.count(num) == 1]
print(unic_numbers) 




# 3rd way:
unic_nums = []
for elem_1 in src_copy:
    i = 0
    for elem_2 in src_copy:
        if elem_1 == elem_2:
            i +=1
    if i == 1:
        unic_nums.append(elem_1)

print(unic_nums)