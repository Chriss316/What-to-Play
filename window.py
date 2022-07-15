from onefile import get_rel_path

from enum import Enum

import tkinter.font as font
from PIL.ImageTk import PhotoImage
from PIL.Image import open as open_image
from tkinter import Tk, Button, Label, Frame, filedialog


class Colours(str, Enum):
    dark_green = '#15413D'
    light_green = '#507370'
    highlight_green = '#9DABA7'
    white = '#FFFFFF'
    black = '#000000'


button_themes = {
    'unselected': {
      "bg": Colours.highlight_green,
      "fg": Colours.black,
      "activebackground": Colours.dark_green,
      "activeforeground": Colours.white,
      "relief": 'flat'
    },
    'selected': {
      "bg": Colours.dark_green,
      "fg": Colours.white,
      "activebackground": Colours.dark_green,
      "activeforeground": Colours.white,
      "relief": 'sunken'
    },
}


class WTPApp:
    def __init__(self, **kwargs):
        # Named Args
        self.run_call = kwargs.get('steam', None)

        # Create window object
        self.win = Tk()

        # Size variables
        self.window_width = 800
        self.window_height = 600
        self.screen_width = self.win.winfo_screenwidth()
        self.screen_height = self.win.winfo_screenheight()

        # Other Variables
        self.selected_path = ''
        self.selected_state = 'steam'

        # Window Settings
        self.win.geometry("{}x{}+{}+{}".format(
            self.window_width,
            self.window_height,
            int(self.screen_width / 2 - self.window_width / 2),
            int(self.screen_height / 2 - self.window_height / 2))
        )
        self.win.title('What to Play?')
        self.win.iconbitmap(get_rel_path('assets/icon.ico'))
        self.win.configure(bg=Colours.light_green)
        self.win.resizable(0, 0)

        # Window Elements
        self.buttons = []
        self.create_background()
        self.launch_button()
        # Store buttons for updating
        self.buttons.append(self.steam_button())
        self.buttons.append(self.shortcuts_button())

    def build(self):
        return self.win.mainloop()

    def create_background(self):
        bg_image_file = open_image(get_rel_path('assets/background.png'))
        bg_image_obj = PhotoImage(bg_image_file)

        lable_img = Label(self.win, image=bg_image_obj, bg=Colours.light_green)
        lable_img.image = bg_image_obj  # keep a reference!
        lable_img.pack()
        lable_img.place(
            x=self.window_width / 2 - bg_image_obj.width() / 2,
            y=self.window_height / 2 - bg_image_obj.height() / 2
        )

    def create_button(self, text, w, h, selected_state, **kwargs):
        callback = kwargs.get('callback', None)
        btn_width = w
        btn_height = h

        # Create a frame to act as a border for the Button
        button_border = Frame(self.win, highlightbackground=Colours.dark_green, highlightthickness=4, bd=0)

        # Create the Button Object
        btn = Button(
            button_border,
            text=text,
            bg=button_themes[selected_state]['bg'],
            fg=button_themes[selected_state]['fg'],
            activebackground=button_themes[selected_state]['activebackground'],
            activeforeground=button_themes[selected_state]['activeforeground'],
            width=btn_width,
            height=btn_height,
            relief=button_themes[selected_state]['relief'],
            command=callback)
        btn['font'] = font.Font(family='Verdana', size=12, weight='bold')
        btn.pack()

        # Render and place the Frame with the button inside
        button_border.pack()
        button_border.update()

        return button_border

    def steam_button(self):
        if self.selected_state == 'steam':
            state = 'selected'
        else:
            state = 'unselected'

        btn = self.create_button("Steam Library", 18, 8, state, callback=self.steam_btn_callback)
        btn.place(
            x=self.window_width / 2 - btn.winfo_width() - 50,
            y=(self.window_height / 2 - btn.winfo_height() / 2) - 50
        )

        return btn

    def shortcuts_button(self):
        if self.selected_state == 'steam':
            state = 'unselected'
        else:
            state = 'selected'

        btn = self.create_button("Shortcut Library", 18, 8, state, callback=self.shortcuts_btn_callback)
        btn.place(
            x=self.window_width / 2 + 50,
            y=(self.window_height / 2 - btn.winfo_height() / 2) - 50
        )

        return btn

    def launch_button(self):
        btn = self.create_button("Get me a game!", 25, 4, 'unselected', callback=self.launch_call)
        btn.place(
            x=self.window_width / 2 - btn.winfo_width() / 2,
            y=(self.window_height - 100) - btn.winfo_height() / 2
        )

    def steam_btn_callback(self):
        self.selected_state = 'steam'
        self.redraw_buttons()

    def shortcuts_btn_callback(self):
        self.selected_state = 'shortcuts'
        self.redraw_buttons()
        self.get_directory()

    def get_directory(self):
        self.selected_path = filedialog.askdirectory()

    def redraw_buttons(self):
        for x in self.buttons:
            x.destroy()

        self.steam_button()
        self.shortcuts_button()

    def launch_call(self):
        self.run_call(self.selected_state, shortcuts=self.selected_path)
