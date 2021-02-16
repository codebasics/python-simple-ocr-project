import cv2
from flask import current_app as app
from extractor import format1
from image_utils.image_to_string import from_image_to_string
import numpy as np

functions = {
    'format1': format1
}


def get_information(img_list, file_format):
    """
    extracts information from images
    returns dict containing information
    """
    # first pass
    for i in range(len(img_list)):
        gray = cv2.cvtColor(np.array(img_list[i]), cv2.COLOR_BGR2GRAY)
        temp = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR) # noqa
        img_list[i] = cv2.adaptiveThreshold(temp, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 61, 11) # noqa

    text = from_image_to_string(img_list)
    app.logger.info(text)
    patient = functions[file_format].extract_details(text)
    # check for missing values in patient
    # empty_values = []
    # for k, v in patient.items():
    #     if v == '':
    #         empty_values.append(k)
    # if empty_values:
    #     text_2 = from_lines_to_string(img_list)
    #     for key in empty_values:
    #         patient[key] = functions[file_format].extract_details(text_2, key) # noqa

    # returned well formated patient information
    # patient = functions[file_format].map_to_format(patient)
    return text, patient
