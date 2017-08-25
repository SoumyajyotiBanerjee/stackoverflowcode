import numpy as np
from keras.models import Sequential
from keras.models import model_from_yaml
from keras.layers import InputLayer, Dense
from keras.layers import LSTM
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.optimizers import SGD
from gensim.models import doc2vec
from sklearn.model_selection import KFold
import pickle

#Seed
seed=7
np.random.seed(seed)

#Load Data
d2v_model = doc2vec.Doc2Vec.load('../data/d2v_set_20k')
X = np.array([e for e in d2v_model.docvecs], dtype='float')
with open('../../Projects/tag_reco_data/data/tag_vec_set_20k', 'rb') as fp:
    Y = pickle.load(fp)
#TODO random shuffle the data set and do cross validation
#x_test = X[5500:5700]
#y_test = Y[5500:5700]
#x_train = x_train.reshape(x_train.shape[0], 1, x_train.shape[1])
#x_test = x_test.reshape(x_test.shape[0], 1, x_test.shape[1])
kfold = KFold(n_splits=5, shuffle=True, random_state=seed)
cv_scr = []

for train, test in kfold.split(X, Y):
    X_train = X[train].reshape(X[train].shape[0], 1, X[train].shape[1])
    X_test = X[test].reshape(X[test].shape[0], 1, X[test].shape[1])
    #Build model
    model = Sequential()
    model.add(InputLayer(input_shape=(X_train.shape[1], X_train.shape[2])))
    model.add(LSTM(2000,dropout=0.1))
    model.add(Dense(Y[train].shape[1],activation='sigmoid'))

    sgd = SGD(lr=0.05, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='binary_crossentropy',
                  optimizer=sgd, metrics=['accuracy'])

    #Train model
    model.fit(X_train, Y[train], epochs=5, batch_size=1000)

    #Evaluate model
    score = model.evaluate(X_test, Y[test], verbose=0)
    print "Acc: %.2f%%"%(score[1]*100)
    cv_scr.append(score[1]*100)

print "Mean Acc: %s, Std Dev: %s"%(np.mean(cv_scr), np.std(cv_scr))

#Save serialized model
'''
model_yaml = model.to_yaml()
with open('../data/model_set_20k.yaml', 'w') as mfp:
    mfp.write(model_yaml)
model.save_weights('../data/model_set_20k.h5')

with open('../data/x_test_set_20k', 'w') as f:
    pickle.dump(x_test, f)
with open('../data/y_test_set_20k', 'w') as f:
    pickle.dump(y_test, f)
'''
