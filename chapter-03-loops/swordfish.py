while True:
    print('who are you?')
    name=input('-')
    if name!='john doe':
        continue
    print('hello joe, what is the password? (it is a fish)')
    password=input('_')
    if password=='swordfish':
        break
print('access granted')