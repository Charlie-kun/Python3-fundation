#21 class
''' Apriori algorithm
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

dataset=[['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
         ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
         ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
         ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
         ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]

te=TransactionEncoder()

te_ary=te.fit(dataset).transform(dataset)
print(te_ary)

df=pd.DataFrame(te_ary, columns=te.columns_)
print(df)

frequnt_itemsets=apriori(df, min_support=0.6, use_colnames=True)
print(frequnt_itemsets)

rules=association_rules(frequnt_itemsets,metric="confidence", min_threshold=0.7)
print(rules)

rules["antecedent_len"]=rules["antecedents"].apply(lambda  x: len(x))

rules[ (rules['antecedent_len']>=2)&
       (rules['confidence']>0.75)]
'''

