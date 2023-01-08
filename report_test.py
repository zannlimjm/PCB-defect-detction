import sys
import math
import cv2 as cv
import numpy as np

def main(argv):
    # img = cv.imread('/Users/zannlim/Desktop/PCB_CV/scratch_polarized.png', cv.IMREAD_GRAYSCALE)
    img = cv.imread('/Users/zannlim/Desktop/PCB_CV/w_wire.jpg')
    # img= cv.flip(img, 0)
    # gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # ret, thresh = cv.threshold(gray, 110, 255, 0)
    blurred = cv.GaussianBlur(img, (11, 11), 0)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # dst = cv.Canny(img, 50, 200, None, 3)
    dst = cv.Canny(blurred,30,150)

    linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 15, 16)
    lines11 = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 15, 11)
    cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
    cdstP = np.copy(cdst)
    
    # # lines = cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)
    
    # # if lines is not None:
    # #     for i in range(0, len(lines)):
    # #         rho = lines[i][0][0]
    # #         theta = lines[i][0][1]
    # #         a = math.cos(theta)
    # #         b = math.sin(theta)
    # #         x0 = a * rho
    # #         y0 = b * rho
    # #         pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
    # #         pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
    # #         cv.line(cdst, pt1, pt2, (0,0,255), 3, cv.LINE_AA)
    # if linesP is not None:
    #     for i in range(0, len(linesP)):
    #         l = linesP[i][0] #x1,y1,x2,y2
    #         l2 = lines11[i][0]
    #         check = check_dist(l[0], l[1],l[2], l[3], l2[0], l2[1],l2[2], l2[3])
    #         # if check != None:
    #         #     cv.circle(cdstP, (l[2],l[3]),10,(0,255,0),2)
    #         #     print(l[2], l[3])
    #         # cv.line(cdstP, (l2[0], l2[1]), (l2[2], l2[3]), (0,255,0), 2, cv.LINE_AA)
    #         cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)
    # cv.circle(cdstP, (786,259),15,(0,255,0),2)

    
    # cv.imshow("Source", img)
    # cv.imshow("Canny", dst)
    # cv.imshow("threshold",thresh)
    # cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)
    # cv.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)
    cv.imshow("B&W", gray)
    cv.waitKey()
    return 0
# def check_gap(x1,x2,y1,y2):
#     threshold = 1000
#     if abs(x1-x2) > threshold or abs(y1-y2) > threshold:
#         return [(x2-x1),(y2-y1)]

def check_dist(x1,y1,x2,y2,x3,y3,x4,y4):
    threshold = 60
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 )
    dist2 = math.sqrt((x4 - x3)**2 + (y4 - y3)**2 )
    if abs(dist2 - dist) > threshold:
        return [(x3-x1),(y3-y1)]

if __name__ == "__main__":
    main(sys.argv[1:])