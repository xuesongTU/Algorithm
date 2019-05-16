"""
Efficient median filtering algorithm.
[Huang et al., 1979; Pitas and Venetsanopoulos, 1990]

coding by Xuesong TU, 2019/05/14
"""


import cv2

def median_filtering(img):
    m, n = img.size()
    t = int(m * n / 2)


if __name__ == "__main__":
    path = ""
    img = cv2.imread(path)
    median_filtering(img)