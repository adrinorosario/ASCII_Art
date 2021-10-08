import sys
from PIL import Image
from colorama import Style


try:
    image_path = sys.argv[1]
    image = Image.open(image_path)

    width, height = image.size
    aspect_ratio = height/width
    new_width = 125
    new_height = aspect_ratio * new_width * 0.55
    image = image.resize((int(new_width), int(new_height)))

    img = image.convert('L')

    pixels = img.getdata()

    ascii_chars = ['!', '@', '#', '$', '%', '^', '&', '*',
                   '<', '>', '?', ';', ':', '.', '.', '//', '~', '+', '=']

    new_pixels = [ascii_chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width]
                   for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)
    print(Style.DIM+ascii_image)

except ValueError or TypeError:
    print(f"{image_path} image path not found, please check and try again")
