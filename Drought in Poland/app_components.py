import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

DATA_PATH = "Data"
col_names = ['Site Id','Site Name','Year','Month','Monthly Rainfall','SUMM measurement status','Number of days with snowfall','LDS measurement status','Maximum precipitation [mm]',\
    'MAXO measurement status','First day of the occurrence of maximum precipitation','Last day of maximum precipitation','Number of days with snow cover','LDPS measurement status']

def replace_space(string):
    first_space = string.find(" ")
    second_space = string.find(" ", first_space + 1)
    if second_space>0:
        return string[:first_space] + "." + string[first_space + 1:second_space] + string[second_space + 1:]
    else:
        return string[:first_space] + "." + string[first_space + 1:]   

def prepare_data():
    data_2022 = pd.read_csv(DATA_PATH+'\o_m_2022.csv',encoding = 'unicode_escape',header=None)
    data_2022.columns = col_names
    data_2022.loc[:,'Month Name'] = data_2022.loc[:,'Month'].replace({1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July',\
        8:'August', 9:'September', 10:'October', 11:'November',12:'December'})

    data_2021 = pd.read_csv(DATA_PATH+'\o_m_2021.csv',encoding = 'unicode_escape',header=None)
    data_2021.columns = col_names
    data_2021.loc[:,'Month Name'] = data_2021.loc[:,'Month'].replace({1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July',\
        8:'August', 9:'September', 10:'October', 11:'November',12:'December'})

    full_data = pd.concat([data_2021,data_2022],axis=0)
    return full_data 


def dates_renge(dates):
    slider = html.Div(
            dcc.RangeSlider(
            id='date-slider',
            min=dates.min(),
            max=dates.max(),
            value=[dates.min(), dates.max()],
            marks={str(year): str(year) for year in dates['x'].unique()},
            step=None
        )
    )
    return slider