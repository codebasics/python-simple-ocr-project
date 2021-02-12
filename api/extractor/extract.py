import cv2
from flask import current_app as app
from extractor import format2
from extractor import format3
from extractor import format4
from extractor import format1
from image_utils.image_to_string import from_image_to_string
import numpy as np

functions = {
    'format1': format1,
    'format2': format2,
    'format3': format3,
    'format4': format4
}


def clarify_text(img):
    img2 = img.copy().astype('uint8')
    disp_img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY).astype('uint8')
    # blur = cv2.GaussianBlur(disp_img, (3, 3), 0).astype('uint8')
    ret3, th3 = cv2.threshold(disp_img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU) # noqa
    disp_img = cv2.medianBlur(th3, 3)
    disp_img = cv2.resize(disp_img, None, fx=5, fy=5, interpolation=cv2.INTER_CUBIC) # noqa
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(th3, kernel, iterations=1)
    eroded = cv2.erode(dilated, kernel, iterations=1)
    dilated = cv2.dilate(eroded, kernel, iterations=1)
    eroded = cv2.erode(dilated, kernel, iterations=1)
    return eroded


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
