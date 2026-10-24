from tkinter import *

def console_variant():
    print("Добро пожаловать в ваш ежедневник!")
    while True:
        choosewrite = input("Что вы хотите сделать?\nДобавить запись - 1\nПосмотреть записи - 2\nУдалить записи - 3\n")
        if choosewrite == "1":
            writenew()
        elif choosewrite == "2":
            lookall()
        elif choosewrite == "3":
            delete()
        elif choosewrite == "exit" or choosewrite == "выход":
            break
        else:
            print("Выберите вариант : 1 / 2")

def writenew():
    with open("diary.txt", "a", encoding="utf-8") as f:
        todayday = input("Сегодняшнее число >_")
        text = input(">_")
        f.write(f"{todayday}\n")
        f.write(f"{text}\n")

def writenew2():
    with open("diary.txt", "a", encoding="utf-8") as f:
        todayday = entry_date.get()
        text = entry_text.get()
        f.write(f"{todayday}\n")
        f.write(f"{text}\n")
        entry_date.delete(0,END)
        entry_text.delete(0,END)


def lookall():
    with open("diary.txt", "r", encoding="utf-8") as f:
        text = f.read()
        print(text)

def lookall2():
    with open("diary.txt", "r", encoding="utf-8") as f:
        content = f.read()
        text_menu.delete(1.0,END)
        text_menu.insert(1.0, content)



def delete():
    with open("diary.txt", "w", encoding="utf-8") as f:
        f.write("")
        entry_date.delete(0,END)
        entry_text.delete(0,END)
        text_menu.delete(1.0, END)


root = Tk()
root.title("Your diary")
root.geometry("450x550")

label1 = Label(root,
               text="Введите дату")
label1.grid(row=0,column=0)
entry_date = Entry(root,
                   width=10)
entry_date.grid(row=1,column=0)

label2 = Label(root,
               text="Введите текст")
label2.grid(row=2, column=0)
entry_text = Entry(root)
entry_text.grid(row=3,column=0,columnspan=3, sticky="nsew")

add_text_btn = Button(root,
                      text="Добавить запись",
                      command=writenew2)
add_text_btn.grid(row=4, column=0)

look_allbtn = Button(root,
                     text="Посмотреть записи",
                     command=lookall2)
look_allbtn.grid(row=4, column=1)

deletebtn = Button(root,
                   text="Удалить записи",
                   command=delete)
deletebtn.grid(row=4,column=2)

text_menu = Text(root,
                 width=35,
                 height=20)
text_menu.grid(row=5,column=0,columnspan=3)

scroll = Scrollbar(root,
                   command=text_menu.yview)
scroll.grid(row=5,column=3,sticky="ns")
text_menu.config(yscrollcommand=scroll.set)

root.mainloop()