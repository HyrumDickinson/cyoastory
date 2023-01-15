"""
concatenation of python creations numbers 21 & 26
"""
import json
import tkinter as tk
from playsound import playsound
from PIL import ImageTk, Image


class Window:
    '''
    window
    '''

    def __init__(self):

        # populate window with initial info
        self.go_to_new_page(1)

    def go_to_new_page(self, page):

        # create new window
        _window1 = tk.Tk()
        _window1.geometry("516x516")
        _window1.title("CHOOSE YOUR OWN ADVENTURE")

        # infer where the page info file is
        # from page - works if info is stored in
        # .json file named the page number
        # load info from file into python
        with open(f'{page}.json') as file:
            page_info = json.load(file)
        self.story = page_info['story']
        self.option_labels = page_info['option labels']
        self.option_number = page_info['option number']

        # these paths are relative paths, meaning they're not the full path
        # but just the path from run_me.py to the file you want
        # which makes it easier cuz you don't have to put the
        # self.music_path = page_info['music path']
        # self.image_path = page_info['image path']

        # populate window with info
        # PATH_MUSIC1 = self.music_path
        # playsound(PATH_MUSIC1, block=False)
        # PATH_IMG1 = self.image_path
        # img1 = ImageTk.PhotoImage(Image.open(PATH_IMG1))
        # label = tk.Label(_window1, image=img1)
        # label.place(x=0, y=0)
        x_1 = tk.Label(_window1, text=self.story)
        x_1.pack()

        # label: page
        button_info = {
            "chesese": 2,
            "asdfasdf": 3,
        }

        # make variable amount of buttons
        for label in button_info:
            button = tk.Button(
                text=label,
                command=lambda: self.go_to_new_page(button_info[label])
            )
            button.pack(tk.LEFT)

        # run window
        _window1.mainloop()


if __name__ == "__main__":
    program = Window()
