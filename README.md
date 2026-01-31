# HybridGlitch_Art_Generator

**Student name:** Nishal Chaudhary  
**Student number:** 2313325
**Project title:** HybridGlitch Art Generator - AI-Inspired Glitch Art from Hybrid Images  
**Link to project video recording:** https://uca.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=8ca27cf9-22b4-4cc6-95af-b3e30098a69f
---

## Project Overview
HybridGlitch is a **visual creativity system inspired by AI** that generates **surreal hybrid images and glitch art**.  
The system combines **two images** (from a mini dataset or user uploads) and applies **creative glitch transformations**, producing **distinct digital artworks**. Users can select **different artistic styles**, such as *surreal, glitchy, chaotic, soft, organic, and neon*.  

Key features include:

- **Imaginative hybridization**: Combine two images creatively using edge detection, blending, and texture overlays.  
- **Glitch effects**: Pixel sorting, noise overlays, RGB/hue shifts, scanline distortions.  
- **Mini dataset support**: Animals, landscapes, textures.  
- **Custom uploads**: Users can provide their own images.  
- **AI-guided generation**: Optional CLIP-based scoring to evolve the hybrid toward user-specified artistic prompts.  
- **User-friendly output**: Export artworks as PNG, downloadable from the interface.  

---


## Setup Instructions
### Clone the repository
```
git clone https://github.com/yourusername/HybridGlitch-Art-Generator.git
cd HybridGlitch-Art-Generator
```
### Create and activate virtual environment
```
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### Install dependencies
```
pip install -r requirements.txt
pip install git+https://github.com/openai/CLIP.git
```

### Prepare the dataset (optional)
- Place images in the dataset/ folder:
```
dataset/
    animals/
    textures/
    landscapes/
```
- Each folder should contain 3–5 images for random hybrid selection.

### Run the Streamlit app
```
streamlit run app.py
```
- Upload two images or select images from the mini dataset.
- Choose a style and optionally enable AI (CLIP-guided) generation.
- Click download to save your final artwork.
