for i in range(1, 100):
    if (i % 50 == 0):
        break
    print(i)

member = []
while True:
    print("welcome to arknights!")
    x = input("input your name: ")
    stop = input("do you want to exit [y/N]")
    if (stop == "y"):
        break
    member.append(x)
    print(member)
