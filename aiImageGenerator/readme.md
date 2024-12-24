# <p style="font-weight: bold; color: beige;">Install these dependencies on Google Colab:
<p>

``` bash
!pip install --upgrade diffusers transformers accelerate torch bitsandbytes scipy safetensors xformers
```

## <p style="font-weight: bold; color: lightgrey;">& for multi pic gen install these

- Install PyTorch with GPU support  
```!pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118```

- Install Hugging Face Diffusers and related dependencies  
```!pip install diffusers[torch]```

- Install Pillow for image processing  
```!pip install pillow```

- Install Matplotlib for image visualization  
```!pip install matplotlib```

- Install Google Colab Drive integration (usually pre-installed in Colab)  
```!pip install google-colab```


<p style="font-weight: bold; color: blue;">OR FOR MULTI PICS JUST ONE BASH LINE LIKE THIS:<P>

**Bash**: 
```bash
 !pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 diffusers[torch] pillow matplotlib google-colab
 ```