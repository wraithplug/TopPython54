people = [("Иван",25),("Мария",23),("Петр",25),("Анна",23)]
result = {}

for name,age in people:
    if age in result:
        result[age].append(name)
        continue
    else:
        result[age] = [name]

print(result)