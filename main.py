import sys
import os
import easygui

from PIL import Image, ImageFilter, ImageDraw, ImageFont
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QFileDialog, QSlider


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data\\window.ui', self)
        self.setFixedSize(552, 508) # Фиксация масштаба главного окна (запрет масштабирования)
        self.setWindowIcon(QIcon('data\\icon.ico')) # Иконка приложения
        self.text_status.setReadOnly(True)
        self.take_img_but.clicked.connect(self.take_img)
        self.folder_to_img_but.clicked.connect(self.folder_img)
        self.blur_but.clicked.connect(self.blur)
        self.contour_but.clicked.connect(self.contour)
        self.ee_but.clicked.connect(self.ee)
        self.eem_but.clicked.connect(self.eem)
        self.emboss_but.clicked.connect(self.emboss)
        self.fe_but.clicked.connect(self.fe)
        self.but_quant.clicked.connect(self.quant)
        self.negativ_but.clicked.connect(self.negativ)
        self.but_gaus.clicked.connect(self.gaus)
        self.gbr_but.clicked.connect(self.gbr)
        self.rbg_but.clicked.connect(self.rbg)
        self.pushButton_3.clicked.connect(self.grb)
        self.bgr_but.clicked.connect(self.bgr)
        self.hbi_but.clicked.connect(self.hbe)
        self.remove_filters_but.clicked.connect(self.remove_filters)
        self.inst_but.clicked.connect(self.open_instruction)
        self.open_converter_but.clicked.connect(self.open_converter)
        self.save_img_but.clicked.connect(self.img_save)
        self.chek_result.clicked.connect(self.chek_image)
        self.text_status.setText('Перед началом работы, выберите изображение')
        self.quant_slider.setMinimum(1)
        self.quant_slider.setMaximum(35)
        self.quant_slider.valueChanged.connect(self.slider_quant)
        self.gaus_slider.setMinimum(1)
        self.gaus_slider.setMaximum(35)
        self.gaus_slider.valueChanged.connect(self.slider_gaus)

        self.fname = None
        self.quant_num = 35
        self.gaus_num = 1
        self.img = None

        self.filt = ''


    def img_save(self):
        try:
            self.img.save(self.filt + '_filpic.png')
            self.text_status.setText('Готово, изображение ' + self.filt + ' сохранено в папку')
        except:
            self.text_status.setText('Сначала выберите изображение и наложите фильтр')

    def take_img(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать изображение', '', "*.png *.jpg *.bmp *.webp *.pdf *.gif")[0]
        if self.fname != '':
            self.text_status.setText('Вы выбрали изображение, используйте теперь фильтры')
        else:
            self.text_status.setText('Вы не выбрали изображение, повторите попытку')
            self.fname = None
        self.img = None
    

    def chek_image(self):
        try:
            draw_text = ImageDraw.Draw(self.img)
            self.text_status.setText('Предпросмотр фильтра ' + self.filt)
            self.img.show()
        except:
            self.text_status.setText('Сначала выберите фильтр')
    
    
    def remove_filters(self):
        if self.fname != '' and self.fname != None:
            try:
                self.img = None
                self.text_status.setText('Наложенные фильтры успешно сброшены')
            except:
                self.text_status.setText('Ошибочка вышла :)')
        else:
            self.text_status.setText('Вы не выбрали изображение')


    def folder_img(self):
        dir = os.path.abspath(os.curdir)
        os.system(r"explorer.exe " + dir)

    def slider_quant(self, value):
        self.quant_num = value
        self.res_quant_label.setText(str(value))

    def slider_gaus(self, value):
        self.gaus_num = value
        self.res_gaus_label.setText(str(value))

    def blur(self):
        try:
            if self.fname != '' and self.fname != None:  # Проверка взятия изображение перед использованием функции
                if self.img == None:
                    self.img = Image.open(self.fname)
                self.img = self.img.filter(ImageFilter.BLUR)
                self.filt = 'BLUR'
                self.text_status.setText('Наложен эффект BLUR')
            else:
                self.text_status.setText('Перед использованием BLUR, выберите изображение')
        except:
            self.text_status.setText('BLUR | К QUANT нельзя применять фильтры')

    def contour(self):
        try:
            if self.fname is not None:  # Проверка взятия изображение перед использованием функции
                if self.img == None:
                    self.img = Image.open(self.fname)
                self.img = self.img.filter(ImageFilter.CONTOUR)
                self.filt = 'CONTOUR'
                self.text_status.setText('Наложен эффект CONTOUR')
            else:
                self.text_status.setText('Перед использованием CONTOUR, выберите изображение')
        except:
            self.text_status.setText('CONTOUR | К QUANT нельзя применять фильтры')

    def ee(self):
        try:
            if self.fname is not None:  # Проверка взятия изображение перед использованием функции
                if self.img == None:
                    self.img = Image.open(self.fname)
                self.img = self.img.filter(ImageFilter.EDGE_ENHANCE)
                self.filt = 'EDGE ENHANCE'
                self.text_status.setText('Наложен эффект EDGE ENHANCE')
            else:
                self.text_status.setText('Перед использованием EDGE ENHANCE, выберите изображение')
        except:
            self.text_status.setText('EE | К QUANT нельзя применять фильтры')

    def eem(self):
        try:
            if self.fname is not None:  # Проверка взятия изображение перед использованием функции
                if self.img == None:
                    self.img = Image.open(self.fname)
                self.img = self.img.filter(ImageFilter.EDGE_ENHANCE_MORE)
                self.filt = 'EDGE ENHANCE MORE'
                self.text_status.setText('Наложен эффект EDGE ENHANCE MORE')
            else:
                self.text_status.setText('Перед использованием EEM, выберите изображение')
        except:
            self.text_status.setText('EEM | К QUANT нельзя применять фильтры')

    def emboss(self):
        try:
            if self.fname is not None:
                if self.img == None:
                    self.img = Image.open(self.fname)
                self.img = self.img.filter(ImageFilter.EMBOSS)
                self.filt = 'EMBOSS'
                self.text_status.setText('Наложен эффект EMBOSS')
            else:
                self.text_status.setText('Перед использованием EMBOSS, выберите изображение')
        except:
            self.text_status.setText('EMBOSS | К QUANT нельзя применять фильтры')

    def fe(self):
        try:
            if self.fname is not None:
                if self.img == None:
                    self.img = Image.open(self.fname)
                self.img = self.img.filter(ImageFilter.FIND_EDGES)
                self.filt = 'FIND EDGES'
                self.text_status.setText('Наложен эффект FIND EDGES')
            else:
                self.text_status.setText('Перед использованием FIND EDGES, выберите изображение')
        except:
            self.text_status.setText('FIND EDGES | К QUANT нельзя применять фильтры')

    def quant(self):
        if self.fname is not None:
            if self.img == None:
                self.img = Image.open(self.fname)
            pixels = self.img.load()  # список с пикселями
            x, y = self.img.size  # ширина (x) и высота (y) изображения
            self.img = self.img.quantize(self.quant_num)
            self.filt = 'QUANT'
            self.text_status.setText('Наложен эффект QUANT')
        else:
            self.text_status.setText('Перед использованием QUANT, выберите изображение')

    def negativ(self):
        try:
            if self.fname is not None:
                if self.img == None:
                    self.img = Image.open(self.fname)
                pixels = self.img.load()  # список с пикселями
                x, y = self.img.size  # ширина (x) и высота (y) изображения
                for i in range(x):
                    for j in range(y):
                        r, g, b = pixels[i, j]
                        pixels[i, j] = 255 - r, 255 - g, 255 - b
                self.filt = 'НЕГАТИВ'
                self.text_status.setText('Наложен эффект НЕГАТИВ')
            else:
                self.text_status.setText('Перед использованием НЕГАТИВ, выберите изображение')
        except:
            self.text_status.setText('Негатив | К QUANT нельзя применять фильтры')

    def gaus(self):
        try:
            if self.fname is not None:
                if self.img == None:
                    self.img = Image.open(self.fname)
                self.img = self.img.filter(ImageFilter.GaussianBlur(radius=self.gaus_num))
                self.filt = 'РАЗМЫТИЕ ПО ГАУСУ'
                self.text_status.setText('Наложен эффект РАЗМЫТИЕ ПО ГАУСУ')
            else:
                self.text_status.setText('Перед использованием размытия, выберите изображение')
        except:
            self.text_status.setText('ГАУС | К QUANT нельзя применять фильтры')

    def gbr(self):
        try:
            if self.fname is not None:
                if self.img == None:
                    self.img = Image.open(self.fname)
                pixels = self.img.load()  # список с пикселями
                x, y = self.img.size  # ширина (x) и высота (y) изображения
                for i in range(x):
                    for j in range(y):
                        r, g, b = pixels[i, j]
                        pixels[i, j] = g, b, r
                self.filt = 'GBR'
                self.text_status.setText('Наложен эффект GBR')
            else:
                self.text_status.setText('Перед использованием GBR, выберите изображение')
        except:
            self.text_status.setText('GBR | К QUANT нельзя применять фильтры')

    def rbg(self):
        try:
            if self.fname is not None:
                if self.img == None:
                    self.img = Image.open(self.fname)
                pixels = self.img.load()  # список с пикселями
                x, y = self.img.size  # ширина (x) и высота (y) изображения
                for i in range(x):
                    for j in range(y):
                        r, g, b = pixels[i, j]
                        pixels[i, j] = r, b, g
                self.filt = 'RBG'
                self.text_status.setText('Наложен эффект RBG')
            else:
                self.text_status.setText('Перед использованием RBG, выберите изображение')
        except:
            self.text_status.setText('RGB | К QUANT нельзя применять фильтры')

    def grb(self):
        try:
            if self.fname is not None:
                if self.img == None:
                    self.img = Image.open(self.fname)
                pixels = self.img.load()  # список с пикселями
                x, y = self.img.size  # ширина (x) и высота (y) изображения
                for i in range(x):
                    for j in range(y):
                        r, g, b = pixels[i, j]
                        pixels[i, j] = g, r, b
                self.filt = 'GRB'
                self.text_status.setText('Наложен эффект GRB')
            else:
                self.text_status.setText('Перед использованием GRB, выберите изображение')
        except:
            self.text_status.setText('GRB | К QUANT нельзя применять фильтры')

    def bgr(self):
        try:
            if self.fname is not None:
                if self.img == None:
                    self.img = Image.open(self.fname)
                pixels = self.img.load()  # список с пикселями
                x, y = self.img.size  # ширина (x) и высота (y) изображения
                for i in range(x):
                    for j in range(y):
                        r, g, b = pixels[i, j]
                        pixels[i, j] = b, g, r
                self.filt = 'BGR'
                self.text_status.setText('Наложен эффект BGR')
            else:
                self.text_status.setText('Перед использованием BGR, выберите изображение')
        except:
            self.text_status.setText('BGR | К QUANT нельзя применять фильтры')

    def hbe(self):
        try:
            if self.fname is not None:
                if self.img == None:
                    self.img = Image.open(self.fname)
                pixels = self.img.load()  # список с пикселями
                x, y = self.img.size  # ширина (x) и высота (y) изображения
                for i in range(x):
                    for j in range(y):
                        r, g, b = pixels[i, j]
                        bw = (r + g + b) // 3
                        pixels[i, j] = bw, bw, bw
                self.filt = 'ЧБИ'
                self.text_status.setText('Наложен эффект ЧБИ')
            else:
                self.text_status.setText('Перед наложением чёрно белого эффекта, выберите файл')
        except:
            self.text_status.setText('ЧБИ | К QUANT нельзя применять фильтры')

    def open_converter(self):
        self.second_form = SecondForm(self, "Данные для второй формы")
        self.second_form.show()

    def open_instruction(self):
        self.third_form = ThirdForm(self, "Данные для второй формы")
        self.third_form.show()


class ThirdForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('data\\instruction.ui', self)
        self.setFixedSize(522, 385) # Фиксация масштаба главного окна (запрет масштабирования)
        self.setWindowIcon(QIcon('data\\icon.ico')) # Иконка приложения
        self.plainTextEdit.appendPlainText('''КРАТКАЯ ИНСТРУКЦИЯ ПО ИСПОЛЬЗОВАНИЮ ФОТОРЕДАКТОРА:
Перед началом работы с фильтрами - требуется выбрать изображение при помощи кнопки "Открыть файл" в верхнем левом углу окна. После можно выбирать фильтры, нажимая на кнопки с их наименованием. Фильтры "QUANT" и "Размытие по гаусу" немного отличаются от остальных, их степень применения выбирает сам пользователь при помощи ползунка, после выбора значение (установки значения при помощи ползунка) требуется нажать кнопку "Применить уровень" справа от ползунка.

После выбора фильтра - можно перейти сразу к сохранению результата при помощи кнопки "Сохранить изображение" или сначала сделать предварительный просмотр результата при помощи кнопки "Предпросмотр наложенного фильтра".

После сохранения - все сохранённые изображения будут хранится в специальной папке, открыть которую можно при помощи кнопки "Открыть папку с изображениями".


КРАТКАЯ ИНСТРУКЦИЯ ПО ИСПОЛЬЗОВАНИЮ КОНВЕРТЕРА
Что бы открыть конвертер - требуется нажать на верхнюю кнопку "Открыть конвертер".
При помощи встроенного конвертера можно:
- конвертировать (преобразовывать) изображение или сразу группу изображений в различные форматы (такие как: .png, .jpg, .pdf и д.р.)
- сжимать изображение или сразу группу изображений в различные разрешения (такие как: 720p, 480p, 360p и д.р.)

Работа с конвертером - аналогична работе с фоторедактором.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ИНФОРМАЦИЯ ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ

Название программы - FilPic
Текущая версия программы: V2.2-FULL

Разработчик(и):
- Матвей Воронцов (Ведущий программист | FullStack)

Технологии используемые при разработке:
- Язык программирования: Python 3.7.8 x86
- PyQt5 для GUI
- Pillow (PIL)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ИЗМЕНЕНИЯ С НОВЫМИ ОБНОВЛЕНИЯМИ:

~~~ V2.2-FULL:
* Исправление орфографических ошибок
* Исправление багов (ошибок) в работе программы
    - была добавлена опция в исполняемый .exe файл программы для запроса прав администратора, это нужно для корректной работы программы

~~~ V2.1-FULL:
* Доработан графический интерфейс
    - стили на кнопки
    - добавление иконки программы на окно
    - и д.р.

* Перероботка содержимого окна "Справка"
    - изменён текст инструкций под новую версию программы

* Меры по борьбе с кражей и взломом программы
    - в коде программы было внесено изменение по отображению содержимого окна "Справка", теперь возможность подделать содержимое данного окна сводится к минимуму

~~~ V2.0-FULL:
* Переработка работы программы
    - было удалено окно "Информация о приложении" с последующем переносом его содержимого в раздел "Справка"
    - переработка системы предварительного осмотра фильтров. Теперь для предосмотра требуется нажать после применения фильтра кнопку "Предосмотр наложенного фильтра"
    - устранение лексических и орфографических ошибок в тексте статус бара

* Полное удаление из кода и файлов программы системы баз данных по причине ненадобности
        ''')
        self.plainTextEdit.setReadOnly(True)


class SecondForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('data\\converter.ui', self)
        self.setFixedSize(482, 365) # Фиксация масштаба главного окна (запрет масштабирования)
        self.setWindowIcon(QIcon('data\\icon.ico')) # Иконка приложения
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setText('Перед началом работы, выберите изображения')
        self.pushButton.clicked.connect(self.img_folder)
        self.more_imgs_but.clicked.connect(self.img_more)
        self.png_but.clicked.connect(self.png)
        self.jpg_but.clicked.connect(self.jpg)
        self.bmp_but.clicked.connect(self.bmp)
        self.pdf_but.clicked.connect(self.pdf)
        self.webp_but.clicked.connect(self.webp)
        self.ultrahd_but.clicked.connect(self.ultra_hd)
        self.fullhd_but.clicked.connect(self.full_hd)
        self.hd_but.clicked.connect(self.hd)
        self.p480_but.clicked.connect(self.p480)
        self.p360_but.clicked.connect(self.p360)
        self.p240_but.clicked.connect(self.p240)
        self.input_file = None

    def img_more(self):
        self.input_file = easygui.fileopenbox(filetypes=["*.png"], multiple=True)
        if self.input_file is not None:
            self.lineEdit.setText('Изображения выбраны, используйте конвертер')
            self.stat = 1
        else:
            self.lineEdit.setText('Изображения не выбраны, повторите попытку')

    def img_folder(self):
        dir = os.path.abspath(os.curdir)
        os.system(r"explorer.exe " + dir)

    def png(self):
        try:
            if self.input_file is not None:
                num = 1
                for i in self.input_file:
                    img = Image.open(i)
                    result = (str(num) + 'PNG_ConPic.png')
                    img.save(result)
                    num += 1

                self.lineEdit.setText('Готово, .PNG изображения сохранено в папку')
            else:
                self.lineEdit.setText('Перед использованием PNG, выберите картинки')
        except:
            self.lineEdit.setText('Ошибка | PNG | Выберите другой файл')

    def jpg(self):
        try:
            if self.input_file is not None:
                num = 1
                for i in self.input_file:
                    img = Image.open(i)
                    result = (str(num) + 'JPG_ConPic.jpg')
                    img.save(result)
                    num += 1

                self.lineEdit.setText('Готово, .JPG изображения сохранено в папку')
            else:
                self.lineEdit.setText('Перед использованием JPG, выберите картинки')
        except:
            self.lineEdit.setText('Ошибка | JPG | Выберите другой файл')

    def bmp(self):
        try:
            if self.input_file is not None:
                num = 1
                for i in self.input_file:
                    img = Image.open(i)
                    result = (str(num) + 'BMP_ConPic.bmp')
                    img.save(result)
                    num += 1

                self.lineEdit.setText('Готово, .BMP изображения сохранено в папку')
            else:
                self.lineEdit.setText('Перед использованием BMP, выберите картинки')
        except:
            self.lineEdit.setText('Ошибка | BMP | Выберите другой файл')


    def pdf(self):
        try:
            if self.input_file is not None:
                num = 1
                for i in self.input_file:
                    img = Image.open(i)
                    result = (str(num) + 'PDF_ConPic.pdf')
                    img.save(result)
                    num += 1

                self.lineEdit.setText('Готово, .PDF изображения сохранено в папку')
            else:
                self.lineEdit.setText('Перед использованием PDF, выберите картинки')
        except:
            self.lineEdit.setText('Ошибка | PDF | Выберите другой файл')

    def webp(self):
        try:
            if self.input_file is not None:
                num = 1
                for i in self.input_file:
                    img = Image.open(i)
                    result = (str(num) + 'WebP_ConPic.webp')
                    img.save(result)
                    num += 1

                self.lineEdit.setText('Готово, .WebP изображения сохранено в папку')
            else:
                self.lineEdit.setText('Перед использованием WebP, выберите картинки')
        except:
            self.lineEdit.setText('Ошибка | WebP | Выберите другой файл')

    def ultra_hd(self):
        try:
            if self.input_file is not None:
                num = 1
                for i in self.input_file:
                    img = Image.open(i)
                    img.thumbnail((3840, 2160))
                    result = (str(num) + '_ULTRA_HD_ConPic.' + i.split('.')[-1])
                    img.save(result)
                    num += 1

                self.lineEdit.setText('Готово, 4K изображения сохранено в папку')
            else:
                self.lineEdit.setText('Перед использованием 4K, выберите картинки')
        except:
            self.lineEdit.setText('Ошибка | 4K | Выберите другой файл')

    def full_hd(self):
        try:
            if self.input_file is not None:
                num = 1
                for i in self.input_file:
                    img = Image.open(i)
                    img.thumbnail((1920, 1080))
                    result = (str(num) + '_FULL_HD_ConPic.' + i.split('.')[-1])
                    img.save(result)
                    num += 1

                self.lineEdit.setText('Готово, 1080p изображения сохранено в папку')
            else:
                self.lineEdit.setText('Перед использованием FULL HD, выберите картинки')
        except:
            self.lineEdit.setText('Ошибка | 1080p | Выберите другой файл')

    def hd(self):
        try:
            if self.input_file is not None:
                num = 1
                for i in self.input_file:
                    img = Image.open(i)
                    img.thumbnail((1280, 720))
                    result = (str(num) + '_HD_ConPic.' + i.split('.')[-1])
                    img.save(result)
                    num += 1

                self.lineEdit.setText('Готово, 720p изображения сохранено в папку')
            else:
                self.lineEdit.setText('Перед использованием HD, выберите картинки')
        except:
            self.lineEdit.setText('Ошибка | 720p | Выберите другой файл')

    def p480(self):
        try:
            if self.input_file is not None:
                num = 1
                for i in self.input_file:
                    img = Image.open(i)
                    img.thumbnail((854, 480))
                    result = (str(num) + '_480p_ConPic.' + i.split('.')[-1])
                    img.save(result)
                    num += 1

                self.lineEdit.setText('Готово, 480p изображения сохранено в папку')
            else:
                self.lineEdit.setText('Перед использованием 480p, выберите картинки')
        except:
            self.lineEdit.setText('Ошибка | 480p | Выберите другой файл')

    def p360(self):
        try:
            if self.input_file is not None:
                num = 1
                for i in self.input_file:
                    img = Image.open(i)
                    img.thumbnail((480, 360))
                    result = (str(num) + '_360p_ConPic.' + i.split('.')[-1])
                    img.save(result)
                    num += 1

                self.lineEdit.setText('Готово, 360p изображения сохранено в папку')
            else:
                self.lineEdit.setText('Перед использованием 360p, выберите картинки')
        except:
            self.lineEdit.setText('Ошибка | 360p | Выберите другой файл')

    def p240(self):
        try:
            if self.input_file is not None:
                num = 1
                for i in self.input_file:
                    img = Image.open(i)
                    img.thumbnail((320, 240))
                    result = (str(num) + '_240p_ConPic.' + i.split('.')[-1])
                    img.save(result)
                    num += 1

                self.lineEdit.setText('Готово, 240p изображения сохранено в папку')
            else:
                self.lineEdit.setText('Перед использованием 240p, выберите картинки')
        except:
            self.lineEdit.setText('Ошибка | 240p | Выберите другой файл')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
