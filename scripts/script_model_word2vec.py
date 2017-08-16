



from gensim.models.word2vec import LineSentence
from gensim.models import Word2Vec
import pickle

sentences = LineSentence('text8')
model = Word2Vec(sentences, size=100, window=5, min_count=5, workers=4)
fname = open('save_model','w')
op = open('store_model','wb')
pickle.dump(model,op)
model2 = pickle.load(open('store_model','rb'))
