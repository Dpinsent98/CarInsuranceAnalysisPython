
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Car = pd.read_csv("C:/Users/dragan/Desktop/UsedCarData.csv")

print(Car.head())

print(Car.shape)

Car_Clean = Car.dropna()

print(Car_Clean.shape)

print(Car_Clean.describe())

Car_Clean_Year = Car_Clean.groupby("Year")["Selling_Price"].agg(["mean","max","min","count"]).reset_index()

Car_Clean_Year["Rank"] = Car_Clean_Year["mean"].rank(ascending = False)

print(Car_Clean_Year.sort_values("Year",ascending = False))

Car_Clean_Fuel = Car_Clean.groupby("Fuel_Type")["Selling_Price"].agg(["mean","max","min","count"])

print(Car_Clean_Fuel)

Car_Clean["Depreciation_%"] = ((Car_Clean["Present_Price"] - Car_Clean["Selling_Price"])/ Car_Clean["Present_Price"])*100

Car_Clean_GroupedYear = Car_Clean.groupby("Year")["Depreciation_%"].agg(["mean"]).sort_values("Year", ascending = False)

Car_Clean_GroupedYear.columns = ["Depreciation"]
 
print(Car_Clean_GroupedYear)

plt.subplot(1,2,1)

plt.scatter(Car_Clean["Year"], Car_Clean["Selling_Price"], color = "red")

plt.xlabel("Year")

plt.ylabel("Selling Price")

plt.title("Selling Price Against Year")

plt.grid()

plt.subplot(1,2,2)

plt.pie(Car_Clean_Fuel["count"], colors = ["red","blue"])

plt.title("Fuel Type Distribution")

plt.legend(["Petrol","Diesel"])

plt.show()


