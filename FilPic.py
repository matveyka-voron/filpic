from tkinter import *
from PIL import Image, ImageFilter
import os, webbrowser, easygui


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

    img.save('BLUR_filpic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - BLUR_filpic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def cont_our():
    img = Image.open(input_file)
    img = img.filter(ImageFilter.CONTOUR)
    img.show()

    img.save('CONTOUR_filpic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - CONTOUR_filpic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def get_ail():
    img = Image.open(input_file)
    img = img.filter(ImageFilter.DETAIL)
    img.show()

    img.save('DETAIL_filpic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - DETAIL_filpic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def edge_en_ha_nce():
    img = Image.open(input_file)
    img = img.filter(ImageFilter.EDGE_ENHANCE)
    img.show()

    img.save('EDGE_ENHANCE_filpic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - EDGE_ENHANCE_filpic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def edge_en_ha_nce_more():
    img = Image.open(input_file)
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    img.show()

    img.save('EDGE_ENHANCE_MORE_filpic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - EDGE_ENHANCE_MORE_filpic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def emb_oss():
    img = Image.open(input_file)
    img = img.filter(ImageFilter.EMBOSS)
    img.show()

    img.save('EMBOSS_filpic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - EMBOSS_filpic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def fi_ng_ed_ges():
    img = Image.open(input_file)
    img = img.filter(ImageFilter.FIND_EDGES)
    img.show()

    img.save('FIND_EDGES_filpic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - FIND_EDGES_filpic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def smo_oth():
    img = Image.open(input_file)
    img = img.filter(ImageFilter.SMOOTH)
    img.show()

    img.save('SMOOTH_filpic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - SMOOTH_filpic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def smo_oth_more():
    img = Image.open(input_file)
    img = img.filter(ImageFilter.SMOOTH_MORE)
    img.show()

    img.save('SMOOTH_MORE_filpic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - SMOOTH_MORE_filpic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def sh_ar_pen():
    img = Image.open(input_file)
    img = img.filter(ImageFilter.SHARPEN)
    img.show()

    img.save('SHARPEN_filpic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - SHARPEN_filpic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def g_b_r():
    img = Image.open(input_file)
    pixels = img.load()  # список с пикселями
    x, y = img.size  # ширина (x) и высота (y) изображения

    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            pixels[i, j] = g, b, r

    img.show()

    img.save('GBR_filpic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - GBR_filpic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def r_b_g():
    img = Image.open(input_file)
    pixels = img.load()  # список с пикселями
    x, y = img.size  # ширина (x) и высота (y) изображения

    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            pixels[i, j] = r, b, g

    img.show()

    img.save('RBG_filpic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - RBG_filpic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def g_r_b():
    img = Image.open(input_file)
    pixels = img.load()  # список с пикселями
    x, y = img.size  # ширина (x) и высота (y) изображения

    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            pixels[i, j] = g, r, b

    img.show()

    img.save('GRB_filpic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - GRB_filpic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def b_g_r():
    img = Image.open(input_file)
    pixels = img.load()  # список с пикселями
    x, y = img.size  # ширина (x) и высота (y) изображения

    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            pixels[i, j] = b, g, r

    img.show()

    img.save('BGR_filpic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - BGR_filpic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def h_b_e():
    img = Image.open(input_file)
    pixels = img.load()  # список с пикселями
    x, y = img.size  # ширина (x) и высота (y) изображения

    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            bw = (r + g + b) // 3
            pixels[i, j] = bw, bw, bw

    img.show()

    img.save('HBE_filpic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - HBE_filpic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def n_e_g():
    img = Image.open(input_file)
    pixels = img.load()  # список с пикселями
    x, y = img.size  # ширина (x) и высота (y) изображения

    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            pixels[i, j] = 255 - r, 255 - g, 255 - b

    img.show()

    img.save('NEG_filpic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - NEG_filpic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def v_s():
    img = Image.open(input_file)
    pixels = img.load()  # список с пикселями
    x, y = img.size  # ширина (x) и высота (y) изображения

    img = img.quantize(19)

    img.show()

    img.save('QUANT_filpic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - QUANT_filpic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def g_b_l():
    img = Image.open(input_file)
    pixels = img.load()  # список с пикселями
    x, y = img.size  # ширина (x) и высота (y) изображения

    img = img.filter(ImageFilter.GaussianBlur(radius=7))

    img.show()

    img.save('GBL_filpic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - GBL_filpic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def u_r_l():
    webbrowser.open('https://vk.com/serv_studio')


root = Tk()
root.config(bg='lavender')
root.geometry('500x425')
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

smooth = Button(root, text='SMOOTH')
smooth.config(width=18, height=2, bg='white', command=smo_oth)
smooth.place(x=182, y=155)

smooth_more = Button(root, text='SMOOTH MORE')
smooth_more.config(width=18, height=2, bg='white', command=smo_oth_more)
smooth_more.place(x=362, y=155)

sharpen = Button(root, text='SHARPEN')
sharpen.config(width=18, height=2, bg='white', command=sh_ar_pen)
sharpen.place(x=2, y=205)

gb_r = Button(root, text='GBR')
gb_r.config(width=18, height=2, bg='white', command=g_b_r)
gb_r.place(x=182, y=205)

rb_g = Button(root, text='RBG')
rb_g.config(width=18, height=2, bg='white', command=r_b_g)
rb_g.place(x=362, y=205)

gr_b = Button(root, text='GRB')
gr_b.config(width=18, height=2, bg='white', command=g_r_b)
gr_b.place(x=2, y=255)

bg_r = Button(root, text='BGR')
bg_r.config(width=18, height=2, bg='white', command=b_g_r)
bg_r.place(x=182, y=255)

hb = Button(root, text='ЧБИ')
hb.config(width=18, height=2, bg='white', command=h_b_e)
hb.place(x=362, y=255)

fl = Button(root, text='Негатив')
fl.config(width=18, height=2, bg='white', command=n_e_g)
fl.place(x=2, y=305)

vs = Button(root, text='QUANT')
vs.config(width=18, height=2, bg='white', command=v_s)
vs.place(x=182, y=305)

gb_l = Button(root, text='Размытие')
gb_l.config(width=18, height=2, bg='white', command=g_b_l)
gb_l.place(x=362, y=305)

url = Button(root, text='Страница разработчика')
url.config(width=20, height=1, bg='white', command=u_r_l)
url.place(x=1, y=400)

info = Label(root, text='Создано: Матвей Воронцов | Service Studio', fg='gray', bg='lavender')
info.config(font=('Arial', 9))
info.place(x=250, y=405)

root.mainloop()
