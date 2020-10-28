#import matplotlib.pyplot as plt
#plt.plot([1,2,3,4])
#plt.ylabel('some numbers')
#plt.show()

import plotly.express as px
#df = px.data.iris()
#fig = px.parallel_coordinates(df, color="species_id", labels={"species_id": "Species",
#                  "sepal_width": "Sepal Width", "sepal_length": "Sepal Length",
#                  "petal_width": "Petal Width", "petal_length": "Petal Length", },
#                    color_continuous_scale=px.colors.diverging.Tealrose, color_continuous_midpoint=2)
#fig.show()

#plt.plot([1,2,3,4], [1,4,9,16])
#plt.plot([1,2,3,4], [1,4,9,16], 'ro')
#plt.axis([0,6,0,20])
#plt.show()

#import numpy as np
#t=np.arange(0,5., 0.2)

#plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
#plt.show()

#data={'a':np.arange(50),
#      'c':np.random.randint(0,50,50),
#      'd':np.random.randn(50)}
#data['b']=data['a']+10*np.random.randn(50)
#data['d']=np.abs(data['d'])*100

#plt.scatter('a', 'b', c='c', s='d', data=data)
#plt.xlabel('entry a')
#plt.ylabel('entry b')
#plt.show()


#names=['group_a', 'group_b', 'group_c']
#values=[1,10,100]

#plt.figure(figsize=(9,3))

#plt.subplot(131)
#plt.bar(names, values)
#plt.subplot(132)
#plt.scatter(names, values)
#plt.subplot(133)
#plt.plot(names, values)
#plt.suptitle('Categorical Plotting')
#plt.show()

'''
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1=np.arange(0.0,5.0,0.1)
t2=np.arange(0.0,5.0,0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
'''
'''
mu, sigma=100,15
x=mu+sigma*np.random.randn(10000)

n, bins, patches=plt.hist(x,50, density=1, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60,.025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160,0,0.03])
plt.grid(True)
plt.show()
'''
'''
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)
mu=100
sigma=15
x=mu+sigma*np.random.randn(437)
num_bins=50
fig, ax=plt.subplots()
n, bins, patches=ax.hist(x, num_bins, density=True)
y=((1/(np.sqrt(2*np.pi)*sigma))*np.exp(-0.5*(1/sigma*(bins-mu))**2))
ax.plot(bins,y,'--')
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ : $\mu=100$, $\sigma=15$')

fig.tight_layout()
plt.show()
'''
'''
import numpy as np
import matplotlib.pyplot as plt

ax=plt.subplot(111)

t=np.arange(0.0, 5.0, 0.01)
s=np.cos(2*np.pi*t)
line, =plt.plot(t,s,lw=2)

plt.annotate('local max', xy=(2,1), xytext=(3,1.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )

plt.ylim(-2,2)
plt.show()
'''
'''
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2*np.pi, num=101)
y1, y2=np.sin(x), np.cos(x)
plt.plot(x,y1, "k--", label="y1=sin(x)")
plt.plot(x,y2,"b-", label="y2=cos(x)")
xmin, xmax, ymin, ymax=x[0], x[-1], -1, 1

plt.axis([xmin, xmax, ymin, ymax])
#plt.xlim(xmin, xmax)
#plt.ylim(ymin, ymax)
plt.legend(loc="best")
plt.savefig("sincos.png")
plt.show()
'''

import numpy as np
import matplotlib.pyplot as plt
def gauss(mu, sigma, x):
    y=1.0/(sigma*np.sqrt(2*np.pi))*np.exp(-((x-mu)**2)/(2*sigma**2))
    return y
mu,sigma=0,2
x=np.linspace(-4*sigma, 4*sigma, num=101)
y1=gauss(mu,sigma, x)
plt.plot(x,y1,color="#ff0000", label="sigma=2")

mu,sigma=0,1
y2=gauss(mu,sigma,x)
plt.plot(x,y2,color="#00ff00", label="sigma=1")

mu,sigma=0,0.5
y3=gauss(mu,sigma,x)
plt.plot(x,y3,color="#0000ff", label="sigma=0.5")
plt.title("Normal dist.N(0,sigma)")
plt.legend(loc="best")
plt.savefig("norm1d.png")
plt.show()
