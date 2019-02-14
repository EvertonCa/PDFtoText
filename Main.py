import pytesseract
from PIL import Image
import os

current_directory = os.getcwd()
images_directory = current_directory + '/Images/'

print(pytesseract.image_to_string(Image.open(images_directory + 'Image3.jpg')))
