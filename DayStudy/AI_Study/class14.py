'''
import numpy as np
import pandas as pd
from sklearn import datasets

from sklearn import model_selection
from sklearn import metrics
from sklearn.linear_model import LinearRegression

dataset=datasets.load_boston()

df=pd.DataFrame(dataset.data,columns=dataset.feature_names)
df['target']=dataset.target
df

df.shape

df.iloc[:,-1].value_counts()
print(df.describe())
'''
'''
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
from sklearn import metrics

from sklearn import datasets
dataset=datasets.load_boston()
x_data=dataset.data
y_data=dataset.target

x_train, x_test, y_train, y_test=model_selection.train_test_split(x_data,y_data,test_size=0.3)

estimator =LinearRegression()

print(estimator.fit(x_train, y_train))

y_pridict=estimator.predict(x_train)

score=metrics.r2_score(y_train,y_pridict)

print(score)

y_pridict=estimator.predict(x_test)

score=metrics.r2_score(y_test, y_pridict)

print(score)
'''

