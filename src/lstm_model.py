import numpy as np
from keras.models import Sequential
from keras.layers import InputLayer, Dense
from keras.layers import LSTM
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.optimizers import SGD
from gensim.models import doc2vec
import pickle

#Load Data
d2v_model = doc2vec.Doc2Vec.load('../data/d2v_set_20k')
x_train = np.array([e for e in d2v_model.docvecs], dtype='float')
with open('../data/tag_vec_set_20k', 'rb') as fp:
    y_train = pickle.load(fp)
#TODO random shuffle the data set and do cross validation
x_test = x_train[5500:5700]
y_test = y_train[5500:5700]
x_train = x_train.reshape(x_train.shape[0], 1, x_train.shape[1])
x_test = x_test.reshape(x_test.shape[0], 1, x_test.shape[1])

#Build model
model = Sequential()
model.add(InputLayer(input_shape=(x_train.shape[1], x_train.shape[2])))
model.add(LSTM(2000,dropout=0.1))
model.add(Dense(y_train.shape[1],activation='sigmoid'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='binary_crossentropy',
                      optimizer=sgd)

#Train model
model.fit(x_train, y_train, epochs=100, batch_size=2000)

#Predict
preds = model.predict(x_test)
preds[preds>=0.5] = 1
preds[preds<0.5] = 0

#Evaluate
score = model.evaluate(x_test, y_test)
Acc = score[1]
print '======================================\nAccuracy: %s'%Acc
