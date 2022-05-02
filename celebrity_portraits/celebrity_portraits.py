########################################################################################################################
#                                                    Import Modules                                                    #
########################################################################################################################
from sources.command_printer import *
from sources.image_converter import *
from sources.image_loader import *


########################################################################################################################
#                                                       Constants                                                      #
########################################################################################################################
WIDTH = 120
DELAY_TIME = 0.000000000000000000000000000000000000000000007
LENGTH_PROCESS_BAR = 87


########################################################################################################################
#                                                       Functions                                                      #
########################################################################################################################
def main():
    # Get input data from keyboard
    print('\n')
    celebrity_name = input("NHẬP TÊN CỦA 1 NGƯỜI NỔI TIẾNG BẤT KỲ: ")

    # Name check and image search
    image_path = search_image_path(celebrity_name)
    # A List of Items
    print('\n')
    items = list(range(0, 100))
    for index, item in enumerate(items):
        # Do stuff...
        time.sleep(0.07)
        # Update Progress Bar
        print_progress_bar(index + 1, len(items), prefix='Image loading:', suffix='Complete', length=LENGTH_PROCESS_BAR)

    # Open an image and convert pixels into characters
    image_characters = pixels_to_characters(
        image_to_gray(
            resize_by_width(open_pixels_image(image_path), width=WIDTH)
        )
    )

    # Show image on command line
    print_image_characters(image_characters, width=WIDTH, delay=DELAY_TIME)


########################################################################################################################
#                                                      Main script                                                     #
########################################################################################################################
if __name__ == '__main__':
    main()
