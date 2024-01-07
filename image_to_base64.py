import base64
import os
from convert_heic_to_png import heic_to_png

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read())
        return encoded_image.decode("utf-8")

def convert_and_encode_if_heic(image_path):
    _, extension = os.path.splitext(image_path)
    extension = extension.lower()

    if extension == ".heic":
        # Convert HEIC to PNG
        png_path = heic_to_png(image_path)
        # Encode PNG to base64
        encoded_image = image_to_base64(png_path)
        # Clean up temporary PNG file
        os.remove(png_path)
        return encoded_image
    else:
        # If not HEIC, simply encode the image
        return image_to_base64(image_path)

def save_to_file(encoded_image, output_file='output.txt'):
    with open(output_file, 'w') as file:
        file.write(encoded_image)
        print(f"Base64 representation of the image saved to {output_file}")

def main():
    # Assuming the CLI argument is the image file path
    import argparse

    parser = argparse.ArgumentParser(description='Convert image to base64, and convert HEIC to PNG if needed.')
    parser.add_argument('image_path', type=str, help='Path to the image file')

    args = parser.parse_args()
    
    image_path = args.image_path

    try:
        encoded_image = convert_and_encode_if_heic(image_path)
        save_to_file(encoded_image)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
