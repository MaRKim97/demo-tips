import torch
import sys
from time import time

from diffusers import DiffusionPipeline

print(f"sys.argv[1:]: {' '.join(sys.argv[1:])}")

if len(sys.argv) > 1:
    prompt = ' '.join(sys.argv[1:])
else: # default
    prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"

print(f"prompt: {prompt}")

start = time()
pipe = DiffusionPipeline.from_pretrained(
    "playgroundai/playground-v2.5-1024px-aesthetic",
    torch_dtype=torch.float16,
    variant="fp16",
).to("cuda")
print(f"Model Loading time = {time() - start}")

# # Optional: Use DPM++ 2M Karras scheduler for crisper fine details
# from diffusers import EDMDPMSolverMultistepScheduler
# pipe.scheduler = EDMDPMSolverMultistepScheduler()

start = time()
image = pipe(prompt=prompt, num_inference_steps=50, guidance_scale=3).images[0]
image.save("result2.png")
print(f"Inference time = {time() - start}")
