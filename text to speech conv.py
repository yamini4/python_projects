from tkinter import*
from gtts import gTTS
from playsound import playsound
root = Tk()
root.geometry("350x300")
root.configure(bg='ghost white')
root.title("DATA FLAIR - TEXT TO SPEECH")
Label(root, text="TEXT_TO_SPEECH", font=('arial', '20', 'bold'), bg='white smoke').pack()
Label(text="DATA FLAIR", font=('arial', '15', 'bold'), bg='white smoke', width=20).pack(side=BOTTOM)

Msg = StringVar()
Label(root, text="ENTER TEXT", font=('arial', '15', 'bold'), bg='white smoke').place(x=20, y=60)

entry_field = Entry(root, textvariable=Msg, width='50')
entry_field.place(x=20, y=100)
def text_to_speech():
    message = entry_field.get()
    speech = gTTS(text=message)
    speech.save('DataFlair.mp3')
    playsound('DataFlair.mp3')

def exit():
    root.destroy()

def reset():
    Msg.set("")


Button(root, text="PLAY", font=('arial', '15', 'bold'), command=text_to_speech, width='4').place(x=25, y=140)
Button(root, font=('arial', '15', 'bold'), text='exit', width='4', command=exit, bg='OrangeRed1').place(x=100, y=140)
Button(root, font=('arial', '15', 'bold'), text='reset', width='6', command=reset).place(x=175, y=140)

root.mainloop()
