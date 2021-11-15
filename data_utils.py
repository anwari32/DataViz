relasi_ekspor_all = './data/relasi_ekspor_all.csv'
relasi_ekspor_gas_by_value = 'data/relasi_ekspor_gas_by_value.csv'
relasi_ekspor_gas_by_volume = 'data/relasi_ekspor_gas_by_volume.csv'
relasi_ekspor_minyak_mentah_by_value = 'data/relasi_ekspor_minyak_mentah_by_value.csv'
relasi_ekspor_minyak_mentah_by_volume = 'data/relasi_ekspor_minyak_mentah_by_volume.csv'
relasi_impor_all = './data/relasi_impor_all.csv'

import pandas as pd

"""
Get data from csv based on mode.
@param mode:    export -> export data
                import -> import data
@param country: Target country.
@return: list of values.
"""


def get_data(mode, country):
    df = {}
    if (mode == 'export'):
        df = pd.read_csv(relasi_ekspor_all)
    elif (mode == 'import'):
        df = pd.read_csv(relasi_impor_all)
    df = df.set_index('country')
    list_of_countries = list(df.index)
    if (country in list_of_countries):
        return list(df.loc[country])
    else:
        return []


def get_data_on_demand(country):
    df_gas = pd.read_csv(relasi_ekspor_gas_by_value)
    df_oil = pd.read_csv(relasi_ekspor_minyak_mentah_by_value)
    df_stack = pd.concat([stacking_df(df_gas, "gas"), stacking_df(df_oil, "oil")])
    return df_stack[df_stack['country'] == country]

import plotly.graph_objects as go
def get_fig_data_on_demand(country):
    years = list(range(2000, 2020))
    df_gas = pd.read_csv(relasi_ekspor_gas_by_value)
    df_gas = df_gas.set_index('country')
    gas_vals = list(df_gas.loc[country, :])[1:]
    
    df_oil = pd.read_csv(relasi_ekspor_minyak_mentah_by_value)
    df_oil = df_oil.set_index('country')
    oil_vals = list(df_oil.loc[country, :])[1:]

    fig = go.Figure(data=[
        go.Bar(name='gas', x=years, y=gas_vals, yaxis='y'),
        go.Bar(name='oil', x=years, y=oil_vals, yaxis='y')
    ])
    fig.update_layout(barmode='stack')
    return fig


# function to transform data to stack format
def stacking_df(df_input, commodity):
    df_output = df_input.set_index(['country', 'id']).stack().reset_index() \
        .rename(columns={"level_2": 'year', 0: 'value'})
    df_output["commodity"] = str(commodity)
    return df_output


"""
Get relation countries.
@param mode:    all -> all countries,  
                export -> all export targets,
                import -> all import targets.
"""


def get_rel_countries(mode):
    countries = []
    if (mode == 'export'):
        df = pd.read_csv(relasi_ekspor_all)
        df = df.set_index('country')
        countries = list(df.index)
    elif (mode == 'import'):
        df = pd.read_csv(relasi_impor_all)
        df = df.set_index('country')
        countries = list(df.index)
    elif (mode == 'on-demand'):
        df_gas = pd.read_csv(relasi_ekspor_gas_by_value)
        df_oil = pd.read_csv(relasi_ekspor_minyak_mentah_by_value)
        df_stack = pd.concat([stacking_df(df_gas, "gas"), stacking_df(df_oil, "oil")])
        countries = list(df_stack['country'].unique())
    else:
        countries = []
    return countries


geo_map_json = './data/geojson.json'

import json


def load_json(json_file):
    obj = json.load(json_file)
    return obj

