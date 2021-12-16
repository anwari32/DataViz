import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from data_utils import get_rel_countries

import_countries = get_rel_countries(mode='import')
export_countries = get_rel_countries(mode='export')
export_countries_on_demand = get_rel_countries(mode='on-demand')

trade_year_range = range(2000, 2021)

base_navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Export", href="/apps/export")),
            dbc.NavItem(dbc.NavLink("Import", href="/apps/import")),
            dbc.NavItem(dbc.NavLink("Export-Import Volume", href="/apps/export-import-volume")),
            dbc.NavItem(dbc.NavLink("Trade Map", href="/apps/trade-map")),
            dbc.NavItem(dbc.NavLink("Energy Trend Map", href="/apps/energy-trend-map")),
            dbc.NavItem(dbc.NavLink("Feedback 1", href="/apps/feedback1")),
            dbc.NavItem(dbc.NavLink("Feedback 2", href="/apps/feedback2")),
        ],
        brand="Home",
        brand_href="/",
        color="dark",
        dark=True,
    )

base_layout = html.Div([
    base_navbar,
    dbc.Row([
        dbc.Col(
            html.Div(
                [
                    # html.Div(
                    #     [
                    #         html.Img(
                    #             src=app.get_asset_url("dash-logo.png"),
                    #             id="plotly-image",
                    #             style={
                    #                 "height": "60px",
                    #                 "width": "auto",
                    #                 "margin-bottom": "25px",
                    #             },
                    #         )
                    #     ],
                    #     className="one-third column",
                    # ),
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
                                html.Button("Give Feedback", id="learn-more-button", style={'backgroundColor':'#F28E2B'},),
                                href="https://docs.google.com/forms/d/e/1FAIpQLSenM15q0N6ZPwsWVKnQSYPtnY3D0sjkp0b3Ks5RhbmQC7G4xg/viewform?usp=sf_link",
                            )
                        ]
                    ),

                ],
                id="header",
            ),
        ),
    ]),
], className="container")

export_import_volume = html.Div([
    base_navbar,
    dbc.Row([
        html.H5("Export-Import volume"),
        dbc.Col(
            html.Div([
                html.P("Country")
            ])
        ),
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
       html.Div([
           dcc.Graph(id='export-import-fig'),
       ])
    ]),], className="container")

trade_map = html.Div([
    base_navbar,
    dbc.Row([
        html.H5("Indonesia Trade Map"),
        dbc.Row([
            dbc.Col(
                html.Div([
                    html.P("Trade"),
                    dcc.Dropdown(
                        id='trade_mode',
                        options=[
                            {'label': x, 'value': x.lower()} for x in ['Export', 'Import']
                        ],
                        value='export'
                    ),
                ])
            ),
            dbc.Col(
                html.Div([
                    html.P("Commodity"),
                    dcc.Dropdown(
                        id='commodity',
                        options=[
                            {'label': x, 'value': x.lower()} for x in ['All', 'Crude Oil']
                        ],
                        value='all'
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
                        ],
                        value='2000'
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
    ]),], className="container")

energy_trend_map = html.Div([
    base_navbar,
    dbc.Row([
        html.H5("Energy Trend Map"),
        dbc.Col(
            html.Div([
                html.P("Energy Theme"),
                dcc.Dropdown(
                    id='energy_map_menu',
                    options=[
                        {'label': str(x[0]), 'value': str(x[1])} for x in
                        [('Energy Demand Trend', 'energy-demand-trend'), ('Renewable Energy Trend', 'renewable-demand-trend')]
                    ],
                    value = 'energy-demand-trend'
                ),
                dcc.Graph(id='energy_map'),
            ])
        )
    ]),
], className="container")