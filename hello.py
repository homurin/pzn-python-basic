def sayHello(str):
    print("Hello "+str)

def greeting(dayTime):
    if(dayTime == "day"):
       return f'good day {dayTime}'
    return 'Hello!'

sayHello('Fajrin') 

print(greeting("night"))
