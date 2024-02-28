from tkinter import *
import os

def verificar_login():
    usuario = usuario_entry.get()
    senha = senha_entry.get()
    if usuario == "ruan" and senha == "123456":
        print("Login correto!")
        os.system("python main.py")
        janela.destroy()
    else:
        print("Nome de usuário ou senha incorretos!")

janela = Tk()

usuario_label = Label(janela, text="Usuário:")
usuario_label.pack()
usuario_entry = Entry(janela)
usuario_entry.pack()

senha_label = Label(janela, text="Senha:")
senha_label.pack()
senha_entry = Entry(janela, show="*")
senha_entry.pack()

botao_login = Button(janela, text="Login", command=verificar_login)
botao_login.pack()

janela.mainloop()
