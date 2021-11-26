from numpy import nan
import pandas as pd
import plotly.graph_objects as go
import os

# Read file and get values of its key.
def read_file(filepath, key):
    if key not in ['produksi', 'ekspor', 'impor', 'konsumsi']:
        return
    df = pd.read_csv(filepath)
    df = df.set_index('Aspek')
    return list(df.loc[key, :])

# Generate plot
def plot(x_data, y_data, plot_type, x_title="Year", y_title="Barrel Oil Equivalent / Year"):
    if plot_type not in ['pie', 'stacked', 'bar', 'line']:
        return

    fig = {}
    return fig


### Export-Import
IMPORT_COMMODITY = [('All', 'all'), ('Crude Oil and Its Products', 'crude_oil_and_products')]

def get_normalized_import_data(filepath):
    if os.path.exists(filepath):
        df = pd.read_csv(data_all_import)
        indexed_df = df[df['id'].notna()]
        indexed_df = indexed_df.set_index('country')
        median = indexed_df[[str(a) for a in list(range(2000, 2021))]].median()
        normalized_df = indexed_df[[str(a) for a in list(range(2000, 2021))]] / median
        normalized_df['id'] = indexed_df['id']
        return normalized_df
    return

# Create map for normalized import map.
def get_normalized_import_map(filepath, year):
    if (os.path.exists(filepath)):
        df = get_normalized_import_data(filepath)
        country_df = df[['id', str(year)]]
