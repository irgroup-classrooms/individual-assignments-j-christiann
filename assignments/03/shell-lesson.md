How do you get the first three lines of the file 2014-01_JA.tsv?
How do you get the total number of lines in each of the *.tsvfiles?
How do you get the file with the highest number of lines and how many does it have? Can you get the output with a single command line call?

1. 
head -n 3 2014-01_JA.tsv

2.
wc -l *.tsv

3. 
wc -l *.tsv | sort -nr | head -n 2 | tail -n 1
