# Task_01
# a = int(input('Введите число а: '))
# b = int(input('Введите число b: '))
# print(a, b)

# Task_02
# time = int(input('Введите количество секунд: '))
# seconds = time % 60 # Например 6500 секунд остаток будет 20 секунд
# time = time / 60 # 6500 секунд - 20 секунд / 60 = 108 минут
# minutes = time % 60 #Остаток от деления = 48. 108 - 48 = 60
# time = time / 60 #60 / 60 = 1
# hours = time
# print('%d' % hours,'%d' % minutes,'%d' % seconds)

# Task_3
# n = int(input("Введите число: "))
# z = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
# print("Сумма:  n + nn + nnn - %d" % z)

#Task_4
# n = int(input("Введите целое положительное число:"))
# max_num = n % 10
# while n >= 1:
#     n = n // 10
#     if n % 10 > max_num:
#         max_num = n % 10
#     if n > 9:
#         continue
#     else:
#         print("Макс цифра в числе ", max_num)
#         break

# Task_5
# profit = float(input("Введите выручку предприятия "))
# costs = float(input("Введите издержки предприятия "))
# if profit > costs:
#     print(f"Предприятие работает с прибылью. Рентабельность выручки составила {profit / costs:.2f}")
#     workers = int(input("Введите количество сотрудников предприятия "))
#     print(f"Прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
# elif profit == costs:
#     print("Предприятие работает в ноль")
# else:
#     print("Предприятие работает в убыток")

Task_6
a = int(input("Введите данные по км первого дня"))
b = int(input("Введите желаемый результат в км "))
result_days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = result_km + a
print(f"Вы достигнете  показателей на %.d день" % result_days)