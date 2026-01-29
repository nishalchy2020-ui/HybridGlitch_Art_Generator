import numpy as np
import cv2
import random


def rgb_shift(img, shift=10):
r, g, b = cv2.split(img)
r = np.roll(r, shift, axis=1)
b = np.roll(b, -shift, axis=0)
return cv2.merge([r, g, b])


def add_noise(img, intensity=0.05):
noise = np.random.randn(*img.shape) * 255 * intensity
noisy = img + noise
return np.clip(noisy, 0, 255).astype(np.uint8)


def pixel_sort(img, strength=50):
out = img.copy()
h, w, _ = img.shape
for y in range(0, h, strength):
row = out[y]
row = row[np.argsort(row.sum(axis=1))]
out[y] = row
return out