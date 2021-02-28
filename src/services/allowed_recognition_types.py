# https://github.com/opencv/opencv/tree/master/data/haarcascades/<trained_models>

def check_type(type):
    allowed = ["eyes", "full-body", "frontal-face-default", "lower-body", "profile-face", "upper-body", "smile"]
    map_urls = {
        "eyes": "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_eye.xml",
        "frontal-face-default": "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
        # TODO other URLs
    }
    if type in allowed:
        return map_urls[type]
    else:
        return False
