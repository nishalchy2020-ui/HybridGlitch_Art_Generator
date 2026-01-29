from glitch_engine import rgb_shift, add_noise, pixel_sort
from clip_guidance import clip_score

def ai_guided_glitch(
    base_image,
    prompt,
    iterations=10,
    shift=10,
    noise=0.05
):
    
    best_image = base_image
    best_score = clip_score(base_image, prompt)

    for i in range(iterations):
        candidate = rgb_shift(best_image, shift)
        candidate = add_noise(candidate, noise)

        if i % 2 == 0:
            candidate = pixel_sort(candidate, strength=40)

        score = clip_score(candidate, prompt)

        if score > best_score:
            best_score = score
            best_image = candidate

    return best_image, best_score
