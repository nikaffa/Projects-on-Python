# Projects on Python
Some of my projects on Python I made during CS50 course:

## DNA
- DNA is a program that identifies a person based on their DNA, per the below.
```bash
$ python dna.py databases/large.csv sequences/5.txt
Lavender
```

- DNA is really just a sequence of molecules called nucleotides, arranged into a particular shape (a double helix). Each nucleotide of DNA contains one of four different bases: adenine (A), cytosine (C), guanine (G), or thymine (T). Every human cell has billions of these nucleotides arranged in sequence. Short Tandem Repeats (STRs) are short sequences of DNA bases that tend to repeat consecutively numerous times at specific locations inside of a person’s DNA. 
In its simplest form, a DNA database as a CSV file, wherein each row corresponds to an individual, and each column corresponds to a particular STR:
```bash
name,AGAT,AATG,TATC
Alice,28,42,14
```
The data in the above file would suggest that Alice has the sequence AGAT repeated 28 times consecutively somewhere in her DNA, the sequence AATG repeated 42 times, and TATC repeated 14 times. 
So given a sequence of DNA, how might you identify to whom it belongs? Well, imagine that you looked through the DNA sequence for the longest consecutive sequence of repeated AGATs and found that the longest sequence was 28 repeats long. If you then found that the longest sequence of AATG is 42 repeats long, and the longest sequence of TATC is 14 repeats long, that would provide pretty good evidence that the DNA was Alice’s. 
- The program takes a sequence of DNA and a CSV file containing STR counts for a list of individuals and then output to whom the DNA (most likely) belongs. It requires as its first command-line argument the name of a CSV file containing the STR counts for a list of individuals and should require as its second command-line argument the name of a text file containing the DNA sequence to identify.


## Tournament
