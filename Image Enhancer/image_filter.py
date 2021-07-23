from PIL import Image, ImageFilter
import sys
import os

image_folder = sys.argv[1]
output = sys.argv[2]

if not os.path.exists(output):
    os.makedirs(output)

for file_names in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{file_names}')

    filtered = img.filter(ImageFilter.SMOOTH)
    filtered = img.filter(ImageFilter.SMOOTH_MORE)

    renewed_pix = filtered.point(lambda i: i*1.5)
    renewed_pix.thumbnail((800, 800), Image.NEAREST)
    renewed_pix.thumbnail((800, 800), Image.LANCZOS)

    clean_name = os.path.splitext(file_names)[0]

    renewed_pix.save(f'{output}{clean_name}.png', "png")
    print("all done!")
