text = input("Введите строку: ")
slovo = text.split(" ")
count = 0
for i in slovo:
    if i[0] == 'е' or i[0] == 'Е':
        count += 1
print("Количество слов:",count)




