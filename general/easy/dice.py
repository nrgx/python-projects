"""
Dice simulator with tkinter
"""
from tkinter import *
from PIL import Image, ImageTk
import random


def main():
    # setup main window
    mw = Tk()
    mw.geometry("400x400")
    mw.title("Dice Rolling Simulator")
    # blank_line is a padding for header
    Label(mw, text="").pack()
    Label(
        mw, text="Roll the Dice!", fg="white", font="sans-serif 16 bold italic"
    ).pack()
    # Iterate over dice sides images in the assets.
    # Notice cd to general/easy to start up dice simulator, otherwise PIL Image won't find them.
    dice_sides = [f"./assets/dice/{index}.jpg" for index in range(1, 7)]
    # choose random dice image
    dice_image = ImageTk.PhotoImage(Image.open(random.choice(dice_sides)))
    # Setup `image` attribute twice in __init__ and direct attribute setup.
    # Strange, but this will not work in `roll` function.
    img_label = Label(mw, image=dice_image)
    img_label.image = dice_image
    # pack it onto main window
    img_label.pack(expand=True)
    Button(
        mw,
        text="Roll",
        font="sans-serif 20 bold",
        fg="blue",
        command=lambda: roll(img_label, dice_sides),
    ).pack(expand=True)
    # Start widget loop
    mw.mainloop()


def roll(image_label: Label, sides: list):
    # Rolling dice
    new_dice_image = ImageTk.PhotoImage(Image.open(random.choice(sides)))
    image_label.configure(image=new_dice_image)
    image_label.image = new_dice_image


if __name__ == "__main__":
    main()
