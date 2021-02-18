import os
import sys
import logging
from pdf2image import convert_from_path
from extractor.extract import get_information

ROOT_DIR = os.path.dirname(__file__)
PARENT_DIR = os.path.dirname(__file__) + '/' + str(os.pardir)
sys.path.append(PARENT_DIR)
logging.basicConfig(level=logging.DEBUG)


def parse(file_name, file_format):
    """
    coverts pdf to a list of image
    returns text and a dict containing information
    """
    pages = convert_from_path(file_name, 500)

    text = ""
    # app.logger.info("sfd");
    error = None
    try:
        # app.logger.info("------")
        text, patient = get_information(pages, file_format)
    except Exception as e:
        patient = None
        error = e
    return text, patient, error
