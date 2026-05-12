import regression
import datasets

X, Y = datasets.load_nonlinear_example1()
ex_X = datasets.polynomial2_features(X)

print(ex_X)
model = regression.RidgeRegression(alpha=0)
print(f"{model.alpha=}")
model.fit(ex_X, Y)
print(f"{model.theta=}")