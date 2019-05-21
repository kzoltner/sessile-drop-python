import numpy as np
import cv2


class EdgeDetection:
    def __init__(self):
        pass

    def sobel_canny(
        self,
        grey_image,
        top_threshold,
        bottom_threshold
    ):
        grey_values = list(grey_image.getdata())
        grey_values = np.uint8(grey_values).reshape(
            (grey_image.size[1], grey_image.size[0])
        )

        result = cv2.Canny(
            grey_values, top_threshold, bottom_threshold
        )

        return np.uint8(result)

    def bw_threshold_linear(
        self,
        grey_image,
        threshold
    ):
        bw_image = grey_image.point(
            lambda x: 0 if x < threshold else 255, "1"
        )
        bw_values = list(bw_image.getdata())
        bw_values = np.uint8(bw_values).reshape(
            (grey_image.size[1], grey_image.size[0])
        )

        return bw_values
