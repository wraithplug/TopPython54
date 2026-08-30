company = {
'emp1': {'name': 'Jhon', 'salary': 7500},
'emp2': {'name': 'Emma', 'salary': 8000},
'emp3': {'name': 'Brad', 'salary': 6500},
}
print(company['emp3'])
print(company['emp3']['salary'])
company['emp3']['salary'] = 8500
for key in company:

    print(key)
    print("name :", company[key]['name'])
    print("salary :", company[key]['salary'])

