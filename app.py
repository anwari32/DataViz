import dash
import datetime as dt
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from data_utils import get_rel_countries
from data_utils import get_data
from data_utils import get_data_on_demand

from dash.dependencies import Input, Output, State, ClientsideFunction



app = dash.Dash(__name__)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

layout = dict(
    autosize=True,
    automargin=True,
    margin=dict(l=30, r=30, b=20, t=40),
    hovermode="closest",
    plot_bgcolor="#F9F9F9",
    paper_bgcolor="#F9F9F9",
    legend=dict(font=dict(size=10), orientation="h"),
    title="Satellite Overview",
    mapbox=dict(
        style="light",
        center=dict(lon=-78.05, lat=42.54),
        zoom=7,
    ),
)


import_countries = get_rel_countries(mode='import')
export_countries = get_rel_countries(mode='export')
export_countries_on_demand = get_rel_countries(mode='on-demand')

trade_year_range = range(2000, 2021)

app.layout = html.Div([    
    dbc.Row([
        dbc.Col(
            html.Div(
                [
                    html.Div(
                        [
                            html.Img(
                                src=app.get_asset_url("dash-logo.png"),
                                id="plotly-image",
                                style={
                                    "height": "60px",
                                    "width": "auto",
                                    "margin-bottom": "25px",
                                },
                            )
                        ],
                        className="one-third column",
                    ),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H2(
                                        "Export-Import Visualization",
                                        style={"margin-bottom": "0px"},
                                    ),
                                    html.H5(
                                        "IF5170 Data Visualization", style={"margin-top": "0px"}
                                    ),
                                ]
                            )
                        ],
                        className="one-half column",
                        id="title",
                    ),
                    html.Div([
                            html.A(
                                html.Button("Feedback", id="learn-more-button"),
                                href="https://docs.google.com/forms/d/e/1FAIpQLSd92s8qqxJ9zgwEQjSF01FBbVF2yAJxIXIIM2THpFzCkwSlYw/viewform",
                            )
                        ]
                    ),
                    
                ],
                id="header",
            ),
        ),
        
    ]),


    html.Div([
        html.Div(
            [
                html.Div(
                    html.Div([
                        dcc.Dropdown(
                            id="country-on-demand",
                            options=[
                                {'label': x, 'value': x} for x in export_countries_on_demand
                            ],
                            value='Jepang',
                            clearable=False,
                        ),
                        
                        dcc.Graph(id='export-on-demand'),
                        ])
                        
                    ),               
            ],
        ),
    ]),
    
    dbc.Row([
        dbc.Col(
            html.Div([
                dcc.Dropdown(
                    id='country-dropdown',
                    options=[
                        {'label': x, 'value': x} for x in set(export_countries + import_countries)
                    ],
                    value='Tiongkok',
                    clearable=False,
                )
            ]),
        )
    ]),
    dbc.Row([
        dbc.Col(
            html.Div([
                dcc.Graph(id='export-fig'),
            ])
        ),
        dbc.Col(
            html.Div([
                dcc.Graph(id='import-fig'),
            ])
        ),
    ]),
    dbc.Row([
        dbc.Row([
            dbc.Col(
                html.Div([
                    html.P("Trade"),
                    dcc.Dropdown(
                        id='trade_mode',
                        options=[
                            {'label': x, 'value': x.lower()} for x in ['Export', 'Import']
                        ]
                    ),
                ])
            ),
            dbc.Col(
                html.Div([
                    html.P("Commodity"),
                    dcc.Dropdown(
                        id='commodity',
                        options=[
                            {'label': x, 'value': x.lower()} for x in ['All', 'Crude Oil', 'Gas']
                        ]
                    ),
                ])
            ),
            dbc.Col(
                html.Div([
                    html.P("Trade Year"),
                    dcc.Dropdown(
                        id='trade_year',
                        options=[
                            {'label': str(x), 'value': str(x)} for x in trade_year_range
                        ]
                    ),
                ])
            ),
        ]),
        dbc.Row([
            dbc.Col(
                html.Div([
                    dcc.Graph(id='map'),
                ])
            ),
        ]),
    ]),
    dbc.Row([
        dbc.Col(
            html.Div([
                html.P("Energy Theme"),
                dcc.Dropdown(
                    id='energy_map_menu',
                    options=[
                        {'label': str(x[0]), 'value': str(x[1])} for x in
                        [('Energy Demand Trend', 'energy-demand-trend'), ('Renewable Energy Trend', 'renewable-demand-trend')]
                    ]
                ),
                dcc.Graph(id='energy_map'),
            ])
        )
    ]),
], className="container")


# grafik bar chart ekspor on demand
from data_utils import get_fig_data_on_demand
@app.callback(Output('export-on-demand', 'figure'), [Input('country-on-demand', 'value')])
def display_export_on_demand(country):
    fig = px.bar(get_data_on_demand(country),
                 y="year",
                 x="value",
                 color="commodity",
                 barmode="stack",
                 orientation='h',
                 
                 
                 )
    fig.update_layout(
    title={
        'text': "Export on Demand",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

    # fig = get_fig_data_on_demand(country)
    return fig


# grafik bar chart impor

# grafik ekspor all
@app.callback(Output("export-fig", "figure"), [Input("country-dropdown", "value")])
def display_export(country):
    title = ''
    if (country):
        title = 'Export Volume to ' + country
    fig = go.Figure(
        data=go.Bar(y=get_data('export', country), x=list(range(2010, 2021))),
        layout={'title': title}
    )
    return fig


# grafik impor all
@app.callback(Output("import-fig", "figure"), [Input('country-dropdown', 'value')])
def display_import(country):
    title = ''
    if (country):
        title = 'Import Volume from ' + country
    fig = go.Figure(
        data=go.Bar(y=get_data('import', country), x=list(range(2010, 2021))),
        layout={'title': title}
    )
    return fig


import pandas as pd
import json
import plotly.express as px


# grafik geo
@app.callback(Output('map', 'figure'),
              [Input("trade_mode", "value"), Input("commodity", "value"), Input("trade_year", "value")])
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
                               zoom=3, center={"lat": 37.0902, "lon": -95.7129},
                               opacity=0.5,
                               labels={'unemp': 'unemployment rate'}
                               )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    # fig.show()
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
        datapath = './data/renewable_energy_demand.csv'
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



# new


app.run_server(debug=True)

