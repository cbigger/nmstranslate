# nmstranslate
Python3 command-line translator for the various languages in No Man's Sky

Repo includes a text rip of the table from the fandom wiki (just google "gek/korvax/vykeen language") which includes ~700 words translated into three different "dialects" - lowercase (informal), -capitalized (formal), and ALL-CAPS (ancient, only a few words for each language). 
These .txt files are needed to run the program.

Currently, as I am using pandas to create a csv, the program spits out the translated words seperately with the pandas notation. I'm trying to get rid of it and have it return reconstructed sentences.
Goal is to complete the command-line translator and then make a discord bot which will allow real-time translation right in discord chat.

usage: python translator.py /path/to/LanguageFile.txt
