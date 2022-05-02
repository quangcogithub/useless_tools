# Modules
import time
from turtle import *


# Classes
class TikTokLogo:
    # Constants
    __COLORS: list[str] = ['#db0f3c', '#50ebe7', 'white']
    __POSITIONS: list[tuple[int]] = [(0, 0), (-5, 13), (-5, 5)]
    __WIDTHS: list[int] = [20, 20, 20]
    __TITLE: dict = {'x': 0, 'y': 0, 'val': 'TikTok'}
    __EFFECTS: list[dict[str: list]] = [
        {'colors': ['#db0f3c', '#50ebe7', 'white'], 'positions': [(0, 0), (-10, 18), (-5, 5)], 'widths': [20, 15, 20]},
        {'colors': ['#db0f3c', '#50ebe7', 'white'], 'positions': [(-5, 5), (-5, 13), (-5, 5)], 'widths': [20, 15, 20]},
        {'colors': ['#db0f3c', '#50ebe7', 'white'], 'positions': [(0, 0), (-5, 13), (-5, 5)], 'widths': [20, 20, 20]}
    ]

    # Constructor
    def __init__(self, user_id='@UserID', x=0, y=50, title_val=None, colors=None, positions=None, widths=None):
        # Variables
        self.__id = user_id
        self.__x = x
        self.__y = y
        self.__title = title_val if title_val else self.__TITLE
        self.__colors = colors if colors else self.__COLORS
        self.__positions = positions if positions else self.__POSITIONS
        self.__widths = widths if widths else self.__WIDTHS

        # Create Object
        self.__logo = Turtle()
        bgcolor('black')

    # Methods
    def _create_form(self):
        for col, (x, y), wid in zip(self.__colors, self.__positions, self.__widths):
            self.__logo.width(wid)
            self.__logo.up()
            self.__logo.goto(x + self.__x, y + self.__y)
            self.__logo.down()
            self.__logo.color(col)
            self.__logo.left(180)
            self.__logo.circle(50, 270)
            self.__logo.forward(120)
            self.__logo.left(180)
            self.__logo.circle(50, 90)

    def _fill_title(self):
        self.__logo.up()
        self.__logo.goto(-65 + self.__x + self.__title['x'], -170 + self.__y + self.__title['y'])
        self.__logo.down()
        self.__logo.write(self.__title['val'], font=('Arial', 40, 'bold'), move=False)

    def _fill_id(self):
        # Username icon
        self.__logo.up()
        self.__logo.goto(-50 + self.__x, -170 + self.__y)
        self.__logo.down()
        self.__logo.width(5)
        self.__logo.circle(2.5)
        self.__logo.up()
        self.__logo.goto(-40 + self.__x, -185 + self.__y)
        self.__logo.down()
        self.__logo.left(90)
        self.__logo.width(1)
        self.__logo.begin_fill()
        self.__logo.circle(10, 180)
        self.__logo.end_fill()

        # Username title
        self.__logo.up()
        self.__logo.goto(-30 + self.__x, -185 + self.__y)
        self.__logo.down()
        self.__logo.write(self.__id, font=('Arial', 16, 'normal'), move=False)

    def drawing(self):
        # Main drawing loop
        self._create_form()
        # Title
        self._fill_title()
        # Username ID
        self._fill_id()
        # Hide cursor
        self.__logo.hideturtle()

    def _clean_face(self):
        self.__logo.clear()
        self.__logo = Turtle()

    def animation(self, total_time=7):
        index = 0
        start_time = time.time()
        end_time = time.time()
        while (end_time - start_time) <= float(total_time):
            index = index if index < len(self.__EFFECTS) else 0
            self._clean_face()
            self.__title.update({'x': index % 2, 'y': index % 2})
            self.__colors = self.__EFFECTS[index]['colors']
            self.__positions = self.__EFFECTS[index]['positions']
            self.__widths = self.__EFFECTS[index]['widths']
            self.drawing()
            index += 1
            end_time = time.time()


# Functions
def main():
    # Initialize
    screen = Screen()
    screen.setup(480, 720)

    # Draw step by Step
    TikTokLogo(user_id='@quangcotiktok').drawing()
    time.sleep(1)

    # Animation
    screen.clear()
    screen.tracer(0)
    TikTokLogo(user_id='@quangcotiktok').animation()


# Main
if __name__ == '__main__':
    main()
