# I'm running this in Google colab so I don't need the hardware to run it locally:
# Import necessary libraries
import torch  # PyTorch for tensor computations and GPU acceleration
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler  # For loading and managing the Stable Diffusion model
import matplotlib.pyplot as plt  # For visualizing the generated image

# Clear any unused GPU memory currently allocated by PyTorch
torch.cuda.empty_cache()

# Specify the model ID for Stable Diffusion version 2.1 from the Hugging Face Model Hub
model_id = "stabilityai/stable-diffusion-2-1"

# Load the pre-trained Stable Diffusion model pipeline
# - `from_pretrained()` downloads and sets up the model configuration and weights
# - `torch_dtype=torch.float16` reduces the model precision to 16-bit for faster inference and lower memory usage
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)

# Replace the default scheduler with a DPMSolverMultistepScheduler
# - Optimizes the denoising process for better efficiency and image quality
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

# Move the entire pipeline (model, scheduler, etc.) to the GPU
# - `"cuda"` specifies the use of GPU for faster computations
pipe = pipe.to("cuda")

# Define the text prompt for image generation
# - This is the input description that guides the model to create a corresponding image
prompt = "cockpit of a jet fighter plane"

# Generate an image using the pipeline
# - `width=1000` and `height=1000` specify the resolution of the output image
# - `.images[0]` extracts the first image from the generated outputs
image = pipe(prompt, width=1000, height=1000).images[0]

# Display the generated image using Matplotlib
plt.imshow(image)  # Render the image in the plot
plt.axis('off')  # Hide axis numbers and ticks for a cleaner display
plt.show()  # Show the plot in the output