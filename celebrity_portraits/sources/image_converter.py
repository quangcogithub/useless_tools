########################################################################################################################
#                                                    Import Modules                                                    #
########################################################################################################################
import os
from PIL import Image


########################################################################################################################
#                                                       Constants                                                      #
########################################################################################################################
# List of functions called when using "import *"
__all_ = ["resize_by_width", "image_to_gray", "pixels_to_characters", "open_pixels_image"]

# List of ascii characters used to build the output text
ASCII_CHAR = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


########################################################################################################################
#                                                       Functions                                                      #
########################################################################################################################
def resize_by_width(image, width=100):
    """
    :param image:
    :param width:
    :return:
    """
    #
    original_width, original_height = image.size
    ratio = original_height / original_width

    #
    final_width = width
    final_height = final_width * ratio * 0.55

    #
    return image.resize((final_width, int(final_height)))


def image_to_gray(image):
    """
    :param image:
    :return:
    """
    return image.convert('L')


def pixels_to_characters(image):
    """
    :param image:
    :return:
    """
    return "".join([ASCII_CHAR[pixel//25] for pixel in image.getdata()])


def open_pixels_image(image_path):
    """
    """
    image_path = os.path.abspath(image_path)
    pixels_image = None

    # Open image by PIL.Image
    try:
        pixels_image = Image.open(image_path)
    except Exception as error:
        print(error)
        exit(-1)
    finally:
        return pixels_image
