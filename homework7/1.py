from random import randint
l = [randint(-10, 10) for i in range(5)]
ls=[]
for i in range(0, len(l)):
        ls.append(l[i-1])
print("Рандомный список -",l)
print('Измененный список -',ls)
