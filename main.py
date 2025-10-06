import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 3000)
pd.set_option('display.max_rows', 25)

df=pd.read_csv("Plane-Crashes.csv")
df=df.drop(columns=["Circumstances","Pax on board","PAX fatalities","Other fatalities","Registration","Operator","Time","Schedule","MSN","YOM","Flight no.","Crash location","Region","Country"])

#PREPROCESSING:
#only 21 century cases:
df["Date"] = pd.to_datetime(df['Date'])
df = df[df["Date"] >="2000-01-01"]
df.dropna(subset=["Aircraft"])
df= df.dropna(subset=["Survivors"])

print(df.head())


plt.hist(df["Survivors"])
plt.title("Histogram of Survivors")
plt.show()

print(df["Flight phase"].value_counts())


print("\nAll aircraft types:\n")
print(df["Aircraft"].value_counts())









