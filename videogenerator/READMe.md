# I ran this to do the install, exactly:
## simple video generator 2 seconds of video
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

## 2nd Colab cell. Model Download: Put Stable Diffusion model into the correct folder.
- Download Stable Diffusion model (replace URL with the actual model link)
```
!wget -O models/stable-diffusion-v1-5.ckpt https://huggingface.co/path-to-model-file
```
- Optional: Clone and install Deforum (if you want animation support)
```
!git clone https://github.com/deforum-art/deforum-stable-diffusion
%cd deforum-stable-diffusion
!pip install -r requirements.txt
%cd ..
```

## 3rd cell Start ComfyUI server
```
!python main.py