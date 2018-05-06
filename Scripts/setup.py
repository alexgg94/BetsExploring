import wget
import sys
import os
from colorama import Fore

main_base_url = "http://www.football-data.co.uk/mmz4281/"
extra_base_url = "http://www.football-data.co.uk/new/"

countries = [  "England", "Scotland", "Germany", 
                "Italy", "Spain", "France", 
                "Netherlands", "Belgium", "Portugal", 
                "Turkey", "Greece", "Argentina", 
                "Austria", "Brazil", "China", 
                "Denmark", "Finland", "Ireland", 
                "Japan", "Mexico", "Norway", 
                "Poland", "Romania", "Russia", 
                "Sweden", "Switzerland", "USA" ]

seasons = [ "0304", "0405", "0506", "0607", 
            "0708", "0809", "0910", "1011", 
            "1112", "1213", "1314", "1415", 
            "1516", "1617", "1718" ]

def download(country):
    print(Fore.GREEN + "Downloading " + country + "...")
    if country == "England":
        for season in seasons:
            try:
                wget.download(main_base_url + season + "/E0.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/England/Premier_" + season + ".csv")
            except:
                print(Fore.RED + "Could not download " + main_base_url + season + "/E0.csv" + Fore.GREEN)
            try:
                wget.download(main_base_url + season + "/E1.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/England/Championship_" + season + ".csv")
            except:
                print(Fore.RED + "Could not download " + main_base_url + season + "/E1.csv" + Fore.GREEN)
            try:
                wget.download(main_base_url + season + "/E2.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/England/League1_" + season + ".csv")
            except:
                print(Fore.RED + "Could not download " + main_base_url + season + "/E2.csv" + Fore.GREEN)
            try:
                wget.download(main_base_url + season + "/E3.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/England/League2_" + season + ".csv")
            except:
                print(Fore.RED + "Could not download " + main_base_url + season + "/E3.csv" + Fore.GREEN)
            try:
                wget.download(main_base_url + season + "/EC.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/England/Conference_" + season + ".csv") 
            except:
                print(Fore.RED + "Could not download " + main_base_url + season + "/EC.csv" + Fore.GREEN)
    elif country == "Scotland":
        for season in seasons:
            try:
                wget.download(main_base_url + season + "/SC0.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Scotland/Premier_" + season + ".csv")
            except:
                print(Fore.RED + "Could not download " + main_base_url + season + "/SC0.csv" + Fore.GREEN)
            try:
                wget.download(main_base_url + season + "/SC1.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Scotland/Division1_" + season + ".csv")
            except:
                print(Fore.RED + "Could not download " + main_base_url + season + "/SC1.csv" + Fore.GREEN)
            try:
                wget.download(main_base_url + season + "/SC2.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Scotland/Division2_" + season + ".csv")
            except:
                print(Fore.RED + "Could not download " + main_base_url + season + "/SC2.csv" + Fore.GREEN)
            try:
                wget.download(main_base_url + season + "/SC3.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Scotland/Division3_" + season + ".csv")
            except:
                print(Fore.RED + "Could not download " + main_base_url + season + "/SC3.csv" + Fore.GREEN)
    elif country == "Germany":
        for season in seasons:
            try:
                wget.download(main_base_url + season + "/D1.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Germany/Bundesliga1_" + season + ".csv")
            except:
                print(Fore.RED + "Could not download " + main_base_url + season + "/D1.csv" + Fore.GREEN)
            try:
                wget.download(main_base_url + season + "/D2.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Germany/Bundesliga2_" + season + ".csv")
            except:
                print(Fore.RED + "Could not download " + main_base_url + season + "/D2.csv" + Fore.GREEN)

    elif country == "Italy":
        for season in seasons:
            try:
                wget.download(main_base_url + season + "/I1.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Italy/SerieA_" + season + ".csv")
            except:
                print(Fore.RED + "Could not download " + main_base_url + season + "/I1.csv" + Fore.GREEN)
            try:
                wget.download(main_base_url + season + "/I2.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Italy/SerieB_" + season + ".csv")
            except:
                print(Fore.RED + "Could not download " + main_base_url + season + "/I2.csv" + Fore.GREEN)

    elif country == "Spain":
        for season in seasons:
            try:
                wget.download(main_base_url + season + "/SP1.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Spain/Primera_" + season + ".csv")
            except:
                print(Fore.RED + "Could not download " + main_base_url + season + "/SP1.csv" + Fore.GREEN)
            try:
                wget.download(main_base_url + season + "/SP2.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Spain/Segunda_" + season + ".csv")
            except:
                print(Fore.RED + "Could not download " + main_base_url + season + "/SP2.csv" + Fore.GREEN)
    elif country == "France":
        for season in seasons:
            try:
                wget.download(main_base_url + season + "/F1.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/France/LeChampionnat_" + season + ".csv")
            except:
                print(Fore.RED + "Could not download " + main_base_url + season + "/F1.csv" + Fore.GREEN)
            try:
                wget.download(main_base_url + season + "/F2.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/France/Division2_" + season + ".csv")
            except:
                print(Fore.RED + "Could not download " + main_base_url + season + "/F2.csv" + Fore.GREEN)
    elif country == "Netherlands":
        for season in seasons:
            try:
                wget.download(main_base_url + season + "/N1.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Netherlands/Eredivisie_" + season + ".csv")
            except:
                print(Fore.RED + "Could not download " + main_base_url + season + "/N1.csv" + Fore.GREEN)
    elif country == "Belgium":
        for season in seasons:
            try:
                wget.download(main_base_url + season + "/B1.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Belgium/JupilerLeague_" + season + ".csv")
            except:
                print(Fore.RED + "Could not download " + main_base_url + season + "/B1.csv" + Fore.GREEN)
    elif country == "Portugal":
        for season in seasons:
            try:
                wget.download(main_base_url + season + "/P1.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Portugal/Liga1_" + season + ".csv")
            except:
                print(Fore.RED + "Could not download " + main_base_url + season + "/P1.csv" + Fore.GREEN)
    elif country == "Turkey":
        for season in seasons:
            try:
                wget.download(main_base_url + season + "/T1.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Turkey/FutbolLigi1_" + season + ".csv")
            except:
                print(Fore.RED + "Could not download " + main_base_url + season + "/T1.csv" + Fore.GREEN)
    elif country == "Greece":
        for season in seasons:
            try:
                wget.download(main_base_url + season + "/G1.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Greece/EthnikiKatigoria_" + season + ".csv")
            except:
                print(Fore.RED + "Could not download " + main_base_url + season + "/G1.csv" + Fore.GREEN)
    elif country == "Argentina":
            try:
                wget.download(extra_base_url + "/ARG.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Argentina/Liga.csv")
            except:
                print(Fore.RED + "Could not download " + extra_base_url + "/ARG.csv" + Fore.GREEN)
    elif country == "Austria":
            try:
                wget.download(extra_base_url + "/AUT.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Austria/Liga.csv")
            except:
                print(Fore.RED + "Could not download " + extra_base_url + "/AUT.csv" + Fore.GREEN)
    elif country == "Brazil":
            try:
                wget.download(extra_base_url +  "/BRA.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Brazil/Liga.csv")
            except:
                print(Fore.RED + "Could not download " + extra_base_url +  "/BRA.csv" + Fore.GREEN)
    elif country == "China":
            try:
                wget.download(extra_base_url +  "/CHN.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/China/Liga.csv")
            except:
                print(Fore.RED + "Could not download " + extra_base_url +  "/CHN.csv" + Fore.GREEN)
    elif country == "Denmark":
            try:
                wget.download(extra_base_url +  "/DNK.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Denmark/Liga.csv")
            except:
                print(Fore.RED + "Could not download " + extra_base_url +  "/DNK.csv" + Fore.GREEN)
    elif country == "Finland":
            try:
                wget.download(extra_base_url +  "/FIN.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Finland/Liga.csv")
            except:
                print(Fore.RED + "Could not download " + extra_base_url +  "/FIN.csv" + Fore.GREEN)
    elif country == "Ireland":
            try:
                wget.download(extra_base_url +  "/IRL.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Ireland/Liga.csv")
            except:
                print(Fore.RED + "Could not download " + extra_base_url +  "/IRL.csv" + Fore.GREEN)
    elif country == "Japan":
            try:
                wget.download(extra_base_url +  "/JPN.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Japan/Liga.csv")
            except:
                print(Fore.RED + "Could not download " + extra_base_url +  "/JPN.csv" + Fore.GREEN)
    elif country == "Mexico":
            try:
                wget.download(extra_base_url +  "/MEX.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Mexico/Liga.csv")
            except:
                print(Fore.RED + "Could not download " + extra_base_url +  "/MEX.csv" + Fore.GREEN)
    elif country == "Norway":
            try:
                wget.download(extra_base_url +  "/NOR.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Norway/Liga.csv")
            except:
                print(Fore.RED + "Could not download " + extra_base_url +  "/NOR.csv" + Fore.GREEN)
    elif country == "Poland":
            try:
                wget.download(extra_base_url +  "/POL.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Poland/Liga.csv")
            except:
                print(Fore.RED + "Could not download " + extra_base_url +  "/POL.csv" + Fore.GREEN)
    elif country == "Romania":
            try:
                wget.download(extra_base_url +  "/ROU.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Romania/Liga.csv")
            except:
                print(Fore.RED + "Could not download " + extra_base_url +  "/ROU.csv" + Fore.GREEN)
    elif country == "Russia":
            try:
                wget.download(extra_base_url +  "/RUS.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Russia/Liga.csv")
            except:
                print(Fore.RED + "Could not download " + extra_base_url +  "/RUS.csv" + Fore.GREEN)
    elif country == "Sweden":
            try:
                wget.download(extra_base_url +  "/SWE.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Sweden/Liga.csv")
            except:
                print(Fore.RED + "Could not download " + extra_base_url +  "/SWE.csv" + Fore.GREEN)
    elif country == "Switzerland":
            try:
                wget.download(extra_base_url +  "/SWZ.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/Switzerland/Liga.csv")
            except:
                print(Fore.RED + "Could not download " + extra_base_url +  "/SWZ.csv" + Fore.GREEN)
    elif country == "USA":
            try:
                wget.download(extra_base_url +  "/USA.csv", "/home/alex/Master/BigData/BetsExploring/Data/Raw/USA/Liga.csv")
            except:
                print(Fore.RED + "Could not download " + extra_base_url +  "/USA.csv" + Fore.GREEN)

if __name__ == '__main__':
    if not os.path.exists("../Data/Raw"):
        os.makedirs("../Data/Raw")

    for country in countries:
        if not os.path.exists("../Data/Raw/" + country):
            os.makedirs("../Data/Raw/" + country)
        download(country)
        