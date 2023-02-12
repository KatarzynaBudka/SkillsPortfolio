import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go

import visualization_tools as vc
import app_components as ac

app = dash.Dash(__name__)
app.title =  'Drought in Poland'

DATA_DIR = 'Data/'

data = ac.prepare_data()
com_fig = vc.comparision_plot(data)

app.layout = html.Div(
    [   
        #first row
        html.Div([ 
                html.Div(
                    [
                html.Img(
                    src=app.get_asset_url("Logo.png"),
                    id='out_world_in_data_log',
                    style={
                                    "height": "80px",
                                    "width": "auto",
                                    "margin-bottom": "0px",
                                    'margin-left':'80px',
                            }
                        ),
                    ],
                    style={'display': 'inline-block'}
                ),
                html.Div(
                    html.H1('Drought in Poland',style={'color': 'white','margin':0,'padding': 0}),
                    style={"height": "80px","width": "auto","margin-left":"300px",'display': 'inline-block','text-align': 'center','vertical-align':'middle','padding': 0}
                )
            ],
            className='row',
            style={'background-color': '#052349', 'height': '80px', 'width': '100%',}
        ),
    
        #secend row
            html.Div(style={'background-color': 'rgb(190, 43, 34)', 'height': '5px', 'width': '100%','margin':0,'padding': 0}) #empty red div
        ,
        #third row
        html.Div(
            html.H3('Autor: Katarzyna Budka',style={'text-align': 'center','vertical-align': 'middle','height': '40px','margin':0,'padding': 0}),
            style={'background-color': 'rgb(242, 189, 52)', 'height': '20px', 'width': '100%','margin':0,'padding': 0}
        ),
        #fourth
        html.Div(
            html.H3('To be added description',style={'text-align': 'center','vertical-align': 'middle','height': '40px','margin':0,'padding': 0}),
            style={'background-color': 'rgb(219, 229, 240)', 'height': '50px', 'width': '100%','margin':0,'padding': 0}
        ),
        #fifth
        html.Div(
            html.Div(
                dcc.Graph(id='com_plot',figure=com_fig)
            )
        )
        #sixth
    ],
    className='row'
)


if __name__ =="__main__":
    app.run_server(use_reloader=False)
