####################################################
## Finding Duplicates of candidates ids in files.
## Will look for a pattern in each line and return the matched pattern (candidate id)
## ASSUMES THAT ALL CANDIDATES PATTERN IS ^#[0-9]+
## That means beginning of the line with # and followed by numbers. 
## Then selects only candidates that appear > 1 times and export to a csv file
## csv file constains the candidates ids and the count (how many times it was found in the files)
## Data Source Files are in a subdirectory called 'data' .
## Results exported to 'duplicated_candidates_vasco.csv'
##
## Miguel Vazquez-Prada , October 2021
## miguelvb (at) posteo.net
####################################################

import os
import re
import csv

cwd = os.getcwd() 
data_dir = os.path.join(cwd, 'data' ) # where data is (text files)
files = os.listdir(data_dir)
candidates = list()
for file_ in files:
    fl = open(os.path.join(data_dir,file_))
    data = fl.readlines()
    print('-----  Reading file ' , file_ ) 
    for line in data:
        cand = re.search('^#[0-9]+',line)
        if cand is not None:
            cand = cand.group()
            candidates.append(cand)
            #print(cand)
    fl.close()

## candidates is the list of found candidates in the files.
## now we look for the ones that appear two or more times.

dupls  = [ {'candidate' : x, 'count' : candidates.count(x)}  for x in candidates if candidates.count(x) > 1] # select only the ones that appear >1 times
duplicated  = [i for n, i in enumerate(dupls) if i not in dupls[n + 1:]]


fields =  ['candidate', 'count']
with open('duplicated_candidates_vasco.csv', 'wb') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fields)
    writer.writeheader()
    writer.writerows(duplicated)

csvfile.close()
