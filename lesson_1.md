# Домашняя работа_1
# Задание 1
'''
Реализовать вывод информации о промежутке времени в зависимости от его
продолжительности duration в секундах: до минуты:
<s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
'''

min_1 = 60
hour_1 = 3600
day_1 = 3600*24


def data_time(sec):
    
    # Вывод до минуты:
    if sec < min_1:
        return (sec, 'secands')
    
    # Вывод до часа:
    elif min_1 <= sec < hour_1:
        minuts = sec // 60  # целое от деления
        sec = sec % min_1
        return ('{} мин {} сек'.format(minuts, sec))
    
    # Вывод до дня:
    elif  hour_1 <= sec < day_1:
        hours = sec // 3600
        sec %= hour_1
        minuts = sec // min_1
        sec = sec % min_1
        return ('{} ч {} мин {} сек'.format(hours, minuts, sec))
    
    # Вывод до года:
    elif sec >= day_1:
        days = sec // day_1
        sec %= day_1
        hours = sec // hour_1
        sec %= hour_1
        minuts = sec // min_1
        sec %= min_1
        return ('{} дн {} ч {} мин {} сек'.format(days, hours, minuts, sec))

duration = int(input('Введите текущее время в секундах: '))
print('\n',data_time(duration))

  
  
  
  
  
# Задание 2
  '''
Создать список, состоящий из кубов нечётных чисел от 1 до 1000
'''

# method generetor (list comprehension):
#cube_lst = [i**3 for i in range(1,1001) if i % 2 != 0]



#cube_lst = []            # Create empty list
#for x in range(1,1001):
   # if x % 2 != 0:       # uneven numbers
    #    cube_lst.append(x**3)

'''
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7
'''
# method generetor (list comprehension):

#cube_lst = [i**3 for i in range(1,1001) if i % 2 != 0]


# method circle for + condition if

cube_lst = []    # list of uneven numbers cubed

for num in range(1,1001):
    if num % 2 != 0:
        cube_lst.append(num**3)



cube_even_7 = [] # list of numbers that (% 7 == 0)


for i in range(len(cube_lst)):

    num = cube_lst[i]
    sum_digits = 0     # сумма цифр i-го числа
    while num != 0:
        sum_digits += num%10
        num //=10
    if sum_digits % 7 == 0:
        cube_even_7.append(cube_lst[i])


# Сумма чисел, нацело делящиеся на 7
sum_num_even_7 = 0
for num in cube_even_7:
    sum_num_even_7 += num
    
print(sum_num_even_7)


'''
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
сумма цифр которых делится нацело на 7.
'''
# Чтобы можно было реализовать данный алгоритм
# можно каждый раз выполнять через функцию

def sum_digits_7(num_list,value):
    list_cube_7 = []
    sum_num_even_7 = 0
    for i in range(len(num_list)):
        num = num_list[i] + value
        sum_digits = 0
        
        while num != 0:
            sum_digits += num % 10
            num //= 10
        if sum_digits % 7 == 0:
            list_cube_7.append(num_list[i] + value)
            
    for numbers in list_cube_7:
        sum_num_even_7 += numbers
    return (sum_num_even_7)
    

value = int(input('Какое добавить число? '))

print('\n',sum_digits_7(cube_lst, value))
  
# вывод
  Какое добавить число? 17

 15392909930
  
  
  
  
  
  # Задание 3
  
  '''
Реализовать склонение слова «процент» во фразе «N процентов».
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
'''

for i in range(1,101):
    new_str=str(i)
    new_list = list(new_str)
    if int(new_list[-1]) == 1 and i != 11:
        print('{} процент'.format(i))
    elif int(new_list[-1])>1 and int(new_list[-1])<= 4:
        if  i> 10 and i<= 14:
            print('{} процентов'.format(i))
        else:
            print('{} процента'.format(i))
    else:
        print('{} процентов'.format(i))
  
  
  
