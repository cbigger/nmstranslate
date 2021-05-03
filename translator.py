import pandas as pd
import csv, re, io, datetime, dateutil
import argparse

# add a cli --help argument and a mandatory file argument
parser = argparse.ArgumentParser()
parser.add_argument("LanguageFile", help="the path to the .txt file you want to use")
args = parser.parse_args()


file = open(args.LanguageFile, "r")
rip = file.read()
file.close()

csvone = pd.read_csv(
    (io.StringIO(rip)), sep=" \\t", index_col=0)
sentence = input("GRAH! SPEAK! >").split(" ")
for word in sentence:
    try:
        print(str(csvone[csvone['English']==word]["Vy'keen"]))
    except: print('whoops')
