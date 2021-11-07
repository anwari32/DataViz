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
    else:
        countries = []
    return countries
    

