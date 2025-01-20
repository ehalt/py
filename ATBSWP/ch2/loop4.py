# continue statement 

while True :
    print('who are you? ')
    name = input()
    if name != 'tori':
        continue
    print('hello, tori. what is the password?')
    password = input()
    if password == 'tori123':
        break
print('Access granted!!')