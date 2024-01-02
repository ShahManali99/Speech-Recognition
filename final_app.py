from tkinter import *

def audio():
    print("Recorded audio")

def mic():
    print("Microphone") 
    

root = Tk()
#frame = Frame(root,height=200,width=300)
#frame.pack()
root.minsize(200,300)
audio_button = Button(root,text="Recorded Audio",command=audio)
audio_button.pack()
mic_button = Button(root,text="Microphone",command=mic)
mic_button.pack()

root.mainloop()

