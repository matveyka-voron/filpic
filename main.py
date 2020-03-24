from tkinter import *
from PIL import Image, ImageFilter
import os, time, webbrowser, easygui, subprocess


def input_img():
    global input_file
    input_file = easygui.fileopenbox(filetypes=["*.docx"])

    win = Tk()
    win.geometry('500x5')
    win.resizable(width=False, height=False)
    win.title('Изображение выбрано, можно закрыть данное окно')

    win.mainloop()


def bl_ur():
    img = Image.open(input_file)
    img = img.filter(ImageFilter.BLUR)
    img.show()

    img.save('saved_filpic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - saved_filpic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()

root = Tk()
root.config(bg='lavender')
root.geometry('500x400')
root.title('FilPic')
root.resizable(width=False, height=False)
root.iconbitmap('data\\icon.ico')


inpF = Button(root, text='Выбрать изображение (.png, .jpg и д.р.)')
inpF.config(width=55, height=2, bg='white smoke', command=input_img)
inpF.pack()

blur = Button(root, text='BLUR')
blur.config(width=18, height=2, bg='white', command=bl_ur)
blur.place(x=10, y=80)

root.mainloop()
