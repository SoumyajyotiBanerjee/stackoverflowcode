import json

with open('/home/sobasu/Projects/tag_reco_data/askubuntu.json', 'r') as data_file:
    data = json.load(data_file)

items = data[:5]
data_list = []
f = open('out.txt', 'w')
f2 = open('out_tag.txt', 'w')
tag_set = set()
for item in items:
    text = " ".join(item['title'].split())+" "+" ".join(item['body'].split())+" "+" ".join(item['tags'])
    f.write('%s\n'%text)
    tag_set = tag_set.union(set(item['tags']))
tag_set = list(tag_set)
f3 = open('tags.txt', 'w')
for tag in tag_set:
    f3.write("%s\n"%tag)
n = len(tag_set)
for item in items:
    tags = item['tags']
    vec = [0]*n
    for tag in tags:
        vec[tag_set.index(tag)]=1
    f2.write("%s\n"%vec)

