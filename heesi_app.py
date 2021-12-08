import dash
from dash_bootstrap_components._components.Tooltip import Tooltip
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from heesi_bps import export_target, plot_dependency, plot_export_stacked_bar, plot_import_stacked_bar, plot_partner
from heesi_bps import import_target
from heesi_bps import commodities_set
from heesi_bps import year_range
from heesi_bps import heesi_relasi_ekspor
from heesi_bps import bps_relasi_impor
from heesi_bps import bps_relasi_import_crude_oil_boe

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
                    value='Japan',
                    clearable=False,
                    placeholder='select export target country'
                ),
                dcc.Graph(id='export-graph'),
            ]), width=8
        ),
        dbc.Col(
            html.Div([
                html.P('Export Target'),
                dbc.Row([
                    dbc.Col(html.Div([
                        dcc.Dropdown(
                            id="export-commodity",
                            options=[
                                {'label': x[0], 'value': x[1]} for x in commodities_set
                            ],
                            value='crude_oil',
                            clearable=False,
                            placeholder="select commodity"
                        ),
                    ])),
                    dbc.Col(html.Div([
                        dcc.Dropdown(
                            id="export-year",
                            options=[
                                {'label': x, 'value': x} for x in year_range
                            ],
                            value='2000',
                            clearable=False,
                            placeholder="select year"
                        ),
                    ]))
                ]),
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
                    value='Singapura',
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
                    value='2000',
                    clearable=False,
                    placeholder='select year'
                ),
                dcc.Graph(id='import-dependency')
            ]),
        ]),
    ])
], className="container")

@heesi_app.callback(Output('export-graph', 'figure'), [Input('export-target-country', 'value')])
def display_export_graph(country):
    fig = plot_export_stacked_bar(heesi_relasi_ekspor, country)
    return fig

@heesi_app.callback(Output('export-target-graph','figure'), [Input('export-commodity', 'value'), Input('export-year', 'value')])
def display_export_target(commodity, year):
    fig = plot_partner(heesi_relasi_ekspor, commodity, year, 'Target Ekspor Th. '.format(year))
    return fig

@heesi_app.callback(Output('import-graph', 'figure'), [Input('import-target-country', 'value')])
def display_import_graph(country):
    fig = plot_import_stacked_bar(bps_relasi_import_crude_oil_boe, country)
    return fig

@heesi_app.callback(Output('import-dependency', 'figure'), [Input('dependency-import-target-country', 'value')])
def display_import_dependency(year):
    fig = plot_dependency(bps_relasi_impor, 'crude_oil', year, 'Mitra Impor Th. {}'.format(year))
    return fig

# heesi_app.run_server(debug=True)

row_viz1 = dbc.Row([
        dbc.Col(
            html.Div([
                html.P('Target Country'),
                dcc.Dropdown(
                    id="export-target-country",
                    options=[
                        {'label': x, 'value': x} for x in export_target
                    ],
                    value='Japan',
                    clearable=False,
                    placeholder='select export target country'
                ),
                dcc.Graph(id='export-graph'),  
            ])
        ),
        dbc.Col(
            html.Div([
                html.P('Export Target'),
                dbc.Row([
                    dbc.Col(html.Div([
                        dcc.Dropdown(
                            id="export-commodity",
                            options=[
                                {'label': x[0], 'value': x[1]} for x in commodities_set
                            ],
                            value='crude_oil',
                            clearable=False,
                            placeholder="select commodity"
                        ),
                    ])),
                    dbc.Col(html.Div([
                        dcc.Dropdown(
                            id="export-year",
                            options=[
                                {'label': x, 'value': x} for x in year_range
                            ],
                            value='2000',
                            clearable=False,
                            placeholder="select year"
                        ),
                    ]))
                ]),
                dcc.Graph(id='export-target-graph')
            ])
        ),
    ])

row_viz2 = dbc.Row([
        dbc.Col([
            html.Div([
                html.P('Target Country'),
                dcc.Dropdown(
                    id='import-target-country',
                    options=[
                        {'label': x, 'value': x} for x in import_target
                    ],
                    value='Singapura',
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
                    value='2000',
                    clearable=False,
                    placeholder='select year'
                ),
                dcc.Graph(id='import-dependency')
            ]),
        ]),
    ])
