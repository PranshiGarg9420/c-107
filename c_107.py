import pandas as pd
import csv
import plotly.express as px

df= pd.read_csv('data_107.csv')

mean=df.groupby(["id_student","level"], as_index = False)["attempt"].mean()


fig = px.scatter(mean,x="id_student",y='level',color='attempt',size='attempt')

fig.show()