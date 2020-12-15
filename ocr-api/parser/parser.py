import os
import sys
import pytesseract
from extractor.format1 import extract_details_format1
from extractor.format2 import extract_details_format2
from extractor.format3 import extract_details_format3
from extractor.format4 import extract_details_format4
from pdf2image import convert_from_path
ROOT_DIR = os.path.dirname(__file__)
PARENT_DIR = os.path.dirname(__file__) + '/' + str(os.pardir)
sys.path.append(PARENT_DIR)

functions = {
    'format1': extract_details_format1,
    'format2': extract_details_format2,
    'format3': extract_details_format3,
    'format4': extract_details_format4
    
}


def parse(file_name, file_format):
    text = get_text(file_name)
    try:
        patient = functions[file_format](text)
    except Exception as e: 
        patient = str(e)
    return text, patient


def get_text(pdf_path):
    pages = convert_from_path(pdf_path, 500)
    text_list = []
    image_counter = 1
    for page in pages:
        text = str(((pytesseract.image_to_string(page))))
        text = text.replace('-\n', '')
        text_list.append(text)
        image_counter = image_counter + 1
    text = "\n".join(text_list)
    return text
