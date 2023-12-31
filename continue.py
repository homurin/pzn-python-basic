def filterOdd(list):
    result = []
    for oddNumber in list:
        if (oddNumber % 2 != 0):
            result.append(oddNumber)
            continue
        # if condition true this code bellow will be ignored and continue to loop
        print(f"{oddNumber} is not odd number")
    return result


myArr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(filterOdd(myArr))
