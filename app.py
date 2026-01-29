import streamlit as st
from preprocess import load_and_prepare
from hybrid_generator import blend_images
from glitch_engine import rgb_shift, add_noise, pixel_sort
from postprocess import enhance
from ai_generator import ai_guided_glitch   
from PIL import Image
import os


st.set_page_config(page_title="HybridGlitch Art Generator", layout="centered")
st.title("🎨 HybridGlitch Art Generator")

# Ensure output folder exists
os.makedirs("outputs", exist_ok=True)


# Inputs

img1_file = st.file_uploader("Upload Image 1", type=["png", "jpg", "jpeg"])
img2_file = st.file_uploader("Upload Image 2", type=["png", "jpg", "jpeg"])

style = st.selectbox(
    "Choose Style",
    ["Soft", "Glitchy", "Chaotic", "Neon"]
)

# Artistic controls
shift = st.slider("RGB Shift Intensity", 0, 30, 10)
noise = st.slider("Noise Intensity", 0.0, 0.3, 0.05)

# AI controls
use_ai = st.checkbox("Use AI (CLIP-guided generation)")
ai_prompt = st.text_input(
    "AI Style Prompt",
    "glitchy surreal neon digital art"
)


# Processing

if img1_file is not None and img2_file is not None:

    # Load & preprocess
    img1 = load_and_prepare(img1_file)
    img2 = load_and_prepare(img2_file)

    # Hybrid base
    hybrid = blend_images(img1, img2, alpha=0.5)

    # AI-guided generation
    if use_ai:
        final, score = ai_guided_glitch(
            base_image=hybrid,
            prompt=ai_prompt,
            iterations=8,
            shift=shift,
            noise=noise
        )
        st.caption(f"🧠 CLIP similarity score: {score:.3f}")

    # Manual / non-AI pipeline
    else:
        if style in ["Glitchy", "Chaotic", "Neon"]:
            hybrid = rgb_shift(hybrid, shift)
            hybrid = add_noise(hybrid, noise)

        if style == "Chaotic":
            hybrid = pixel_sort(hybrid, strength=40)

        final = enhance(hybrid)

  
    # Output
   
    st.image(final, caption="Generated Artwork", use_column_width=True)

    output_path = "outputs/hybrid_glitch.png"
    Image.fromarray(final).save(output_path)

    with open(output_path, "rb") as f:
        st.download_button(
            label="⬇️ Download Image",
            data=f,
            file_name="hybrid_glitch.png",
            mime="image/png"
        )
