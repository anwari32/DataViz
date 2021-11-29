import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from data_utils import get_rel_countries
from data_utils import get_data
from data_utils import get_data_on_demand

heesi_app = dash.Dash(__name__)
heesi_app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

heesi_app.layout = html.Div([
    dbc.Row([
        dbc.Col(
            html.Div([
                html.P("Commodity"),
                dcc.Dropdown(
                    id="profile_commodity",
                    options=[
                        {'label': x[0], 'value': x[1]} for x in [('All', 'all'), ('Coal', 'coal'), ('Crude Oil', 'crude_oil'), ('Gas', 'gas')]
                    ],
                    value='',
                    clearable=False,
                ),
            ])
        ),
        dbc.Col(
            html.Div([
                html.P('Aspect'),
                dcc.Dropdown(
                    id="profile_aspect",
                    options=[
                        {'label': x[0], 'value': x[1]} for x in [('Consumption', 'cons'), ('Production', 'prod'), ('Export', 'Import'), ('Import', 'import')]
                    ],
                    value='',
                    clearable=False,
                )
            ])
        )
    ]),
    dbc.Row([
        dbc.Col(
            html.Div([
                dcc.Graph(id='profile_commodity_graph')
            ])
        ),
    ]),
    dbc.Row([
        html.Div([
            html.P('Dependency')
        ])   
    ]),
    dbc.Row([
        dbc.Col(
            html.Div([
                dcc.Graph(id="fuel_import_dependency_ratio_graph")
            ]),
        ),
        dbc.Col(
            html.Div([
                dcc.Graph(id="import_source_comparison_graph")
            ]),
        )
    ]),


], className="container")

heesi_app.run_server(debug=True)

