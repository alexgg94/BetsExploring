# Unifying and cleaning data original information

# In this file we well create a new file with all files information,
# cleaned of bad information and selecting needed columns

import json
import os.path
import sys
import csv
import numpy as np
import pandas as pd


pathori = "../Data/Raw/"
pathtemp = "../Data/Interim/"
pathdest = "../Data/Processed/"
filetemp = "all_competitions.csv"

# Following folders

season_list = []
for folder in os.listdir(pathori):
    country = folder
    for file in os.listdir(pathori+folder):
        url=pathori + folder + "/" + file
        print "File: ", url
        
        competition = file.split("_")[0]
        season_short = (file.split("_")[1]).split(".")[0]
        season = "20" + season_short[0:2] + "-" + "20" + season_short[2:4]
        
        try:
            # Read file
            parse_dates=["Date"]
            ds = pd.read_csv(url, parse_dates=parse_dates)

            # Select and add cols
            ds_cols = ds[["Div", "Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR", "B365H", "B365D", "B365A","BWH","BWD","BWA" ]]
            ds_cols["Country"] = country
            ds_cols["Season"] = season
            ds_cols["Competition"] = competition

            # Remove incorrect rows
            ds_filter = ds_cols[(ds2["FTHG"]>=0) & (ds2["FTAG"]>=0) & (ds2["FTR"].isin(["H","D","A"]))]

            # Save file
            if not os.path.isfile(pathtemp + filetemp):
                ds_filter.to_csv(pathtemp + filetemp, index="false")
            else:
                with open(pathtemp + filetemp, 'a') as output_file:
                    ds_filter.to_csv(output_file, header=None, index=None)
        except:
            print "Incorrect format: ", url
                