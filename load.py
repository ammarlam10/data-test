
import pandas as pd

#!pip install dbnomics

from dbnomics import fetch_series, fetch_series_by_api_link

# \provider_code/dataset_code/series_code

import pandas as pd

def get_from_oecd(sdmx_query):
    return pd.read_csv(
        f"https://stats.oecd.org/SDMX-JSON/data/{sdmx_query}?contentType=csv"
    )

# print(fetch_series('Eurostat/ei_bsco_m/M.BAL.BS-CSMCI.NSA.DE')['dataset_name'].iloc[0])

df1=fetch_series('Eurostat/ei_bsco_m/M.BAL.BS-CSMCI.NSA.DE')

# fetch_series('Eurostat/ei_bsco_m/M.BAL.BS-CSMCI.NSA.DE').columns

#print(fetch_series('Eurostat/ei_bsin_m_r2/M.BAL.BS-ICI.NSA.DE')['dataset_name'].iloc[0])

df2=fetch_series('Eurostat/ei_bsin_m_r2/M.BAL.BS-ICI.NSA.DE')

#fetch_series('Eurostat/ei_bsin_m_r2/M.BAL.BS-ICI.NSA.DE').columns

#print(fetch_series('Eurostat/ei_bsbu_m_r2/M.BS-CCI-BAL.NSA.DE')['dataset_name'].iloc[0])

df3=fetch_series('Eurostat/ei_bsbu_m_r2/M.BS-CCI-BAL.NSA.DE')

#fetch_series('Eurostat/ei_bsbu_m_r2/M.BS-CCI-BAL.NSA.DE').columns

#print(fetch_series('Eurostat/ei_bsrt_m_r2/M.BAL.BS-RAS.NSA.DE')['dataset_name'].iloc[0])
df4=fetch_series('Eurostat/ei_bsrt_m_r2/M.BAL.BS-RAS.NSA.DE')

#fetch_series('Eurostat/ei_bsrt_m_r2/M.BAL.BS-RAS.NSA.DE').columns

#print(fetch_series('Eurostat/ei_bsse_m_r2/M.BAL.BS-PE3M.NSA.DE')['dataset_name'].iloc[0])

df5=fetch_series('Eurostat/ei_bsse_m_r2/M.BAL.BS-PE3M.NSA.DE')

#fetch_series('Eurostat/ei_bsse_m_r2/M.BAL.BS-PE3M.NSA.DE').columns

#print(fetch_series('Eurostat/ei_bssi_m_r2/M.BS-CCI-BAL.NSA.DE')['dataset_name'].iloc[0])

df6=fetch_series('Eurostat/ei_bssi_m_r2/M.BS-CCI-BAL.NSA.DE')

#fetch_series('Eurostat/ei_bssi_m_r2/M.BS-CCI-BAL.NSA.DE').columns

#print(fetch_series('Eurostat/ei_bsse_m_r2/M.BAL.BS-PE3M.NSA.DE')['dataset_name'].iloc[0])

df7=fetch_series('Eurostat/ei_bsse_m_r2/M.BAL.BS-PE3M.NSA.DE')

#fetch_series('Eurostat/ei_bsse_m_r2/M.BAL.BS-PE3M.NSA.DE').columns

#euro zone business climate
#print(fetch_series('Eurostat/ei_bsci_m_r2/M.BS-BCI.SA.EA19')['dataset_name'].iloc[0])

df8=fetch_series('Eurostat/ei_bsci_m_r2/M.BS-BCI.SA.EA19')

#euro zone business climate
#fetch_series('Eurostat/ei_bsci_m_r2/M.BS-BCI.SA.EA19').columns

#Financial services - monthly data
#print(fetch_series('Eurostat/ei_bsfs_m/M.NSA.K.BS-DEVP3.EU27_2020')['dataset_name'].iloc[0])

df9=fetch_series('Eurostat/ei_bsfs_m/M.NSA.K.BS-DEVP3.EU27_2020')

#Financial services - monthly data
#fetch_series('Eurostat/ei_bsfs_m/M.NSA.K.BS-DEVP3.EU27_2020').columns

#Monthly – Million euro – Total economy – Total economy
#print(fetch_series('Eurostat/ei_bpm6ca_m/M.MIO_EUR.S1.S1.NSA.CA.BAL.WRL_REST.DE')['dataset_name'].iloc[0])

df10=fetch_series('Eurostat/ei_bpm6ca_m/M.MIO_EUR.S1.S1.NSA.CA.BAL.WRL_REST.DE')

#Monthly – Million euro – Total economy – Total economy

#fetch_series('Eurostat/ei_bpm6ca_m/M.MIO_EUR.S1.S1.NSA.CA.BAL.WRL_REST.DE').columns

#Financial account - monthly data [ei_bpm6fa_m]
#print(fetch_series('Eurostat/ei_bpm6fa_m/M.MIO_EUR.S1.S1.NSA.EO.NET.WRL_REST.DE')['dataset_name'].iloc[0])

df11=fetch_series('Eurostat/ei_bpm6fa_m/M.MIO_EUR.S1.S1.NSA.EO.NET.WRL_REST.DE')

#Financial account - monthly data [ei_bpm6fa_m]
#fetch_series('Eurostat/ei_bpm6fa_m/M.MIO_EUR.S1.S1.NSA.EO.NET.WRL_REST.DE').columns

#Harmonised index of consumer prices - monthly data [ei_cphi_m]
#print(fetch_series('Eurostat/ei_cphi_m/M.NSA.HICP2015.CP-HI00.DE')['dataset_name'].iloc[0])

df12=fetch_series('Eurostat/ei_cphi_m/M.NSA.HICP2015.CP-HI00.DE')

#Harmonised index of consumer prices - monthly data [ei_cphi_m]
#fetch_series('Eurostat/ei_cphi_m/M.NSA.HICP2015.CP-HI00.DE').columns

#energy monthly
#print(fetch_series('Eurostat/ei_isen_m/M.NSA.IS-CEL-GWH.DE')['dataset_name'].iloc[0])

df13=fetch_series('Eurostat/ei_isen_m/M.NSA.IS-CEL-GWH.DE')

#energy monthly
#fetch_series('Eurostat/ei_isen_m/M.NSA.IS-CEL-GWH.DE').columns

#print(fetch_series('Eurostat/ei_cphi_m/M.NSA.HICP2015.CP-HI00.DE')['dataset_name'].iloc[0])

#df11.shape

#df9

#df10

#pd.concat([df10,df11], axis=0, ignore_index=True)

output=pd.concat([df1,df2,df3,df4,df5,df8,df9,df12,df13], axis=0, ignore_index=True)

#output.index

#df10 = df10.reset_index(drop=True)

#df10

#output

output.to_csv('regression_data.csv')

'''from google.colab import files
files.download('regression_data.csv')

len(output['series_name'].unique())

df1['series_name'].unique()

df2['series_name'].unique()

df3['series_name'].unique()

df4['series_name'].unique()

df5['series_name'].unique()

df6['series_name'].unique()

df7['series_name'].unique()

df8['series_name'].unique()

df9['series_name'].unique()

df10['series_name'].unique()

df11['series_name'].unique()

df12['series_name'].unique()

df13['series_name'].unique()

df14['series_name'].unique()

'''