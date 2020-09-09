import pickle
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
import time

# NAME="Shoot-or-Not-Classifier-64x2{}".format(int(time.time()))

X=pickle.load(open("X.pickle", 'rb'))
y=pickle.load(open("y.pickle", 'rb'))

X=X/255.0

# Best model is 0 dense layers, 32 nodes and 4 convolutional layers for 13 epochs 
# NEED to fix! Apparently too complex to run...

dense_layers=[0]
layer_sizes=[64]
conv_layers=[4]

for dense_layer in dense_layers:
    for layer_size in layer_sizes:
        for conv_layer in conv_layers:
            NAME="{}-conv-{}-nodes-{}-dense-{}".format(conv_layer,layer_size,dense_layer,int(time.time()))
            tensorboard=TensorBoard(log_dir='logs/{}'.format(NAME))
            print(NAME)

            model=Sequential()

            model.add(Conv2D(layer_size, (3,3), input_shape=X.shape[1:]))
            model.add(Activation("relu"))
            model.add(MaxPooling2D(pool_size=(2,2)))

            for l in range(conv_layer-1):
                model.add(Conv2D(layer_size, (3,3)))
                model.add(Activation("relu"))
                model.add(MaxPooling2D(pool_size=(2,2)))

            model.add(Flatten())

            for l in range(dense_layer):
                model.add(Dense(512))
                model.add(Activation('relu'))
            
            # model.add(Dense(64))
            # model.add(Activation('relu'))

            model.add(Dense(1))
            model.add(Activation('sigmoid'))

            model.compile(loss="binary_crossentropy",
                            optimizer="adam",
                            metrics=['accuracy'])

            model.fit(X,y,batch_size=18,epochs=10,validation_split=0.3,
                        callbacks=[tensorboard])
# Don't forget to change version number when training a new model!
model.save('64x4_v3.2-CNN.model')