from tkinter import *

window = Tk()
window.title("AutoClicker")
window.geometry("550x300")
window.configure(bg="#d0e0e3")

text1 = Label(window, text="Auto Clicker",bg="#d0e0e3",fg="#42939f", font="Arial, 36 ")
text2 = Label(window, text="Clicks in second:",bg="#d0e0e3",fg="#42939f", font="Arial, 20 " )

inputs= Entry(window)

button_frame = Frame(window, bg="#d0e0e3")
button_1=Button(button_frame,text="Start",font="Arial, 15 ", bg="#89bf0e", fg="white", width=8, height=1)
button_2=Button(button_frame,text="Stop",font="Arial, 15 ", bg="#c40d0d", fg="white",width=8, height=1)


text1.pack(pady=10)
text2.pack(pady=10)
inputs.pack(pady=10)
button_frame.pack(pady=10)
button_1.pack(side="left", padx=10)
button_2.pack(side="left", padx=10)
window.mainloop()