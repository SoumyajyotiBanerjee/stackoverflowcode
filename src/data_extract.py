import xml.etree.ElementTree as ET
import json
import re
from utils import arg_parser

def main(infile, outfile):
    tree = ET.parse(infile)
    root = tree.getroot()
    _regex = re.compile('<.*?>|\n|"')
    data_list = []
    data_list_append = data_list.append
    tag_set = set()
    for child in root:
        data = child.attrib
        #body = " ".join(re.sub(_regex, ' ', data['Body']).split())
        title = None
        if data.get('Title'):
            title = " ".join(re.sub(_regex, ' ', data['Title']).split())
        tags=None
        if data.get('Tags'):
            tags = re.sub('<|>', ' ', data['Tags']).split()
            tag_set = tag_set.union(set(tags))
        if title==None or tags==None:
            continue
        #data_list_append({'body': body, 'tags': tags, 'title': title})
    
    #f = open(outfile+'.json', 'w')
    #dumps = json.dumps(data_list, sort_keys=True, indent=2)
    #f.write(dumps)
    #f.close()

    fl = open(outfile+'tags.txt', 'w')
    tag_list = list(tag_set)
    for item in tag_list:
        fl.write("%s\n"%item)
    
    
if __name__ == '__main__':
    infile, outfile = arg_parser()
    main(infile, outfile)

