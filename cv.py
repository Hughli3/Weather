import tensorflow as tf
import numpy
import scipy
import cv2
import numpy as np
import os
os.chdir("C:/Users/hughli/OneDrive/河南气象局项目/数据")
os.chdir("/Users/hughli/Documents/学习/共享/OneDrive/henan/data")

tf.__version__
hello = tf.constant('Hello,TensorFlow')
sess = tf.Session()
print(sess.run(hello))

img = cv2.imread('image-00047.jpeg')

img1 = cv2.imread('dog.jpeg')

cv2.imshow('image',img)
cv2.waitKey()
cv2.destoryAllWidows()
img.read()

img[0,0] = [255,255,255]
c = img[0:3,0:3]
print(c)

imshow(c)
