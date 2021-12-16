import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from layouts import base_layout, energy_trend_map, export_import_volume, trade_map
from heesi_app import row_viz1, row_viz2
from response1 import feedback1
from response2 import feedback2
import callbacks


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return base_layout
    elif pathname == '/apps/export':
        return row_viz1
    elif pathname == '/apps/import':
        return row_viz2
    elif pathname == '/apps/export-import-volume':
        return export_import_volume
    elif pathname == '/apps/trade-map':
        return trade_map
    elif pathname == '/apps/energy-trend-map':
        return energy_trend_map
    elif pathname == '/apps/feedback1':
        return feedback1
    elif pathname == '/apps/feedback2':
        return feedback2
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)