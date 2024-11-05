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
