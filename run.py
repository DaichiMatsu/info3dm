import datasets

X, Y = datasets.load_liner_example1()
print(X)
print(X[0])
print(Y)


import regression

model = regression.LinerRegression()
print(model.x)
