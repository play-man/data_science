from sklearn import datasets
from matplotlib import pyplot as plt
from linear_reg import LinReg

diabetes = datasets.load_diabetes()
x_real = diabetes.data
y_real = diabetes.target

print(x_real[:40])
m = x_real.shape[0]
x = [i for i in range(m)]
LR = LinReg()
LR.gradient_descent(x_real, y_real)
y_exp = LR.predict_values(x_real)

a = 0
b = 10
plt.plot(x[a:b], y_real[a:b], color='g',label="Real target")
plt.plot(x[a:b], y_exp[a:b], color='r',label="Predicted target")
plt.show()
