import re
from pynput.keyboard import Controller
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter as tk
import time
import keyboard as kb
import sys
import webbrowser
from pathlib import Path

from tkinter import Tk, Canvas, Text, Button, PhotoImage
from tkinter import *
import tkinter as tk


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = Path(__file__).parent
    return Path(base_path) / relative_path


def relative_to_assets(path: str) -> Path:
    return resource_path(Path("res") / Path(path))

# Use ThemedTk to apply a theme. "equilux" is a good dark theme.
root = ThemedTk(theme="equilux")

#Windows Title
root.title("Auto Typer by Arin Choubey")
root.geometry("600x400")
root.resizable(0,0)

# The main background will be handled by the theme, so configure is not needed.
# root.configure(bg = "#FFFFFF")

# Set the window icon using an .ico file for best results on Windows.
root.iconbitmap(default=relative_to_assets("app_icon.ico"))


keyboard = Controller()

fontSmall= ('', 8)
cursor="hand2"

def callback(event):
    webbrowser.open_new_tab(event)

def rTime():
    time.sleep(4)
def rTime1():
    time.sleep(1)

def get_current_text():
    """Gets the text from the Text widget of the currently selected tab."""
    try:
        # Get the widget of the selected tab
        selected_tab_widget = root.nametowidget(notebook.select())
        # Find the Text widget inside that tab's frame
        text_widget = selected_tab_widget.winfo_children()[0]
        return text_widget.get(1.0, tk.END+"-1c")
    except (tk.TclError, IndexError):
        # Handle cases where no tab is selected or tab has no text widget
        return ""

def paste():
    input1 = get_current_text()
    rTime()
    keyboard.type(input1)

def paste1():
    input1 = get_current_text()
    rTime1()
    keyboard.type(input1)

def linebyline():
    input1=re.sub(r'\t', '', get_current_text())
    rTime()
    keyboard.type(input1)

def singleline():
    input1=re.sub(r'\n', '', get_current_text())
    rTime()
    keyboard.type(input1)

def linebyline1():
    input1=re.sub(r'\t', '', get_current_text())
    rTime1()
    keyboard.type(input1)

def singleline2():
    input1=re.sub(r'\n', '', get_current_text())
    rTime1()
    keyboard.type(input1)


canvas = Canvas(
    root,
    bg = "#464646",
    height = 400,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    300.5,
    154.0,
    image=entry_image_1
)

# Create a Notebook (tabbed interface)
notebook = ttk.Notebook(root)
notebook.place(
    x=19.0,
    y=6.0,
    width=563.0,
    height=294.0
)

# Create tabs
num_tabs = 10
for i in range(num_tabs):
    tab_frame = ttk.Frame(notebook, width=563, height=294)
    notebook.add(tab_frame, text=f'Tab {i+1}')

    # Add a Text widget to each tab
    text_widget = Text(
        tab_frame,
        bd=0,
        # bg="#E6F0FF", # Let's use the theme's default background
        highlightthickness=0
    )
    text_widget.pack(expand=True, fill='both')

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = ttk.Button(
    image=button_image_1,
    command=paste,
    style="Image.TButton"
)
button_1.place(
    x=246.0,
    y=324.0,
    width=95.0,
    height=35.0
)

kb.add_hotkey('ctrl+6', paste1)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = ttk.Button(
    image=button_image_2,
    command=singleline,
    style="Image.TButton"
)
button_2.place(
    x=362.0,
    y=323.0,
    width=95.0,
    height=37.30769348144531
)

kb.add_hotkey('ctrl+7', singleline2)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = ttk.Button(
    image=button_image_3,
    command=linebyline,
    style="Image.TButton"
)
button_3.place(
    x=474.0,
    y=324.0,
    width=113.0,
    height=35.0
)

kb.add_hotkey('ctrl+8', linebyline1)

canvas.create_text(
    6.0,
    389.0,
    anchor="nw",
    text="Version: 1.0.1",
    fill="#FFFFFF",
    font=("Microsoft Himalaya", 15 * -1)
)

canvas.create_text(
    440.0,
    388.0,
    anchor="nw",
    text="Auto Typing Software by Arin Choubey",
    fill="#FFFFFF",
    font=("Microsoft Himalaya", 15 * -1)
)


canvas.create_text(
    279.0,
    360.0,
    anchor="nw",
    text="ctrl+6",
    fill="#FFFFFF",
    font=("Inter Regular", 10 * -1)
)

canvas.create_text(
    396.0,
    360.0,
    anchor="nw",
    text="ctrl+7",
    fill="#FFFFFF",
    font=("Inter Regular", 10 * -1)
)

canvas.create_text(
    510.0,
    360.0,
    anchor="nw",
    text="ctrl+8",
    fill="#FFFFFF",
    font=("Inter Regular", 10 * -1)
)

style = ttk.Style()
style.configure("Image.TButton", padding=0)
style.configure("Red.TLabel", foreground="red", background="#464646", borderwidth=2, relief="solid")

lbl = ttk.Label(root, text="Github", style="Red.TLabel", font=('', 20, 'bold'))
lbl.place(x=50, y=320)
lbl.bind("<Button>", lambda e: callback("https://github.com/Anonymous-0143"))

root.attributes('-topmost', True)

root.mainloop()