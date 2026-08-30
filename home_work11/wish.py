
def wish():
    s = ('ab', 'abcd', 'cde', 'abc', 'def')
    search = input("s = ")
    if search in s:
        print(f'{search} yes')
    else:
        print(f'{search} no :(')
if __name__ == '__main__':
    wish()