import re
a = input("Введите emai")
if len(re.findall("@", a))==1:
        print("cool")
else:
        print("Некорректный email")
