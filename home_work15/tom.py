students = [
    {'name': 'Jennifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nikolas', 'final': 98}
]

maxsax = max(students, key=lambda x: x['final'])
minsax = min(students, key=lambda x: x['final'])
print(maxsax)
print(minsax)