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
                
                


        
