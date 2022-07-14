from enum import Enum

from tkinter import Tk, Button, Label, Frame, PhotoImage
import tkinter.font as font
import PIL.Image
import PIL.ImageTk


class Colours(str, Enum):
    dark_green = '#15413D'
    light_green = '#507370'
    highlight_green = '#9DABA7'
    white = '#FFFFFF'
    black = '#000000'


class WTPApp:
    def __init__(self, **kwargs):
        # Named Args
        self.steam_call = kwargs.get('steam', None)

        # Create window object
        self.win = Tk()

        # Size variables
        self.window_width = 800
        self.window_height = 600
        self.screen_width = self.win.winfo_screenwidth()
        self.screen_height = self.win.winfo_screenheight()

        # Window Settings
        self.win.geometry("{}x{}+{}+{}".format(
            self.window_width,
            self.window_height,
            int(self.screen_width / 2 - self.window_width / 2),
            int(self.screen_height / 2 - self.window_height / 2))
        )
        self.win.title('What to Play?')
        self.win.iconbitmap(
            'C:\\Users\\chris\\Documents\\1. Primary Documents\\Coding\\Projects\\Python\\Pycharm\\WhatToPlay\\icon.ico'
        )
        self.win.configure(bg=Colours.light_green)
        self.win.resizable(0, 0)

        # Window Elements
        self.create_background()
        self.steam_button()

    def build(self):
        return self.win.mainloop()

    def create_background(self):
        bg_image_file = PIL.Image.open(
            'C:\\Users\\chris\\Documents\\1. Primary Documents\\Coding\\Projects\\Python\\Pycharm\\WhatToPlay\\background.png'
        )
        bg_image_obj = PIL.ImageTk.PhotoImage(bg_image_file)

        lable_img = Label(self.win, image=bg_image_obj, bg=Colours.light_green)
        lable_img.image = bg_image_obj  # keep a reference!
        lable_img.pack()
        lable_img.place(
            x=self.window_width / 2 - bg_image_obj.width() / 2,
            y=self.window_height / 2 - bg_image_obj.height() / 2
        )

    def steam_button(self):
        btn_width = 25
        btn_height = 6

        # Create a frame to act as a border for the Button
        button_border = Frame(
            self.win,
            highlightbackground=Colours.dark_green,
            highlightthickness=4,
            bd=0
        )

        # Create the Button Object
        btn = Button(
            button_border,
            text="Get me a game!",
            bg=Colours.highlight_green,
            fg=Colours.black,
            activebackground=Colours.dark_green,
            activeforeground=Colours.white,
            width=btn_width,
            height=btn_height,
            relief='flat',
            command=self.steam_callback)
        btn['font'] = font.Font(family='Verdana', size=12, weight='bold')
        btn.pack()

        # Render and place the Frame with the button inside
        button_border.pack()
        button_border.update()
        button_border.place(
            x=self.window_width / 2 - button_border.winfo_width() / 2,
            y=self.window_height / 2 - button_border.winfo_height() / 2
        )

    def steam_callback(self):
        self.steam_call()
