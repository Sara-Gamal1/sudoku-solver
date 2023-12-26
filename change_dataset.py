

from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier  # MLP is an NN
import numpy as np
import pickle 
import argparse
import cv2
import os
import random
from skimage.feature import hog
from sklearn import svm
from sklearn import cluster
import matplotlib.pyplot as plt
path_to_dataset = r'testset'
img_filenames = os.listdir(path_to_dataset)
def show_images(images,titles=None):
    n_ims = len(images)
    if titles is None: titles = ['(%d)' % i for i in range(1,n_ims + 1)]
    fig = plt.figure()
    n = 1
    for image,title in zip(images,titles):
        a = fig.add_subplot(1,n_ims,n)
        if image.ndim == 2: 
            plt.gray()
        plt.imshow(image)
        a.set_title(title)
        n += 1
    fig.set_size_inches(np.array(fig.get_size_inches()) * n_ims)
    plt.show()
for i, fn in enumerate(img_filenames):
        if fn.split('.')[-1] != 'jpg':
            continue

        label = fn.split('.')[0]
        path = os.path.join(path_to_dataset, fn)
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        img1=np.where(img>150,0,255)
        cv2.imwrite('./test2/'+fn,img1)


        
     
   