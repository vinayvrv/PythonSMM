ABOUT THE CODE:

1. There is a code which is used for the word cloud it is named as "code for word cloud.py". It uses the library Wordcloud and mathplotlib.
   and produces a visual representation of the words used by the candidate in the candidate.

2. POS tagger, tags the words to identify the core issues addressed by the candidate and then this data is used for generating POS wordcloud.
   ( The tags used are NNP, NN, JJ)

3. "Match POS with tweets" file/code, looks up all the POS tagged words for each candidate in the labbled tweets files to generate the numbers of times 
   the POS tagged word occurs in each category of labled tweets i.e positive or negative. This gives a genearal opinion of the citizens towards the agenda of the candidates.

4. The Stemmer code, stem the given POS tagged word. This was done to get even a clearer representation of the word cloud.

