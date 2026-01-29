from PIL import Image
import numpy as np

def load_and_prepare(file, size=(512, 512)):
    
    img = Image.open(file).convert("RGB")
    img = img.resize(size)
    return np.array(img)
