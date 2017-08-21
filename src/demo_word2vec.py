import gensim
from nltk.corpus import brown

sentences = brown.sents()
model = gensim.models.Word2Vec(sentences, min_count=1)
model.save('brown_model')
print "Brown corpus model saved."

model = gensim.models.Word2Vec.load('brown_model')
#words most similar to mother
print model.most_similar('mother')
#find the odd one out
print model.doesnt_match("breakfast cereal dinner lunch".split())
print model.doesnt_match("cat dog table".split())
#vector representation of word human
print model['human']
