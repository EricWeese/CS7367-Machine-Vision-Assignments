from PIL import Image
import numpy as np
import math
import cv2
import matplotlib.pyplot as plt

morphology = Image.open("./Images/morphology.png").convert('L')
# morphology.show()
morphology = np.asarray(morphology)

fingerPrint = Image.open("./Images/fingerprint_BW.png").convert('L')
fingerPrint.show()
fingerPrint = np.asarray(fingerPrint)


def dilation(img):
    newImage = [[0 for x in range(len(img[0]))] for x in range(len(img))]
    i, j = 1, 1
    while i < len(img)-1:
        while j < len(img[0])-1:
            if img[i][j] != 0:
                  newImage[i][j] = 255
                  newImage[i-1][j] = 255
                  newImage[i+1][j] = 255
                  newImage[i][j-1] = 255
                  newImage[i][j+1] = 255

            j += 1
        j = 0
        i += 1
    newImage = Image.fromarray(np.array(newImage, dtype=np.uint8))
    newImage.show()
    newImage = np.asarray(newImage)
    return newImage

def erosion(img):
    newImage = [[0 for x in range(len(img[0]))] for x in range(len(img))]
    i, j = 1, 1
    while i < len(img)-1:
        while j < len(img[0])-1:
            if 255 == img[i][j] and 255 == img[i+1][j] and 255 == img[i-1][j] and 255 == img[i][j+1] and 255 == img[i][j-1]:
                  newImage[i][j] = 255

            j += 1
        j = 0
        i += 1
    newImage = Image.fromarray(np.array(newImage, dtype=np.uint8))
    newImage.show()
    newImage = np.asarray(newImage)
    return newImage

def medianFilter(img):
    newImage = [[0 for x in range(len(img[0]))] for x in range(len(img))]
    i, j = 1, 1
    while i < len(img)-1:
        while j < len(img[0])-1:
            neighbors = [img[i][j], img[i+1][j], img[i-1][j], img[i][j+1], img[i][j-1]]
            neighbors.sort()
            newImage[i][j] = neighbors[2]
            j += 1
        j = 0
        i += 1
    newImage = Image.fromarray(np.array(newImage, dtype=np.uint8))
    newImage.show()
    newImage = np.asarray(newImage)
    return newImage


# dilation(dilation(morphology))
# erosion(erosion(morphology))

dilation(fingerPrint)
erosion(fingerPrint)
medianFilter(medianFilter(fingerPrint))
