def sum(*number_list):
    result = 0
    for i in number_list:
        result += i
    return (number_list, result)


number_list, result = sum(1, 1, 1, 1, 1)

print(f"total {number_list} is {result}")
