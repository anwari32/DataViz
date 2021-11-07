import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

from data_utils import get_rel_countries
from data_utils import get_data

app = dash.Dash(__name__)

import_countries = get_rel_countries(mode='import')
export_countries = get_rel_countries(mode='export')

app.layout = html.Div([
    html.P("Export Target"),
    dcc.Dropdown(
        id="export-dropdown",
        options=[
            {'label': x, 'value': x} for x in export_countries
        ], 
        value='',
        clearable=False,
    ),
    dcc.Graph(id='export-fig'),
    html.P("Import Target"),
    dcc.Dropdown(
        id="import-dropdown",
        options=[
            {'label': x, 'value': x} for x in import_countries
        ], 
        value='',
        clearable=False,
    ),
    dcc.Graph(id='import-fig'),
    html.P("Map"),
    dcc.Graph(id='map'),
])

@app.callback(Output("export-fig", "figure"), [Input("export-dropdown", "value")])
def display_export(country):
    fig = go.Figure(
        data=go.Bar(y=get_data('export', country), x=list(range(2010, 2021))),
        layout={'title': country}
    )
    return fig
    
@app.callback(Output("import-fig", "figure"), [Input("import-dropdown", "value")])
def display_import(country):
    fig = go.Figure(
        data=go.Bar(y=get_data('import', country), x=list(range(2010, 2021))),
        layout={'title': country}
    )
    return fig
    
import pandas as pd
import json
import plotly.express as px

@app.callback(Output('map', 'figure'), [Input("import-dropdown", "value")])
def display_map(maps):
    countries_json = json.load(open('./data/geojson.json'))
    df = pd.read_csv('./data/fips.csv')
    fig = px.choropleth_mapbox(df, geojson=countries_json, locations='fips', color='unemp', 
        color_continuous_scale="Viridis",
        range_color=(0, 12),
        mapbox_style="carto-positron",
        zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
        opacity=0.5,
        labels={'unemp':'unemployment rate'}
    )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    #fig.show()
    return fig
        
app.run_server(debug=True)

