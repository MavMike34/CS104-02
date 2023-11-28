names = []

for i in range(10):
    currentName = input('Enter name: ')
    names.append(currentName)

print(names)

for i in range(10):
    print(names.pop(0))
    

print(names)
