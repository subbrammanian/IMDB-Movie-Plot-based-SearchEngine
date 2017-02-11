import sys
import nltk.tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
import csv

def processPlot(content):
	toker = RegexpTokenizer(r'\w+')
	tokens = toker.tokenize(content.lower())
	porter_stemmer = PorterStemmer()
	stopwordsSet = set(stopwords.words('english'))
	final_tokens = [porter_stemmer.stem(t) for t in tokens if t not in stopwordsSet ]
	return final_tokens

reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
	if len(line)==10:
		movID, plot = line[0].strip(),line[4].strip()
		plotTokens = processPlot(plot)

		for word in plotTokens:
			print word,"\t",movID
	