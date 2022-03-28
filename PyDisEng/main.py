import tkinter
from tkinter import messagebox
import PIL
import PIL.ImageTk
import PIL.Image
from tkinter import filedialog as fd
root = tkinter.Tk()
root.geometry('800x400+200+150')
root.configure(bg='#222222',)
l = []
ph = []
po = []
def popupmsg(msg=''):
       messagebox.showerror("File canceled",f"file opening was canceled")
def ask():
      global filename
      global po
      global ph
      try:
            filename = fd.askopenfilename(filetypes = [("","*.png")])
            photo = PIL.Image.open(filename)
            p = photo.resize((40,40))
            ph.append(PIL.ImageTk.PhotoImage(p))
            po.append(tkinter.Label())
            for t in range(len(ph)):
                  print(t)
                  po[t]['image'] = ph[t]
                  po[t].pack()
                  po[t].place(x = t*68,y=300)
      except AttributeError:
            popupmsg()
def ask2():
      global filename
      global po
      global ph
      try:
            filename = fd.askopenfilename(filetypes = [("","*.py")])
            photo = PIL.Image.open(filename)
            p = photo.resize((20,20))
            ph.append(PIL.ImageTk.PhotoImage(p))
            po.append(tkinter.Label())
            for t in range(len(ph)):
                  print(t)
                  po[t]['image'] = ph[t]
                  po[t].pack()
                  po[t].place(x = t*29,y=300)
      except AttributeError:
            popupmsg()
def export():
      import os,random
      os.makedirs('folder'+random.randint(0,1000)
      os.makedirs('folder'+random.randint(0,1000)
button = tkinter.Button(bg = '#333333',activebackground='#444444',fg='#ffffff',activeforeground='#ffffff',command = ask)
button2 = tkinter.Button(bg = '#333333',activebackground='#444444',fg='#ffffff',activeforeground='#ffffff',command = ask2)
button3 = tkinter.Button(bg = '#333333',activebackground='#444444',fg='#ffffff',activeforeground='#ffffff',command = export)

button['text'] = '''New sprite

'''

button2['text'] = '''Add Script

'''
button3['text'] = '''Script.export'''
button.pack()
button.place(x=0,y=343)
button2.pack()
button2.place(x=67,y=343)
button3.pack()
button3.place(x=0,y=0)
root.mainloop()

