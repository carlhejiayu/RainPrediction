import pandas as pd
import numpy as np

def getData():
    CSVData = pd.read_csv('2016.csv').fillna(0)
    Label = CSVData['Total Precip (mm)']
    processData  = CSVData.drop(['Date/Time', 'Month','Day','Total Precip (mm)'],1)
    processData['Total Rain Flag'] = processData['Total Rain Flag'].map({0:0, 'T':1 ,'M':2 })
    processData['Total Snow Flag'] = processData['Total Snow Flag'].map({0: 0, 'T': 1, 'M': 2})
    processData['Total Precip Flag'] = processData['Total Precip Flag'].map({0: 0, 'T': 1, 'M': 2})
    processData['Spd of Max Gust (km/h)'] = processData['Spd of Max Gust (km/h)'].replace(['<31'],1)
    return processData, Label
