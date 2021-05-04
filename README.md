# nmstranslate
Python3 command-line translator for the various languages in No Man's Sky

ISSUES:

Doesn't clearly show when a word is not found, occasionally making it hard to figure out which part of the sentence may be missing. SHITTY FIX DONE

Repo includes a text rip of the table from the fandom wiki (just google "gek/korvax/vykeen language") which includes ~700 words translated into three different "dialects":


lowercase (aka informal)

Capitalized (aka formal) 

ALL-CAPS (aka ancient, only a few words for each language) 


These .txt files are needed to run the program.
As I am using pandas to create a csv, the program currently spits out the translated words seperately with the pandas notation. I'm trying to get rid of it and have it return reconstructed sentences, but this works for now, and you can type in a whole sentence and have it spit back the words one by one.


Goal is to complete the command-line translator and then make a discord bot which will allow real-time translation right in discord chat.

usage: 

  python3 translator.py [OPTIONS] /path/to/LanguageFile.txt




requires pandas, everything else should be built in

