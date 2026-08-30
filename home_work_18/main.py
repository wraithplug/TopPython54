srezslovo = input("Введите строку: ")
first_h = srezslovo.find('h')
last_h = srezslovo.rfind('h')

srez = srezslovo[:first_h] + srezslovo[first_h + 1 : last_h] [::-1] + srezslovo[last_h:]


print(srez)
