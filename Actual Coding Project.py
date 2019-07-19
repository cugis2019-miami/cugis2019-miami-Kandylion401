df = pd.read_excel("GISdata.xlsx", sheet_name = "cancercases")
cancercases = go.Bar(x=df["CancerType"], y=df["Number"])
plot([cancercases])
fig = go.Figure(data=[cancercases])
plot(fig)

df = pd.read_excel("GISdata.xlsx", sheet_name = "womenOccupation")
plot([womenOccupation])
fig = go.Figure(data=[womenOccupation])
plot(fig)
plot([womenOccupation])
fig = go.Figure(data=[womenOccupation])
plot(fig)

