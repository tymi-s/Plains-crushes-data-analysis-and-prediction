import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import train_test_split
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


#survivorst histogram
plt.hist(df["Survivors"])
plt.title("Histogram of Survivors")
plt.show()

#other data
print(df["Flight phase"].value_counts())
print("\nAll aircraft types:\n")
print(df["Aircraft"].value_counts())


#changing surviviors to binary data:
df["Survivors"] = df["Survivors"].map({"Yes":1,"No":0})

print(df.head())

X = df.drop(columns=["Survivors","Date"])
y = df["Survivors"]


#TRAIN TEST SPLIT:
X_train, X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)







