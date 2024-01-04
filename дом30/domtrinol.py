#######################1
#print("введите  с клавиатуры два числа чтобы определить сумму нечетных, четных и кратных 9.")
#
#a = int(input("ВВедите  в диапозоне число"))
#b = int(input("ВВедите в диапозоне число"))
#chet = 0
#nechet = 0
#cumma = 0
#chislo = 0
#krat9 = 0
#sredkrat9 = 0
#for i in range(a, b + 1):
#    if i % 2 == 0:
#        chet += i
#        nechet += 1
#    else:
#        cumma += i
#        chislo += 1
#    if i % 9 == 0:
#        krat9 += i
#        sredkrat9 += 1
#        arifchet = chet / nechet
#        arifnechet = cumma / chislo
#        arifkrat9 = krat9 / sredkrat9
#        print("Сумма четных чисел: ", chet)
#        print("Сумма нечетных чисел: ", nechet)
#        print("Сумма чисел, кратных 9: ", krat9)
#        print("Среднее арифметическое четных чисел: ", arifchet)
#        print("Среднее арифметическое нечетных чисел: ", arifnechet)
#        print("Среднее арифметическое чисел, кратных 9: ", arifkrat9)
####################2
#a = int(input("введите число, отобразится вертикальная линия"))
#for i in range(a):
#    for j in range(a):
#        if i == 0:
#            print("%")
##########################3
# print("НЕ вводите число 7")
# while True:
#
#     a = int(input("Введите число"))
#     if a == 7:
#         print("Пока")
#         print()
#         break
#     elif a > 0:
#         print("Хорошо")
#     elif a < 0:
#         print("Плохо")
#     else:
#         print("Норм")

###################################4
print("найти сумму  минимальное и максимальное число. Число 7 прекращает работу. ")
summa = 0
max = float()
min = float()
while True:
    a = int(input("Введите число:"))
    summa += a

    if a > max:
        max, min = a, a
    elif min > a:
        max, min = a, a
    elif a == 7:
        print("пока")
        break
    print("Сумма чисел:", summa)
    print("Максимальное число:", max)
    print("Минимальное число:", min)
    print()





