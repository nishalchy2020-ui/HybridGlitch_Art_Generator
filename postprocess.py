import cv2

def enhance(img, contrast=1.2, brightness=10):

    return cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)
