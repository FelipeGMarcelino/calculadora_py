# importa a biblioteca customtkinter em vez do tkinter
import customtkinter as ctk

# importa a bibliteca re para expressao regular
import re

# funcao adiciona texto ao campo de entrada e limpa se houver erro
def adicionar_texto(valor):
    if entrada.get() == "Erro":
        limpar()
    entrada.insert(ctk.END, valor)

# funcao que calcula o resultado da expressao
def calcular():
    expressao = entrada.get()
    
    # se a entrada estiver vazia nao faz nada.
    if not expressao:
        return

    # verificacao de seguranca
    caracteres_permitidos = r"^[0-9\.\/\*\-\+\(\) ]*$"
    
    # se a expressao contiver qualquer caractere ilegal mostra "Erro"
    if not re.match(caracteres_permitidos, expressao):
        limpar()
        entrada.insert(ctk.END, "Erro")
        return

    # se a expressao for segura tenta calcular usando eval()
    try:
        resultado = eval(expressao)
        limpar()
        # garante que numeros muito grandes ou pequenos sejam exibidos de forma legivel
        if isinstance(resultado, float) and resultado.is_integer():
            resultado = int(resultado)
        entrada.insert(ctk.END, str(resultado))
    # erros comuns como sintaxe invalida ou divisao por zero
    except (SyntaxError, ZeroDivisionError):
        limpar()
        entrada.insert(ctk.END, "Erro")
    # outros erros inesperados
    except Exception:
        limpar()
        entrada.insert(ctk.END, "Erro")

# funcao para limpar o campo de entrada
def limpar():
    entrada.delete(0, ctk.END)

# configuracoes de aparencia
ctk.set_appearance_mode("system")

# cores personalizadas modo claro e escuro
# paleta de cores: Voodoo Lady Palette by Jude Buffum
# (https://lospec.com/palette-list/voodoo-lady)
cor_numero = ("#ffda71", "#3e2542")
cor_operador = ("#ba877f", "#ba877f")
cor_igual = ("#7f425a", "#ffda71")
cor_destaque = ("#d0a047")

# texto
cor_texto_numero = ("#3e2542", "#ffda71")
cor_texto_outro = ("#ffda71", "#3e2542")

# janela principal agora eh um CTk
root = ctk.CTk()
root.title("Calculadora CustomTkinter")
root.geometry("380x520")
root.configure(fg_color=("#ba877f", "#3e2542"))

# configuracao de peso das colunas e linhas
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# frame principal agora eh um CTkFrame
frame = ctk.CTkFrame(root, corner_radius=15)
frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
frame.configure(fg_color=("#e8b08e", "#7f425a"))

# grid continua sendo configurado da mesma forma
# 1 linha para display e 5 para botoes
for i in range(6):
    frame.rowconfigure(i, weight=1)
# 4 colunas para os botoes
for i in range(4):
    frame.columnconfigure(i, weight=1)

# fonte agora eh definida como uma tupla diretamente nos widgets
fonte_entrada = ("Calibri", 40, "bold")
fonte_btn = ("Calibri", 20, "bold")

# entrada de texto agora eh um CTkEntry
entrada = ctk.CTkEntry(
    frame,
    font=fonte_entrada,
    justify="right",
    border_width=2,
    corner_radius=10,
    height=70
)
entrada.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=20)
entrada.bind('<Return>', lambda event: calcular())

# nova estrutura de botoes
botoes = [
    # formato: (texto, linha, coluna, tipo)
    ('C', 1, 0, 'operador'), ('(', 1, 1, 'operador'), (')', 1, 2, 'operador'), ('/', 1, 3, 'operador'),
    ('7', 2, 0, 'numero'),   ('8', 2, 1, 'numero'),   ('9', 2, 2, 'numero'),   ('*', 2, 3, 'operador'),
    ('4', 3, 0, 'numero'),   ('5', 3, 1, 'numero'),   ('6', 3, 2, 'numero'),   ('-', 3, 3, 'operador'),
    ('1', 4, 0, 'numero'),   ('2', 4, 1, 'numero'),   ('3', 4, 2, 'numero'),   ('+', 4, 3, 'operador'),
    ('.', 5, 0, 'numero'),   ('0', 5, 1, 'numero'),   ('=', 5, 3, 'igual')
]

# criacao dos botoes usando CTkButton e aplicando estilos diferentes
for (texto, linha, coluna, tipo) in botoes:
    # cada botao tem um estilo diferente baseado no tipo
    if tipo == 'numero':
        btn = ctk.CTkButton(
            frame,
            text=texto,
            font=fonte_btn,
            fg_color=cor_numero,
            text_color=cor_texto_numero,
            hover_color=cor_operador,
            corner_radius=10,
            command=lambda t=texto: adicionar_texto(t)
        )
    elif tipo == 'operador':
        btn = ctk.CTkButton(
            frame,
            text=texto,
            font=fonte_btn,
            fg_color=cor_operador,
            text_color=cor_texto_outro,
            hover_color=cor_texto_numero,
            corner_radius=10,
            command=limpar if texto == 'C' else lambda t=texto: adicionar_texto(t)
        )
    elif tipo == 'igual':
        btn = ctk.CTkButton(
            frame,
            text=texto,
            font=fonte_btn,
            fg_color=cor_igual,
            text_color=cor_texto_outro,
            hover_color=cor_operador,
            corner_radius=10,
            command=calcular
        )

    # configuracao do grid para cada botão
    if texto == '0':
        # faz o botão '0' ocupar duas colunas
        btn.grid(row=linha, column=coluna, columnspan=2, sticky="nsew", padx=5, pady=5)
    else:
        btn.grid(row=linha, column=coluna, sticky="nsew", padx=5, pady=5)

# manter a janela aberta
root.mainloop()
