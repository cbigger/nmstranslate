import pandas as pd
import csv, re, io
import argparse

# add a cli --help argument and a mandatory file argument, as well as flags for the diff dialects
# default dialect is informal
parser = argparse.ArgumentParser()
parser.add_argument("LanguageFile", help="--> the path to the .txt file you want to use")
parser.add_argument("-i","--informal", help="--> use the informal (lowercase) dialect (default)", action="store_true", default="True")
parser.add_argument("-f","--formal", help="--> use the formal (capitalized) dialect", action="store_true")
parser.add_argument("-a","--ancient", help="--> search for an ancient (ALL-CAPS) translation", action="store_true")
args = parser.parse_args()

# can't translate to two languages at once
if args.formal and args.ancient:
    print("Please choose only one desired translation path")
    exit()

# undo default when other dialect flags are present
if args.formal or args.ancient:
    args.informal = False

print("\nStarting translator...")

# set dialects
if args.formal:
    print("\nDialect set to formal.")
    dialect=2
elif args.ancient:
    print("\nDialect set to ancient. Good luck!")
    dialect=3
elif args.informal:
    print("\nDialect set to informal (default).")
    dialect=1

# open the LanguageFile
try:
    file = open(args.LanguageFile, "r")
    rip = file.read()
    file.close()
except FileNotFoundError:
    print("File not found. Please double check path.")
    exit()

# begin the input and translate loop
while (True):
    csvone = pd.read_csv(
        (io.StringIO(rip)), sep=" \\t", index_col=0, dtype=str, engine='python')
    sentence = input("\nWhat would you like to translate? > ").split(" ")
    for word in sentence:
        try:
            if csvone[csvone['English']==word].empty:
                  print("\n"+word+" (NOT FOUND)")
            else:
                  print(csvone[csvone['English']==word].iloc[:,dialect])

        except:
            print('Something went wrong! Send gizmo a DM.')
            exit()
