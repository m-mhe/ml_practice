listNumber = list(range(1,7))
print(listNumber)

listEvenSqr = list(map(lambda x: x**2,list(filter(lambda x: x%2==0, listNumber))))
print(listEvenSqr)