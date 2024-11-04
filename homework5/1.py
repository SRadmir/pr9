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
