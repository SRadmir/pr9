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

