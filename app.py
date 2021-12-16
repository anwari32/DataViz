import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# import dash
# import datetime as dt
# import pandas as pd
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output
# import plotly.graph_objects as go
# import dash_bootstrap_components as dbc
# import json
# import plotly.express as px
# from data_utils import get_rel_countries
# from data_utils import get_data
# from data_utils import get_data_on_demand
#
# from dash.dependencies import Input, Output, State, ClientsideFunction
# from heesi_bps import export_target, plot_dependency, plot_export_stacked_bar, plot_import_stacked_bar, plot_partner
# from heesi_bps import import_target
# from heesi_bps import commodities_set
# from heesi_bps import year_range
# from heesi_bps import heesi_relasi_ekspor
# from heesi_bps import bps_relasi_impor
# from heesi_bps import bps_relasi_import_crude_oil_boe
# from heesi_app import row_viz1, row_viz2
#
#
# app = dash.Dash(__name__)
# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
#
# layout = dict(
#     autosize=True,
#     automargin=True,
#     margin=dict(l=30, r=30, b=20, t=40),
#     hovermode="closest",
#     plot_bgcolor="#F9F9F9",
#     paper_bgcolor="#F9F9F9",
#     legend=dict(font=dict(size=10), orientation="h"),
#     title="Satellite Overview",
#     mapbox=dict(
#         style="light",
#         center=dict(lon=-78.05, lat=42.54),
#         zoom=7,
#     ),
# )
#
# # server = app.server
# app.title = "IF5170 - Visualisasi Ekspor-Impor Indonesia"
#
# import_countries = get_rel_countries(mode='import')
# export_countries = get_rel_countries(mode='export')
# export_countries_on_demand = get_rel_countries(mode='on-demand')
#
# trade_year_range = range(2000, 2021)
#
# app.layout = html.Div([
#     dbc.Row([
#         dbc.Col(
#             html.Div(
#                 [
#                     html.Div(
#                         [
#                             html.Img(
#                                 src=app.get_asset_url("dash-logo.png"),
#                                 id="plotly-image",
#                                 style={
#                                     "height": "60px",
#                                     "width": "auto",
#                                     "margin-bottom": "25px",
#                                 },
#                             )
#                         ],
#                         className="one-third column",
#                     ),
#                     html.Div(
#                         [
#                             html.Div(
#                                 [
#                                     html.H2(
#                                         "Export-Import Visualization",
#                                         style={"margin-bottom": "0px"},
#                                     ),
#                                     html.H5(
#                                         "IF5170 Data Visualization", style={"margin-top": "0px"}
#                                     ),
#                                 ]
#                             )
#                         ],
#                         className="one-half column",
#                         id="title",
#                     ),
#                     html.Div([
#                             html.A(
#                                 html.Button("Give Feedback", id="learn-more-button", style={'backgroundColor':'#F28E2B'},),
#                                 href="https://docs.google.com/forms/d/e/1FAIpQLSenM15q0N6ZPwsWVKnQSYPtnY3D0sjkp0b3Ks5RhbmQC7G4xg/viewform?usp=sf_link",
#                             )
#                         ]
#                     ),
#
#                 ],
#                 id="header",
#             ),
#         ),
#     ]),
#     #html.Div([
#     #    html.Div(
#     #        [
#                 #html.Div(
#                     #html.Div([
#                     #    html.P('Export'),
#                     #    dcc.Dropdown(
#                     #        id="export-target-country",
#                     #        options=[
#                     #            {'label': x, 'value': x} for x in export_target
#                     #        ],
#                     #        value='Japan',
#                     #        clearable=False,
#                     #        placeholder='select export target country'
#                     #    ),
#                     #    dcc.Graph(id='export-graph'),
#                     #])
#                 #),
#
#     #        ],
#     #    ),
#     #]),
#     html.H5("Export Viz"),
#     row_viz1,
#     html.H5("Import Viz"),
#     row_viz2,
#     dbc.Row([
#         html.H5("Export-Import volume"),
#         dbc.Col(
#             html.Div([
#                 html.P("Country")
#             ])
#         ),
#         dbc.Col(
#             html.Div([
#                 dcc.Dropdown(
#                     id='country-dropdown',
#                     options=[
#                         {'label': x, 'value': x} for x in set(export_countries + import_countries)
#                     ],
#                     value='Tiongkok',
#                     clearable=False,
#                 )
#             ]),
#         )
#     ]),
#     dbc.Row([
#        html.Div([
#            dcc.Graph(id='export-import-fig'),
#        ])
#     ]),
#     dbc.Row([
#         html.H5("Indonesia Trade Map"),
#         dbc.Row([
#             dbc.Col(
#                 html.Div([
#                     html.P("Trade"),
#                     dcc.Dropdown(
#                         id='trade_mode',
#                         options=[
#                             {'label': x, 'value': x.lower()} for x in ['Export', 'Import']
#                         ],
#                         value = 'export'
#                     ),
#                 ])
#             ),
#             dbc.Col(
#                 html.Div([
#                     html.P("Commodity"),
#                     dcc.Dropdown(
#                         id='commodity',
#                         options=[
#                             {'label': x, 'value': x.lower()} for x in ['All', 'Crude Oil']
#                         ],
#                         value = 'all'
#                     ),
#                 ])
#             ),
#             dbc.Col(
#                 html.Div([
#                     html.P("Trade Year"),
#                     dcc.Dropdown(
#                         id='trade_year',
#                         options=[
#                             {'label': str(x), 'value': str(x)} for x in trade_year_range
#                         ],
#                         value = '2000'
#                     ),
#                 ])
#             ),
#         ]),
#         dbc.Row([
#             dbc.Col(
#                 html.Div([
#                     dcc.Graph(id='map'),
#                 ])
#             ),
#         ]),
#     ]),
#     dbc.Row([
#         html.H5("Energy Trend Map"),
#         dbc.Col(
#             html.Div([
#                 html.P("Energy Theme"),
#                 dcc.Dropdown(
#                     id='energy_map_menu',
#                     options=[
#                         {'label': str(x[0]), 'value': str(x[1])} for x in
#                         [('Energy Demand Trend', 'energy-demand-trend'), ('Renewable Energy Trend', 'renewable-demand-trend')]
#                     ],
#                     value = 'energy-demand-trend'
#                 ),
#                 dcc.Graph(id='energy_map'),
#             ])
#         )
#     ]),
# ], className="container")
#
#
# # grafik bar chart ekspor on demand
# from data_utils import get_fig_data_on_demand
# # @app.callback(Output('export-on-demand', 'figure'), [Input('country-on-demand', 'value')])
# def display_export_on_demand(country):
#     fig = px.bar(get_data_on_demand(country),
#                  y="year",
#                  x="value",
#                  color="commodity",
#                  barmode="stack",
#                  orientation='h',
#
#
#                  )
#     fig.update_layout(
#     title={
#         'text': "Export on Demand",
#         'y':0.9,
#         'x':0.5,
#         'xanchor': 'center',
#         'yanchor': 'top'})
#
#     # fig = get_fig_data_on_demand(country)
#     return fig
#
#
# # grafik bar chart impor
#
# # grafik ekspor-impor
# @app.callback(Output("export-import-fig", "figure"), [Input("country-dropdown", "value")])
# def display_export_import(country):
#     if (country):
#         title = 'Export-Import Volume with ' + country
#     fig = go.Figure()
#     fig.add_trace(go.Bar(x=list(range(2010, 2021)), y=get_data('export', country),
#                          base=0,
#                          marker_color='#4E79A7',
#                          name='export'))
#     fig.add_trace(go.Bar(x=list(range(2010, 2021)), y=get_data('import', country),
#                          base=0,
#                          marker_color='#F28E2B',
#                          name='import'))
#     fig.update_layout(
#         xaxis_tickfont_size=14,
#         yaxis=dict(
#             title='Transaction Volume (thousand tons) ',
#             titlefont_size=16,
#             tickfont_size=14,
#         ),
#         xaxis=dict(
#             title='Year'
#         ),
#         margin={"r": 20, "t": 20, "l": 70, "b": 30, "pad": 10}
#     )
#     return fig
#
# # grafik ekspor all
# # @app.callback(Output("export-fig", "figure"), [Input("country-dropdown", "value")])
# # def display_export(country):
# #     title = ''
# #     if (country):
# #         title = 'Export Volume to ' + country
# #     fig = go.Figure(
# #         data=go.Bar(y=get_data('export', country), x=list(range(2010, 2021))),
# #         layout={'title': title}
# #     )
# #     return fig
#
#
# # grafik impor all
# # @app.callback(Output("import-fig", "figure"), [Input('country-dropdown', 'value')])
# # def display_import(country):
# #     title = ''
# #     if (country):
# #         title = 'Import Volume from ' + country
# #     fig = go.Figure(
# #         data=go.Bar(y=get_data('import', country), x=list(range(2010, 2021))),
# #         layout={'title': title}
# #     )
# #     return fig
#
# # grafik geo
# @app.callback(Output('map', 'figure'), [Input("trade_mode", "value"), Input("commodity", "value"), Input("trade_year", "value")])
# def display_map(trade, commodity, trade_year):
#     # countries_json = json.load(open('./data/geojson.json'))
#     countries_json = json.load(open('./data/countries.geo.json'))
#     # df = pd.read_csv('./data/fips.csv')
#     df = pd.read_csv('./data/relasi_ekspor_all.csv')
#     if (trade == 'export'):
#         if (commodity == 'crude oil'):
#             df = pd.read_csv('./data/relasi_ekspor_minyak_mentah_by_volume.csv')
#         elif (commodity == 'gas'):
#             df = pd.read_csv('./data/relasi_ekspor_gas_by_volume.csv')
#         else:
#             df = pd.read_csv('./data/relasi_ekspor_all.csv')
#     elif (trade == 'import'):
#         if (commodity == 'crude oil'):
#             df = pd.read_csv('./data/relasi_impor_minyak_bumi_dan_hasil_ribu_ton.csv')
#         # elif (commodity == 'gas'):
#         #     df = pd.read_csv('./data/relasi_impor_gas_by_volume.csv')
#         else:
#             df = pd.read_csv('./data/relasi_impor_all.csv')
#     else:
#         trade = 'import'
#
#     if (not trade_year):
#         trade_year = '2000'
#
#     df_country = pd.read_csv('./data/energy_demand.csv')
#     df_country.drop(df_country.columns[2:], axis=1, inplace=True)
#     df_country.rename(columns={'Country': 'country', 'Code': 'id'}, inplace=True)
#     df = pd.concat([df, df_country], axis=0, ignore_index=True).\
#                                drop_duplicates(subset=['id']).fillna(0)
#     tyr = list(df.loc[:, trade_year])
#     min_val = min(tyr)
#     max_val = max(tyr)
#     # fig = px.choropleth_mapbox(df, geojson=countries_json, locations='fips', color='unemp',
#     fig = px.choropleth_mapbox(df,
#                                geojson=countries_json,
#                                locations='id',
#                                color=str(trade_year),
#                                color_continuous_scale="Viridis",
#                                range_color=(min_val, max_val),
#                                mapbox_style="carto-positron",
#                                zoom=0.8,
#                                center={"lat": 30, "lon": 0},
#                                labels={'unemp': 'unemployment rate'}
#                                )
#     fig.update_layout(margin={"r": 0, "t": 10, "l": 20, "b": 0})
#     fig.layout.coloraxis.colorbar.title = 'Volume<br>(thousand tons)'
#     # fig.show()
#     return fig
#
#
# @app.callback(Output('energy_map', 'figure'), [Input('energy_map_menu', 'value')])
# def display_energy_map(info_type):
#     datapath = './data/energy_demand.csv'
#     col = 'Trend'
#     title = 'Energy Demand Map'
#     label = 'Energy Demand Trend'
#     if (info_type == 'energy-demand-trend'):
#         datapath = './data/energy_demand.csv'
#         col = 'Trend'
#         label = 'Energy Demand Trend'
#     elif (info_type == 'renewable-demand-trend'):
#         datapath = './data/renewable_energy_demand.csv'
#         col = 'Trend'
#         label = 'Renewable Energy Demand Trend'
#
#     countries_json = json.load(open('./data/countries.geo.json'))
#     df = pd.read_csv(datapath)
#     trend = list(df.loc[:, col])
#     # min_trend = min(trend)
#     max_trend = max(trend)
#
#     fig = px.choropleth_mapbox(df, geojson=countries_json, locations="Code", color=col,
#                                color_continuous_scale='viridis',
#                                range_color=(0, max_trend),
#                                mapbox_style="carto-positron",
#                                labels={'Trend': label},
#                                zoom=1,
#                                center={"lat": 30, "lon": 0}
#                                )
#     fig.update_layout(margin={"r": 0, "t": 30, "l": 20, "b": 0})
#     fig.layout.coloraxis.colorbar.title = 'Changes %'
#     fig.layout.coloraxis.colorbar.tickformat = '%0f'
#     return fig
#
# @app.callback(Output('export-graph', 'figure'), [Input('export-target-country', 'value')])
# def display_export_graph(country):
#     fig = plot_export_stacked_bar(heesi_relasi_ekspor, country)
#     return fig
#
# @app.callback(Output('export-target-graph','figure'), [Input('export-commodity', 'value'), Input('export-year', 'value')])
# def display_export_target(commodity, year):
#     fig = plot_partner(heesi_relasi_ekspor, commodity, year, 'Target Ekspor Th. '.format(year))
#     return fig
#
# @app.callback(Output('import-graph', 'figure'), [Input('import-target-country', 'value')])
# def display_import_graph(country):
#     fig = plot_import_stacked_bar(bps_relasi_import_crude_oil_boe, country)
#     return fig
#
# @app.callback(Output('import-dependency', 'figure'), [Input('dependency-import-target-country', 'value')])
# def display_import_dependency(year):
#     fig = plot_dependency(bps_relasi_impor, 'crude_oil', year, 'Mitra Impor Th. {}'.format(year))
#     return fig
#
#
#
# app.run_server(debug=True)
#
