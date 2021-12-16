import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from layouts import base_navbar

df_r2 = pd.read_csv("data/Responses2.csv", usecols=[3, 4, 5, 6, 9, 10, 11, 12, 15, 16, 19, 20, 23, 24, 25], header=None, skiprows=1)

# Visualisasi Ekspor
fig1 = px.pie(df_r2.groupby(3).size().reset_index().rename({0 : 'Total', 3: 'Respon'}, axis=1),
              values='Total',
              names='Respon',
              title="Apakah Anda dapat membandingkan besaran ekspor batubara dan minyak bumi untuk tiap negara?")

fig2 = px.pie(df_r2.groupby(10).size().reset_index().rename({0 : 'Total', 10: 'Respon'}, axis=1),
              values='Total',
              names='Respon',
              title="Apakah Anda dapat menentukan negara yang menjadi target ekspor batubara atau minyak bumi <br>yang paling dominan untuk tahun tertentu?")

fig3 = px.bar(df_r2.groupby(5).size().reset_index().rename({0: 'Total', 5: 'Nilai Rating'}, axis=1),
              x='Nilai Rating',
              range_x = [0,6],
              y='Total',
              range_y = [0,5],
              text= 'Total',
              title="Bagaimana penilaian Anda terhadap visualisasi perbandingan jumlah ekspor komoditas energi <br>pada negara target ekspor? "
              "(nilai 1 = sangat baik dan nilai 5 = sangat buruk)")

fig3.update_traces(textposition="outside")

fig4 = px.bar(df_r2.groupby(6).size().reset_index().rename({0: 'Total', 6: 'Nilai Rating'}, axis=1),
              x='Nilai Rating',
              range_x = [0,6],
              y='Total',
              range_y = [0,5],
              text= 'Total',
              title="Bagaimana penilaian Anda terhadap visualisasi perbandingan jumlah ekspor ke tiap negara?"
              "<br>(nilai 1 = sangat baik dan nilai 5 = sangat buruk)")

fig4.update_traces(textposition="outside")

# Visualisasi Impor
fig5 = px.pie(df_r2.groupby(9).size().reset_index().rename({0 : 'Total', 9: 'Respon'}, axis=1),
              values='Total',
              names='Respon',
              title="Apakah Anda dapat melihat dan menentukan tren impor energi Indonesia dari negara lain?")

fig6 = px.pie(df_r2.groupby(4).size().reset_index().rename({0 : 'Total', 4: 'Respon'}, axis=1),
              values='Total',
              names='Respon',
              title="Apakah Anda dapat melihat negara yang menjadi tempat bergantung Indonesia untuk pemenuhan <br>suplai energi domestik nasional?")

fig7 = px.bar(df_r2.groupby(11).size().reset_index().rename({0: 'Total', 11: 'Nilai Rating'}, axis=1),
              x='Nilai Rating',
              range_x = [0,6],
              y='Total',
              range_y = [0,5],
              text= 'Total',
              title="Bagaimana penilaian Anda tentang visualisasi besaran impor energi Indonesia?"
              "<br>(nilai 1 = sangat baik dan nilai 5 = sangat buruk)")

fig7.update_traces(textposition="outside")

fig8 = px.bar(df_r2.groupby(12).size().reset_index().rename({0: 'Total', 12: 'Nilai Rating'}, axis=1),
              x='Nilai Rating',
              range_x = [0,6],
              y='Total',
              range_y = [0,5],
              text= 'Total',
              title="Bagaimana penilaian Anda tentang visualisasi negara yang menjadi asal impor Indonesia?"
              "<br>(nilai 1 = sangat baik dan nilai 5 = sangat buruk)")

fig8.update_traces(textposition="outside")

# Visualisasi Trade Balance
fig9 = px.pie(df_r2.groupby(15).size().reset_index().rename({0 : 'Total', 15: 'Respon'}, axis=1),
              values='Total',
              names='Respon',
              title="Apakah Anda dapat melihat trade-balance Indonesia pada negara tertentu secara umum?")

fig10 = px.bar(df_r2.groupby(16).size().reset_index().rename({0: 'Total', 16: 'Nilai Rating'}, axis=1),
              x='Nilai Rating',
              range_x = [0,6],
              y='Total',
              range_y = [0,5],
              text= 'Total',
              title="Bagaimana penilaian Anda terhadap visualisasi Trade Balance terhadap insight yang Anda <br>harapkan atau temukan?"
               "(nilai 1 = sangat baik dan nilai 5 = sangat buruk)")

fig10.update_traces(textposition="outside")

# Visualisasi Trade Map
fig11 = px.pie(df_r2.groupby(19).size().reset_index().rename({0 : 'Total', 19: 'Respon'}, axis=1),
              values='Total',
              names='Respon',
              title="Apakah Anda dapat menemukan negara yang menjadi mitra ekspor <br>atau impor komoditas tertentu pada peta?")

fig12 = px.bar(df_r2.groupby(20).size().reset_index().rename({0: 'Total', 20: 'Nilai Rating'}, axis=1),
              x='Nilai Rating',
              range_x = [0,6],
              y='Total',
              range_y = [0,5],
              text= 'Total',
              title="Bagaimana penilaian Anda terhadap visualisasi peta Trade Map di atas terhadap insight yang <br>Anda harapkan atau temukan?"
               "(nilai 1 = sangat baik dan nilai 5 = sangat buruk)")

fig12.update_traces(textposition="outside")

# Visualisasi Peta Tematik
fig13 = px.pie(df_r2.groupby(23).size().reset_index().rename({0 : 'Total', 23: 'Respon'}, axis=1),
              values='Total',
              names='Respon',
              title="Apakah Anda dapat menemukan negara yang memiliki peningkatan penggunaan energi paling tinggi?")

fig14 = px.pie(df_r2.groupby(24).size().reset_index().rename({0 : 'Total', 24: 'Respon'}, axis=1),
              values='Total',
              names='Respon',
              title="Apakah Anda dapat menemukan negara dengan pertumbuhan investasi paling besar<br>pada energi terbarukan?")

fig15 = px.bar(df_r2.groupby(25).size().reset_index().rename({0: 'Total', 25: 'Nilai Rating'}, axis=1),
              x='Nilai Rating',
              range_x = [0,6],
              y='Total',
              range_y = [0,5],
              text= 'Total',
              title="Bagaimana penilaian Anda terhadap visualisasi peta tematik di atas terhadap<br>insight yang Anda harapkan atau dapatkan?"
               "(nilai 1 = sangat baik dan nilai 5 = sangat buruk)")

fig15.update_traces(textposition="outside")



import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

# app = dash.Dash()
# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

feedback2 = html.Div([
    base_navbar,
    html.Div([
        html.H2("Visualisasi Ekspor"),
        html.Div([
            dbc.Row([
                html.Div([
                    dcc.Graph(figure=fig1)
                ])
            ]),
        ]),
        html.Div([
            dbc.Row([
                html.Div([
                    dcc.Graph(figure=fig2)
                ])
            ]),
        ]),
        html.Div([
            dbc.Row([
                html.Div([
                    dcc.Graph(figure=fig3)
                ])
            ]),
        ]),
        html.Div([
            dbc.Row([
                html.Div([
                    dcc.Graph(figure=fig4)
                ])
            ]),
        ]),
        html.H2("Visualisasi Impor"),
        html.Div([
            dbc.Row([
                html.Div([
                    dcc.Graph(figure=fig5)
                ])
            ]),
        ]),
        html.Div([
            dbc.Row([
                html.Div([
                    dcc.Graph(figure=fig6)
                ])
            ]),
        ]),
        html.Div([
            dbc.Row([
                html.Div([
                    dcc.Graph(figure=fig7)
                ])
            ]),
        ]),
        html.Div([
            dbc.Row([
                html.Div([
                    dcc.Graph(figure=fig8)
                ])
            ]),
        ]),
        html.H2("Visualisasi Trade Balance"),
        html.Div([
            dbc.Row([
                html.Div([
                    dcc.Graph(figure=fig9)
                ])
            ])
        ]),
        html.Div([
            dbc.Row([
                html.Div([
                    dcc.Graph(figure=fig10)
                ])
            ])
        ]),
        html.H2("Visualisasi Trade Map"),
        html.Div([
            dbc.Row([
                html.Div([
                    dcc.Graph(figure=fig11)
                ])
            ])
        ]),
        html.Div([
            dbc.Row([
                html.Div([
                    dcc.Graph(figure=fig12)
                ])
            ])
        ]),
        html.H2("Visualisasi Peta Tematik"),
        html.Div([
            dbc.Row([
                html.Div([
                    dcc.Graph(figure=fig13)
                ])
            ])
        ]),
        html.Div([
            dbc.Row([
                html.Div([
                    dcc.Graph(figure=fig14)
                ])
            ])
        ]),
        html.Div([
            dbc.Row([
                html.Div([
                    dcc.Graph(figure=fig15)
                ])
            ])
        ]),
    ])
], className="container")
# app.run_server(debug=True)
