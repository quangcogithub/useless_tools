########################################################################################################################
#                                                    Import Modules                                                    #
########################################################################################################################
import time


########################################################################################################################
#                                                       Constants                                                      #
########################################################################################################################
# List of functions called when using "import *"
__all_ = ["print_image_characters", "print_progress_bar"]


########################################################################################################################
#                                                       Functions                                                      #
########################################################################################################################
def print_image_characters(characters='', width=120, delay=0):
    """
    :param characters:
    :param width:
    :param delay:
    """
    if len(characters) > 0:
        # Split characters by the width of the command line frame
        all_lines = [
            characters[index:(index+width)] for index in range(0, len(characters), width)
        ]
        for line in all_lines:
            print('\n', end='')
            for character in line:
                print(character, sep='', end='', flush=True)

                if delay > 0:
                    time.sleep(delay)


def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=120, fill='█', end=""):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=end)

    # Print wew line on complete
    if iteration == total:
        print()
