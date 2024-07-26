import os
from PIL import Image
import pillow_heif


output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

def heic_to_jpg(heic_file_path, jpg_file_path):
    heif_file = pillow_heif.read_heif(heic_file_path)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
    )

    image.save(jpg_file_path, format("jpeg"))

for filename in os.listdir('.'):
    if filename.lower().endswith('.heic'):
        input_path = os.path.join('.', filename)
        output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.jpg")
        heic_to_jpg(input_path, output_path)
        print(f"Converted {filename} to {output_path}")

print("Done")
