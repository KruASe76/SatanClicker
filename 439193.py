from tkinter import *
import time, random

window=Tk()
window.geometry('500x500')
window.title('Кликер Сотоны')
window.resizable(False, False)

counter=0

def tap():
    global counter
    counter+=1
    label['text']='ЧТО??? КАК ТЫ ЭТО СДЕЛАЛ????? читер\nПока только 1 попадание, Сатана сделал 100'
    label['font']='arial 17'

def run():
    window.after(400, run)
    button.place(x=random.randint(0, 450), y=random.randint(100, 450))
    
button=Button(window, command=tap, width=4, height=2, bg='#ff0000')

label=Label(text='У тебя не получится\nПока ты ни разу не попал))', font='arial 10')

label.pack()
run()
window.mainloop()