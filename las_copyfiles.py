##import os
#os.listdir("C:\\Users\\James Mcdonald\\OneDrive\\Documents\\Python Scripts\\lasio-master\\lasio-master\\tests\\examples")
##testdir=os.listdir("Z:\Data\GeoPhysical_Logs\LAS")
##print (testdir)

##for folder in testdir:
##    if os.path.isdir(testdir + "\\" + folder):
##        lasfile=os.path.abspath(folder)
##        print(folder)

import sys, os, shutil

##testfilename = "34013208930000_MUD-GR-DIR-GAS-LI-RP_HOR_1184K_2288_10402.las"

root = "Z:\Data\GeoPhysical_Logs\LAS"
path = os.path.join(root, "targetdirectory")

flas = open("C:\\Users\\10001810\\OneDrive - State of Ohio\\Documents\\Projects\\Python Scripts\\qryUTICAEOR_TOPS_CWRU_Logs_v2.txt", 'rt')

while True:
    line=flas.readline()
    if not line:
        break
    lasfilename=line.strip().strip("\n")
    for path, subdirs, files in os.walk(root):
        for name in files:
            if name == lasfilename:
                print(name)
                print(path)
                shutil.copy(os.path.join(path,name), "C:\\Temp")
            
##        print(os.path.join(path, name))
##        print(name)
