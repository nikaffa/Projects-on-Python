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


## Readability
Readability figures out what the reading level of a text is. For example:
```bash
$ ./readability
Text: Congratulations! Today is your day. You\'re off to Great Places! You\'re off and away!
Grade 3
```
```bash
$ ./readability
Text: As the average number of letters and words per sentence increases, the Coleman-Liau index gives the text a higher reading level. If you were to take this paragraph, for instance, which has longer words and sentences than either of the prior two examples, the formula would give the text an eleventh grade reading level. 
Grade 11
```
The allgorithm is based on the Coleman-Liau index which designed to output what grade level is needed to understand the text. The formula is: **`index = 0.0588 * L - 0.296 * S - 15.8`**


## Tournament
- Tournament is a program that simulates a number of tournaments of the FIFA World Cup and outputs each team’s probability of winning.
```bash
python tournament.py 2018m.csv
Belgium: 20.9% chance of winning
Brazil: 20.3% chance of winning
Portugal: 14.5% chance of winning
Spain: 13.6% chance of winning
Switzerland: 10.5% chance of winning
Argentina: 6.5% chance of winning
England: 3.7% chance of winning
France: 3.3% chance of winning
Denmark: 2.2% chance of winning
Croatia: 2.0% chance of winning
Colombia: 1.8% chance of winning
Sweden: 0.5% chance of winning
Uruguay: 0.1% chance of winning
Mexico: 0.1% chance of winning
```
- The program simulates the entire tournament by repeatedly simulating rounds many times (e.g. 1000 simulations) until there's left just one team. 
- The algorithm estimates the probability that either team wins a game based on their current FIFA Ratings.