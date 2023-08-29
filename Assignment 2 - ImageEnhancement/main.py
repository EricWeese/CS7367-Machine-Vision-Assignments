from PIL import Image
import numpy as np
import math
import cv2
import matplotlib.pyplot as plt

img = Image.open("./Images/fourierspectrum.pgm")
# img.show()
img = np.asarray(img)

banker = Image.open("./Images/banker.jpeg")
banker = np.asarray(banker)

def logTransform(img, c):
    logImage = [[0 for x in range(len(img[0]))] for x in range(len(img))]
    i, j = 0, 0
    while i < len(img):
        while j < len(img[0]):
            logImage[i][j] = c * np.log(img[i][j]+1)
            j += 1
        j = 0
        i += 1
    logImage = Image.fromarray(np.array(logImage, dtype=np.uint8))
    logImage.save(f"./Images/LogTransform.png")
    logImage.show()

def powerTransform(img, c, y):
    powerImage = [[0 for x in range(len(img[0]))] for x in range(len(img))]
    i, j = 0, 0
    while i < len(img):
        while j < len(img[0]):
            powerImage[i][j] = c * np.power(img[i][j], y)
            j += 1
        j = 0
        i += 1
    powerImage = Image.fromarray(np.array(powerImage, dtype=np.uint32))
    powerImage.save(f"./Images/{y}PowerTransform.png")
    powerImage.show()

def histogramGrayscale(img):
    imgRaw = Image.fromarray(img, mode="L")
    imgRaw.show()
    # Histogram of each occurance of the 255 values
    hist = np.bincount(img.flatten(), minlength=256)
    plt.plot(hist, label="Original Image")

    # Generates a list with each pixel value (0-255). Used to calculate mean and std.
    histInv = []
    for i in range(len(hist)):
        histInv.extend([i] * hist[i])
    print("Original Image: ")
    print(f'Mean: {np.mean(histInv)}')
    print(f'Standard Deviation: {np.std(histInv)}')
    # Percentage of each value
    hist = hist / np.sum(hist)

    # Cumulative percentage of each value
    cumHist = np.cumsum(hist)

    # New transofrm contrast map
    transformMap = np.floor(255 * cumHist).astype(np.uint8)
    
    # New contrast list where each value is derived from the transformMap
    constrastImg = [transformMap[x] for x in list(img.flatten())]

    # Histogram for new contrast image
    contrastHist = np.bincount(constrastImg, minlength=256)
    plt.plot(contrastHist, label="Contrast Image")
    
    # Generates a list with each new pixel value (0-255). Used to calculate mean and std.
    contrastHistInv = []
    for i in range(len(contrastHist)):
        contrastHistInv.extend([i] * contrastHist[i])
    print("Contrast Image: ")
    print(f'Mean: {np.mean(contrastHistInv)}')
    print(f'Standard Deviation: {np.std(contrastHistInv)}')

    # Reshaping contrast array to be 2D
    constrastImg = np.reshape(np.asarray(constrastImg), img.shape)
    constrastImg = Image.fromarray(constrastImg, mode="L")
    constrastImg.show()
    plt.legend()
    plt.show()



c = 255 / np.log(1 + np.max(img))

# Transform
# logTransform(img, c)
# powerTransform(img, c, 0.05)
# powerTransform(img, c, 0.2)
# powerTransform(img, c, 0.8)
# powerTransform(img, c, 1)
# powerTransform(img, c, 5)
# powerTransform(img, c, 25)

# Histogram (Grayscale)
histogramGrayscale(banker)
