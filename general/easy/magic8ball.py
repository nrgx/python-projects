from tkinter import *
from PIL import Image, ImageTk
import random


responses = [
    "As I see it, yes.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don’t count on it.",
    "It is certain.",
    "It is decidedly so.",
    "Most likely.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Outlook good.",
    "Reply hazy, try again.",
    "Signs point to yes.",
    "Very doubtful.",
    "Without a doubt.",
    "Yes.",
    "Yes – definitely.",
    "You may rely on it.",
]


def pick_response():
    return random.choice(responses)


def main():
    mw = Tk()
    mw.geometry("800x800")
    mw.title("Magic 8-Ball")
    magic_8_ball_img = ImageTk.PhotoImage(Image.open("assets/magic-8-ball.png"))
    question = StringVar()
    answer = StringVar()
    img_label = Label(
        mw,
        text="",
        font="sans-serif 8 bold",
        fg="white",
        textvariable=answer,
        image=magic_8_ball_img,
        justify=CENTER,
        compound="center",
    )
    img_label.pack()
    Entry(
        mw, font="sans-serif 16 bold", textvariable=question, fg="black", bg="white"
    ).place(x=250, y=700)
    Button(
        mw,
        font="sans-serif 16 bold",
        text="Ask",
        padx=5,
        command=lambda: answer_question(question, answer),
    ).pack(side=BOTTOM)
    mw.mainloop()


def answer_question(question, answer):
    q = question.get()
    if q == "":
        return
    answer.set(pick_response())


if __name__ == "__main__":
    main()
