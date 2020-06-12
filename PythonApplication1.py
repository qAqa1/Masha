from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Radiobutton
import random as rdm

import numpy as np
from PIL import Image, ImageTk
import sys


class Main(Frame):
    def __init__(self, main, name, bg_hex):
        super().__init__()
        self.name = name
        self.main = main
        self.startUI(name, bg_hex)

    def startUI(self, name, bg_hex):

        orig_color = (255, 255, 255, 255)
        replacement_color = (250, 0, 255, 255)
        img = Image.open("images\\rock.png").convert('RGBA')
        data = np.array(img)
        data[(data == orig_color).all(axis=-1)] = replacement_color
        img2 = Image.fromarray(data, mode='RGBA')
        img2.show()

        def create_game_button(image, click_value, x, width, y=200, height=120):
            btn = Button(root_start, image=image,
                         command=lambda x=click_value: self.btn_click(x))
            btn.image = image
            btn.place(x=x, y=y, width=width, height=height)

        image = Image.open("images/rock.png")
        photo = ImageTk.PhotoImage(img2)
        create_game_button(photo, 1, 30, 125)

        image = Image.open("images/scissors.png")
        photo = ImageTk.PhotoImage(image)
        create_game_button(photo, 2, 170, 168)

        image = Image.open("images/paper.png")
        photo = ImageTk.PhotoImage(image)
        create_game_button(photo, 3, 350, 116)

        # img = Image.open(sys.argv[1])
        # img = img.convert("RGBA")
        # pixdata = img.load()
        #
        # for y in range(img.size[1]):
        #     for x in range(img.size[0]):
        #         if pixdata[x, y] == (255, 255, 255, 255):
        #             pixdata[x, y] = (0, 0, 0, 255)
        #
        # pixdata.save('test.png')




        self.lbl = Label(root_start, text="Привет, " + name + "!",
                         font=("Times New Roman", 22, "bold"), bg=bg_hex)

        self.lbl.place(x=160, y=25)

        self.win = self.drow = self.lose = 0

        self.lbl2 = Label(root_start, justify="left", font=("Times New Roman", 14),
                          text=f"Побед: {self.win}\nПроигрышей:"f" {self.lose}\nНичей: {self.drow}", bg=bg_hex)
        self.lbl2.place(x=190, y=100)

    def btn_click(self, choise):
        comp_choise = rdm.randint(1, 3)

        if choise == comp_choise:
            self.drow += 1
            self.lbl.configure(text="Ничья")
        elif choise == 1 and comp_choise == 2 \
                or choise == 2 and comp_choise == 3 \
                or choise == 3 and comp_choise == 1:
            self.win += 1
            self.lbl.configure(text="Победа")

            if self.win == 2:
                root_start.withdraw()
                while True:
                    messagebox.showerror('Внимание', self.name + ', Ваш компьютер и вы заражены коронавирусом\n'
                                                     'Отправьте деньги на этот номер, чтобы получить вакцину\n'
                                                     '8 800 555 35 35')

        else:
            self.lose += 1
            self.lbl.configure(text="Проигрыш")

        self.lbl2.configure(text=f"Побед: {self.win}\nПроигрышей:"f" {self.lose}\nНичей: {self.drow}")

        del comp_choise


class Hello(Frame):

    def __init__(self, main):
        super().__init__()
        self.main = main
        self.helloUI()

    def helloUI(self):
        self.inputNameTextBox = Text(root_hello, width=11, height=1, font=("Times New Roman", 14), wrap="none")
        self.inputNameTextBox.place(x=170, y=30)

        self.lbl3 = Label(root_hello, text="Имя", font=("Times New Roman", 14))
        self.lbl3.place(x=130, y=30)

        self.lbl4 = Label(root_hello, text="Пол", font=("Times New Roman", 14))
        self.lbl4.place(x=130, y=70)

        self.lbl5 = Label(root_hello, text="Цвет", font=("Times New Roman", 14))
        self.lbl5.place(x=127, y=110)

        self.lbl6 = Label(root_hello, text="Уровень сложности:", font=("Times New Roman", 14))
        self.lbl6.place(x=130, y=150)

        combo = Combobox(root_hello, font=("Times New Roman", 12))
        combo1 = Combobox(root_hello, font=("Times New Roman", 12))
        combo['values'] = ("женщина", "мужчина")
        combo1['values'] = ("розовый", "голубой", "жёлтый")
        combo.current(1)
        combo1.current(1)
        combo.grid(column=0, row=0)
        combo1.grid(column=0, row=0)
        combo.place(x=170, y=72, width=100, height=25)
        combo1.place(x=170, y=112, width=100, height=25)

        chk = Radiobutton(root_hello, text='1', value=1)
        chk1 = Radiobutton(root_hello, text='2', value=2)
        chk2 = Radiobutton(root_hello, text='3', value=3)
        chk.grid(column=0, row=0)
        chk1.grid(column=1, row=0)
        chk2.grid(column=2, row=0)
        chk.place(x=130, y=180, width=30, height=30)
        chk1.place(x=200, y=180, width=30, height=30)
        chk2.place(x=270, y=180, width=30, height=30)

        def startGame_click():
            input_text = self.inputNameTextBox.get(1.0, END).replace('\n', '')
            if input_text == '':
                return

            color = combo1.get()

            bg_hex = None

            if color == "розовый":
                bg_hex = "#ffc0cb"

            if color == "голубой":
                bg_hex = "#42aaff"

            if color == "жёлтый":
                bg_hex = "#ffff00"

            root_start["bg"] = bg_hex

            root_hello.withdraw()

            root_start.deiconify()

            app_start = Main(root_start, input_text, bg_hex)
            app_start.pack()
            app_start.mainloop()

        btn4 = Button(root_hello, text="Поехали", font=("Times New Roman", 15), command=startGame_click)
        btn4.place(x=160, y=220, width=100, height=30)


def on_closing():
    root_hello.destroy()
    root_start.destroy()


if __name__ == '__main__':
    root_start = Tk()
    root_start.withdraw()
    root_start.protocol("WM_DELETE_WINDOW", on_closing)
    root_start.iconbitmap("py.ico")
    root_start.geometry("500x350+200+200")
    root_start.title("Игра началась...")
    root_start.resizable(False, False)

    root_hello = Tk()
    root_hello.iconbitmap("py1.ico")
    root_hello.geometry("400x270+200+200")
    root_hello.title("Приветствие")
    root_hello.resizable(False, False)

    app_hello = Hello(root_hello)
    app_hello.pack()
    app_hello.mainloop()