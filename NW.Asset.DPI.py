import pandas as pd
import matplotlib.pyplot as plt
net_worth = pd.read_excel('C:/Users/nicok/Documents/Jupyter Visualizations/Household and Nonprofit Net Worth Data - MODIFIED DATES.xlsx',
                         0, usecols = "B")
date_col = pd.read_excel('C:/Users/nicok/Documents/Jupyter Visualizations/Household and Nonprofit Net Worth Data - MODIFIED DATES.xlsx',
                         0, usecols = "A")
DPI = pd.read_excel('C:/Users/nicok/Documents/Jupyter Visualizations/Household and Nonprofit Net Worth Data - MODIFIED DATES.xlsx',
                         0, usecols = "D")
total_asset = pd.read_excel('C:/Users/nicok/Documents/Jupyter Visualizations/Household and Nonprofit Net Worth Data - MODIFIED DATES.xlsx',
                         0, usecols = "C")
nw_vis = plt.plot(date_col, net_worth, label = 'US Net Worth since 1952')
DPI_vis = plt.plot(date_col, DPI, label = 'US Disposable Income since 1952')
asset_vis = plt.plot(date_col, total_asset, label = 'US Total Assets since 1952')
plt.xlabel("Year")
plt.ylabel("Trillions of USD")
plt.legend()
plt.show()