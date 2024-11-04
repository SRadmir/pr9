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
