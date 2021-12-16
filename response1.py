import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from layouts import base_navbar

df_r1 = pd.read_csv("data/Responses1.csv", usecols=[1, 2, 3, 4, 6, 7], header=None, skiprows=1)

fig1 = px.pie(df_r1.groupby(1).size().reset_index().rename({0 : 'Total', 1: 'Respon'}, axis=1),
              values='Total',
              names='Respon',
              title="Apakah Anda dapat melihat dan menentukan komoditas ekspor Indonesia yang paling dominan?")

fig2 = px.bar(df_r1.groupby(2).size().reset_index().rename({0: 'Total', 2: 'Nilai Rating'}, axis=1),
              x='Nilai Rating',
              range_x = [0,7],
              y='Total',
              range_y = [0,10],
              text= 'Total',
              title="Bagaimana penilaian Anda tentang visualisasi untuk menentukan komoditas ekspor Indonesia?")

fig2.update_traces(textposition="outside")

fig3 = px.pie(df_r1.groupby(3).size().reset_index().rename({0: 'Total', 3: 'Respon'}, axis=1),
              values='Total',
              names='Respon',
              title="Apakah Anda dapat melihat sumber energi yang paling banyak diimpor?")

fig4 = px.bar(df_r1.groupby(4).size().reset_index().rename({0: 'Total', 4: 'Nilai Rating'}, axis=1),
              x='Nilai Rating',
              range_x=[0, 7],
              y='Total',
              range_y=[0, 10],
              text='Total',
              title="Bagaimana penilaian Anda terhadap visualisasi yang menjelaskan sumber energi yang Indonesia impor?<br>"
                    "(1: Sangat Baik dan 6: Sangat Buruk)")

fig4.update_traces(textposition="outside")

fig5 = px.pie(df_r1.groupby(6).size().reset_index().rename({0: 'Total', 6: 'Respon'}, axis=1),
              values='Total',
              names='Respon',
              title="Apakah Anda dapat menemukan negara mana saja yang menjadi tempat bergantung Indonesia<br>dalam pemenuhan energi domestik?")

fig6 = px.bar(df_r1.groupby(7).size().reset_index().rename({0: 'Total', 7: 'Nilai Rating'}, axis=1),
              x='Nilai Rating',
              range_x = [0, 7],
              y='Total',
              range_y=[0, 10],
              text='Total',
              title="Bagaimana penilaian Anda terhadap visualisasi yang digunakan untuk mencari negara tempat<br>bergantung "
                    "Indonesia dalam pemenuhan energi domestik? (1: Paling Baik dan 6: Sangat Buruk)")

fig6.update_traces(textposition="outside")


import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

# app = dash.Dash()

feedback1 = html.Div([
    base_navbar,
    html.Div([
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
        ])
    ])
], className="container")
# app.run_server(debug=True)
