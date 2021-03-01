from flask import current_app as app
from utils.image_utils import get_text_from_image_list
from . import FUNCTIONS


def extract_details(page_list, file_format):
    """Extract details from a page list

    Extract details from a page list depending upon the document type.

    Parameters
    ----------
    page_list : list(np.ndarray)
        list of pages extracted from pdf
    file_format : str
        format a particular file is following

    Returns
    -------
    text: str
        text as extracted from teh set of images
    data: list(tuple)
        data stored as list of tuples
    """

    text = get_text_from_image_list(page_list)
    app.logger.info(text)
    data = FUNCTIONS[file_format].extract_details(text)
    return text, data
