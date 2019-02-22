#importing the required libraries
from __future__ import print_function
import argparse
import cv2

#Finding the path of the image
obj = argparse.ArgumentParser()
obj.add_argument("-i", "--image", required = True, help = "Path to the image" )
args = vars(obj.parse_args())

#Loading the image from the specified path

image = cv2.imread(args["image"])
print("width: {} pixels".format(image.shape[1]))
print("height {} pixels".format(image.shape[0]))
print("channels {} pixels".format(image.shape[2]))

#displaying the image

cv2.imshow("Image", image)
cv2.waitKey(0)



