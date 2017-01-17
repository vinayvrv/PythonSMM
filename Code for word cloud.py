from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Read the whole text.
IN = open("D:\\SMM\\Project\\Speeches\\Bernie_Sanders\\Bernei_Sander_Commencement_Speech.txt")

text = IN.read().strip().lower()


#Convert all the required text into a single string here 
#and store them in word_string


wordcloud = WordCloud(stopwords=STOPWORDS).generate(text)


plt.imshow(wordcloud)
plt.axis('off')
plt.show()