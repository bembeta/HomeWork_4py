# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import random
a = int(input("введите количество кустов: "))
b = list(random.randint(0, 10) for i in range(a))
result = []
i = 0
sum = 0

print(b)

while (i < a):
    if (i == a - 1):
        sum = b[i] + b[i - 1] + b[0]
    else:
        sum = b[i] + b[i - 1] + b[i + 1]
        result.append(sum)
        result.sort()
    i += 1

print(f"максимальное число ягод за сбор {result[-1]}")