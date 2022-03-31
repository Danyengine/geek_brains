"""
Task_1
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
>>> odd_to_15 = odd_nums(15)
>>> next(odd_to_15)
1
>>> next(odd_to_15)
3
...
>>> next(odd_to_15)
15
>>> next(odd_to_15)
...StopIteration...
Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""
from itertools import islice
import sys

n = int(input('До какого предела вывести нечетные числа?'))

def gen_odd_num(n):
    for num in range(1, n + 1, 2):
        yield num
  
# вывод элементов генератора через цикл for:
i = 0
for num in gen_odd_num(n):
    if n % 2 == 0:              # if n is even
        if i == (n // 2) - 1:
            print(num)          # дополнительные условия для того, чтобы при выводе в конце не было запятой
            break
        print(num, end = ',')   
        i +=1
    else:                       # if n is even
        if i == (n // 2):     
            print(num)
            break
        print(num, end = ',')
        i +=1
   

# output by object - variable + "*"":
odd_to_21 = gen_odd_num(n)
print(*odd_to_21, sep = ',')

# output by method itertools.islice:
print(*islice(gen_odd_num(n),0, sys.maxsize), sep = ',')

"""
Task 2.
не используя ключевое слово "yield"
"""

gen_nums = (num for num in range(1, n + 1, 2))
print(*gen_nums, sep = ',')