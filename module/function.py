def sayHello(name):
    return f'hello {name}'


def sum(*nums):
    result = 0
    for i in nums:
        result += i
    return result
