dict1 = {
    1: {"name": "Иван", "age": 17},
    2: {"name": "Максим", "age": 27},
    3: {"name": "Петр", "age": 30}
}
dict2 = {
    2: {"name": "Мария", "age": 20},
    4: {"name": "Анна", "age": 22}
}
huz = dict1.copy()
huz.update(dict2)

ban = {}
for user_id,user_data in huz.items():
    if user_data['age'] >= 18:
        ban[user_id] = user_data


print(ban)