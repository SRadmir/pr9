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
      

        

        
