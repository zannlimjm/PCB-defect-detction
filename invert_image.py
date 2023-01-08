import sys
import math
import cv2 as cv
import numpy as np

def main(argv):
    img = cv.imread('/Users/zannlim/Desktop/PCB_CV/defect_smd.png')
    imagem = cv.flip(img, 0)
    imagem = cv.flip(imagem, 1)
    # dst = cv.Canny(img, 50, 200, None, 3)
    # dst = cv.Canny(img,10,100)

    cv.imshow("Original", img)
    cv.imshow("inverted",imagem)
    cv.waitKey()
    return 0

if __name__ == "__main__":
    main(sys.argv[1:])