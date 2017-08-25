from gensim.models import doc2vec
from collections import namedtuple

# Load data
doc = []
with open('/home/deeplearning/stackoverflow/part2/tag_reco_data/data/set_1k', 'r') as f_doc:
    for line in f_doc:
        doc.append(str(line))

# Transform data (you can add more data preprocessing steps) 
docs = []
analyzedDocument = namedtuple('AnalyzedDocument', 'words tags')
for i, text in enumerate(doc):
    words = text.lower().split()
    tags = [i]
    docs.append(analyzedDocument(words, tags))

# Train model (set min_count = 1, if you want the model to work with the provided example data set)
model = doc2vec.Doc2Vec(docs, size = 100, window = 300, min_count = 1, workers = 4)

# Get the vectors
#model.docvecs[0]
#model.docvecs[1]

model.save("/home/deeplearning/stackoverflow/part2/tag_reco_data/data/d2v_set_1k")
#ax = doc2vec.Doc2Vec.load("doc2vectrain")
