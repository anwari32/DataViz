import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

from data_utils import get_rel_countries

app = dash.Dash(__name__)

import_countries = get_rel_countries(mode='import')
export_countries = get_rel_countries(mode='export')

app.layout = html.Div([
    html.P("Color:"),
    dcc.Dropdown(
        id="dropdown",
        options=[
            {'label': x, 'value': x}
            for x in ['Gold', 'MediumTurquoise', 'LightGreen']
        ],
        value='Gold',
        clearable=False,
    ),
    html.P("Export Target"),
    dcc.Dropdown(
        id="export-dropdown",
        options=[
            {'label': x, ' value': x} for x in export_countries
        ], 
        value='Thailand',
        clearable=False,
    ),
    dcc.Dropdown(
        id="import-dropdown",
        options=[
            {'label': x, ' value': x} for x in import_countries
        ], 
        value='',
        clearable=False,
    ),
    
    dcc.Graph(id="graph"),
    dcc.Graph(id="export"),
    dcc.Graph(id="import")
])

@app.callback(Output("graph", "figure"), [Input("dropdown", "value")])
def display_color(color):
    fig = go.Figure(
        data=go.Bar(y=[2, 3, 1], marker_color=color))
    return fig
    
from data_utils import get_data

@app.callback(Output("export", "figure"), [Input("export-dropdown", "value")])
def display_export(country):
    if (country):
        fig = go.Figure(
            data=go.Bar(y=get_data(mode='export', country=country), x=range(2010, 2021))
        )
        return fig
    
@app.callback(Output('import', 'figure'), [Input('import-dropdown', "value")])
def display_import(country):
    if (country):
        
        fig = go.Figure(
            data=go.Figure(y=[])
        )

app.run_server(debug=True)