'''
Created on 5 Jan 2017

@author: Morris Franken

Extract deeplearning features from a given image
'''
from keras.applications.inception_v3 import InceptionV3
from sklearn.preprocessing import normalize
from tensorflow.keras.models import Model

class FeatureExtractor:
    def __init__(self):
        print("loading DeepNet (Inception-V3) ...")
        base_model = InceptionV3(weights='imagenet')
        
        # Define the model up to the second to last layer
        self.model = Model(inputs=base_model.input, outputs=base_model.layers[-2].output)
     
    def get_features(self, batch):
        features =  self.model.predict(batch)
        features = features.reshape(-1, features.shape[-1])
        return normalize(features, axis=1, norm='l2')
