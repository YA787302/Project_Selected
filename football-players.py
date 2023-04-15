#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
DATADIR = "D:/Univirsity/Level3/Second Term/Selected_2/selectedProject/football_golden_foot/football_golden_foot"

CATEGORIES = ['cristiano_ronaldo', 'lionel_messi',
              'mohamed_salah', 'pele', 'ronaldinho', 'zlatan_ibrahimovic']

for category in CATEGORIES:
    path = os.path.join(DATADIR, category)
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
        #plt.imshow(img_array, cmap="gray")
        #plt.show()
        break
    break


IMG_SIZE = 150
new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))


training_data = []
print("hello")

def TrainData():
    for CATEGORIES in os.listdir(DATADIR):
        id = 1
        if id == 1:
            class_name = 'cristiano_ronaldo'
        elif id == 2:
            class_name = 'lionel_messi'
        elif id == 3:
            class_name = 'mohamed_salah'
        elif id == 4:
            class_name = 'pele'
        elif id == 5:
            class_name = 'ronaldinho'
        elif id == 6:
            class_name = 'zlatan_ibrahimovic'
        for img_array in os.listdir(f"{DATADIR }/{CATEGORIES}"):
            path = os.path.join(f"{DATADIR }/{CATEGORIES}/{img_array}")
            image = cv2.imread(os.path.join(path))


            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            resized_image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))

            training_data.append([resized_image, class_name])
        id += 1    


# In[2]:


TrainData()


# In[5]:


training_data.shape


# In[6]:


np_training =np.array(training_data,dtype=object)


# In[7]:


np_training.shape


# In[ ]:




