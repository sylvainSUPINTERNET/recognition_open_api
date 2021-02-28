import requests
import os
import cv2 as cv

def dl_model(url_model):

    r = requests.get(url_model)
    file_name_to_save = url_model.split("/")[len(url_model.split("/")) - 1]

    f = open(f'{os.path.basename("../data")}/{file_name_to_save}', 'w')
    f.write(r.content.decode('utf-8'))
    f.close()

    file_saved = f'{os.path.basename("../data")}/{file_name_to_save}'
    return file_saved

def prepare_classifier(model_file):
    # Create classifier
    cascade = cv.CascadeClassifier(model_file)
    cascade.load(model_file)
    return cascade
