from tkinter import *
from PIL import Image, ImageFilter
import os, time, webbrowser, easygui, subprocess


def input_img():
    global input_file
    input_file = easygui.fileopenbox(filetypes=["*.png"])

    win = Tk()
    win.geometry('700x5')
    win.resizable(width=False, height=False)
    win.title('Изображение выбрано, можно закрыть данное окно, теперь можете выбирать фильтры')

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


def cont_our():
    img = Image.open(input_file)
    img = img.filter(ImageFilter.CONTOUR)
    img.show()

    img.save('saved_filpic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - saved_filpic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def get_ail():
    img = Image.open(input_file)
    img = img.filter(ImageFilter.DETAIL)
    img.show()

    img.save('saved_filpic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - saved_filpic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def edge_en_ha_nce():
    img = Image.open(input_file)
    img = img.filter(ImageFilter.EDGE_ENHANCE)
    img.show()

    img.save('saved_filpic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - saved_filpic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def edge_en_ha_nce_more():
    img = Image.open(input_file)
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    img.show()

    img.save('saved_filpic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - saved_filpic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def emb_oss():
    img = Image.open(input_file)
    img = img.filter(ImageFilter.EMBOSS)
    img.show()

    img.save('saved_filpic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - saved_filpic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def fi_ng_ed_ges():
    img = Image.open(input_file)
    img = img.filter(ImageFilter.FIND_EDGES)
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
blur.place(x=2, y=55)

contour = Button(root, text='CONTOUR')
contour.config(width=18, height=2, bg='white', command=cont_our)
contour.place(x=182, y=55)

detail = Button(root, text='DETAIL')
detail.config(width=18, height=2, bg='white', command=get_ail)
detail.place(x=362, y=55)

edge_enhance = Button(root, text='EDGE ENHANCE')
edge_enhance.config(width=18, height=2, bg='white', command=edge_en_ha_nce)
edge_enhance.place(x=2, y=105)

edge_enhance_more = Button(root, text='EDGE ENHANCE MORE')
edge_enhance_more.config(width=18, height=2, bg='white', command=edge_en_ha_nce_more)
edge_enhance_more.place(x=182, y=105)

emboss = Button(root, text='EMBOSS')
emboss.config(width=18, height=2, bg='white', command=emb_oss)
emboss.place(x=362, y=105)

find_edges = Button(root, text='FIND EDGES')
find_edges.config(width=18, height=2, bg='white', command=fi_ng_ed_ges)
find_edges.place(x=2, y=155)

root.mainloop()
