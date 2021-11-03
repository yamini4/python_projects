# import all the necessary items to form the alarm clock
from tkinter import *
import datetime
import time
import winsound
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("the set date is:", date)
        print(now)
        if now == set_alarm_timer:
            print("time to wake up")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break
def actual_time():
    set_alarm_timer = f"{hour.get()}:{Min.get()}:{sec.get()}"
    alarm(set_alarm_timer)
clock = Tk()
clock.title("DataFlair Alarm Clock")
clock.geometry("650x150")
time_format = Label(clock, text="enter time in 24 hour format!", fg="black", bg="white", font=("Helvetica", 12, "bold")).place(x=400, y=60)
addTime = Label(clock, text="Hour                     Min                   Sec", font=60).place(x=350)
setYourAlarm = Label(clock, text="when to wake you up", fg="blue", relief="solid", font=("Helvetica", 20, "bold")).place(x=10, y=20)

# the variables we require to set the alarm(initialization):
hour = StringVar()
Min = StringVar()
sec = StringVar()

# time required to set the alarm clock:
hourTime = Entry(clock, textvariable=hour, bg="pink", width=10).place(x=350, y=20)
minTime = Entry(clock, textvariable=Min, bg="blue", width=10).place(x=450, y=20)
secTime = Entry(clock, textvariable=sec, bg="pink", width=10).place(x=550, y=20)

# to take the time input by user:
submit = Button(clock, text="Set Alarm", fg="red", width=10, command=actual_time).place(x=210, y=90)

clock.mainloop()
# Execution of the window.

