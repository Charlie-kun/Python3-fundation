#import pandas
#print(pandas.__version__)

'''
import pandas as pd
import numpy as np

data=np.array(['a', 'b', 'c', 'd'])
series=pd.Series(data, index=[100, 101, 102, 103])
print(series)

data={100:'a', 101:'b', 102:'c', 103:'d'}
series=pd.Series(data)
print(series)
'''

'''
import pandas as pd

data={1:'A', 2:'B', 3:'C', 4:'D', 5:'E'}
series=pd.Series(data)
print(series)
'''
'''
import pandas as pd
import numpy as np

data={
    'Artist':pd.Series(['Billie Holiday', 'Jimi Hendrix']),
    'Genre':pd.Series(['Jazz', 'Rock']),
    'Listeners':pd.Series([1300000, 2700000]),
    'Plays':pd.Series([27000000, 70000000])
}
series=pd.DataFrame(data)
print(series)
'''
'''
import pandas as pd
#movies_df=pd.read_csv("D:/my file/지역 ICT 인공지능교육/10차수 데이터/IMDB-Movie-Data.csv", index_col="Title")
movies_df=pd.read_csv("./10차수 데이터/IMDB-Movie-Data.csv", index_col="Title")
print(movies_df)
'''
'''
import pandas as pd
cars=pd.read_csv("./10차수 데이터/usedcars.csv")
print(cars)
cars.info()
'''
'''
import pandas as pd
movies_df=pd.read_csv("./10차수 데이터/IMDB-Movie-Data.csv", index_col="Title")
print(movies_df.describe())
print(movies_df['Genre'].describe())
print(movies_df.columns)

movies_df.rename(columns={'Runtime (Minutes)': 'Runtime'}, inplace=True)
print(movies_df.columns)

print(movies_df[movies_df['Rating']>=8.6].head(5))
'''
'''
import pandas as pd
movies_df=pd.read_csv("./10차수 데이터/IMDB-Movie-Data.csv", index_col="Title")

#movies_df.dropna(inplace=True)
#print(movies_df.isnull().sum())

movies_df['Revenue (Millions)'].fillna(movies_df['Revenue (Millions)'].mean(), inplace=True)
print(movies_df.isnull().sum())
'''
'''
import plotly.graph_objs as go
import pandas as pd
movies_df=pd.read_csv("./10차수 데이터/IMDB-Movie-Data.csv", index_col="Title")

x_values=movies_df['Rating']
y_values=movies_df['Revenue (Millions)']

mydata=go.Scatter(x=x_values, y=y_values, mode="markers")

mylayout=go.Layout(title='Revenue vs rating',
                   xaxis_title='Rating',
                   yaxis_title="Revenue")

fig=go.Figure(data=mydata, layout=mylayout)
fig.show()
'''
'''
import plotly.graph_objects as go
import pandas as pd

movies_df=pd.read_csv("./10차수 데이터/IMDB-Movie-Data.csv", index_col="Title")
movies_df.plot(kind='scatter', x='Rating', y='Revenue (Millions)', title='Revenue (millions) vs Rating');

y_values=movies_df['Rating']

mydata=go.Box(y=y_values)

mylayout=go.Layout(title='Boxplot for Ratings', yaxis_title="Rating")

fig=go.Figure(mydata, mylayout)

fig.show()

movies_df['Rating'].plot(kind="box")
'''
'''
import plotly.graph_objects as go
import pandas as pd

movies_df=pd.read_csv("./10차수 데이터/IMDB-Movie-Data.csv", index_col="Title")

x_values=movies_df['Rating']

mydata=go.Histogram(x=x_values)

mylayout=go.Layout(title='Histogram for Ratings', xaxis_title="Rating")

fig=go.Figure(mydata, mylayout)

fig.show()
'''
'''
import plotly.graph_objs as go
import pandas as pd
cars_df=pd.read_csv("./10차수 데이터/usedcars.csv")

# year, mileage, color, price

x_values=cars_df['color']
y_values=cars_df['price']

mydata=go.Scatter(x=x_values, y=y_values, mode="markers")

mylayout=go.Layout(title='Color vs Price',
                   xaxis_title='Color',
                   yaxis_title="Price")

fig=go.Figure(data=mydata, layout=mylayout)
fig.show()
'''

import plotly.graph_objects as go
import pandas as pd

cars_df=pd.read_csv("./10차수 데이터/usedcars.csv")

# year, mileage, color, price

x_values=cars_df['price']

mydata=go.Histogram(x=x_values)

mylayout=go.Layout(title='Histogram for price', xaxis_title="price")

fig=go.Figure(mydata, mylayout)

fig.show()
