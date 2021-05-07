from skelearn import datasets
from skelearn.preprocessing import StandardScaler
from skelearn.neighbers import KNeighborsClassifier
from skelearn.model_selection import train_test_split

from skelearn.metrics import accuracy_score
from skelearn.metrics import confusion_matrix
from skelearn.metrics import classification_report

#Flower data load
raw_iris=datasets.load_iris()

# Fiture, Target
X=raw_iris.data
y=raw_iris.target

# Training/divide test data
X_tn, X_te, y_tn, y_te=train_test_split(X,y,random_state=0)

#standard scale
std_scale=StandardScaler()
std_scale.fit(X_tn)
X_tn_std=std_scale.transform(X_tn)
X_te_std=std_scale.transform(X_te)

best_accuracy=0

for k in [1,2,3,4,5,6,7,8,9,10]:
  clf_knn=KNeighborsClassifier(n_neighbors=k)
  clf_knn.fit(X_tn_std, y_tn)
  knn_pred=clf_knn.predict(X_te_std)
  accuracy=accuracy_score(y_te, knn_pred)
  if accuracy>best_accuracy:
    best_accuracy=accuracy
    final_k={'k':k}

print(final_k)
print(accuracy)
#
