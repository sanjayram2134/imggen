import streamlit as st
from PIL import Image
from io import BytesIO
import torch
from diffusers import StableDiffusionPipeline

# Load the diffusion pipeline model
def load_model(model_path):
    pipe = StableDiffusionPipeline.from_pretrained(model_path)
    return pipe

model_path = "dreamlike_diffusion_model"
# Load the model
pipe = load_model(model_path)

# Streamlit UI for generating image based on text prompt
def main():
    st.title('Image Generator')

    # Input prompt
    prompt = st.text_input('Enter your prompt:')

    if st.button('Generate Image'):
        # Generate image based on prompt
        image = generate_image(prompt, pipe)

        # Display the generated image
        st.image(image, caption='Generated Image', use_column_width=True)

# Function to generate image based on prompt
def generate_image(prompt, pipe):
    image_bytes = pipe(prompt).images[0]
    print(image_bytes)
      # Assuming pipe returns a list of images, get the first one
    #image = Image.open(BytesIO(image_bytes))
    return image_bytes

if __name__ == '__main__':
    main()
