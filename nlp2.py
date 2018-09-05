from sklearn.datasets import load_digits
digits_dataset=load_digits()
print(type(digits_dataset))
print(digits_dataset.data)
print(digits_dataset.target)
