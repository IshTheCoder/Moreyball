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
plotly.tools.set_credentials_file(username='swishan', api_key='nQfq97kmHYvg1HhlKSp5')


# playoffs=pd.read_html('Playoff_per.xls')
# DF=(playoffs[0])
# names=DF.iloc[:,1]

# TS=DF.iloc[:,-1]


#print(TS)
f1='leaguedashplayershotlocations_per.json'
f2='leaguedashplayershotlocations.json'

magma = [[0.0, 'rgb(0, 0, 3)'],
 [0.1, 'rgb(20, 13, 53)'],
 [0.2, 'rgb(59, 15, 111)'],
 [0.3, 'rgb(99, 25, 127)'],
 [0.4, 'rgb(140, 41, 128)'],
 [0.5, 'rgb(182, 54, 121)'],
 [0.6, 'rgb(221, 73, 104)'],
 [0.7, 'rgb(246, 112, 91)'],
 [0.8, 'rgb(253, 159, 108)'],
 [0.9, 'rgb(253, 207, 146)'],
 [1.0, 'rgb(251, 252, 191)']]


inferno = [[0.0, 'rgb(0, 0, 3)'],
 [0.1, 'rgb(22, 11, 57)'],
 [0.2, 'rgb(65, 9, 103)'],
 [0.3, 'rgb(106, 23, 110)'],
 [0.4, 'rgb(147, 37, 103)'],
 [0.5, 'rgb(187, 55, 84)'],
 [0.6, 'rgb(220, 80, 57)'],
 [0.7, 'rgb(243, 119, 25)'],
 [0.8, 'rgb(251, 164, 10)'],
 [0.9, 'rgb(245, 215, 69)'],
 [1.0, 'rgb(248, 250, 100)']]


with open(f1) as f:
    data = json.load(f)



def create_morey_vector(array_profile):
	morey_vector_A=[]

	morey_vector_A.append(array_profile[6])
	morey_vector_A.append(array_profile[9])
	morey_vector_A.append(array_profile[12])

	return 




	


with open(f2) as fx:
    data_reg = json.load(fx)
FGA_restricted=0.0
FGM_restricted=0.0
FGM_3=0.0
FGA_3=0.0



morey_names=[]
morey_vals=[]
morey_dict={}
FGA_list=[]
for each_row in data['resultSets']['rowSet']:




	#print(each_row)
	try:
		FGA_restricted+=each_row[6]
		FGM_restricted+=each_row[5]
		FGA_3+=each_row[21]+each_row[18]+each_row[15]+each_row[24]
		FGM_3+=each_row[20]+each_row[17]+each_row[14]+each_row[23]



	except:
		pass

	new_row=[0 if v is None  else v for v in each_row]
	#print(new_row)

	FGA_restricted_1=float(new_row[6])
	FGA_3_1=new_row[21]+new_row[18]+new_row[15]+new_row[24]+0.0
	if str(each_row[1])=='James Harden':
		print('James')
		print(FGA_3_1)
		print(FGA_restricted_1)
		print(each_row[9]+each_row[12])

	try:

		morey_rate=(FGA_restricted_1+FGA_3_1)/(FGA_3_1+FGA_restricted_1+new_row[9]+new_row[12])
		Total_FGA=FGA_3_1+FGA_restricted_1+new_row[9]+new_row[12]
		if Total_FGA>=4:
			print(Total_FGA)
			morey_names.append(str(each_row[1])+' '+str(Total_FGA))
			morey_vals.append(morey_rate)
			morey_dict[str(each_row[1])]=morey_rate
			FGA_list.append(Total_FGA)

		#morey_dict1[str(each_row[1])]=morey_rate
	except:
		pass




FGP_R=FGM_restricted/FGA_restricted
FGP_3=FGM_3/FGA_3

moreyball=[0.5,0,0,0.5]
print(morey_names)

data_dict={'Names':morey_names,'Morey_index':morey_vals}

df = pd.DataFrame(data_dict,index=None) 

df_new=df.sort_values('Morey_index')
df_new.to_csv('Morey_vals',index=False)

# print(morey_dict['James Harden'])

# print(morey_dict['Stephen Curry'])


# print(morey_dict['Giannis Antetokounmpo'])

# print(morey_dict['Damian Lillard'])


data = [
    go.Scatter(
        x =[0.5]*len(morey_dict.values()),
        y = morey_vals,
        text = morey_names,
        hoverinfo = 'text',
        mode='markers',
        marker=dict(
        	size=FGA_list,
        	cmax=1.0,
        	cmin=0.0,
        	color=morey_vals,
        	colorbar=dict(
        	title="Morey-range percentage"
        	),
       	colorscale=inferno


        	)

		),
    
]


layout = go.Layout(

	plot_bgcolor='rgba(0,0,0)',
	paper_bgcolor='rgba(0,0,0)',



	title='League-wide Moreyball indexes',
	font=dict(
        family="sans serif",
        color="LightSeaGreen"
    ),

    xaxis=dict( 
    	showticklabels=False,

        range=[0, 1],
    ),
    yaxis=dict(showgrid=True,
    	gridcolor='SeaGreen',
        range=[0, 1],
        title='Moreyball index',

    )

)

fig = go.Figure(data=data, layout=layout)

#py.iplot(fig,sharing='public',filename='moreyball')

plotly.offline.plot(fig, filename='moreyball.html')









