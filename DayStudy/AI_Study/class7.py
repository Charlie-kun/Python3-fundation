#import plotly
#print(plotly.__version__)

import plotly.graph_objects as go
flg=go.Figure(data=go.Bar(y=[2,3,1]))
flg.show()

langs=['C', 'C++', 'Java', 'Python', 'PHP']
students=[23, 17,35,29,12]

data=[go.Bar(
    x=langs, y=students,
    marker=dict(color=['red', 'blue',2,3,4]),
    text=students,
    textposition='inside'
)]

fig=go.Figure(data=data)
fig.show()

branches=['CSE', 'Mech', 'Electonics']

fy=[23,17,35]
sy=[20,23,30]
ty=[30,20,15]

trace1=go.Bar(
    x=branches,
    y=fy,
    name='FY'
)

trace2=go.Bar(
    x=branches, y=sy, name='SY'
)

trace3=go.Bar(
    x=branches, y=ty, name='TY'
)

data=[trace1, trace2, trace3]

layout=go.Layout(barmode='group', title='Departments Bar Graf', yaxis_title='Number of students', xaxis_title='Branches')

fig=go.Figure(data=data, layout=layout)

fig.show()

langs=['C', 'C++', 'Java', 'Python', 'PHP']
students=[35, 29,25,17,12]

data=[go.Bar(
    x=langs, y=students,
    marker=dict(color=[5,1,2,3,4]),
    text=students,
    textposition='outside'
)]

fig=go.Figure(data=data)
fig.update_layout(title={'text':"Popular Language",
                          'y':0.9,'x':0.5,
                          'xanchor':'center',
                          'yanchor':'top'})
fig.show()

langs=['C', 'C++', 'Java', 'Python', 'PHP']
students=[23,17,35,29,12]

data=[go.Pie(
    labels=langs,
    values=students,
    pull=[0.1,0,0,0,0],
    hole=0.4
)]

fig=go.Figure(data=data)
fig.show()

import numpy as np

x_vals=[45,55,47,75,90,100,100,95,88,50,45,58]
y_vals=[15,25,17,34,41,47,50,46,37,22,20,30]

data=[go.Scatter(
    x=x_vals,
    y=y_vals,
    mode='markers'
)]
fig=go.Figure(data=data)
fig.show()
