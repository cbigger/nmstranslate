# nmstranslate
Python3 command-line translator for the various languages in No Man's Sky

NOTES

Only works in lowercase, and punctuation must be part of the word (ie. "vy'keen" works but "Vykeen" will return nothing)

Will default to returning the entire row of the word(s) you are trying to translate

Use the -i, -f, and -a flags to set translation mode to informal, formal, or ancient

Repo includes a text rip of the table from the fandom wiki (just google "gek/korvax/vykeen/atlas language") which includes ~700 words (~220 for the Atlas language) translated into three different "dialects"


lowercase (aka informal)

Capitalized (aka formal) 

ALL-CAPS (aka ancient, only a few words for each language) 


The included .txt files are needed to run the program.

As I am using pandas to create a csv, the program currently spits out the translated words seperately with the pandas notation. I'm trying to get rid of it and have it return reconstructed sentences, but this works for now, and you can type in a whole sentence and have it spit back the words one by one.




Goal is to complete the command-line translator and then make a discord bot which will allow real-time translation right in discord chat.

USAGE

  python3 translator.py [OPTIONS] /path/to/LanguageFile.txt

EXAMPLE (view raw for actual output example as I have no clue how tf to format for githubs stupid readme parser)

$ python3 translator.py korvax.txt 

Starting translator...

No dialect selected.
All available translations will be returned.

What would you like to translate? > how are you
    English Korvax Korvax(Capitalized) Korvax(ALL-CAPS)
#                                                      
667     how    ezn                 Gop             None
    English Korvax Korvax(Capitalized) Korvax(ALL-CAPS)
#                                                      
385     are    lak                 Rus             None
    English Korvax Korvax(Capitalized) Korvax(ALL-CAPS)
#                                                      
388     you   ludo                 Tin             None




REQUIREMENTS

python3 & pandas, everything else should be built in

ISSUES

Need to add reverse translation ie. alien --> english

Need to change output to be strings only, not the full pandas object vomit (currently working on this)

Doesn't clearly show when a word is not found, occasionally making it hard to figure out which part of the sentence may be missing. 
(SHITTY FIX DONE)
