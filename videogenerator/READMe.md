# w.i.p. working on the set up and this is what I have

## 1. I did hugging face auth first for a smoother workflow

1. Got the token from hugging face. 
2. added 
it to colab manually then ran this to 
check if its loaded in Colab:
- **python**
```python
from google.colab import userdata
import os

hf_token = userdata.get('HUGGING_FACE_HUB_TOKEN')  # Fetch the secret
if hf_token:
    os.environ["HUGGING_FACE_HUB_TOKEN"] = hf_token
    print(f"Token loaded successfully: {hf_token[:5]}...")  # Mask token for safety
else:
    print("Token not found in secrets.")
```
Check if you can login to hugging face from colab:
```python
from huggingface_hub import login

hf_token = os.environ.get("hug_face_three")  # Retrieve token from env
if hf_token:
    login(hf_token)  # Log in to Hugging Face Hub
    print("Logged in to Hugging Face Hub successfully!")
else:
    print("Token is not set. Please check your Colab secrets.")
```
Then I verified it to see if I can get my own info:
```python
from huggingface_hub import HfApi
api = HfApi()

try:
    user_info = api.whoami()
    print("Authentication successful:", user_info)
except Exception as e:
    print("Authentication failed:", str(e))
```
# Check what directory your in before you start

## 2 
I ran this to do the install of ComfyUI:
## (Change runtime at some point) simple video generator
```
 <!-- Clone ComfyUI repository -->
!git clone https://github.com/comfyanonymous/ComfyUI
!apt-get install -y libgl1-mesa-glx

 <!-- Change directory to ComfyUI -->
%cd ComfyUI

 <!-- Install required packages -->
!pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
!pip install opencv-python
!pip install imageio[ffmpeg]
```
pro note: check what directory your in and make sure everything was successful as you go.


## 2.5 Model Download: Put Stable Diffusion model into the correct folder. using -v for verbose
- Download Stable Diffusion model (replace URL with the actual model link)
```
!wget -v -O models/stable-diffusion-v1-5.ckpt https://huggingface.co/CompVis/stable-diffusion-v-1-5-original/resolve/main/sd-v1-5.ckpt

```
- Optional: Clone and install Deforum (if you want animation support)
```
!git clone https://github.com/deforum-art/deforum-stable-diffusion
%cd deforum-stable-diffusion
!pip install -r requirements.txt
%cd ..
```

## 3 Start ComfyUI server
```
!python server.py