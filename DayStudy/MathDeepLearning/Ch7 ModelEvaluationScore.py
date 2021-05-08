# Accuracy
from sklearn.metrics import accuracy_score
y_pred=[0,2,1,3]
y_true=[0,1,2,3]
print(accuracy_score(y_true,y_pred))
print(accuracy_score(y_true,y_pred,normalize=False))

#confusion_matrix
from sklearn.metrics import confusion_matrix
y_true=[2,0,2,2,0,1]
y_pred=[0,0,2,2,0,2]
confusion_matrix(y_true,y_pred)

#classification report
from skelarn.metrics import classification_report
y_true=[0,1,2,2,0]
y_pred=[0,0,2,1,0]
target_names=['class0', 'class1', 'class2']
print(classification_report(y_ture, y_pred, target_names=target_names))
