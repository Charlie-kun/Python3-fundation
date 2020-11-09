#class 13
'''
import pandas as pd

titanic_df=pd.read_csv("./13차수 데이터/titanic.csv")
'''
'''
print(titanic_df.head(5))

print(titanic_df.info())
'''

'''
titanic_df.drop(columns=['Name', 'Cabin', 'Embarked', 'Ticket'], inplace=True)

print(titanic_df)

print(titanic_df.tail(10))

print(titanic_df[titanic_df.duplicated()])
'''
'''
titanic_df.drop_duplicates(inplace=True)        # Delete duplicate data
titanic_df[titanic_df.duplicated()]
print(titanic_df.tail(10))
'''
'''
print(titanic_df.isnull().head(10))

titanic_df.dropna(inplace=True)         #Delete null
print(titanic_df.isnull().sum())
'''
'''
titanic_df.rename(columns=, inplace=True)

print(titanic_df.columns)
'''
'''
print(titanic_df.head(10))
print(titanic_df.replace({'Gender':{'Female':1}}, inplace=True))
'''
'''
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

scaler=MinMaxScaler()

titanic_df[['Fare']]=scaler.fit_transform(titanic_df[['Fare']])

print(titanic_df.describe())

titanic_df.drop(titanic_df[titanic_df.Fare>=1].index, inplace=True)

titanic_df['Fare'].plot(kind="box")
plt.show()

'''

import pandas as pd

insur_df=pd.read_csv("./13차수 데이터/insurance.csv")

print(insur_df.head(5))

insur_df.drop(columns='Number', inplace=True)

print(insur_df.head(5))     # 1. Drop Number columns

insur_df.drop_duplicates(inplace=True)

print(insur_df)     #2. Drop duplicaate

insur_df.dropna(inplace=True)

print(insur_df)     #3. dropna

print(insur_df.columns)

insur_df.rename(columns={'Gender':'gender', 'Insurance Fee': 'charges'}, inplace=True)

print(insur_df.columns)     #4 Rename Gender and Insurance Fee

insur_df.replace({'gender':{'male':0}}, inplace=True)
insur_df.replace({'gender':{'female':1}}, inplace=True)

print(insur_df)     #5 Replace Gender male :0, female :1

print(insur_df.describe())

from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

scaler=MinMaxScaler()
insur_df[['charges']]=scaler.fit_transform(insur_df[['charges']])
print(insur_df.describe())      #6. MinMaxScaler

insur_df['charges'].plot(kind="box")
plt.show()

insur_df.drop(insur_df[insur_df.charges >=1].index, inplace=True)
insur_df['charges'].plot(kind="box")
plt.show()                      #7. Normalize

corr=insur_df.corr(method='pearson')

print(corr)

insur_df.drop(insur_df[-0.1<=corr & corr <=0.1].index, inplace=True)
print(insur_df)
