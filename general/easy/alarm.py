"""
An alarm clock in Python
"""
from tkinter import *
import time
import datetime as dt
import playsound as ps


def alarm(when):
    while True:
        time.sleep(1)
        current = dt.datetime.now()
        today, now = current.strftime("%d/%m/%Y"), current.strftime("%H:%M")
        print(f"Date is {today} {now}")
        print(f"{now} | {when}")
        if now == when:
            ps.playsound("assets/alarm_clock.mp3", True)
            print("played alarm")
            break
        print("still running")


def get_now(hour, minutes):
    """
    A call back command for button
    :param hour: StringVar
    :param minutes: StringVar
    :return:
    """
    alarm(f"{hour.get()}:{minutes.get()}")


def start():
    """
    Starting GUI for alarm clock
    :return:
    """
    mw = Tk()
    mw.title("Alarm clock")
    mw.geometry("400x200")

    Label(
        mw,
        text="Enter time in 24-hour format",
        fg="white",
        font="sans-serif 14",
        compound="center",
    ).place(x=60, y=0)
    Label(mw, text="Hour : Minutes", font="sans-serif 14", compound="center").place(
        x=110, y=90
    )
    Label(
        mw,
        text="When to wake you up?",
        relief="solid",
        font="sans-serif 14",
        compound="center",
    ).place(x=90, y=30)

    hour_var = StringVar()
    min_var = StringVar()

    Entry(mw, textvariable=hour_var, fg="black", bg="white", width=8).place(
        x=100, y=120
    )
    Entry(mw, textvariable=min_var, fg="black", bg="white", width=8).place(x=200, y=120)

    Button(
        mw,
        text="SET",
        fg="white",
        font="sans-serif 16",
        width=10,
        command=lambda: get_now(hour_var, min_var),
    ).place(x=100, y=150)
    mw.mainloop()


if __name__ == "__main__":
    start()
