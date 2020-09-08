import numpy as np
import matplotlib.pyplot as plt
import os
import random
import pickle
import cv2

class data_tools:
    def create_training_data(self, DATADIR='images', 
    CATEGORIES=['negative/30_n', 'positive/All_Positives']):
        training_data=[]
        for category in CATEGORIES:
            path=DATADIR+'/'+category # paths to respective images classes
            class_num=CATEGORIES.index(category)
            for img in os.listdir(path):
                # training_data.append([img])
                img_array=cv2.imread(os.path.join(path,img))
                new_img=cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
                training_data.append([new_img,class_num])
            # Just to show that images can be read   
            #     plt.imshow(new_img)
            #     plt.show()
            #     break
            # break
        return training_data

    def prepare_data(self):
        training_dataset=data_tools().create_training_data()
        # print(len(training_dataset))

        # Shuffling Data
        random.shuffle(training_dataset)

        X=[]
        y=[]

        for features,label in training_dataset:
            X.append(features)
            y.append(label)

        X = np.array(X).reshape(-1,104,169,3)
        y = np.array(y)

        pickle_out = open("X.pickle", 'wb')
        pickle.dump(X, pickle_out)
        pickle_out.close()

        pickle_out = open("y.pickle", 'wb')
        pickle.dump(y, pickle_out)
        pickle_out.close()

        return print('Done!')

data_tools().prepare_data()
