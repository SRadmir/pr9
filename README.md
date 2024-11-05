# Это практическая работа №8 
## задание 1 ##
### код
```
def isdigit(di):
        return di.lstrip('-').replace('.', '', 1).isdigit()
while True:
        l=[]
        a = input("Введите число а:")
        if a.lower() == 'stop' or  a.lower() == 'break':
                break
        if not isdigit(a):
                print("Некорректный ввод ")
                continue
        a=float(a)
        b= input("Введите число b:")

        if not isdigit(b):
                print("Некорректный ввод")
                continue
        b=float(b)
        if a<b:
                for i in range(int(a)-1,int(b)+1):
                        if a<i<b:
                                l.append(i**2)
                                continue
                print(l)
        elif a>b:
                for i in range(int(b)-1, int(a)+1):
                        if b<i<a:
                                l.append(i**2)
                                continue
                print(l)
        else:
                print("a и b равны")


```
## задание 2 ##
```
def isdigit(di):
        return di.lstrip('-').replace('.', '', 1).isdigit()
l=[]
while True:
        a = input("Введите целое число (или end для завершения)")
        b=a
        if a == 'end':
                print(l)
                break
        if not isdigit(a):
                print("Некорректо")
                continue
        if b.count('.')!=0:
                print("Не целое число")
        a=int(float((a)))
        if a%2!=0 and b.count('.')==0 :
                l.append(a)
      
```
## задание 3 ##

```
def isdigit(di):
        return di.lstrip('-').replace('.', '', 1).isdigit()
l=[]
c=0
while True:
        a = input("Введите целое число (или end для завершения)")
        b=a
        if a == 'end':
                print(l)
                print("Кол-во четных - ",c)
                print("Кол-во нечетных - ", len(l)-c)
                break
        if not isdigit(a):
                print("Некорректо")
                continue
        if b.count('.')!=0:
                print("Не целое число")
        a=int(float((a)))
        if b.count('.')==0 :
                l.append(a)
                if a%2==0:
                        c+=1
                
```
## задание 4 ##

```
from random import randint
l = [randint(-10, 10) for i in range(10)]
answ=[]
if len(l)!=0:
        for i in range(0, len(l)):
                if l[i]> l[i-1]:
                        answ.append(l[i])
        if len(answ)!=0:
                print("Рандомный список", l)
                print("Список элементов, которые больше предыдущего элемента", answ)
        else:
                print("В списке нет элементов, которые больше предыдущего элемента")
else:
        print("список пустой")
```

## задание 5 ##

```
from random import randint
l = [randint(-10, 10) for i in range(10)]
a=max(l)
b=min(l)
indexa = l.index(a)
indexb = l.index(b)
print("Список до ",l)
print("максимальный элемент", a, "с индексом", indexa)
print("минимальный элемент", b, "с индексом", indexb)
l[indexa], l[indexb] = l[indexb], l[indexa]  
print("Список после",l)

                
```

## задание 6 ##

```
from random import randint
l = [randint(-10, 10) for i in range(5)]
ls=[]
for i in range(0, len(l)):
        ls.append(l[i-1])
print("Рандомный список -",l)
print('Измененный список -',ls)

                
```
## задание 7 ##

```
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

                
```
## задание 6 ##

```
import re
def em(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        match = re.fullmatch(pattern, email)
        if match:
                group = email.split('@')
                name = group[0]
                domain = group[1]
                return name, domain
        else:
                return None, None
while True:
        a = input("Введите емаил или stop ")
        if a =="stop":
                break
        name, domain = em(a)
        if name and domain:
                print("Имя пользователя: ", name)
                print("Домен: ", domain)
                continue
        else:
                print("Неверный формат электронной почты")
                continue

                
```