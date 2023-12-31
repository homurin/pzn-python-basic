maxLength = int(input("input maxlength: "))

name = []
age = []

for i in range(0, maxLength):
    print(f"data - {i+1}")
    nameInput = input("input name: ")
    ageInput = int(input("age input: "))
    name.append(nameInput)
    age.append(ageInput)

for i in range(0, maxLength):
    print(f'{i+1}. name: {name[i]}, age: {age[i]}')
