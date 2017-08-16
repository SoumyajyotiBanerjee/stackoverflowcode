
import nltk
from nltk.corpus import stopwords
import re


def preprocessing_line(line):
	opline = ""
	line = line.lower()
	line = re.sub(r'[^\w]', ' ', line)
	text=nltk.word_tokenize(line)
	tagged_text = nltk.pos_tag(text)
	stops = set(stopwords.words('english'))
	#Ignore List

	ignore_list = ('CC','CD','DT','EX','IN','JJR','JJS','MD','RB','RBS','RBR','VB','VBD','VBG','VBN','VBP','VBZ','WDT','WP','WP$','WRB')

	for element in tagged_text:
		
		if element[0].strip() not in stops and element[1].strip() not in ignore_list:
			opline +=" "+element[0] + " "


	return opline.strip()


print preprocessing_line("How to do POS tagging using the NLTK POS tagger in Python?")

fr = open("../data/text8_op","w")
i = 0
with open("../data/text8","r") as f:
	for l in f:
		ab = l.split(".")
		for k in ab:
			if i%1000 == 0:
				print "running",i
			i+=1
			am = preprocessing_line(k)
			fr.write(am)



		
	