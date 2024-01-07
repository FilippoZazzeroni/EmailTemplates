import argparse
from PIL import Image, ImageOps
from pillow_heif import register_heif_opener
import os

def heic_to_png(input_path, output_path=None):
    register_heif_opener()

    image = Image.open(input_path)

    # Generate output filename if not provided
    if output_path is None:
        output_path = "output.png"

    # Save as PNG
    image.save(output_path, quality=85)
    return output_path

def main():
    parser = argparse.ArgumentParser(description="Convert HEIC to PNG")
    parser.add_argument("input", help="Input HEIC file path")
    parser.add_argument("-o", "--output", help="Output PNG file path")

    args = parser.parse_args()

    output_path = heic_to_png(args.input, args.output)
    print(f"Conversion complete. Result saved at {output_path}")

if __name__ == "__main__":
    main()
