import tkinter as tk
from tkinter import messagebox
from fpdf import FPDF

# Cria a função adicionar_convidado, que adiciona o nome digitado na caixa de entrada à lista de convidados
def adicionar_convidado():
    nome = entry_nome.get()
    convidados.append(nome)
    entry_nome.delete(0, tk.END)
    messagebox.showinfo("Convidado adicionado", f"{nome} foi adicionado à lista de convidados.")

# Cria a função remover_convidado, que remove o nome digitado na caixa de entrada da lista de convidados
def remover_convidado():
    nome = entry_nome.get()
    if nome in convidados:
        convidados.remove(nome)
        entry_nome.delete(0, tk.END)
        messagebox.showinfo("Convidado removido", f"{nome} foi removido da lista de convidados.")
    else:
        messagebox.showerror("Erro", f"{nome} não está na lista de convidados.")

# Cria a função ver_convidados, que exibe a lista de convidados em uma caixa de mensagem
def ver_convidados():
    messagebox.showinfo("Lista de convidados", "\n".join(convidados))

# Cria uma janela principal
janela = tk.Tk()
janela.title("Lista de convidados")

# Cria um rótulo para pedir o nome do convidado
label_nome = tk.Label(janela, text="Nome do convidado:")
label_nome.pack()

# Cria uma caixa de entrada para o nome do convidado
entry_nome = tk.Entry(janela)
entry_nome.pack()

# Cria um botão para adicionar o convidado à lista
botao_adicionar = tk.Button(janela, text="Adicionar convidado", command=adicionar_convidado)
botao_adicionar.pack()

# Cria um botão para remover o convidado da lista
botao_remover = tk.Button(janela, text="Remover convidado", command=remover_convidado)
botao_remover.pack()

# Cria um botão para ver a lista de convidados
botao_ver = tk.Button(janela, text="Ver lista de convidados", command=ver_convidados)
botao_ver.pack()

# Cria a função gerar_pdf, que gera um arquivo pdf com a lista de convidados
def gerar_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=24)
    pdf.cell(200, 10, txt="Lista de Convidados", ln=1, align="C")
    pdf.set_font("Arial", size=12)
    for convidado in convidados:
        pdf.cell(200, 10, txt=convidado, ln=1, align="C")
    pdf.output("convidados.pdf")
    messagebox.showinfo("PDF gerado", "Lista de convidados gerada com sucesso em 'convidados.pdf'.")

# Cria um botão para gerar o arquivo pdf
botao_pdf = tk.Button(janela, text="Gerar PDF", command=gerar_pdf)
botao_pdf.pack()


# Cria uma lista vazia para armazenar os nomes dos convidados
convidados = []

# Inicia a janela
janela.mainloop()

