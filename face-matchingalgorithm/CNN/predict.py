import os
import cv2
from PIL import Image
import numpy as np

import tensorflow as tf

imag=cv2.imread(os.getcwd() +'/CNN/data/Chala_Golicha/20240303_170440.jpg')
img_from_ar = Image.fromarray(imag, 'RGB')
resized_image = img_from_ar.resize((50, 50))

test_image =np.expand_dims(resized_image, axis=0) 

# load model
model = tf.keras.models.load_model(os.getcwd() + '/my_model.keras')

result = model.predict(test_image) 
print(result) 
print("Result is: ", result[0][0])
print("Prediction: " + str(np.argmax(result)))
