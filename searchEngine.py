import sys
import csv
import nltk.tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer

reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
reverseIndex = {}

#Creating Reverse Index for the Search Engine
def createIndex():
	try:
		f = open("index.txt","r")
		for line in f:
			line = line.split("\t")
			word,indexList = line[0].strip(),line[1].strip()
			if reverseIndex.get(word,0)==0:
				reverseIndex[word]=indexList
		print "\nINDEX LOADED SUCCESSFULLY!\n"
	except:
		print "\nLOADING INDEX FAILED...TERMINATING PROGRAM!\n"
		exit()

#Getting input
def getTokens(keyword):
	keyword = keyword.strip()
	toker = RegexpTokenizer(r'\w+')
	tokens = toker.tokenize(keyword.lower())
	porter_stemmer = PorterStemmer()
	stopwordsSet = set(stopwords.words('english'))  #Converting to set to increase performance
	final_tokens = [porter_stemmer.stem(t) for t in tokens if t not in stopwordsSet]   #Stemming all the words and removing stop words
	final_tokens = [temp.decode('unicode_escape').encode('ascii','ignore') for temp in final_tokens]  #Converting unicode to ascii
	return final_tokens

def getMovieDetails(v1,v2,v3):
	f = open("movieslist.txt","r")
	for line in f:
		content = line.split("\t")
		if str(content[0]).strip()==v1:
			p1 = content
		elif str(content[0]).strip()==v2:
			p2 = content
		elif str(content[0]).strip()==v3:
			p3 = content
		else:
			pass
	print "Movie: "+p1[2].strip()+" || Rating: "+p1[6].strip().replace("null","Not Available")+" ("+p1[7].strip().replace("null","No")+" votes) || Genre: "+p1[9].strip().replace("null","Not Available")
	print "Movie: "+p2[2].strip()+" || Rating: "+p2[6].strip().replace("null","Not Available")+" ("+p2[7].strip().replace("null","No")+" votes) || Genre: "+p2[9].strip().replace("null","Not Available")
	print "Movie: "+p3[2].strip()+" || Rating: "+p3[6].strip().replace("null","Not Available")+" ("+p3[7].strip().replace("null","No")+" votes) || Genre: "+p3[9].strip().replace("null","Not Available")

if __name__ == "__main__":
	createIndex()
	inp = raw_input("Enter: ")
	keyword=inp.strip()
	final_tokens = getTokens(keyword)
	cwList = []
	rDic = {}
	for word in final_tokens:
		cwList=reverseIndex.get(word,None)[1:-1].split(",")
		if cwList:
			for val in cwList:
				val = val.strip()
				rDic[val]=rDic.get(val,0)+1
	r1=r2=r3=0
	v1=v2=v3="No result"
	for k,count in rDic.items():
		if count>r1:
			r1,v1 = count,k
		elif count>r2:
			r2,v2 = count,k
		elif count>r3:
			r3,v3 = count,k
		else:
			pass
	getMovieDetails(v1,v2,v3)