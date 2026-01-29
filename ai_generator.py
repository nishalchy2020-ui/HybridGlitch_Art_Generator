from glitch_engine import rgb_shift, add_noise, pixel_sort
from clip_guidance import clip_score
import numpy as np

def ai_guided_glitch(base_image, prompt, iterations=15, shift=15, noise=0.1):
    
    best_image = base_image.copy()
    best_score = clip_score(best_image, prompt)

    for i in range(iterations):
        candidate = best_image.copy()

        # Accumulate glitches
        candidate = rgb_shift(candidate, shift + i*2)
        candidate = add_noise(candidate, noise + i*0.02)
        if i % 2 == 0:
            candidate = pixel_sort(candidate, strength=30)

        score = clip_score(candidate, prompt)
        if score > best_score:
            best_score = score
            best_image = candidate

    return best_image, best_score
