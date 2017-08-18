import sys
import optparse
import utils
from utils import word_removal, find_pos_tag

'''
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

'''
def arg_parser():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--infile", dest="infile",
                       action="store", help="Input file name")
    parser.add_option("-o", "--outfile", dest="outfile",
                       action="store", help="Output file name")
    options, args = parser.parse_args()
    return options.infile, options.outfile

def main(infile, outfile):
    fr = open(outfile,"w")
    i = 0
    with open(infile,"r") as f:
	for l in f:
            ab = l.split(".")
            for k in ab:
                if i%1000 == 0:
    		    print "running",i
		i+=1
		am = word_removal(k)
		fr.write(am)

if __name__ == '__main__':
    infile, outfile = arg_parser()
    main(infile, outfile)
#Run as $ python proprocess.py -i <input_filename> -o <output_filename>
#print word_removal("How to do POS tagging using the NLTK POS tagger in Python?")

		
	
