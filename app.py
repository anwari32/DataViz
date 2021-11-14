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

trade_year_range = range(2000, 2021)

app.layout = html.Div([
    html.Div([
        html.Div([
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
        ]),
        html.Div([
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
        ]),
    ]),
    html.Div([
        html.Div([
            html.Div([
                html.P("Trade"),
                dcc.Dropdown(
                    id='trade_mode',
                    options=[
                        {'label': x, 'value': x.lower()} for x in ['Export', 'Import']
                    ]
                ),
            ]),
            html.Div([
                html.P("Commodity"),
                dcc.Dropdown(
                    id='commodity',
                    options=[
                        {'label': x, 'value': x.lower()} for x in ['All', 'Crude Oil', 'Gas']
                    ]
                ),
            ]),
            html.Div([
                html.P("Trade Year"),
                dcc.Dropdown(
                    id='trade_year',
                    options=[
                        {'label': str(x), 'value': str(x)} for x in trade_year_range
                    ]
                ),
                dcc.Graph(id='map'),        
            ]),    
        ]),
    ]),
    html.Div([
        html.P("Energy Theme"),
        dcc.Dropdown(
            id='energy_map_menu',
            options=[
                {'label': str(x[0]), 'value': str(x[1])} for x in [('Energy Demand Trend', 'energy-demand-trend') ,('Renewable Energy Trend', 'renewable-trend')]
            ]
        ),
        dcc.Graph(id='energy_map'),
    ], className="row"),
])

@app.callback(Output("export-fig", "figure"), [Input("export-dropdown", "value")])
def display_export(country):
    fig = go.Figure(
        data=go.Bar(y=get_data('export', country), x=list(range(2010, 2021))),
        layout={'title': country}
    )
    return fig
    
@app.callback(Output("import-fig", "figure"), [Input('import-dropdown', 'value')])
def display_import(country):
    fig = go.Figure(
        data=go.Bar(y=get_data('import', country), x=list(range(2010, 2021))),
        layout={'title': country}
    )
    return fig
    
import pandas as pd
import json
import plotly.express as px

@app.callback(Output('map', 'figure'), [Input("trade_mode", "value"), Input("commodity", "value"), Input("trade_year", "value")])
def display_map(trade, commodity, trade_year):
    # countries_json = json.load(open('./data/geojson.json'))
    countries_json = json.load(open('./data/countries.geo.json'))
    # df = pd.read_csv('./data/fips.csv')
    df = pd.read_csv('./data/relasi_ekspor_all.csv')
    if (trade == 'export'):
        if (commodity == 'crude oil'):
            df = pd.read_csv('./data/relasi_ekspor_minyak_mentah_by_volume.csv')
        elif (commodity == 'gas'):
            df = pd.read_csv('./data/relasi_ekspor_gas_by_volume.csv')
        else:
            df = pd.read_csv('./data/relasi_ekspor_all.csv')
    elif (trade == 'import'):
        if (commodity == 'crude oil'):
            df = pd.read_csv('./data/relasi_impor_minyak_mentah_by_volume.csv')
        elif (commodity == 'gas'):
            df = pd.read_csv('./data/relasi_impor_gas_by_volume.csv')
        else:
            df = pd.read_csv('./data/relasi_impor_all.csv')
    else:
        trade = 'import'

    if (not trade_year):
        trade_year = '2000'

    tyr = list(df.loc[:, trade_year])
    min_val = min(tyr)
    max_val = max(tyr)
    # fig = px.choropleth_mapbox(df, geojson=countries_json, locations='fips', color='unemp', 
    fig = px.choropleth_mapbox(df, geojson=countries_json, locations='id', color=str(trade_year), 
        color_continuous_scale="Viridis",
        range_color=(min_val, max_val),
        mapbox_style="carto-positron",
        zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
        opacity=0.5,
        labels={'unemp':'unemployment rate'}
    )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    #fig.show()
    return fig

@app.callback(Output('energy_map', 'figure'), [Input('energy_map_menu', 'value')])
def display_energy_map(info_type):
    datapath = './data/energy_demand.csv'
    col = 'Trend'
    title = 'Energy Demand Map'
    label = 'Energy Demand Trend'
    if (info_type == 'energy-demand-trend'):
        datapath = './data/energy_demand.csv'
        col = 'Trend'
        label = 'Energy Demand Trend'
    elif (info_type == 'renewable-demand-trend'):
        datapath = './data/renewable_demand.csv'
        col = 'Trend'
        label = 'Renewable Energy Demand Trend'
    
    countries_json = json.load(open('./data/countries.geo.json'))
    df = pd.read_csv(datapath)
    trend = list(df.loc[:, col])
    min_trend = min(trend)
    max_trend = max(trend)

    fig = px.choropleth_mapbox(df, geojson=countries_json, locations="Code", color=col, 
            color_continuous_scale='viridis', 
            range_color=(0, max_trend), 
            mapbox_style="carto-positron",
            labels={'Trend': label},
            zoom=1,
            title=title)
    return fig
        
app.run_server(debug=True)
