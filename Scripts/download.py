import wget
import sys
import os
from colorama import Fore
import pandas as pd

index_url="../Scripts/file_index.csv"
main_base_url = "http://www.football-data.co.uk/mmz4281/"
extra_base_url = "http://www.football-data.co.uk/new/"
dest_base_url = "/home/david/Documentos/PracticaFinal/BetsExploring/Data/Raw/"

seasons = [ "0304", "0405", "0506", "0607", 
            "0708", "0809", "0910", "1011", 
            "1112", "1213", "1314", "1415", 
            "1516", "1617", "1718" ]

def downloadFiles():
    ds = pd.read_csv(index_url)
    for index, row in ds.iterrows():
        for season in seasons:
            file_ori_url = main_base_url + season + '/' + row['file'] + '.csv'
            file_dest_url = dest_base_url + row['country'] + '/' + row['competition'] + "_" + season + ".csv"
            print
            print Fore.BLUE + "Reading: " + row['country'], row['file'], row['competition'], season
            print Fore.GREEN + file_ori_url 
            print Fore.GREEN + "-> " + file_dest_url
            
            if not os.path.exists(dest_base_url + row['country']):
                os.makedirs(dest_base_url + row['country'])

            try:
                wget.download(file_ori_url, file_dest_url)
            except:
                print Fore.RED + "Could not download " + file_ori_url 
    print
    print Fore.YELLOW + "Download finished"
                
    
if __name__ == '__main__':
    if not os.path.exists("../Data/Raw"):
        os.makedirs("../Data/Raw")
    downloadFiles()