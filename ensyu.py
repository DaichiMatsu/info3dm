import numpy as np

# (1) 5個の要素を持つ列ベクトルを作成せよ。値は全て1とする。
a = np.array([[1]] * 5, dtype = float)
print(a)

# (2) 1で作成した列ベクトルのうち、2番目の要素を3.14に更新せよ。なおインデックスは0から数える（0番目、1番目、2番目、、）ものとする。
a[2, 0] = 3.14
print(a)

# (3) 2で作成した列ベクトルを複製し、転置により行ベクトルに変換せよ。
a_copy = a
a_trans = a_copy.T
print(a_copy.T)

# (4) 用意した列ベクトルと行ベクトルの内積を求めよ。
a_inner = np.dot(a, a_trans)
print(a_inner)

# (5) np.random.randを用いて、10個の要素を持つ列ベクトルを作成せよ。
b = np.random.rand(10, 1)
print(b)

# (6) np.random.normalを用いて、平均値10、標準偏差2の正規分布に基づく、2行5列の行列を作成せよ。
c = np.random.normal(10, 2, (2, 5))
print(c)

# (7) 6で作成した行列から、2列目の要素を抜き出だせ。
print(c[:,1])

# (8) 6で作成した行列から、3列目と4列目の要素を抜き出せ。
print(c[:,2], c[:,3])

# (9) np.random.randで5行2列の行列を用意し、6で用意した行列との積を求めよ。
d= np.random.rand(5, 2)

cd = np.dot(c, d)
print(cd)