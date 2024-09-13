import random

first_number = random.randrange(3, 20)
print('1-ое случайное число: ', first_number)

def result(n):
    solved = []
    for i in range(1, n):       #1-ое число из пары
        for j in range(2, n):   #2-ое число из пары
            if n % (i + j) == 0:
                is_def = True
            else:
                continue
            if is_def == True and i < j:
                new_list = []
                solved.append(new_list)
                new_list.append(i)
                new_list.append(j)
    print('Решение (пары чисел): ', solved)
    return result

result = result(first_number)
