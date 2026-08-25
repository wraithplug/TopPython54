import re
spisok = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
reg = r"[a-zA-Z0-9а-яА-Я._-]+@[a-zA-Z0-9а-яА-Я.-]+[a-zA-Zа-яА-Я]{2,}"
mails = re.findall(reg, spisok)
print(mails)








