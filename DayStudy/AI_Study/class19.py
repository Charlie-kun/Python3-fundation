'''
from sklearn.datasets import load_iris

iris=load_iris()

print(iris.target_names)

print(iris.feature_names)

from sklearn.model_selection import train_test_split

trains_points=iris.data
train_labels=iris.target

X_train, X_test, y_train, y_test=train_test_split(trains_points, train_labels, test_size=0.2, random_state=15)

from sklearn.tree import DecisionTreeClassifier

classifier=DecisionTreeClassifier(random_state=0)

classifier.fit(X_train,y_train)

guesses=classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

print("confusion Matrix : ", confusion_matrix(y_test,guesses))

print("Accuracy : ", accuracy_score(y_test, guesses))
'''

'''
import pandas as pd

data=pd.read_csv("./19차수 data/pima-indians-diabetes.csv")

print(data.info())

train_points=data.drop("class", axis=1)
train_labels=data["class"]

from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()
train_points_scaled=scaler.fit_transform(train_points)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test=train_test_split(train_points_scaled, train_labels, test_size=0.2, random_state=5)

from sklearn.ensemble import RandomForestClassifier

classifier=RandomForestClassifier(random_state=0, n_estimators=3)

classifier.fit(X_train,y_train)

guesses=classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

print("Confusion Matrix : ", confusion_matrix(y_test, guesses))

print("Accuracy : ", accuracy_score(y_test,guesses))

from sklearn.ensemble import RandomForestClassifier

classifier=RandomForestClassifier(random_state=0, n_estimators=5)

classifier.fit(X_train, y_train)

guesses=classifier.predict(X_test)

from sklearn.ensemble import RandomForestClassifier

classifier =RandomForestClassifier(random_state=0, n_estimators=10)

classifier.fit(X_train,y_train)

guesses=classifier.predict(X_test)

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(random_state=0, n_estimators=100)

classifier.fit(X_train, y_train)

guesses = classifier.predict(X_test)

#그래프 그리기
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

n_range = range(1, 100)
accuracy_scores = []

for n in n_range:
    classifier = RandomForestClassifier(random_state=0, n_estimators=n)
    classifier.fit(X_train, y_train)
    guesses = classifier.predict(X_test)
    accuracy_scores.append(accuracy_score(y_test, guesses))
print(accuracy_scores)

import matplotlib.pyplot as plt

plt.plot(n_range, accuracy_scores)
plt.xlabel('Value of n for Random Forest')
plt.ylabel('Testing Accuracy')
plt.show()


# Colum-Dimension 차원->차원 수 증가->reduce
# Check Important features
feature_importances = pd.DataFrame(classifier.feature_importances_,
                                   index = train_points.columns,
                                   columns=['importance']).sort_values('importance', ascending=False)
print(feature_importances)


'''

import pandas as pd
#데이터 작성
data=pd.read_csv("./19차수 data/heart.csv")

train_points=data.drop(["target","thal", "age", "chol", "trestbps", "exang", "slope", "sex","restecg", "fbs"], axis=1)
train_labels=data["target"]

from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()
train_points_scaled=scaler.fit_transform(train_points)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test=train_test_split(train_points_scaled, train_labels, test_size=0.2, random_state=5)

#Decision Tree
from sklearn.tree import DecisionTreeClassifier

classifier=DecisionTreeClassifier(random_state=0)

classifier.fit(X_train,y_train)

guesses=classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

print("confusion Matrix : ", confusion_matrix(y_test,guesses))

print("Accuracy : ", accuracy_score(y_test, guesses))


#Random Forest
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

n_range = range(1, 100)
accuracy_scores = []

for n in n_range:
    classifier = RandomForestClassifier(random_state=0, n_estimators=n)
    classifier.fit(X_train, y_train)
    guesses = classifier.predict(X_test)
    accuracy_scores.append(accuracy_score(y_test, guesses))
print(accuracy_scores)

import matplotlib.pyplot as plt

plt.plot(n_range, accuracy_scores)
plt.xlabel('Value of n for Random Forest')
plt.ylabel('Testing Accuracy')
plt.show()

#Feature_Importances
feature_importances = pd.DataFrame(classifier.feature_importances_,
                                   index = train_points.columns,
                                   columns=['importance']).sort_values('importance', ascending=False)
print(feature_importances)
