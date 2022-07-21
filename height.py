import plotly.figure_factory as pf
import pandas as pd

data = pd.read_csv("data.csv")

height = data["Height(Inches)"].tolist()

graph = pf.create_distplot([height] ,["Height"] , show_hist = False)

graph.show()




 


