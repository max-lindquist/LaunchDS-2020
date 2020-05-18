import matplotlib.pyplot as plt  # for viz
import seaborn as sns  # for viz
import pandas as pd  # for data manipulation and analysis
import numpy as np  # math funcitonality
import csv
from IPython.display import display


sns.set(style="darkgrid")
sns.set_palette("Dark2")


list = []
filename = "acceptance_rate_data.csv"
df = pd.read_csv(filename)
filename = "school_salary_data.csv"
df2 = pd.read_csv(filename)

schools = df[['School Name', 'Acceptance Rate']]

#schools2 = df2['School Name']
#print(schools2)
#df3 = pd.merge(df,df2)

df["School Name"] = df["School Name"].astype(str)
df2["School Name"] = df2["School Name"].astype(str)

#print(df3)
df["School Name"] = [c.strip() for c in df["School Name"]]
df2["School Name"] = [c.strip() for c in df2["School Name"]]

df2["Starting Median Salary"] = [c.replace('$','') for c in df2["Starting Median Salary"]]
df2["Starting Median Salary"] = [c.strip() for c in df2["Starting Median Salary"]]
df2["Starting Median Salary"] = [c.replace(',','') for c in df2["Starting Median Salary"]]
df2["Starting Median Salary"] = [float(c) for c in df2["Starting Median Salary"]]


df2["Mid-Career Median Salary"] = [c.replace('$','') for c in df2["Mid-Career Median Salary"]]
df2["Mid-Career Median Salary"] = [c.strip() for c in df2["Mid-Career Median Salary"]]
df2["Mid-Career Median Salary"] = [c.replace(',','') for c in df2["Mid-Career Median Salary"]]
df2["Mid-Career Median Salary"] = [float(c) for c in df2["Mid-Career Median Salary"]]

merged_data = pd.merge(df,df2, on ="School Name")


merged_data["Acceptance Rate"] = [c.replace('%','') for c in merged_data["Acceptance Rate"]]
merged_data["Acceptance Rate"] = [float(c) for c in merged_data["Acceptance Rate"]]



#ax = sns.scatterplot(x = "Acceptance Rate", y = "Starting Median Salary", s = 60, data = merged_data)
#ax.set( title = "Median Starting Salary vs Acceptance Rate", ylabel = "Median Salary (Dollars)", xlabel = "Acceptance Rate (%)",)
#plt.show()

ax = sns.scatterplot(x = "Acceptance Rate", y = "Mid-Career Median Salary", s=60, data = merged_data)
ax.set( title = "Median Mid-Career Salary vs Acceptance Rate", ylabel = "Median Salary (Dollars)", xlabel = "Acceptance Rate (%)",)
plt.show()


regions = df2.groupby("Region")

midwest = regions.get_group("Midwestern\xa0")
california = regions.get_group("California\xa0")
northeast = regions.get_group("Northeastern\xa0")
south = regions.get_group("Southern\xa0")
west = regions.get_group("Western\xa0")

print(midwest)
meanmw = midwest["Starting Median Salary"].median()
meancal = california["Starting Median Salary"].median()
meanne = northeast["Starting Median Salary"].median()
meansouth = south["Starting Median Salary"].median()
meanwest = west["Starting Median Salary"].median()


b = pd.DataFrame({'Geographic Location': ["California","Northeast","West", "South","Midwest"],
                  'Median Starting Salary': [meancal,meanne,meanwest, meansouth,meanmw]})


qualitative_colors = sns.color_palette("BuGn",5)
ax = sns.barplot(data = b, palette = "BuGn_r", x = "Geographic Location", y = "Median Starting Salary")
#ax = sns.barplot(meanne)
#ax = sns.barplot(meansouth)
#ax = sns.barplot(meanwest)

plt.ylim(20000,60000)
plt.title("Median Starting Salary of Major US Colleges, by Region")
plt.show()