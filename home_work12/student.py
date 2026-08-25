spros = int(input("Введите число пользователя: "))
student = {}
for i in range(spros):
    names = input(f"{i + 1}-й студент: ")
    bal = int(input("Введите балл: "))
    student.update({names: bal})
    print(student)