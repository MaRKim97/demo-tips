import torch
import sys
from time import time

from diffusers import StableDiffusionPipeline

print(f"sys.argv[1:]: {' '.join(sys.argv[1:])}")

if len(sys.argv) > 1:
    prompt = ' '.join(sys.argv[1:])
else: # default
    prompt = "a photo of trendy intel offices in Santa Clara"

print(f"prompt: {prompt}")

start = time()
model_id = "stabilityai/stable-diffusion-2-1"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")
print(f"Model Loading time = {time() - start}")

start = time()
image = pipe(prompt).images[0]
image.save("result1.png")
print(f"Inference time = {time() - start}")
