import csv
import sys

currentList = []
prevWord = None

for line in sys.stdin:
	word,movieID = line.strip().split("\t")

	if prevWord and prevWord!=word:
		print prevWord,"\t",currentList
		currentList = []

	currentList.append(int(movieID))
	prevWord=word

print prevWord,"\t",currentList
