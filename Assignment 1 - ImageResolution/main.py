from PIL import Image
import numpy as np
import math

img = Image.open("./Images/rose.jpg")
originalImage = img.load()
# img.show()

def upSizeImage(size, image):
    upSizeFactor = 1024 / size
    newImage = [[0 for x in range(1024)] for x in range(1024)]
    i, j = 0, 0
    while i < 1024:
        while j < 1024:
            newImage[i][j] = image[int(i/upSizeFactor)][int(j/upSizeFactor)]
            j += 1
        j = 0
        i += 1
    imageArray = np.array(newImage, dtype=np.uint8)
    resultImage = Image.fromarray(np.array(imageArray), mode="L")
    resultImage.save(f"./Images/{size}x{size}Upsized.png")
    resultImage.show()
    print(f"Upsized image: {resultImage.size}")

def downSizeImage(size, image):
    downsizeFactor = 1024 / size
    newImage = [[0 for x in range(size)] for x in range(size)]
    i, j = 0, 0
    while i < size:
        while j < size:
            newImage[i][j] = image[j*downsizeFactor,i*downsizeFactor]
            j += 1
        j = 0
        i += 1
    imageArray = np.array(newImage, dtype=np.uint8)
    resultImage = Image.fromarray(np.array(imageArray), mode="L")
    resultImage.save(f"./Images/{size}x{size}.png")
    resultImage.show()
    print(f"Downsized image: {resultImage.size}")
    upSizeImage(size, newImage)

def changeGrayScale(level, image):
    size = 1024
    grayScaleFactor = 256 / (level)
    grayValues = set()
    newImage = [[0 for x in range(size)] for x in range(size)]
    i, j = 0, 0
    while i < size:
        while j < size:
            if image[j,i]/grayScaleFactor <= 1:
                newImage[i][j] = 0
            else:
                newImage[i][j] = int(math.ceil(image[j,i]/grayScaleFactor)*grayScaleFactor-1)
            grayValues.add(newImage[i][j])
            j += 1
        j = 0
        i += 1
    imageArray = np.array(newImage, dtype=np.uint8)
    resultImage = Image.fromarray(np.array(imageArray), mode="L")
    resultImage.load()
    resultImage.show()
    resultImage.save(f"./Images/{level}Grayscale.png")
    print(f"Grayscale image: {level}")
    print(f'Gray values: {grayValues}')
    print(f'Number of unique gray values: {len(grayValues)}')
    
#Downsizing and then Upsizing
# downSizeImage(512, originalImage)
# downSizeImage(256, originalImage)
# downSizeImage(128, originalImage)
# downSizeImage(64, originalImage)
# downSizeImage(32, originalImage)

# Grayscale Images
changeGrayScale(128, originalImage)
changeGrayScale(64, originalImage)
changeGrayScale(32, originalImage)
changeGrayScale(16, originalImage)
changeGrayScale(8, originalImage)
changeGrayScale(4, originalImage)
changeGrayScale(2, originalImage)

