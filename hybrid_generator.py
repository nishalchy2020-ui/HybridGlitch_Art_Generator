import cv2
import numpy as np

def imaginative_hybrid(img1, img2, mode="edges", alpha=0.6):
   
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    hybrid = img1.copy()

    if mode == "edges":
        gray = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        mask = edges > 0
        hybrid[mask] = img2[mask]

    elif mode == "blend":
        hybrid = cv2.addWeighted(img1, alpha, img2, 1-alpha, 0)

    elif mode == "texture":
        blur = cv2.GaussianBlur(img2, (15,15), 0)
        texture = cv2.subtract(img2, blur)
        hybrid = cv2.addWeighted(img1, alpha, texture, 1-alpha, 0)

    return hybrid.astype(np.uint8)
