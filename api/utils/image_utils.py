import pytesseract
import cv2
import numpy as np

config_str = (
            r'-c tessedit_char_whitelist=" 0123456789'
            r'abcdefghijklmnopqrstuvwxyz'
            r'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            r':.,/|()-" '
            r'-c preserve_interword_spaces=1 '
            )


def get_text_from_image_list(img_list):
    """[summary]

    [extended_summary]

    Parameters
    ----------
    img_list : list(np.ndarray)
        list of images to extract text from, supposed to be different pages of
        the same document in an order.

    Returns
    -------
    str
        text extracted and combined from all the images.
    """

    text_list = [get_text_from_image(img) for img in img_list]
    text = "\n".join(text_list)
    return text


def get_text_from_image(img):
    """extract text from an image

    Use tesseract to get text from an image

    Parameters
    ----------
    img : np.ndarray
        image to get text from.

    Returns
    -------
    str
        text extracted from the img.
    """

    processed_img = preprocess_image(img)
    text = str(pytesseract.image_to_string(processed_img, lang='eng'))
    text = text.replace('-\n', '')
    return text


def preprocess_image(img):
    """preprocess image to make it suitable for reading text

    Applies various morphological operations to the image to get better text

    Parameters
    ----------
    img : np.ndarray
        image to processed

    Returns
    -------
    np.ndarray
        preprocessed img
    """

    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR) # noqa
    processed_img = cv2.adaptiveThreshold(resized, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 61, 11) # noqa
    return processed_img
