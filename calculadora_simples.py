# bibliteca tkinter para interface grafica
import tkinter as tk
from tkinter import font

# bibliteca re para expressao regular
import re

# funcao adiciona texto ao campo de entrada e limpa se houver erro
def adicionar_texto(valor):
    if entrada.get() == "Erro":
        limpar()
    entrada.insert(tk.END, valor)

# funcao que calcula o resultado da expressão
def calcular():
    expressao = entrada.get()
    
    # se a entrada estiver vazia, não faz nada.
    if not expressao:
        return

    # verificacao de seguranca
    caracteres_permitidos = r"^[0-9\.\/\*\-\+\(\) ]*$"
    
    # se a expressão contiver qualquer caractere ilegal mostra "Erro"
    if not re.match(caracteres_permitidos, expressao):
        limpar()
        entrada.insert(tk.END, "Erro")
        return

    # se a expressão for segura tenta calcular usando eval()
    try:
        resultado = eval(expressao)
        limpar()
        entrada.insert(tk.END, str(resultado))
    # erros comuns como sintaxe invalida ou divisao por zero
    except (SyntaxError, ZeroDivisionError):
        limpar()
        entrada.insert(tk.END, "Erro")
    # outros erros inesperados
    except Exception:
        limpar()
        entrada.insert(tk.END, "Erro")

# limpar o campo de entrada
def limpar():
    entrada.delete(0, tk.END)

# configuracao da janela principal
root = tk.Tk()
root.title("Calculadora Simples")
root.config(bg="thistle")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# configuracao do layout dentro da janela
frame = tk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
frame.config(bg="dark orchid")
for i in range(7):
    frame.rowconfigure(i, weight=1)
    frame.columnconfigure(i, weight=1)

# configuracao da fonte dos botoes e da entrada
fonte_btn = font.Font(family="Calibri", size=12)
fonte_entrada = font.Font(family="Calibri", size=18)

# entrada de texto com teclado
entrada = tk.Entry(frame, width=20, font=fonte_entrada, justify="right")
entrada.grid(row=0, column=0, columnspan=4, sticky="ew", padx=5, pady=5)
entrada.bind('<Return>', lambda event: calcular())

# botoes da calculadora
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('.', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('(', 5, 0), (')', 5, 1)
]

# cria os botoes e adiciona ao grid
for (texto, linha, coluna) in botoes:
    if texto == '=':
        btn = tk.Button(frame, text=texto, width=5, height=2, command=calcular, font=fonte_btn)
    else:
        btn = tk.Button(frame, text=texto, width=5, height=2, command=lambda t=texto: adicionar_texto(t), font=fonte_btn)
    btn.grid(row=linha, column=coluna, sticky="nsew", padx=5, pady=5)

# botao de limpar
btn_limpar = tk.Button(frame, text="C", width=5, height=2, command=limpar, font=fonte_btn)
btn_limpar.grid(row=5, column=2, columnspan=2, sticky="nsew", padx=5, pady=5)

# manter janela aberta
root.mainloop()
