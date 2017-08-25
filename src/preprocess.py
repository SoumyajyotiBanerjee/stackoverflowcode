import sys
import optparse
from utils import arg_parser, find_pos_tag
import nltk
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
import re

MIN_TAG_COUNT = 1

def get_tags(data):
    tags = []
    tag_counts = []
    for d in data:
        _tags = d['tags']
        for t in _tags:
            if t not in tags:
                tags.append(t)
                tag_counts.append(1)
            else:
                tag_counts[tags.index(t)] += 1
    return tags, tag_counts

def main(infile, outfile, size):
    with open(infile, 'r') as data_file:
        data = json.load(data_file)
    items = data[:size]

    IGNORE_LIST = ['CC','CD','DT','EX','IN','JJR','JJS','MD','RB','RBS','RBR',\
                   'VB','VBD','VBG','VBN','VBP','VBZ','WDT','WP','WP$','WRB']
    STOPWORDS = set(stopwords.words('english'))
   
    tags, tag_counts = get_tags(items)

    fout = open(outfile, 'w')
    for item in items:
        _tags = item['tags']
        _skip_post = True
        for t in _tags:
            if tag_counts[tags.index(t)] > MIN_TAG_COUNT:
                _skip_post = False

        if _skip_post:
            for t in _tags:
                tag_counts.[tags.index(t)] -= 1
            continue

        text = item['title']+" "+item['body']+" "+" ".join(_tags)
        text = re.sub('\(|\)|\{|\}|\[|\]', ' ', text)
        text = " ".join(re.sub('\?', '. ', text).split())

        lines = text.split(".")
        for line in lines:
            tagged_text = find_pos_tag(line)
            word_list = []
            word_list_append = word_list.append
            for text in tagged_text:
                if text[0].strip() not in STOPWORDS and text[1].strip() not in IGNORE_LIST:
                    word_list_append(text[0])
            proc_text = " ".join(word_list)
            fout.write("%s "%proc_text)
        fout.write('\n')

    for i, count in enumerate(tag_counts):
        if count == 0:
            tags.pop(i)
            tag_counts.pop(i)
    


if __name__ == '__main__':
    opts = arg_parser()
    main(opts.infile, opts.outfile, opts.size)
#Run as $ python proprocess.py -i <input_filename> -o <output_filename> -s <dataset_size>

		
	
