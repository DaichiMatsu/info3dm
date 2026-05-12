import datasets

X, Y = datasets.load_liner_example1()
ex_X = datasets.polynomial2_features(X)

print(f"{X=}")
print(f"{ex_X=}")
