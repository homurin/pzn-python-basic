def showAllData(data):
    text = ""
    for i in range(0, len(data)):
        text += f"{i+1}. {data[i]}\n"
    return text


def main():
    name = []
    isStop = ""
    while isStop != "n":
        memberName = input("input guild member name here: ")
        name.append(memberName)
        print("this is your guild member: ")
        print(showAllData(name))
        decision = input("are you want to add new guild member?[y/N]").lower()
        isStop = "n" if decision != "y" else ''
        print(isStop and ('\nhave a nice day :)\n'))


main()
