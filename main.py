agenda = []

# Funções
def adicionar_contato():
    nome = entry_nome.get()
    numero = entry_numero.get()

    if nome and numero:
        agenda.append([nome, numero])
        messagebox.showinfo("Sucesso", f"Contato {nome} adicionado!")
        entry_nome.delete(0, tk.END)
        entry_numero.delete(0, tk.END)
        atualizar_lista()
    else:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")

def atualizar_lista():
    lista_contatos.delete(0, tk.END)
    for contato in agenda:
        lista_contatos.insert(tk.END, f"{contato[0]} - {contato[1]}")

def remover_contato():
    selecionado = lista_contatos.curselection()
    if selecionado:
        idx = selecionado[0]
        contato = agenda.pop(idx)
        messagebox.showinfo("Removido", f"Contato {contato[0]} removido!")
        atualizar_lista()
    else:
        messagebox.showwarning("Atenção", "Selecione um contato para remover!")