import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import json
import os

datapath = 'data'
data_all_import = datapath + '/relasi_impor_all.csv'
bps_relasi_import_crude_oil_boe = datapath + '/bps_relasi_impor_minyak_bumi_dan_produk_minyak_bumi_boe.csv'
heesi_relasi_ekspor_coal_boe = datapath + '/heesi_relasi_ekspor_coal_boe.csv'
heesi_relasi_ekspor_crude_oil_boe = datapath + '/heesi_relasi_ekspor_crude_oil_boe.csv'
heesi_coal_balance = datapath + '/heesi_coal_boe.csv'
heesi_crude_oil_balance = datapath + '/heesi_crude_oil_boe.csv'
heesi_lng_balance = datapath + '/heesi_lng_boe.csv'
heesi_lpg_balance = datapath + '/heesi_lpg_boe.csv'

geojson = datapath + '/countries.geo.json'

heesi_energy_balance = {
    'coal': heesi_coal_balance,
    'crude_oil': heesi_crude_oil_balance,
    'lpg': heesi_lpg_balance,
    'lng': heesi_lng_balance
}

heesi_relasi_ekspor = {
    'coal': heesi_relasi_ekspor_coal_boe,
    'crude_oil': heesi_relasi_ekspor_crude_oil_boe
    # 'lpg': '',
    # 'lng': ''
}

bps_relasi_ekspor = {
    'coal': '',
    'crude_oil': '',
    'lpg': '',
    'lng': ''
}

bps_relasi_impor = {
    'coal': '',
    'crude_oil': bps_relasi_import_crude_oil_boe,
    'lpg': '',
    'lng': ''
}

# commodities = ['coal', 'crude_oil', 'lpg', 'lng']
commodities = ['coal', 'crude_oil']
# commodities_set = [('Coal', 'coal'), ('Crude Oil', 'crude_oil'), ('LNG', 'lng'), ('LPG', 'lpg')]
commodities_set = [('Coal', 'coal'), ('Crude Oil', 'crude_oil')]
year_range = list(range(2000, 2021))


### Export and Import Partner
def _get_country_partner(dataset, commodities):
    export_target = []
    for c in commodities:
        if (dataset[c] != '' and os.path.exists(dataset[c])):
            df = pd.read_csv(dataset[c])
            target = list(df['country'])
            export_target += target

    export_target = list(set(export_target))
    return export_target


export_target = _get_country_partner(heesi_relasi_ekspor, commodities)
import_target = _get_country_partner(bps_relasi_impor, commodities)


def plot_partner(dataset, commodity, year, title):
    datapath = dataset[commodity]
    if not os.path.exists(datapath):
        return "{} not found.".format(datapath)
    df = pd.read_csv(datapath)
    rel_ekspor_df = pd.DataFrame()
    rel_ekspor_df['country'] = df['country']
    rel_ekspor_df['value'] = df[str(year)]
    fig = px.pie(rel_ekspor_df, names='country', values='value', title=title)

    return fig


def plot_dependency(dataset, commodity, year, title):
    datapath = dataset[commodity]
    if not os.path.exists(datapath):
        return '{} not found.'.format(datapath)
    df = pd.read_csv(datapath)
    rel_impor_df = pd.DataFrame()
    rel_impor_df['country'] = df['country']
    rel_impor_df['value'] = df[str(year)]
    fig = px.pie(rel_impor_df, names='country', values='value', title=title)
    return fig


def plot_import_fraction(filepath, commodity, year):
    if not (os.path.exists(filepath)):
        return
    df = pd.read_csv(filepath)
    cons_impor_df = df.loc[df['key'].isin(['konsumsi', 'impor'])]
    title = 'Fraksi Impor {} Th. {}'.format(commodity, year)
    fig = px.pie(cons_impor_df, values=str(year), names="key", title=title)
    return fig


def plot_export_fraction(filepath, commodity, year):
    if not (os.path.exists(filepath)):
        return -1
    df = pd.read_csv(filepath)
    df = df.set_index('key')
    df.loc['net_produksi', :] = df.loc['produksi', :] - df.loc['ekspor', :]
    df = df.reset_index()
    net_prod_ekspor_df = df.loc[df['key'].isin(['net_produksi', 'ekspor'])]
    title = 'Fraksi Ekspor {} Th. {}'.format(commodity, year)
    fig = px.pie(net_prod_ekspor_df, values=str(year), names='key', title=title)
    return fig


# Display stacked bar for exports.
def plot_export_stacked_bar(dataset, country):
    # print('country = {}'.format(country))
    coal_export_df = pd.read_csv(dataset['coal'])
    crude_oil_export_df = pd.read_csv(dataset['crude_oil'])

    coal_export_target = list(coal_export_df['country'])
    crude_oil_export_target = list(crude_oil_export_df['country'])
    export_target = list(set(coal_export_target + crude_oil_export_target))

    print(export_target)
    coal_values = []
    crude_oil_values = []
    if (country in coal_export_target):
        coal_values = coal_export_df.loc[coal_export_df['country'] == country, [str(a) for a in range(2000, 2021)]]
        coal_values = list(coal_values.iloc[0])
    else:
        coal_values = np.zeros(21).tolist()

    if (country in crude_oil_export_target):
        crude_oil_values = crude_oil_export_df.loc[
            crude_oil_export_df['country'] == country, [str(a) for a in range(2000, 2021)]]
        crude_oil_values = crude_oil_values.iloc[0]
    else:
        crude_oil_values = np.zeros(21).tolist()

    df = pd.DataFrame()
    df['year'] = range(2000, 2021)
    df['coal'] = list(coal_values)
    df['crude_oil'] = list(crude_oil_values)
    fig = px.bar(df, x='year', y=['coal', 'crude_oil'], title='Our Export to {}'.format(country),
                 labels={'variable': 'commodity', 'value': 'boe'})
    return fig


# Display pie chart representing export target portion by commodity.
def plot_partner(dataset, commodity, year, title):
    datapath = dataset[commodity]
    if not os.path.exists(datapath):
        return "{} not found.".format(datapath)
    df = pd.read_csv(datapath)
    rel_ekspor_df = pd.DataFrame()
    rel_ekspor_df['country'] = df['country']
    rel_ekspor_df['value'] = df[str(year)]
    fig = px.pie(rel_ekspor_df, names='country', values='value', title=title)

    return fig


# Display stacked bar for imports.
def plot_import_stacked_bar(dataset, country):
    import_df = pd.read_csv(dataset)
    import_countries = list(import_df['country'])

    crude_oil_values = import_df.loc[import_df['country'] == country, [str(a) for a in list(range(2000, 2021))]]

    df = pd.DataFrame()
    df['year'] = list(range(2000, 2021))
    df['crude_oil'] = list(crude_oil_values.iloc[0])

    fig = px.bar(df, x='year', y=['crude_oil'], title='Our Import from {}'.format(country),
                 labels={'variable': 'commodity', 'value': 'boe'})
    return fig