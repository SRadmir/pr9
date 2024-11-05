def isdigit(di):
        return di.lstrip('-').replace('.', '', 1).isdigit()
from random import randint
while True:
        a1 = input("Введите число для первого билета (или stop для остановки игры)")
        if a1.lower() == "stop":
                break
        if not isdigit(a1) or -10>float(a1) or float(a1)>10 and a1.count('.') :
                print("Некорректный ввод( Нужно ввести  число от -10 до 10)")
                continue
        if a1.count('.')!=0:
                print("Нужно ввести целое число")
                continue
        a2 = input("Введите число для первого билета (или stop для остановки игры)")
        if a2.lower() == "stop":
                break
        if not isdigit(a2) or -10>float(a2) or float(a2)>10 and a2.count('.') :
                print("Некорректный ввод( Нужно ввести  число от -10 до 10)")
                continue
        if a2.count('.')!=0:
                print("Нужно ввести целое число")
                continue
        a3 = input("Введите число для первого билета (или stop для остановки игры)")
        if a3.lower() == "stop":
                break
        if not isdigit(a3) or -10>float(a3) or float(a3)>10 and a3.count('.') :
                print("Некорректный ввод( Нужно ввести  число от -10 до 10)")
                continue
        if a3.count('.')!=0:
                print("Нужно ввести целое число")
                continue
        a4 = input("Введите число для первого билета (или stop для остановки игры)")
        if a4.lower() == "stop":
                break
        if not isdigit(a4) or -10>float(a4) or float(a4)>10 and a4.count('.') :
                print("Некорректный ввод( Нужно ввести  число от -10 до 10)")
                continue
        if a4.count('.')!=0:
                print("Нужно ввести целое число")
                continue
        a5 = input("Введите число для первого билета (или stop для остановки игры)")
        if a5.lower() == "stop":
                break
        if not isdigit(a5) or -10>float(a5) or float(a5)>10 and a5.count('.') :
                print("Некорректный ввод( Нужно ввести  число от -10 до 10)")
                continue
        if a5.count('.')!=0:
                print("Нужно ввести целое число")
                continue
        c1=randint(-10,10)
        c2=randint(-10,10)
        c3=randint(-10,10)
        c4=randint(-10,10)
        c5=randint(-10,10)
        ticket=[]
        bilet1 = [randint(-10, 10) for i in range(5)]
        bilet2 = [randint(-10, 10) for i in range(5)]
        bilet3 = [randint(-10, 10) for i in range(5)]
        bilet4 = [randint(-10, 10) for i in range(5)]
        bilet5 = [randint(-10, 10) for i in range(5)]
        ticket.append(bilet1)
        ticket.append(bilet2)
        ticket.append(bilet3)
        ticket.append(bilet4)
        ticket.append(bilet5)
        countergamer= ticket[0].count(int(a1))+ticket[1].count(int(a2))+ticket[2].count(int(a3))+ticket[3].count(int(a4))+ticket[4].count(int(a5))
        counterpk=ticket[0].count(c1)+ticket[1].count(c2)+ticket[2].count(c3)+ticket[3].count(c4)+ticket[4].count(c5)
        if countergamer>counterpk:
                print("Позравляю вы победили!!")
                print('Билет 1 -', ticket[0], "Вы выбрали - ",a1, "Компьютер выбрал - ",c1)
                print('Билет 2 -', ticket[1], "Вы выбрали - ",a2, "Компьютер выбрал - ",c2)
                print('Билет 3 -', ticket[2], "Вы выбрали - ",a3, "Компьютер выбрал - ",c3)
                print('Билет 4 -', ticket[3], "Вы выбрали - ", a4,"Компьютер выбрал - ",c4)
                print('Билет 5 -', ticket[4], "Вы выбрали - ", a5,"Компьютер выбрал - ",c5)
                continue
        elif countergamer<counterpk:
                print("Вы проиграли!!")
                print('Билет 1 -', ticket[0], "Вы выбрали - ",a1, "Компьютер выбрал - ",c1)
                print('Билет 2 -', ticket[1], "Вы выбрали - ",a2, "Компьютер выбрал - ",c2)
                print('Билет 3 -', ticket[2], "Вы выбрали - ",a3, "Компьютер выбрал - ",c3)
                print('Билет 4 -', ticket[3], "Вы выбрали - ",a4, "Компьютер выбрал - ",c4)
                print('Билет 5 -', ticket[4], "Вы выбрали - ",a5, "Компьютер выбрал - ",c5)
                continue
        else:
                print("Ничья")
                print('Билет 1 -', ticket[0], "Вы выбрали - ",a1, "Компьютер выбрал - ",c1)
                print('Билет 2 -', ticket[1], "Вы выбрали - ",a2, "Компьютер выбрал - ",c2)
                print('Билет 3 -', ticket[2], "Вы выбрали - ",a3, "Компьютер выбрал - ",c3)
                print('Билет 4 -', ticket[3], "Вы выбрали - ",a4, "Компьютер выбрал - ",c4)
                print('Билет 5 -', ticket[4], "Вы выбрали - ",a5, "Компьютер выбрал - ",c5)
                continue
