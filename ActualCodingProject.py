import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go

df = pd.read_excel("GISdata.xlsx", sheet_name = "cancercases")
cancercases = go.Bar(x=df["CancerType"], y=df["Number"],
marker = {"color": df["Number"], "colorscale": "Jet"}
)
plot([cancercases])
fig = go.Figure(data=[cancercases])
plot(fig)


