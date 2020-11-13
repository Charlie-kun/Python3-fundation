import pandas as pd
from sklearn.datasets import load_breast_cancer
breast_cancer_data=load_breast_cancer()

df_data=pd.DataFrame(breast_cancer_data.data)
df_labels=pd.DataFrame(breast_cancer_data.target)

print(df_data)
print(df_labels)

from sklearn.model_selection import train_test_split
training_data, validation_data, training_labels, validation_labels=train_test_split(df_data, df_labels, test_size=0.2, random_state=100)

print(training_data)
print(validation_data)

from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=3)
classifier.fit(training_data, training_labels)
print("neighbors=3",classifier.score(validation_data,validation_labels))

classifier10=KNeighborsClassifier(n_neighbors=10)
classifier10.fit(training_data, training_labels)
print("neighbors=10",classifier10.score(validation_data,validation_labels))

import matplotlib.pyplot as plt

k_list=range(1,101)
k_value=[]
accuracies=[]
t_accuracies=[]

for k in k_list:
    classifier=KNeighborsClassifier(n_neighbors=k)
    classifier.fit(training_data, training_labels)
    accuracies.append(classifier.score(validation_data, validation_labels))
    t_accuracies.append(classifier.score(training_data, training_labels))
    k_value.append(k)

plt.plot(k_list, accuracies)
plt.plot(k_value,t_accuracies)
plt.xlabel("k")
plt.ylabel("validation_accuracy")
plt.title("Breast Cancer Classifier Accuracy")
plt.show()

from sklearn.datasets import make_blobs
import mglearn
x,y=make_blobs(random_state=42)
mglearn.discrete_scatter(x[:,0], x[:,1],y)
plt.xlabel("0")
plt.ylabel("1")
plt.legend(["class 0", "class 1", "class 2"])
plt.show()

import numpy as np
from sklearn.svm import LinearSVC

liner_svm=LinearSVC(C=0.01)
liner_svm.fit(x,y)

mglearn.plots.plot_2d_classification(liner_svm, x, fill=True, alpha=.7)
mglearn.discrete_scatter(x[:,0],x[:,1],y)
line=np.linspace(-15,15)
for coef,intercept, color in zip(liner_svm.coef_, liner_svm.intercept_, mglearn.cm3.colors):

    plt.plot(line,-(line * coef[0]+intercept)/coef[1], c=color)
    plt.legend(['class 0', 'class1', 'class2', 'class 0 edge', 'class 1 edge', 'class 2 dege'],loc=(1.01, 0.3))
    plt.xlabel("0")
    plt.ylabel("1")
    plt.show()

cancer=load_breast_cancer()
from sklearn.tree import DecisionTreeClassifier
x_train,x_test, y_train, y_test=train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=42)
tree=DecisionTreeClassifier(random_state=0)
tree.fit(x_train, y_train)
print("train set correct percent : {:3f}".format(tree.score(x_train,y_train)))
print("test set correct percent : {:3f}".format(tree.score(x_test,y_test)))

from sklearn.tree import export_graphviz
export_graphviz(tree, out_file="tree.dot", class_names=["Critical", "correct"], feature_names=breast_cancer_data.feature_names, impurity=False, filled=True)

from IPython.display import display
import graphviz
with open("tree.dot", encoding='UTF-8') as f:
    dot_graph=f.read()
    display(graphviz.Source(dot_graph))

def plot_feature_impotances_cancer(model):
    n_features=cancer.data.shape[1]
    plt.barh(range(n_features),model.feature_importances_, align="center")
    plt.yticks(np.arange(n_features), cancer.feature_names)
    plt.xlabel("important")
    plt.ylabel("charactor")
    plt.ylim(-1,n_features)
    plot_feature_impotances_cancer(tree)
