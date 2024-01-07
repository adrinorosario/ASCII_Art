import sys
import os
import commonSteps

# poetry run python ASCIIArt/ascii_artx1.py ASCIIArt/images/ l/
# poetry run python ASCIIArt/ascii_artx1.py ASCIIArt/images/nasa.png
image_path = sys.argv[1]
image_folder = ""

if os.path.isfile(image_path):
    commonSteps.ascii_to_file("", image_path)
else:
    output_folder = sys.argv[2]
    commonSteps.create_dir(output_folder)
    image_folder = image_path
    for images in os.listdir(image_folder):
        commonSteps.ascii_to_file(output_folder, images, image_folder)

