# PREREQUISITES
# pip install seaborn
# pip install seaborn[stats]

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

print ("IMPORT DATA FROM SPECIFIED FILE")
rawVehicles = "DataIO/FuelEconomy-gov-VehicleData.csv"
try:
    dataVehicles = pd.read_csv(rawVehicles)
    dataVehicles.info()
    #print (dataVehicles.describe())
    print (dataVehicles.describe(include=['object']))
except Exception as e:
    print (f"********** Error importing data: {repr(e)}")

# CALCULATE DESCRIPTIVE STATISTICS
print ("CALCULATE DESCRIPTIVE STATISTICS")
try:
    descrVehicles = dataVehicles.describe()
    print (descrVehicles)
    descrVehicles.to_csv("DataIO/DataFrame_describe.csv")
except Exception as e:
    print (f"********** Error outputing correlation matrix: {repr(e)}")

# CALCULATE CORRELATION MATRIX AND OUTPUT
print ("CALCULATE CORRELATION MATRIX AND OUTPUT")
try:
    matrixCorrelation = dataVehicles.corr(method = 'pearson')
    matrixCorrelation.to_csv("DataIO/DataFrame_corr.csv")
    #matrixCorrelation.to_excel("DataIO/CorrelationMatrix.xlsx")
    sn.heatmap(matrixCorrelation, annot=True)
    plt.show()
except Exception as e:
    print (f"********** Error outputing correlation matrix: {repr(e)}")