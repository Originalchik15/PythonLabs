'''
Требуется для своего варианта второй части л.р. №6 (усложненной программы) разработать реализацию с использованием графического интерфейса.
Допускается использовать любую графическую библиотеку питона. 
Рекомендуется использовать внутреннюю библиотеку питона  tkinter.
'''
from tkinter import *
from itertools import permutations

def var1h(elements, l):
    el = list(map(lambda e: e, elements))
    return list(permutations(el, l))

def sm(perm):
    return sum(int(d) for d in perm if d.isdigit())

def clear():
    entry1.delete(0,END)
def display():
    label["text"] = entry1.get()

def validsim():  
    try:
        K = int(entry1.get())
        T = int(entry2.get())
        L = int(entry4.get())
        P = str(entry3.get())
        
        if L > K or T > K:
            errorlable.config(text="Введены неверные числа")
            return 
             
        if len(P) == K and len(set(P)) == K and P[:T].isalpha() and any(d.isdigit() for d in P[T:]):
            errorlable.config(text=f"Пароль '{P}' соответствует требованиям.")
        else:
            errorlable.config(text="Пароль не соответствует требованиям. Введите заново.")
            return  

        window = Tk()
        window.title("Результат")
        window.geometry("500x350+400+200")
        window.resizable(False,False)

        label = Label(window, text="Ответ")
        label.pack()
        
        results = var1h(P, L) 
        opt = max(results,key=sm)
        label2 = Label(window,text=f"Оптимальный пароль: {''.join(opt)} с суммой {sm(opt)}")
        label2.place(x=20,y=300)

        frame = Frame(window)
        frame.pack()

        text_widget = Text(frame, wrap='word', height=15, width=60)
        text_widget.pack(side=LEFT)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        text_widget.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=text_widget.yview)

        result_string = ' '.join(''.join(result) for result in results)
        text_widget.insert(END, result_string)

        window.mainloop()
    except ValueError:
        errorlable.config(text="Не введено число или введено неккоректно. Введите корректные значения.")

root = Tk()
root.title("Перебор пароля")
root.geometry("500x350+400+200")
root.resizable(False,False)
label = Label(text="Программа для перебора паролей")
label.pack()

label1 = Label(text="Количество символов в пароле")
label2 = Label(text="Первые символоы которые точно буквы ")
label3 = Label(text="Ваш пароль")
label4 = Label(text="Длина пароля")
label1.place(x=20,y=20)
label2.place(x=250,y=20)
label3.place(x=20,y=70)
label4.place(x=250,y=70)
errorlable = Label(fg="red")
errorlable.place(x=20,y=150)

btn1 = Button(text="Начать перебор паролей",command=validsim)
btn1.place(x=20,y=120,height=20,width=220)

entry1 = Entry()
entry1.place(x=20,y=45,height=20,width=220)
entry2 = Entry()
entry2.place(x=250,y=45,height=20,width=220)
entry3 = Entry()
entry3.place(x=20,y=95,height=20,width=220)
entry4 = Entry()
entry4.place(x=250,y=95,height=20,width=220)

root.mainloop()