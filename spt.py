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
class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Speech to Text Application")
        self.pack(fill=BOTH, expand=True)

        self.style = Style()
        self.style.theme_use("default")
        
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        lbl = Label(self, text="Keep your eyes on screen")
        lbl.grid(sticky=W, pady=4, padx=5)

        area = Text(self)
        area.grid(row=1, column=0, columnspan=2, rowspan=5,
                  padx=8, sticky=E + W + S + N)

        abtn = Button(self, text="Audio File")
        abtn.grid(row=1, column=3, padx=4)

        cbtn = Button(self, text="Microphone")
        cbtn.grid(row=2, column=3, padx=4, pady=4)

        hbtn = Button(self, text="Help")
        hbtn.grid(row=7, column=0, padx=5)

        obtn = Button(self, text="Exit")
        obtn.grid(row=7, column=3)

        cbtn.bind('<Button-1>', mic1(area))

        


def main():
    root = Tk()
    root.geometry("500x450+300+500")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main() 
