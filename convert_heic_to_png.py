from PIL import Image, ImageOps
from pillow_heif import register_heif_opener

def heic_to_png(image_path):
    register_heif_opener()

    image = Image.open(image_path)

    # Save as PNG
    output_path = 'output.png'
    image.save(output_path, quality=85)
    return output_path
