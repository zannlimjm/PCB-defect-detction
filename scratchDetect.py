## Detecting scratches on PCB board##

import sys
import math
import cv2 as cv
import numpy as np

def main(argv):
    img = cv.imread('/Users/zannlim/Desktop/PCB_CV/scratch_polarized.png', cv.IMREAD_GRAYSCALE)
    kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
    # image_sharp = cv.filter2D(src=img, ddepth=-1, kernel=kernel)
    # img = cv.resize(img,dsize=None,fx=1,fy=1,interpolation=cv.INTER_CUBIC)
    # dst = cv.Canny(img, 50, 200, None, 3)
    dst = cv.Canny(img,40,80)
    linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 10, 50)
    cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
    cdstP = np.copy(cdst)
    
    # lines = cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)
    
    # if lines is not None:
    #     for i in range(0, len(lines)):
    #         rho = lines[i][0][0]
    #         theta = lines[i][0][1]
    #         a = math.cos(theta)
    #         b = math.sin(theta)
    #         x0 = a * rho
    #         y0 = b * rho
    #         pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
    #         pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
    #         cv.line(cdst, pt1, pt2, (0,0,255), 3, cv.LINE_AA)

    # if linesP is not None:
    #     for i in range(0, len(linesP)):
    #         l = linesP[i][0]
    #         cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)
    cv.imshow("Source", img)
    cv.imshow("Canny", dst)
    cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)
    # cv.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)
    cv.waitKey()
    return 0

if __name__ == "__main__":
    main(sys.argv[1:])