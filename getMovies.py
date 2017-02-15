import imdb
import csv
import sys

a = imdb.IMDb()
f = open("movieslist.txt","a")
for i in range(1530000,1600000):
	try:
		b = a.get_movie(str(i))
	
		if b.guessLanguage()=="English" or b.guessLanguage()=="None":
			print "Working on",i
			plot = a.get_movie_plot(str(i))
			plot = plot.get('data','null')
			
			if plot!='null':
				plot = plot.get('plot','null')
				plot = str(plot)
			
			if len(plot)>5: plot = plot[3:-2]

			genres = b.get('genres','null')
			if genres!='null':
				genres = str(genres)
				genres = genres.replace("u'","")
				genres = genres.replace("'","")
				genres = genres.replace(" ","")
				genres = genres[1:-1].strip()

			director = b.get('director','null')
			if director!='null':
				director = str(director)
				director = director.replace('[<Person id:','')
				director = director.replace('[http] name:_','')
				director = director.replace('_>]','')
				director = ''.join([c for c in director if not c.isdigit()])
				director = director.split(",")
				director = str(director[1].strip()+' '+director[0].strip())

			content=str(i)+"\t"+str(b)+"\t"+str(b.get('long imdb title','null'))+"\t"+str(b.guessLanguage())+"\t"+str(plot)+"\t"+str(director)+"\t"+str(b.get('rating','null'))+"\t"+str(b.get('votes','null'))+"\t"+str(b.get('cover url','null'))+"\t"+str(genres)
			f.write(content+"\n")
	except:
		print "Failed - "+str(i)
		continue