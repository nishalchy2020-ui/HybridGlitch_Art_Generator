import torch
import clip
from PIL import Image

device = "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

def clip_score(image_np, prompt):
    
    image = Image.fromarray(image_np)
    image_input = preprocess(image).unsqueeze(0).to(device)
    text_input = clip.tokenize([prompt]).to(device)

    with torch.no_grad():
        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text_input)

    similarity = torch.cosine_similarity(image_features, text_features)
    return similarity.item()
