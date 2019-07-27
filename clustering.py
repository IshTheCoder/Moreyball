#Clustering

import json
import plotly
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import PIL
import imageio
from imageio import imread
from scipy.stats import entropy
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly 
plotly.tools.set_credentials_file(username='swishan', api_key='nQfq97kmHYvg1HhlKSp5'


playoffs=pd.read_html('Playoff_per.xls')
DF=(playoffs[0])
names=DF.iloc[:,1]

TS=DF.iloc[:,-1]


#print(TS)
f1='leaguedashplayershotlocations_per.json'
