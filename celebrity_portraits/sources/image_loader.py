########################################################################################################################
#                                                    Import Modules                                                    #
########################################################################################################################
import json
import os
from difflib import get_close_matches


########################################################################################################################
#                                                       Constants                                                      #
########################################################################################################################
__all__ = ["search_image_path"]
CELEBRITY_DEFAULT_FILE = os.path.join(os.path.dirname(__file__), "..", "databases", "celebrity_data.json")


########################################################################################################################
#                                                       Functions                                                      #
########################################################################################################################
def search_image_path(celebrity_name, database=CELEBRITY_DEFAULT_FILE):
    """
    :param celebrity_name:
    :param database:
    :return:
    """
    image_path = None

    try:
        celebrity_data = json.load(open(database, encoding="utf-8"))

        # Check name of celebrity in database
        keys = get_close_matches(celebrity_name.title(), celebrity_data.keys())
        if len(keys) > 0:
            name = celebrity_data[keys[0]]['name']
            overview = celebrity_data[keys[0]]['overview']
            answer = input(f"Ý CỦA BẠN LÀ: {name}, {overview}? Nhập \"Y\" nếu Đúng, \"N\" nếu Sai: ")

            if answer.upper().strip() == "Y":
                image_path = celebrity_data[keys[0]]['portrait']
            elif answer.upper().strip() == "N":
                print("Có thể bạn đang nhập sai tên của người mà bạn đang tim kiếm :(.")
                image_path = None
            else:
                print("Chúng tôi không hiểu câu trả lời của bạn. :(")
                image_path = None

    except Exception as error:
        print(error)
        exit(-2)

    if image_path is not None:
        return image_path
    else:
        print("Vui lòng thử lại. :(")
        exit(-3)
