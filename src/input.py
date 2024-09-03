import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 3, 2, 4, 3, 4, 6, 5]
))


fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 4, 5, 1, 2, 2, 3, 4, 2]
))

fig.add_annotation(x=2, y=5,
            text="Text annotation with arrow",
            showarrow=True,
            ax=6,
            ay=6,
            axref='x',
            ayref='y',
            arrowhead=1)
fig.add_annotation(x=4, y=4,
            text="Text annotation without arrow",
            showarrow=False,
            yshift=10)

fig.update_layout(showlegend=False)

fig.show()