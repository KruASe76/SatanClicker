from tkinter import *
import time, random

window=Tk()
window.geometry('500x500')
window.title('Кликер Сотоны')
window.resizable(False, False)

counter=0

def close():
    global counter
    if counter>=100:
        window.quit()
        print('Вы приняты на работу в ад! Поздравляем!')
def tap():
    global counter
    counter+=1
    if (str(counter))[-1]=='1':
        label['text']=f'ЧТО??? КАК ТЫ ЭТО СДЕЛАЛ????? читер\nПока только {counter} попадание, Сатана сделал 100'
    elif (str(counter))[-1]=='2' or (str(counter))[-1]=='3' or (str(counter))[-1]=='4':
        label['text']=f'ЧТО??? КАК ТЫ ЭТО СДЕЛАЛ????? читер\nПока только {counter} попадания, Сатана сделал 100'
    else:
        label['text']=f'ЧТО??? КАК ТЫ ЭТО СДЕЛАЛ????? читер\nПока только {counter} попаданий, Сатана сделал 100'
    label['font']='arial 17'
    close()

def run():
    window.after(400, run)
    button.place(x=random.randint(0, 450), y=random.randint(100, 450))
    
button=Button(window, command=tap, text='Ӹ', font='arial 10', width=4, height=2, bg='#ff0000')

label=Label(text='У тебя не получится\nПока ты ни разу не попал))', font='arial 10')

label.pack()
run()
window.mainloop()
