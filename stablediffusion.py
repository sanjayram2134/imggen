from diffusers import StableDiffusionPipeline

def main():
    # Model ID for diffusion pipeline
    model_id1 = "dreamlike-art/dreamlike-diffusion-1.0"

    # Load the diffusion pipeline model
    pipe = StableDiffusionPipeline.from_pretrained(model_id1)

    # Save the model
    pipe.save_pretrained('dreamlike_diffusion_model')
    print('DONEEEEEEEEEE')

if __name__ == '__main__':
    main()
