from cv2 import cv2
import numpy as np


def get_lines(img):
    """
    returns a list of numpy ndarrays containing line segments extracted from the image # noqa
    """
    lines = []

    # pre-processing image
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU) # noqa

    # finding lines
    hist = cv2.reduce(threshed, 1, cv2.REDUCE_AVG).reshape(-1)
    th = 1
    H = img.shape[0]
    uppers = [y for y in range(H-1) if hist[y] <= th and hist[y+1] > th]
    lowers = [y for y in range(H-1) if hist[y] > th and hist[y+1] <= th]

    # storing image line by line in a list
    threshed = cv2.bitwise_not(threshed)
    min_height = 40
    max_height = 100
    for s, e in zip(uppers[:-1], lowers[1:]):
        if e-s > min_height and e-s < max_height:
            temp_img = cv2.copyMakeBorder((threshed[s-5:e+5]), 50, 50, 0, 0, cv2.BORDER_CONSTANT, None, (255, 255, 255)) # noqa
            lines.append(temp_img)

    return lines
