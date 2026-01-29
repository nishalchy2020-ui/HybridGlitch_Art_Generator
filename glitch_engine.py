import cv2
import numpy as np

def rgb_shift(img, shift=15):
    r, g, b = cv2.split(img)
    r = np.roll(r, shift, axis=1)
    g = np.roll(g, -shift//2, axis=0)
    b = np.roll(b, shift//3, axis=1)
    return cv2.merge([r, g, b])

def add_noise(img, intensity=0.1):
    noise = np.random.randn(*img.shape) * 255 * intensity
    noisy = img.astype(np.float32) + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)

def pixel_sort(img, strength=30):
    out = img.copy()
    h, w, _ = img.shape
    for y in range(0, h, strength):
        row = out[y]
        brightness = row.sum(axis=1)
        out[y] = row[np.argsort(brightness)]
    return out
