students = [
    {'name': 'Jennifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nikolas', 'final': 98}
]
prikol = sorted(students, key=lambda x: x['final'] ,reverse=True)
sortpls =  sorted(students, key=lambda x: x['name'])
print("По оценкам убывание:", prikol)
print("По имени возрастани:", sortpls)

