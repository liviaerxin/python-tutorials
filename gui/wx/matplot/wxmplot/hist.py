import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


"""Original Image"""
#image read function
img=mpimg.imread('1.jpg')
# x co-ordinate denotation. 
plt.xlabel("Value")
# y co-ordinate denotation.
plt.ylabel("pixels Frequency")
# title of an image .
plt.title("Original Image")
# imshow function with comperision of gray level value.
plt.imshow(img)
#plot the image on a plane.
plt.show()

lum_img = img[:, :, 0]


"""Histogram of Image"""
plt.title("HIstogramm for given Image'  ")
plt.xlabel("Value")
plt.ylabel("pixels Frequency")
# #hist function is used to plot the histogram of an image.
# plt.hist(x)
#plt.hist()
plt.hist(lum_img.ravel(), bins=256)
plt.show()