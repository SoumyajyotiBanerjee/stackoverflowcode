from gensim.models.word2vec import LineSentence
from gensim.models import Word2Vec
import pickle

sentences = LineSentence('p_out.txt')
model = Word2Vec(sentences, size=100, window=5, min_count=5, workers=4)
model.save('au_model')
