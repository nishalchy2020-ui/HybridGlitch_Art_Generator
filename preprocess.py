from PIL import Image
import numpy as np


def load_and_prepare(img_path, size=(512, 512)):
img = Image.open(img_path).convert("RGB")
img = img.resize(size)
return np.array(img)