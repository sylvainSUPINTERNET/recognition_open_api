import os
import cv2 as cv


def process_picture():
    # TODO => get picture from request ...
    img = cv.imread(f'{os.path.basename("../data")}/test.jpeg')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return cv.equalizeHist(gray), img

def draw_ROI (gray_pic, target_cascade, pic) :
    detected = target_cascade.detectMultiScale(gray_pic)

    for (x,y,w,h) in detected:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(pic, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = gray_pic[y:y+h,x:x+w]

    cv.imwrite(f'{os.path.basename("../data")}/test_with_draw.jpeg', pic)
    cv.imshow('Capture - Face detection', pic)

    return "ROI wip"