import cv2
import numpy as np

def blend_images(img1, img2, mode="overlay", alpha=0.5):
    if mode == "overlay":
        return cv2.addWeighted(img1, alpha, img2, 1 - alpha, 0)

    elif mode == "mask":
        gray = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
        _, mask = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        mask = mask / 255.0
        return (img1 * mask[..., None] + img2 * (1 - mask[..., None])).astype(np.uint8)

    return img1
