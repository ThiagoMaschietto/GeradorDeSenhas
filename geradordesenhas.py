import random as r
from customtkinter import *

num_caracteres = 0

def gerasenha_minusculas(numero_de_caracteres):
    senha_gerada.delete("1.0","end")
    if numero_de_caracteres == 0 :
        senha_gerada.insert("1.0","Por Favor escolha a quantidade de caracteres!")
        return
    
    letras = "abcedfghijklmnopqrstuvwxyz"
    senha = ""
    contador = 0
    while contador < numero_de_caracteres:
        senha += (letras[r.randrange(0, 26)])
        contador += 1 
    senha_gerada.insert("1.0",senha)


def gerasenha_minusculas_maiusculas(numero_de_caracteres):
    senha_gerada.delete("1.0","end")
    if numero_de_caracteres == 0 :
        senha_gerada.insert("1.0","Por Favor escolha a quantidade de caracteres!")
        return
    letras = "abcedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    senha = ""
    contador = 0
    while contador < numero_de_caracteres:
        senha += (letras[r.randrange(0, 52)])
        contador += 1 
    senha_gerada.insert("1.0",senha)



def gerasenha_minusculas_numeros(numero_de_caracteres):
    senha_gerada.delete("1.0","end")
    if numero_de_caracteres == 0 :
        senha_gerada.insert("1.0","Por Favor escolha a quantidade de caracteres!")
        return
    letras = "abcedfghijklmnopqrstuvwxyz1234567890"
    senha = ""
    contador = 0
    while contador < numero_de_caracteres:
        senha += (letras[r.randrange(0, 36)])
        contador += 1 
    senha_gerada.insert("1.0",senha)

def gerasenha_minusculas_caracteres(numero_de_caracteres):
    senha_gerada.delete("1.0","end")
    if numero_de_caracteres == 0 :
        senha_gerada.insert("1.0","Por Favor escolha a quantidade de caracteres!")
        return
    letras = "abcedfghijklmnopqrstuvwxyz@!#$%&*"
    senha = ""
    contador = 0
    while contador < numero_de_caracteres:
        senha += (letras[r.randrange(0, 33)])
        contador += 1 
    senha_gerada.insert("1.0",senha)

def gerasenha_minusculas_maiusculas_numeros(numero_de_caracteres):
    senha_gerada.delete("1.0","end")
    if numero_de_caracteres == 0 :
        senha_gerada.insert("1.0","Por Favor escolha a quantidade de caracteres!")
        return
    letras = "abcedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    contador = 0
    senha= ""
    while contador < numero_de_caracteres:
        senha += (letras[r.randrange(0, 62)])
        contador += 1 
    senha_gerada.insert("1.0",senha)

def gerasenha_minusculas_maiusculas_caracteres(numero_de_caracteres):
    senha_gerada.delete("1.0","end")
    if numero_de_caracteres == 0 :
        senha_gerada.insert("1.0","Por Favor escolha a quantidade de caracteres!")
        return
    letras = "abcedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@!#$%&*"
    contador = 0
    senha= ""
    while contador < numero_de_caracteres:
        senha += (letras[r.randrange(0, 59)])
        contador += 1 
    senha_gerada.insert("1.0",senha)

def gerasenha_minusculas_numeros_caracteres(numero_de_caracteres):
    senha_gerada.delete("1.0","end")
    if numero_de_caracteres == 0 :
        senha_gerada.insert("1.0","Por Favor escolha a quantidade de caracteres!")
        return
    letras = "abcedfghijklmnopqrstuvwxyz1234567890@!#$%&*"
    contador = 0
    senha= ""
    while contador < numero_de_caracteres:
        senha += (letras[r.randrange(0, 42)])
        contador += 1 
    senha_gerada.insert("1.0",senha)


def gerasenha_minusculas_maiusculas_caracteres_numeros(numero_de_caracteres):
    senha_gerada.delete("1.0","end")
    if numero_de_caracteres == 0 :
        senha_gerada.insert("1.0","Por Favor escolha a quantidade de caracteres!")
        return
    letras = "abcedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@!#$%&*"
    contador = 0
    senha= ""
    while contador < numero_de_caracteres:
        senha += (letras[r.randrange(0, 69)])
        contador += 1 
    senha_gerada.insert("1.0",senha)

def define_numero_de_caracteres(num):
    global num_caracteres
    num_caracteres = num
    

janela = CTk()
janela.title("Gerador de senhas")
janela.geometry("950x500")

senha_gerada = CTkTextbox(janela,height = 100, width=300, font=("Arial",25))
senha_gerada.grid(row = 0,column = 1)

radio_var = IntVar(value = 1)

radio_8 = CTkRadioButton(janela, text="8 caracteres",command= lambda:define_numero_de_caracteres(8),value = 8,variable = radio_var)
radio_8.grid(row=1, column=0, padx=10, pady=(200,30))

radio_12 = CTkRadioButton(janela, text="12 caracteres",command= lambda:define_numero_de_caracteres(12),value = 12,variable = radio_var)
radio_12.grid(row=1, column=1, padx=10, pady=(200,30))

radio_16 = CTkRadioButton(janela, text="16 caracteres",command= lambda:define_numero_de_caracteres(16),value = 16,variable = radio_var)
radio_16.grid(row=1, column=2, padx=10, pady=(200,30))

botao_minusculas = CTkButton(janela, text="Letras Minusculas",command = lambda: gerasenha_minusculas(num_caracteres))
botao_minusculas.grid(row=2, column=0, padx= 10, pady=(0,30))

botao_minusculas_maiusculas = CTkButton(janela, text="Letras Minusculas e Maiusculas",command = lambda: gerasenha_minusculas_maiusculas(num_caracteres))
botao_minusculas_maiusculas.grid(row=2, column=1, padx=10, pady=(0,30))

botao_minusculas_numeros = CTkButton(janela, text="Letras Minusculas e Numeros",command = lambda: gerasenha_minusculas_numeros(num_caracteres))
botao_minusculas_numeros.grid(row=2, column=2, padx=10, pady=(0,30))

botao_minusculas_caracteres = CTkButton(janela, text="Letras Minusculas e Caracteres",command = lambda: gerasenha_minusculas_caracteres(num_caracteres))
botao_minusculas_caracteres.grid(row=3, column=0, padx=10, pady=(0,30))

botao_minusculas_maiusculas_numeros = CTkButton(janela, text="Letras Minusculas Maiusculas e Numeros",command = lambda: gerasenha_minusculas_maiusculas_numeros(num_caracteres))
botao_minusculas_maiusculas_numeros.grid(row=3, column=1, padx=10, pady=(0,30))

botao_minusculas_maiusculas_caracteres = CTkButton(janela, text="Letras Minusculas Maiusculas e Caracteres",command = lambda: gerasenha_minusculas_maiusculas_caracteres(num_caracteres))
botao_minusculas_maiusculas_caracteres.grid(row=3, column=2, padx=10, pady=(0,30))

botao_minusculas_numeros_caracteres = CTkButton(janela, text="Letras Minusculas Numeros e Caracteres",command = lambda: gerasenha_minusculas_numeros_caracteres(num_caracteres))
botao_minusculas_numeros_caracteres.grid(row=4, column=0, padx=10, pady=(0,30))

botao_minusculas_maiusculas_caracteres_numeros = CTkButton(janela, text="Letras Minusculas Maiusculas Numeros e Caracteres",command = lambda: gerasenha_minusculas_maiusculas_caracteres_numeros(num_caracteres))
botao_minusculas_maiusculas_caracteres_numeros.grid(row=4, column=1, padx=10, pady=(0,30))

janela.mainloop()
