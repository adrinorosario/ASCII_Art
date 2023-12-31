from PIL import Image, ImageOps
import os


ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", ".",
               '-', '_', '+', '<', '>', 'i', '!', 'l', 'I', '?',
               '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']',
               'r', 'c', 'v', 'u', 'n', 'x', 'z', 'j', 'f', 't',
               'L', 'C', 'J', 'U', 'Y', 'X', 'Z', 'O', '0', 'Q',
               'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm',
               '*', 'W', 'M', 'B', '8', '&', '%', '$', '#', '@']


def create_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def pixel_to_ascii(image):
        pixels = Image.Image.getdata(image)
        ascii_string = ""
        for pixel in pixels:
            ascii_string += ASCII_CHARS[pixel//25]
        return ascii_string

def ascii_to_file(outputFolder, image, imageFolder = ""):
    images1 = Image.open(f'{imageFolder}{image}')

    images1.thumbnail((100, 100))
    imgs = ImageOps.grayscale(images1)

    # converting greyscale images to ascii strings
    ascii_str = pixel_to_ascii(imgs)

    width = imgs.width
    ascii_str_len = len(ascii_str)

    ascii_image_art = ""

    for indexes in range(0, ascii_str_len, width):
        ascii_image_art += ascii_str[indexes: indexes+width] + "\n"

    #print(ascii_image_art)
    clean_name = os.path.splitext(image)[0]
    with open(f'{outputFolder}{clean_name}.txt', "w") as file:
        file.write(ascii_image_art)



