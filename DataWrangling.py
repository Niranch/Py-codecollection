# -*- coding: utf-8 -*-
"""
Created on Sun May 24 11:24:31 2020

@author: Niranch
"""
#Data source: https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data. 
#Assignment for coursera's IBM DataScience Project on DataWrangling
#Process of cleaning and prepping the automobile dataset(link above) for better analysis

import pandas as pd
import matplotlib as plt
from matplotlib import pyplot
import numpy as np
filename="\\auto.csv"
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv(filename, names = headers)
#Examine few sets of data
print(df.head(5))

#Missing values from source have come as ? in the data file. Replace them with NaN(Not A Null)

df.replace("?", np.nan, inplace = True)
print(df.head(5))

#Evaluate Missing Data

missing_data = df.isnull()
missing_data.head(5)

#Looping through the missing data array get the number of missing rows in each col. True data rows represent missing rows
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("") 
    
#==============================================================================
# Make replacement of missing data by making right decisions. For this dataset
# below replacment was recommended

#==============================================================================
# "normalized-losses": 41 missing data, replace them with mean
# "stroke": 4 missing data, replace them with mean
# "bore": 4 missing data, replace them with mean
# "horsepower": 2 missing data, replace them with mean
# "peak-rpm": 2 missing data, replace them with mean
# Replace by frequency:
# 
# "num-of-doors": 2 missing data, replace them with "four".
# Reason: 84% sedans is four doors. Since four doors is most frequent, it is most likely to occur
# Drop the whole row:
# 
# "price": 4 missing data, simply delete the whole row
# Reason: price is what we want to predict. Any data entry without price data cannot be used for prediction; therefore any row now without price data is not useful to us
#    
#==============================================================================
#==============================================================================

avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses:", avg_norm_loss)
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)

avg_bore=df['bore'].astype('float').mean(axis=0)
print("Average of bore:", avg_bore)
df["bore"].replace(np.nan, avg_bore, inplace=True)

avg_stroke=df['stroke'].astype('float').mean(axis=0)
print("Average of stroke:", avg_stroke)
df["stroke"].replace(np.nan, avg_stroke, inplace=True)

avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
print("Average horsepower:", avg_horsepower)
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
print("Average peak rpm:", avg_peakrpm)
df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)

df['num-of-doors'].value_counts()
df['num-of-doors'].value_counts().idxmax()
df["num-of-doors"].replace(np.nan, "four", inplace=True)


#Drop entier row with NaN in "price" column
df.dropna(subset=["price"], axis=0, inplace=True)

#Reset index, as the rows are dropped
df.reset_index(drop=True, inplace=True)

print("Dataset without missing values: ",df.head())

#Check datatypes of cols and changing the type if necessary
print("Original data Types: ",df.dtypes)
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")
print("Corrected data Types: ",df.dtypes)

#Keep data with uniform metrics for analysis
#Convert mpg to L/100km by mathematical operation (235 divided by mpg)
df['city-L/100km'] = 235/df["city-mpg"]

#Transform mpg to L/100km by mathematical operation (235 divided by mpg)
df["highway-mpg"] = 235/df["highway-mpg"]

#Rename column name from "highway-mpg" to "highway-L/100km"
df.rename(columns={'"highway-mpg"':'highway-L/100km'}, inplace=True)

#Check transformed data 
print("With Corrected Metrics: ", df.head())

#Normalization is the process of transforming values of several variables into a similar range.
#Typical normalizations include scaling the variable so the variable average is 0, 
#scaling the variable so the variance is 1, or scaling variable so the variable values range from 0 to 1
#Target:would like to Normalize variables columns "length", "width" and "height" so their value ranges from 0 to 1.
#Approach: replace original value by (original value)/(maximum value)

df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()
df['height'] = df['height']/df['height'].max() 
# show the scaled columns
print("Scaled Cols: ",df[["length","width","height"]].head())


