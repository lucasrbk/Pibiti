import tensorflow
import keras
import sklearn
from sklearn import linear_model
import pandas as pd
import numpy as np
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

data = pd.read_csv("train.csv", sep=",")

mass = data["mean_atomic_mass"]

predict = "critical_temp"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])



x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.5)

linear = linear_model.LinearRegression()

#with open("linearDump.pickle","wb") as f:
#    pickle.dump(linear, f)

pickle_in = open("linearDump.pickle","rb")
linear = pickle.load(pickle_in)

linear.fit(x_train, y_train)
score = linear.score(x_test, y_test)

print('Score', score)
print('Coeficiente: \n', linear.coef_)

p = "critical_temp"

style.use("ggplot")
pyplot.scatter(data[p], data["mean_atomic_mass"])
pyplot.xlabel("Critical temperature")
pyplot.ylabel("Atomic mass")
pyplot.savefig("linearImage.png")

