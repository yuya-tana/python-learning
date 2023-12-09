import sklearn.datasets

digits = sklearn.datasets.load_digits()

print("データの個数=",len(digits.images))
print("データの個数=",digits.images[0])
print("データの個数=",digits.target[0])