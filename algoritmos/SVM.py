import numpy as np
import pandas as pd
import sklearn
from matplotlib import pyplot, style
from sklearn import preprocessing
from sklearn import svm
from sklearn import metrics


data = pd.read_csv("train.csv", sep=",")

mass = data["mean_atomic_mass"]

le = preprocessing.LabelEncoder()
cls = le.fit_transform(list(data["critical_temp"]))

predict = "critical_temp"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

y = list(cls)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.5)

model = svm.SVC()
model.fit(x_train, y_train)


score = metrics.accuracy_score(y_test, y_test)

print(score)

p = "critical_temp"

style.use("ggplot")
pyplot.scatter(data[p], data["mean_atomic_mass"])
pyplot.xlabel("Critical temperature")
pyplot.ylabel("Atomic mass")
pyplot.savefig("SVMImage.png")