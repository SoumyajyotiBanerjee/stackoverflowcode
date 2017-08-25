import numpy as np
from keras.models import Sequential
from keras.models import model_from_yaml
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
#with open('/home/deeplearning/stackoverflow/part2/tag_reco_data/data/tag_vec_set_1k', 'rb') as fp:
#    y_train = pickle.load(fp)
fp = open('../data/tag_vec_set_20k', 'rb')
y_train = pickle.load(fp)
#TODO random shuffle the data set and do cross validation
x_test = x_train[5500:5700]
y_test = y_train[5500:5700]
x_train = x_train.reshape(x_train.shape[0], 1, x_train.shape[1])
x_test = x_test.reshape(x_test.shape[0], 1, x_test.shape[1])

#Build model
model = Sequential()
model.add(InputLayer(input_shape=(x_train.shape[1], x_train.shape[2])))
model.add(LSTM(2000,dropout=0.1),activation='relu')
model.add(LSTM(2000,dropout=0.1),activation='relu')
model.add(Dense(y_train.shape[1],activation='hard_sigmoid'))

sgd = SGD(lr=0.05, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='binary_crossentropy',
                      optimizer=sgd, metrics=[metrics.mae, metrics.categorical_accuracy])

#Train model
model.fit(x_train, y_train, epochs=10, batch_size=2000)

#Save serialized model
model_yaml = model.to_yaml()
with open('/home/deeplearning/stackoverflow/part2/tag_reco_data/data/model_set_20k.yaml', 'w') as mfp:
    mfp.write(model_yaml)
model.save_weights('/home/deeplearning/stackoverflow/part2/tag_reco_data/data/new_model_set_20k.h5')

with open('/home/deeplearning/stackoverflow/part2/tag_reco_data/data/x_test_set_20k', 'w') as f:
    pickle.dump(x_test, f)
with open('/home/deeplearning/stackoverflow/part2/tag_reco_data/data/y_test_set_20k', 'w') as f:
    pickle.dump(y_test, f)

