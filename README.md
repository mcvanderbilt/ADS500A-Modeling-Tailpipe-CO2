# EXAMPLE RESEARCH PAPER FOR STUDENTS #
University of San Diego</br>
Shiley-Marcos School of Engineering</br>
Master of Applied Data Science</br>


ADS-500A: Probability & Statistics for Data Science

---

#### NOTE FOR STUDENTS: #####
This example research is performed using a more recent extract from FuelEconomy.gov and applies more techniques and research than is required for course project. _You may use this repo as one of the required references but **do not** use this to cross reference calculated figures; they will not match._ Additionally, this research is performed significantly beyond that required for your paper. Please check your content against the paper rubric not this sample.

---

#### Course Research Paper Objective
The objective of this analysis is to statistically investigate the association of primary fuel tailpipe carbon dioxide emissions in grams per mile to annual primary-fuel petroleum consumption in barrels after controlling for combined miles-per-gallon for the primary fuel type, vehicle manufacturer, make, engine displacement, engine cylinders, combined luggage and passenger volume in cubic feet, vehicle type, transmission type, and primary fuel type.

---

#### Import Notes/Footnotes Copied from FuelEconomy.gov
- Annual fuel costs shown in 1997-2014 Fuel Economy Guides are based on fuel prices when the guide was originally printed.
1. 1 barrel = 42 gallons. Petroleum consumption is estimated using the Department of Energy's GREET model and includes petroleum consumed from production and refining to distribution and final use. Vehicle manufacture is excluded.
2. The MPG estimates for all 1985-2007 model year vehicles and some 2011-2016 model year vehicles have been updated.  Learn More
3. Unrounded MPG values are not available for some vehicles.
4. This field is only used for blended PHEV vehicles.
5. For model year 2013 and beyond, tailpipe CO2 is based on EPA tests. For previous model years, CO2 is estimated using an EPA emission factor. -1 = Not Available.
6. For PHEVs this is the charge depleting range.
7. Annual fuel cost is based on 15,000 miles, 55% city driving, and the price of fuel used by the vehicle.
8. Interior volume dimensions are not required for two-seater passenger cars or any vehicle classified as truck which includes vans, pickups, special purpose vehicles, minivan and sport utility vehicles.
9. Fuel prices for gasoline and diesel fuel are from the Energy Information Administration and are usually updated weekly.
10. Fuel prices for E85, LPG, and CNG are from the Office of Energy Efficiency and Renewable Energy's Alternative Fuel Price Report and are updated quarterly.
11. For electric and CNG vehicles this number is MPGe (gasoline equivalent miles per gallon).

---

#### Related Links
- <a href="https://github.com/mcvanderbilt/USD-ADS500A">ASD500A Research Project Information for Students (GitHub)</a>
- <a href="https://www.overleaf.com/read/ttgqypjwcpkk">Overleaf LaTeX Files for Written Report</a> (drafted in APA-7)
- <a href="https://fueleconomy.gov/feg/download.shtml">FuelEconomy.gov Download Site</a> (updated 7 Sep 2022; downloaded 11 Sep 2022)
- <a href="https://fueleconomy.gov/feg/ws/">FuelEconomy.gov Web Services (includes data dictionary)</a> (updated 7 Sep 2022; downloaded 11 Sep 2022)

---

#### Python References
- <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html">pandas.DataFrame</a>
- <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html">pandas.DataFrame.corr</a>
- <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html">pandas.read_csv</a>
- <a href ="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html?highlight=to_csv">pandas.DataFrame.to_csv</a>
- <a href ="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html">pandas.DataFrame.to_excel</a>