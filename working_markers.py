from cgitb import grey
import sys
import cv2 as cv
import numpy as np
def main(argv):
    
    default_file = ('/Users/zannlim/Desktop/PCB_CV/IR_actual.jpg')
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
    src = cv.flip(src, 0)
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1
    
    
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    
    
    gray = cv.medianBlur(gray, 5)
    
    # cv.imshow("gray", gray)
    # cv.waitKey(0)

    rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 64,
                               param1=100, param2=30,
                               minRadius=20, maxRadius=50)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            # cv.circle(src, center, 1, (0, 100, 100), 3)
            print(center)
            # circle outline
            radius = i[2]
            # cv.circle(src, center, radius, (0, 255, 0), 3)
    cv.circle(src, (694, 290), radius, (0, 255, 0), 3)
    
    cv.imshow("detected circles", src)
    cv.waitKey(0)
    
    return 0
if __name__ == "__main__":
    main(sys.argv[1:])