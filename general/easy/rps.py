"""
Rock | Paper | Scissors
Easy Implementation of RPS game
Make GUI app more beautiful
Move all to functions
"""
from tkinter import *
import random


mw: Tk = Tk()
mw.geometry("400x400")
mw.resizable(0, 0)
mw.title("Rock | Paper | Scissors")
mw.config(bg="gray")
Label(mw, text="Rock | Paper | Scissors", font="sans-serif 20 bold", bg="gray").pack()
user = StringVar()
Label(
    mw, text="Choose rock, paper or scissors", font="sans-serif 16 bold", bg="gray"
).place(x=10, y=70)
Entry(mw, font="sans-serif 16 bold", textvariable=user, bg="white").place(x=50, y=130)
random_pick = random.randint(1, 3)
if random_pick == 1:
    random_pick = "rock"
elif random_pick == 2:
    random_pick = "paper"
else:
    random_pick = "scissors"

result = StringVar()


def start():
    win = "You won"
    loss = "You loose"
    pick = user.get()
    if pick == random_pick:
        result.set("Stalemate")
    elif (
        (pick == "rock" and random_pick == "scissors")
        or (pick == "paper" and random_pick == "rock")
        or (pick == "scissors" and random_pick == "paper")
    ):
        result.set(win)
    elif (
        (pick == "rock" and random_pick == "paper")
        or (pick == "paper" and random_pick == "scissors")
        or pick == "scissors"
        and random_pick == "rock"
    ):
        result.set(loss)
    else:
        result.set(f"Invalid value given: {user}")


def reset():
    result.set("")
    user.set("")


def exit_rps():
    mw.destroy()


Entry(
    mw,
    font="sans-serif 10 bold",
    textvariable=result,
    bg="white",
    width=50,
).place(x=25, y=250)
Button(
    mw, font="sans-serif 13 bold", text="PLAY", padx=5, bg="black", command=start
).place(x=150, y=190)
Button(
    mw, font="sans-serif 13 bold", text="RESET", padx=5, bg="black", command=reset
).place(x=70, y=310)
Button(
    mw, font="sans-serif 13 bold", text="EXIT", padx=5, bg="black", command=exit_rps
).place(x=230, y=310)
mw.mainloop()
