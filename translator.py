from tkinter import *
from googletrans import Translator

class translator:

    def translate(self):
        self.translatedfinal = self.translator.translate(str(self.fn.get()), dest=self.variable.get())
        print(self.translatedfinal.pronunciation)

        self.name = Label(self.root, text="Translated Text:", bg='black',fg='cyan',font='1')
        self.name.place(x=100, y=400)
        self.final = Label(self.root, text=self.translatedfinal.text+"                 ", font=100,bg='black',fg='cyan')
        self.final.place(x=400, y=400)

        if self.translatedfinal.pronunciation !="None":
            self.prolabel = Label(self.root, text="Pronunciation:", bg='black',fg='cyan',font='1')
            self.prolabel.place(x=100, y=600)
            self.pro = Label(self.root, text=self.translatedfinal.pronunciation+"                 ", font=100,bg='black',fg='cyan')
            self.pro.place(x=400, y=600)

    def __init__(self):
        self.root = Tk()
        self.root.geometry('900x700')
        self.root.title("Translator")
        self.root.config(bg='black')

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

        self.trans = Button(self.root, text="Translate", bd=7, bg='black', fg='cyan',command=self.translate)
        self.trans.place(x=800, y=500)

        self.variable = StringVar(self.root)
        self.variable.set(self.languages[0])

        w=OptionMenu(self.root,self.variable,*self.languages)
        w.config(bg='black',fg='cyan',border=0)
        w.place(x=600,y=305)

        self.root.mainloop()

s = translator()

"""
from googletrans import Translator
translator = Translator()
print(translator.translate('안녕하세요.'))
a = translator.translate('안녕하세요.', dest='ja')
print(translator.detect('이 문장은 한글로 쓰여졌습니다.'))

self.translated = self.translator.translate('안녕하세요', src='ko') # Pass only source language
self.translated2 = self.translator.translate('안녕하세요', dest='en') # Pass only destination language
self.translated3 = self.translator.translate('안녕하세요', src='ko', dest='fr')

print(self.translated.text)
print(self.translated2)
print(self.translated3)

Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print(Dict['name'])
"""
#arcore
