'''
from bokeh.plotting import figure, output_file, show

x=[1,3,5,7]
y=[2,4,6,8]

p=figure()

p.circle(x,y, size=10, color='red', legend='circle')
p.line(x,y,color='blue', legend='line')
p.triangle(y,x, color='gold', size=10, legend='triangle')
p.legend.click_policy='hide'

show(p)

output_file("bokech_01.html")
'''
'''
from bkcharts import figure, output_file, show

data={"y":[1,2,3,4,5]}
p=figure(data, title="Line Chart Example", xlabel='x', ylabel='values', width=400, height=400)

show(p)
'''
'''
from bokeh.plotting import figure, output_notebook, show

#output_notebook()
p=figure(plot_width=400, plot_height=400)
p.square([2,5,6,4,8], [2,3,2,1,2], size=20, color="navy", alpha=0.5)
p.line([1,2,3,4,5], [1,2,2,4,5], line_width=2)

p.xaxis.axis_label="x axis"
p.yaxis.axis_label="y axis"

show(p)
'''
'''
from bokeh.io import output_file, show
from bokeh.layouts import column
from bokeh.plotting import figure

output_file("lay out.html")

x=list(range(11))
y0=x
y1=[10-i for i in x]
y2=[abs(i-5) for i in x]

s1=figure(plot_width=250, plot_height=250, background_fill_color="#fafafa")
s1.circle(x,y0, size=12, color="#53777a", alpha=0.8)

s2=figure(plot_width=250, plot_height=250, background_fill_color="#fafafa")
s2.triangle(x,y1, size=12, color="#c02942", alpha=0.8)

s3=figure(plot_width=250, plot_height=250, background_fill_color="#fafafa")
s3.square(x,y1, size=12, color="#d95b43", alpha=0.8)

show(column(s1, s2, s3))
'''
'''
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="ticks")
tips=sns.load_dataset("tips")
g=sns.relplot(x="total_bill", y="tip", hue="day", data=tips)

plt.show()
'''
'''
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()
tips=sns.load_dataset("tips")
ax=sns.scatterplot(x="total_bill", y="tip", hue="time", data=tips)

plt.show()
'''
'''
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()
fmri=sns.load_dataset("fmri")
ax=sns.lineplot(x="timepoint", y="signal", hue="region", data=fmri)

plt.show()
'''
'''
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="ticks")
exercise=sns.load_dataset("exercise")
g=sns.catplot(x="time", y="pulse", hue="kind", data=exercise)

plt.show()
'''
'''
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")
tips=sns.load_dataset("tips")
#gx=sns.stripplot(x="sex", y="total_bill", hue="day", data=tips)
gx=sns.swarmplot(x="sex", y="total_bill", hue="day", data=tips)

plt.show()
'''
'''
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")
tips=sns.load_dataset("tips")
#gx=sns.boxplot(x="time", y="tip", data=tips, order=["Dinner", "Lunch"])
gx=sns.violinplot(x="time", y="tip", hue="sex", data=tips, order=["Dinner", "Lunch"])

plt.show()
'''
'''
import seaborn as sns
from numpy import median
import matplotlib.pyplot as plt

sns.set(style="darkgrid")
titanic=sns.load_dataset("titanic")
ax=sns.countplot(x="class", hue="who", data=titanic).set_title("Titanic passenger")

plt.show()
'''
'''
import seaborn as sns
from numpy import median
import matplotlib.pyplot as plt

sns.set(style="whitegrid")
tips=sns.load_dataset("tips")
ax=sns.barplot(x="size", y="tip", data=tips, estimator=median)

plt.show()
'''
'''
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set(color_codes=True)
tips=sns.load_dataset("tips")
#g=sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips)
g=sns.regplot(x="size", y="tip", data=tips, x_estimator=np.median)

plt.show()
'''
'''
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()
flights=sns.load_dataset("flights")
flights=flights.pivot("month", "year", "passengers")
ax=sns.heatmap(flights)

plt.show()
'''

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="ticks", color_codes=True)
iris=sns.load_dataset("iris")
g=sns.pairplot(iris, hue="species")

plt.show()
