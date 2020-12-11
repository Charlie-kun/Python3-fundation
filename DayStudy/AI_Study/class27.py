import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data=sns.load_dataset('titanic')
df=pd.DataFrame(data)
print(df.head(), '\n')
print(df.tail())

from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("http://python.org")
soup=BeautifulSoup(html.read(), "html.parser")
print(soup.h1)
