import os
import cv2 as cv


def process_picture():
    # TODO => get picture from request ...
    img = cv.imread(f'{os.path.basename("../data")}/test.jpeg')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return cv.equalizeHist(gray)

def draw_ROI (gray_pic, target_cascade) :
    return "ROI wip"