import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from gensim.models import doc2vec

#Load Data
d2v_model = doc2vec.Doc2Vec.load('doc2train')

input_length = len(d2v_model.docvecs)

model = Sequential()
model.add(InputLayer(input_shape=100))
model.add(LSTM(100,dropout=0.1,recurrent_dropout=0.2))
model.add(Dense(15,activation='sigmoid'))


