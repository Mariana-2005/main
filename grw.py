from customtkinter import *
import os
from PIL import Image

#функція
def z():
    e = (entry.get())
    if e.strip():
        with open("C:/Users/user/Desktop/notes.txt", "a", encoding="utf-8") as f:
            f.write(e + "\n")
        entry.delete(0, "end")

#вікно
set_appearance_mode("dark")
set_default_color_theme("green")
w = CTk()
w.title("Notes")
w.geometry("550x500")

#зображення
i1 = CTkImage(light_image=Image.open("883f483943eaed5549e43c88af0129f9.jpg"),
               dark_image=Image.open("883f483943eaed5549e43c88af0129f9.jpg"),size=(300,150))
b = CTkLabel(w, image=i1, text="")
b.pack(side="bottom", pady=50)

#рамки
rframe = CTkFrame(w, corner_radius=19, fg_color="#2b2b2b")
rframe.pack(pady=10, padx=230, fill="both")
rframe1 = CTkFrame(w, corner_radius=19, fg_color="#2b2b2b")
rframe1.pack(pady=10, padx=170, fill="both")

#текст
label = CTkLabel(rframe, text="Notes", font=("Georgia", 25), text_color="#8ea682")
label.pack(pady=10)
label1 = CTkLabel(rframe1, text="Next open your Desktop", font=("Georgia", 15))
label1.pack(pady=5)

#ввод
entry = CTkEntry(w, placeholder_text="Write something:", border_color="black")
entry.pack(pady=20)

#кнопка сейву
save_button = CTkButton(w, text="Save to file", command=z, fg_color="#8ea682", hover_color="#586452", width=100, height=50)
save_button.pack(pady=10)

w.mainloop()