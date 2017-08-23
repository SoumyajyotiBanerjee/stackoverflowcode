import numpy as np
from keras.models import Sequential
from keras.models import model_from_yaml
from keras.layers import InputLayer, Dense
from keras.layers import LSTM
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.optimizers import SGD
import pickle

with open('../data/x_test_set_20k', 'rb') as f:
    x_test = pickle.load(f)
with open('../data/y_test_set_20k', 'rb') as f:
    y_test = pickle.load(f)

yaml_file = open('../data/model_set_20k.yaml', 'r')
loaded_model = yaml_file.read()
yaml_file.close()
model = model_from_yaml(loaded_model)
model.load_weights('../data/model_set_20k.h5')

sgd = SGD(lr=0.05, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='binary_crossentropy',
                      optimizer=sgd, metrics=['accuracy'])

#Predict
preds = model.predict(x_test)
preds[preds>=0.5] = 1
preds[preds<0.5] = 0
with open('../data/pred_set_20k', 'w') as f:
    pickle.dump(preds, f)
#Evaluate
loss, accuracy = model.evaluate(x_test, y_test, verbose=2)
print loss
print accuracy
#print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

