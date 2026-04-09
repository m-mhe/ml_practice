def batch_generator(*args, batchSize):
    for i in range(0, len(args), batchSize):
        yield args[i: i+batchSize]

data = [1, 2, 3, 4, 5, 6, 7, 8]
x = batch_generator(1, 2, 3, 4, 5, 6, 7, 8, batchSize = 3)
print(next(x))

print(next(x))

print(next(x))
