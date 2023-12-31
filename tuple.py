# tuple does not support item assigment
customers = ("lorem", "ipsum", "dolor")
# customers[0] = "amet" <= wil error
print(customers)

lorem, ipsum, dolor = customers
print(lorem)
print(ipsum)
print(dolor)
