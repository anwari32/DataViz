import dash
from dash_bootstrap_components._components.Tooltip import Tooltip
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from heesi_bps import export_target
from heesi_bps import import_target
from heesi_bps import commodities_set
from heesi_bps import year_range

heesi_app = dash.Dash(__name__)
heesi_app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

heesi_app.layout = html.Div([
    dbc.Row([
        dbc.Col(
            html.Div([
                html.P('Export'),
                dcc.Dropdown(
                    id="export-target-country",
                    options=[
                        {'label': x, 'value': x} for x in export_target
                    ],
                    value='',
                    clearable=False,
                    placeholder='select export target country'
                ),
                dcc.Graph(id='export-graph'),
            ]), width=8
        ),
        dbc.Col(
            html.Div([
                html.P('Export Target'),
                dcc.Dropdown(
                    id="export-commodity",
                    options=[
                        {'label': x[0], 'value': x[1]} for x in commodities_set
                    ],
                    value='',
                    clearable=False,
                    placeholder="select commodity"
                ),
                dcc.Graph(id='export-target-graph')
            ]), width=4
        ),
    ]),
    dbc.Row([
        dbc.Col([
            html.Div([
                html.P('Import'),
                dcc.Dropdown(
                    id='import-target-country',
                    options=[
                        {'label': x, 'value': x} for x in import_target
                    ],
                    value='',
                    clearable=False,
                    placeholder='select country'
                ),
                dcc.Graph(id='import-graph')
            ])
        ], width=8),
        dbc.Col([
            html.Div([
                html.P('Crude Oil and Its Product Dependency'),
                dcc.Dropdown(
                    id='dependency-import-target-country',
                    options=[
                        {'label': x, 'value': x} for x in year_range
                    ],
                    value='',
                    clearable=False,
                    placeholder='select year'
                )
            ]),
        ]),
    ])
], className="container")

heesi_app.run_server(debug=True)

