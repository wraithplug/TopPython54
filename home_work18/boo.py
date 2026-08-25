spezslovo = input("Введите строку: ")
first_h = spezslovo.find('h')
last_h = spezslovo.rfind('h')
srez = spezslovo[:first_h] + spezslovo[last_h + 1:]
print(srez)
