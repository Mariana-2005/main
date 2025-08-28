from customtkinter import *
from tkinter import *

#ФУНКЦІЇ ДЛЯ ТЕМ
def light():
    w.config(bg="#f7e9da")
    display.configure(bg_color="#f7e9da",fg_color="#fff8f1")
    frame.configure(bg_color="#f7e9da", fg_color="#f7e9da")
    for b in buttons_list:
        b.configure(fg_color="#fff8f1", hover_color="#e1d5c8", text_color="#c1a384")
def dark():
    w.config(bg="#444444")
    display.configure(bg_color="#444444", fg_color="#bcbcbc")
    frame.configure(bg_color="#444444", fg_color="#444444")
    for b in buttons_list:
        b.configure(fg_color="#bcbcbc", hover_color="#999999", text_color="#292929")
def pink():
    w.config(bg="#f4cccc")
    display.configure(bg_color="#f4cccc", fg_color="#fae5e5")
    frame.configure(bg_color="#f4cccc", fg_color="#f4cccc")
    for b in buttons_list:
        b.configure(fg_color="#fae5e5", hover_color="#efd1d1", text_color="#d79999")
def green():
    w.config(bg="#6aa84f")
    display.configure(bg_color="#6aa84f", fg_color="#b6d7a8")
    frame.configure(bg_color="#6aa84f", fg_color="#6aa84f")
    for b in buttons_list:
        b.configure(fg_color="#b6d7a8", hover_color="#8faf81", text_color="#669b4e")
def red():
    w.config(bg="#c63838")
    display.configure(bg_color="#c63838", fg_color="#e16d6d")
    frame.configure(bg_color="#c63838", fg_color="#c63838")
    for b in buttons_list:
        b.configure(fg_color="#e16d6d", hover_color="#c76767", text_color="#ac3939")
def blue():
    w.config(bg="#6fa8dc")
    display.configure(bg_color="#6fa8dc", fg_color="#cfe2f3")
    frame.configure(bg_color="#6fa8dc", fg_color="#6fa8dc")
    for b in buttons_list:
        b.configure(fg_color="#cfe2f3", hover_color="#95b2cc", text_color="#527ea6")


w = CTk()
w.title("Калькулятор")
w.geometry("400x350")

display = CTkTextbox(w, height=50, corner_radius=10, font=("Arial", 20))
display.pack(side="top", padx=10, pady=20, fill="x")

frame = CTkFrame(w, width=100, height=200)
frame.pack(pady=20)

#ТЕМИ
menubar = Menu(w)
menu= Menu(w, tearoff=0)
menu.add_command(label="Light", command=light)
menu.add_command(label="Dark", command=dark)
menu.add_command(label="Pink", command=pink)
menu.add_command(label="Green", command=green)
menu.add_command(label="Red", command=red)
menu.add_command(label="Blue", command=blue)
menubar.add_cascade(label="Theme", menu=menu)

#ВИХІД
menu1 = Menu(w, tearoff=0)
menu1.add_command(label="Exit", command=w.destroy)
menubar.add_cascade(label="Exit", menu=menu1)

w.config(menu=menubar)

#КНОПКИ
buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2),("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2),("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2),("-", 2, 3),
    ("C",3, 0), ("0", 3, 1), ("=", 3, 2), ("+", 3, 3)
]

buttons_list = []

for text, row, col in buttons:
    btn = CTkButton(frame, text=text, width=60, height=40, font=("Arial", 14, "bold"))
    btn.grid(row=row, column=col, padx=5, pady=5)
    buttons_list.append(btn)

w.mainloop()