import pandas as pd
import numpy as np
import csv, re, io, datetime, dateutil

file = open("G:\Watchtower\\vykeenlanguagetable.txt", "r")
rip = file.read()
file.close()

csvone = pd.read_csv(
    (io.StringIO(rip)), sep=" \\t", index_col=0)
sentence = input("GRAH! SPEAK! >").split(" ")
for word in sentence:
    try:
        print(str(csvone[csvone['English']==word]["Vy'keen"]))
    except: print('whoops')
