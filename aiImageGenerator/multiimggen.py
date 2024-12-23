# Import necessary libraries
import torch  # For handling computations on GPUs and managing PyTorch operations
from diffusers import StableDiffusionPipeline, StableDiffusionImg2ImgPipeline  # Diffusers for AI-based image generation
from PIL import Image  # For handling and processing images
import matplotlib.pyplot as plt  # For displaying images
import os  # For handling file paths and directories
from google.colab import drive  # For mounting Google Drive in Colab

# Step 1: Mount Google Drive
# This mounts your Google Drive to the Colab environment so you can access files stored in it.
drive.mount('/content/drive')

# Step 2: Set Google Drive paths
# Define the base path of your Google Drive and specific paths for output images and the reference image.
drive_base_path = "/content/drive/My Drive"  # Base directory of Google Drive
output_dir = os.path.join(drive_base_path, "generated_images")  # Directory to save generated images
ref_image_path = os.path.join(drive_base_path, "reference_image.jpg")  # Path to the reference image

# Create the output directory IF it doesn't already exist
os.makedirs(output_dir, exist_ok=True)

# Step 3: Setup the Stable Diffusion pipelines
# Clear the GPU memory cache to ensure there's enough free memory for processing.
torch.cuda.empty_cache()

# Define the model ID for Stable Diffusion 2.1
model_id = "stabilityai/stable-diffusion-2-1"

# Load the text-to-image pipeline from the pretrained model
pipe_text2img = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)

# Load the image-to-image pipeline from the pretrained model
pipe_img2img = StableDiffusionImg2ImgPipeline.from_pretrained(model_id, torch_dtype=torch.float16)

# Move both pipelines to the GPU for faster processing
pipe_text2img = pipe_text2img.to("cuda")
pipe_img2img = pipe_img2img.to("cuda")

# Step 4: Generate an image from text (Text-to-Image)
# Define the prompt that describes the image you want to generate.
prompt = "A serene sunset over a rustic cityscape with neon lights"

# Generate the image using the text-to-image pipeline
image = pipe_text2img(prompt, width=768, height=768).images[0]  # Width and height define image resolution

# Save the generated image to the output directory
image.save(os.path.join(output_dir, "text2img_example.jpg"))

# Display the generated image in the notebook
plt.imshow(image)
plt.axis("off")  # Remove axis labels for better visualization
plt.show()

# Step 5: Generate an image using another image as a reference (Image-to-Image)
# Check if the reference image exists at the specified path
if os.path.exists(ref_image_path):
    # Open the reference image and convert it to RGB format
    ref_image = Image.open(ref_image_path).convert("RGB")
    
    # Generate a new image based on the reference image and a prompt
    image = pipe_img2img(
        prompt="An enchanted rain forest with glowing plants and fireflies",  # Description of the desired output image
        init_image=ref_image,  # Reference image
        strength=0.75,  # Degree of transformation (0 = very close to reference, 1 = very freeform)
        guidance_scale=7.5  # Controls adherence to the prompt (higher = stricter adherence)
    ).images[0]
    
    # Save the generated image to the output directory
    image.save(os.path.join(output_dir, "img2img_example.jpg"))

    # Display the generated image in the notebook
    plt.imshow(image)
    plt.axis("off")  # Remove axis labels for better visualization
    plt.show()
else:
    # Inform the user if the reference image is not found
    print(f"Reference image not found at {ref_image_path}. Please upload it to Google Drive.")

# Notify the user where all images have been saved
print(f"All images are saved in: {output_dir}")
