import optparse
import nltk
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
import re

IGNORE_LIST = ['CC','CD','DT','EX','IN','JJR','JJS','MD','RB','RBS','RBR',\
               'VB','VBD','VBG','VBN','VBP','VBZ','WDT','WP','WP$','WRB']

STOPWORDS = set(stopwords.words('english'))

def arg_parser():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--infile", dest="infile",
                       action="store", help="Input file name")
    parser.add_option("-o", "--outfile", dest="outfile",
                       action="store", help="Output file name")
    options, args = parser.parse_args()
    return options.infile, options.outfile


def find_pos_tag(line):
    """Find POS tags of a given line"""
    line = line.lower()
    line = re.sub(r'[^\w]', ' ', line)
    tokens = word_tokenize(line)
    tagged_text = pos_tag(tokens)
    return tagged_text

def word_removal(line):
    """Removes stopwords and words with unwanted POS tags from a line"""
    word_list = []
    tagged_text = find_pos_tag(line)
    word_list_append = word_list.append
    for text in tagged_text:
	if text[0].strip() not in STOPWORDS and text[1].strip() not in IGNORE_LIST:
            word_list_append(text[0])

    return " ".join(word_list)

if __name__ == '__main__':
    res = word_removal('Testing python POS tagger via this line')
    print res
