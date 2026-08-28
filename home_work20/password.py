import re


def validate_name(name):
    return re.findall(r"^[-\w@]{6,18}$", name, re.I)
password = input("Enter your password: ")
result = validate_name(password)
if result:
    print("Пароль принят")
else:
    print("Пароль не подходит")
print(result)



