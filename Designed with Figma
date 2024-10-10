# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\mszat\Documents\Masa e-Learning\EGYETEM\coding_course\python\Tkinter-Designer-master\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("589x496")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 496,
    width = 589,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    700.0,
    80.0,
    fill="#1813F2",
    outline="")

canvas.create_text(
    43.0,
    13.0,
    anchor="nw",
    text="Budget Tracker",
    fill="#FFFFFF",
    font=("Inter BlackItalic", 40 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    138.0,
    135.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    435.0,
    135.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    290.0,
    217.0,
    image=image_image_3
)

canvas.create_text(
    34.0,
    113.0,
    anchor="nw",
    text="Income",
    fill="#000000",
    font=("Inter SemiBoldItalic", 16 * -1)
)

canvas.create_text(
    324.0,
    113.0,
    anchor="nw",
    text="Expenses",
    fill="#000000",
    font=("Inter SemiBoldItalic", 16 * -1)
)

canvas.create_text(
    34.0,
    195.0,
    anchor="nw",
    text="Balance",
    fill="#000000",
    font=("Inter SemiBoldItalic", 16 * -1)
)

canvas.create_text(
    34.0,
    140.0,
    anchor="nw",
    text="500,000HUF",
    fill="#000000",
    font=("Inter SemiBoldItalic", 16 * -1)
)

canvas.create_text(
    324.0,
    140.0,
    anchor="nw",
    text="150,000HUF",
    fill="#000000",
    font=("Inter SemiBoldItalic", 16 * -1)
)

canvas.create_text(
    34.0,
    222.0,
    anchor="nw",
    text="2,000,000HUF",
    fill="#000000",
    font=("Inter SemiBoldItalic", 16 * -1)
)

canvas.create_text(
    24.0,
    269.0,
    anchor="nw",
    text="Add expense:",
    fill="#1813F2",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    24.0,
    295.0,
    anchor="nw",
    text="Name:",
    fill="#000000",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    24.0,
    347.0,
    anchor="nw",
    text="Amount:",
    fill="#000000",
    font=("Inter Bold", 12 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    172.5,
    329.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=34.0,
    y=316.0,
    width=277.0,
    height=24.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    172.5,
    381.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=34.0,
    y=368.0,
    width=277.0,
    height=24.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=74.0,
    y=421.0,
    width=197.0,
    height=33.0
)
window.resizable(False, False)
window.mainloop()
