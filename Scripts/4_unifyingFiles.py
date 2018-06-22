# Unifying and cleaning data original information

# In this file we well create a new file with all files information,
# cleaned of bad information and selecting needed columns

import os.path
import sys
import csv
import pandas as pd
from colorama import Fore


pathori = "../Data/Raw/Main/"
pathtemp = "../Data/Interim/"
pathdest = "../Data/Processed/"
filetemp = "main_competitions.csv"

colsdest = ["Country", "Competition", "Season", "Div", "Date", \
            "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR", \
            "B365H", "B365D", "B365A","BSH","BSD","BSA",\
            "BWH","BWD","BWA","GBH","GBD","GBA","IWH","IWD","IWA"\
            "LBH","LBD","LBA","SJH","SJD","SJA","VCH","VCD","VCA"\
            "WHH", "WHD", "WHA"]

# Following folders

cont = 0
season_list = []
os.remove(pathtemp + filetemp)
for folder in os.listdir(pathori):
    country = folder
    for file in os.listdir(pathori+folder):
        url=pathori + folder + "/" + file
        print (Fore.RESET + "Loading file: "+ folder + "/" + file)
        
        competition = file.split("_")[0]
        season_short = (file.split("_")[1]).split(".")[0]
        season = "20" + season_short[0:2] + "-" + "20" + season_short[2:4]
        
        try:
            # Read file
            parse_dates=["Date"]
            ds = pd.read_csv(url, parse_dates=parse_dates, index_col=False)
        
            # Select and add cols
            ds["Country"] = country
            ds["Season"] = season
            ds["Competition"] = competition

            colsori = list(ds)
            #print (ds.head(1))        

            for coldest in colsdest:
                if coldest not in colsori:
                    #print ("Column to add: " + coldest)
                    ds[coldest] = ""    

            ds_cols = ds[colsdest]        
            #print (ds_cols.head(1))

            # Remove incorrect rows
            ds_filter = ds_cols[(ds_cols["FTHG"]>=0) & (ds_cols["FTAG"]>=0) & (ds_cols["FTR"].isin(["H","D","A"]))]

            # Save file
            if not os.path.isfile(pathtemp + filetemp):
                ds_filter.to_csv(pathtemp + filetemp, header=colsdest, index=None)
            else:
                with open(pathtemp + filetemp, 'a') as output_file:
                    ds_filter.to_csv(output_file, header=None, index=None)
        except:
            print (Fore.RED + "Incorrect file format: " + url)
        