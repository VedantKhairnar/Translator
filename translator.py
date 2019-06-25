from tkinter import *
from googletrans import Translator
import win32com.client as wincl
import speech_recognition as sr
class translator:

    def translate(self):
        if str(self.fn.get())!="":
            self.translatedfinal = self.translator.translate(str(self.fn.get()), dest=self.variable.get())
        else:
            self.translatedfinal = self.translator.translate(self.text, dest=self.variable.get())

        self.name = Label(self.root, text="Translated Text:", bg='black',fg='cyan',font='1')
        self.name.place(x=100, y=400)
        self.final = Label(self.root, text=self.translatedfinal.text+"                 ", font=100,bg='black',fg='cyan')
        self.final.place(x=400, y=400)


    def voiceinput(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak Anything :")
            self.speak.Speak("Speak Anything")
            audio = r.listen(source)
            try:
                self.text = r.recognize_google(audio)
                print("You said : {}".format(self.text))
            except:
                print("Sorry could not recognize your voice")

    def voiceoutput(self):
        self.speak.Speak(self.translatedfinal.text)

    def __init__(self):
        self.root = Tk()
        self.root.geometry('900x700')
        self.root.title("Translator")
        self.root.config(bg='black')
        self.speak = wincl.Dispatch("SAPI.SpVoice")

        self.raw = ""
        self.fn = StringVar()
        self.ln = StringVar()
        self.translator = Translator()

        self.languages = [
            "English",
            "Spanish",
            "French",
            "Arabic",
            "Bulgarian",
            "Danish",
            "German",
            "Greek",
            "Persian",
            "Hindi",
            "Italian",
            "Japanese",
            "Korean",
            "Polish",
            "Urdu",
        ]


        self.name = Label(self.root, text="Language Translator", bg='black',fg='cyan')
        self.name.config(font=("Old Stamper",30))
        self.name.place(x=200, y=130)

        self.input = Label(self.root, text="Enter text here:", bg='black',fg='cyan',font=100)
        self.input.place(x=100, y=305)

        self.firste = Entry(self.root, textvariable=self.fn, bg='black', fg='cyan',font='10')
        self.firste.place(x=280, y=305)

        self.voiceinput = Button(self.root, text="For Voice Input", bd=7, bg='black', fg='cyan',command=self.voiceinput)
        self.voiceinput.place(x=100, y=500)

        self.voiceoutput = Button(self.root, text="For Voice Output", bd=7, bg='black', fg='cyan',command=self.voiceoutput)
        self.voiceoutput.place(x=330, y=500)

        self.trans = Button(self.root, text="Translate", bd=7, bg='black', fg='cyan',command=self.translate)
        self.trans.place(x=600, y=500)

        self.variable = StringVar(self.root)
        self.variable.set(self.languages[0])

        w=OptionMenu(self.root,self.variable,*self.languages)
        w.config(bg='black',fg='cyan',border=0)
        w.place(x=600,y=305)

        self.root.mainloop()

s = translator()
