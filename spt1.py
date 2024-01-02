from tkinter import Tk, Text, BOTH, W, N, E, S, END, INSERT 
from tkinter.ttk import Frame, Button, Label, Style
import speech_recognition as sr
from docx import Document


def mic1(area):
    """r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        area.insert(INSERT,"Say Something")
        audio = r.listen(source)
        area.insert(END, "Time Over")
        
    b=r.recognize_google(audio)
    document = Document()
    p = document.add_paragraph(b)
    document.save('demo_mi1.docx')
    """
    print("Hi")

root = Tk()
root.geometry("500x450+300+500")

root.title("Speech to Text Application")
#root.pack(fill=BOTH, expand=True)
frame = Frame(root)
frame.pack()
root.style = Style()
root.style.theme_use("default")
        
frame.columnconfigure(1, weight=1)
frame.columnconfigure(3, pad=7)
frame.rowconfigure(3, weight=1)
frame.rowconfigure(5, pad=7)

lbl = Label(frame, text="Keep your eyes on screen")
lbl.grid(sticky=W, pady=4, padx=5)

area = Text(frame)
area.grid(row=1, column=0, columnspan=2, rowspan=5, padx=8, sticky=E + W + S + N)

abtn = Button(frame, text="Audio File")
abtn.grid(row=1, column=3, padx=4)

cbtn = Button(frame, text="Microphone",command=mic1(area))
cbtn.grid(row=2, column=3, padx=4, pady=4)
"""
hbtn = Button(root, text="Help")
hbtn.grid(row=7, column=0, padx=5)

obtn = Button(root, text="Exit")
obtn.grid(row=7, column=3)
"""
#cbtn.bind('<Button-1>', mic1(area))

root.mainloop()

