import numpy
import cv2
import sys


if(len(sys.argv) != 2):
    print("usage: python3 pic-to-asci.py <pic>")
    exit(1)
img = cv2.imread(sys.argv[1])

result = ""
size = (300,300)
avg =numpy.ndarray(size + tuple([3]))
stride = (img.shape[0]//size[0], img.shape[1]//size[1])

# what algorithm should I use?

asciGradient = [".","~","*","!","?","(","+","#","@"]
asciGradient.reverse()

## striding avg
for y in range(size[0]):
    for x in range(size[1]):
        minY = y*stride[0] 
        maxY = (y+1)*stride[0]

        minX = x*stride[1]
        maxX = (x+1)*stride[1]

        toAvg =img[minY:maxY, minX:maxX]

        avgPixel = numpy.average(toAvg, (0,1,2))
        avg[y,x] = avgPixel
        result += asciGradient[int(avgPixel//(255/len(asciGradient)))]
        result += asciGradient[int(avgPixel//(255/len(asciGradient)))]
    result += "\n"


cv2.imwrite(sys.argv[1]+".avg.jpg", avg)
with open("output.txt", "w") as f:
    f.write(result)
