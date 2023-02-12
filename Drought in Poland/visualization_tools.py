import plotly.express as px


def comparision_plot(data):
    grouped_data = data.groupby(['Year','Month','Month Name']).mean('Monthly Rainfall').reset_index()
    fig = px.line(grouped_data,x='Month Name',y='Monthly Rainfall',color='Year',markers=True)
    fig.show()
    return fig