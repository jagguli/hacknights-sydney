"""
1 get data.
2 analyse input data
3 train algotithm
4 test algorithm


- classsify job type by profession, area, salary range, sector, date posted
- forex rates
- interest rates
"""

import datetime
import logging
import pandas as pd
import numpy as np


def load_employment_data():
    def parse_datetime(line):
        try:
            return datetime.datetime.strptime(line.strip(), "%b-%Y")
        except:
            return datetime.datetime.strptime(line.strip(), "%B-%Y")

    return pd.read_csv("data/intrest_rates.txt",
                       parse_dates=[0], date_parser=parse_datetime,
                       index_col=0)


def load_seek_ei():
    def parse_datetime(line):
        return datetime.datetime.strptime(line.strip(), "%b-%y")
    return pd.read_csv("data/SEEK_AU_EI_Data_Apr2012.xlsx.csv",
                       parse_dates=[0], date_parser=parse_datetime,
                       index_col=0)

interest_rates = load_employment_data()
employment_index = load_seek_ei()

mindate = max(interest_rates.index.min(), employment_index.index.min())
maxdate = min(interest_rates.index.max(), employment_index.index.max())
print mindate, maxdate

ir_data = interest_rates[mindate:maxdate]
# possible bug in pandas employment_index[employment_index.index[0]:]
# throws slice error #WTF?
if employment_index.index[0] == mindate:
    ei_data = employment_index[:maxdate]
else:
    ei_data = employment_index[mindate:maxdate]

#ir_data.plot(figsize=(10, 8))
#ei_data.plot(figsize=(10, 8))

xArr = map(lambda x: [1, x], ei_data['NSW'])
yArr = ir_data['Rate']


def standRegres(xArr, yArr):
    xMat = np.mat(xArr)
    yMat = np.mat(yArr).T
    xTx = xMat.T * xMat
    if np.linalg.det(xTx) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = xTx.I * (xMat.T * yMat)
    return ws

print standRegres(xArr, yArr)
