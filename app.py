import streamlit as st
from preprocess import load_and_prepare
from hybrid_generator import imaginative_hybrid
from glitch_engine import rgb_shift, add_noise, pixel_sort
from postprocess import enhance
from ai_generator import ai_guided_glitch
from PIL import Image
import os
import random
import numpy as np
import glob

st.set_page_config(page_title="HybridGlitch Art Generator", layout="centered")
st.title("🎨 HybridGlitch Art Generator")

# Ensure output folder exists
os.makedirs("outputs", exist_ok=True)


# Dataset selection

dataset_choice = st.selectbox(
    "Choose from mini dataset or upload your own",
    ["Animals", "Textures", "Landscapes", "Upload Your Own"]
)

def pick_random_image(category):
    files = glob.glob(f"dataset/{category.lower()}/*.*")
    if files:
        return random.choice(files)
    return None

img1_file = None
img2_file = None

if dataset_choice != "Upload Your Own":
    img1_file = pick_random_image(dataset_choice)
    img2_file = pick_random_image(dataset_choice)
else:
    img1_file = st.file_uploader("Upload Image 1", type=["png","jpg","jpeg"])
    img2_file = st.file_uploader("Upload Image 2", type=["png","jpg","jpeg"])


# Style and parameters

style = st.selectbox(
    "Choose Style",
    ["surreal", "glitchy", "soft", "chaotic", "organic", "neon"]
)

shift = st.slider("RGB Shift", 0, 30, 15)
noise = st.slider("Noise Intensity", 0.0, 0.3, 0.1)

use_ai = st.checkbox("Use AI (CLIP-guided generation)")
ai_prompt = st.text_input("AI Style Prompt", "glitchy surreal neon digital art")


# Generate hybrid
if img1_file is not None and img2_file is not None:
    img1 = load_and_prepare(img1_file)
    img2 = load_and_prepare(img2_file)

    hybrid = imaginative_hybrid(img1, img2, mode="edges")

    # Apply style (manual)
    if not use_ai:
        from glitch_engine import rgb_shift, add_noise, pixel_sort
        if style == "surreal":
            hybrid = rgb_shift(hybrid, shift)
            hybrid = add_noise(hybrid, noise)
        elif style == "glitchy":
            hybrid = pixel_sort(hybrid, 30)
            hybrid = add_noise(hybrid, noise)
        elif style == "soft":
            import cv2
            hybrid = cv2.GaussianBlur(hybrid, (7,7), 0)
        elif style == "chaotic":
            hybrid = pixel_sort(hybrid, 40)
            hybrid = rgb_shift(hybrid, shift)
            hybrid = add_noise(hybrid, noise)
        elif style == "organic":
            hybrid = rgb_shift(hybrid, shift)
            hybrid = add_noise(hybrid, noise)
        elif style == "neon":
            import cv2
            hsv = cv2.cvtColor(hybrid, cv2.COLOR_RGB2HSV)
            hsv[...,1] = np.clip(hsv[...,1]*1.5,0,255)
            hsv[...,2] = np.clip(hsv[...,2]*1.2,0,255)
            hybrid = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
            hybrid = rgb_shift(hybrid, shift)

        final = enhance(hybrid)

    # AI-guided generation
    else:
        final, score = ai_guided_glitch(
            hybrid, ai_prompt,
            iterations=15,
            shift=shift,
            noise=noise
        )
        st.caption(f"CLIP similarity score: {score:.3f}")


    # Output

    st.image(final, caption="Generated Artwork", use_column_width=True)

    output_path = "outputs/hybrid_glitch.png"
    Image.fromarray(final).save(output_path)

    with open(output_path,"rb") as f:
        st.download_button(
            label="Download Image",
            data=f,
            file_name="hybrid_glitch.png",
            mime="image/png"
        )
