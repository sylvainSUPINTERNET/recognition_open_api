import cv2 as cv


from services.allowed_recognition_types import check_type
from services.download_model import dl_model, prepare_classifier
from services.picture import process_picture, draw_ROI


def process( type ):
    analysis(type)

def analysis(recognition_type):
    test_resp = check_type(recognition_type)

    if test_resp != False :
        # Downloads model
        url_to_download = test_resp
        xml_model_file = dl_model(url_model=url_to_download)

        # Init classifier for target model
        target_cascade = prepare_classifier(xml_model_file)

        # Process picture
        gray_pic, img = process_picture() # TODO => add parameter to accept body request picture
        draw_ROI(gray_pic, target_cascade, img)


        # TODO : WIP
        return True
    else :
        return False

