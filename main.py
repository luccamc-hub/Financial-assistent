
import tkinter as tk
from tkinter import ttk, messagebox



janela = tk.Tk()

janela.title("Personal Finance Manager")
janela.geometry("1000x750")
janela.configure(bg="#F4F6F8")




movimentacoes = []

total_receitas = 0
total_despesas = 0




titulo = tk.Label(
    janela,
    text="Personal Finance Manager",
    font=("Arial", 22, "bold"),
    bg="#F4F6F8",
    fg="#222222"
)

titulo.pack(pady=20)




area_cartoes = tk.Frame(janela, bg="#F4F6F8")
area_cartoes.pack(pady=10)


def criar_cartao(nome, cor):

    cartao = tk.Frame(
        area_cartoes,
        bg="white",
        width=280,
        height=120
    )

    cartao.pack(side="left", padx=10)
    cartao.pack_propagate(False)

    tk.Label(
        cartao,
        text=nome,
        font=("Arial", 12),
        bg="white",
        fg="#777777"
    ).pack(pady=(20, 5))

    valor = tk.Label(
        cartao,
        text="R$ 0,00",
        font=("Arial", 22, "bold"),
        bg="white",
        fg=cor
    )

    valor.pack()

    return valor


valor_saldo = criar_cartao("SALDO TOTAL", "#222222")
valor_receitas = criar_cartao("RECEITAS", "#16A36A")
valor_despesas = criar_cartao("DESPESAS", "#DC4545")




titulo_formulario = tk.Label(
    janela,
    text="Nova movimentação",
    font=("Arial", 16, "bold"),
    bg="#F4F6F8",
    fg="#222222"
)

titulo_formulario.pack(anchor="w", padx=50, pady=(25, 10))


formulario = tk.Frame(janela, bg="#F4F6F8")
formulario.pack(padx=50, fill="x")




tk.Label(
    formulario,
    text="Descrição",
    bg="#F4F6F8"
).grid(row=0, column=0, sticky="w")

campo_descricao = tk.Entry(formulario, width=25)
campo_descricao.grid(row=1, column=0, padx=(0, 15), pady=5)




tk.Label(
    formulario,
    text="Valor (R$)",
    bg="#F4F6F8"
).grid(row=0, column=1, sticky="w")

campo_valor = tk.Entry(formulario, width=15)
campo_valor.grid(row=1, column=1, padx=(0, 15), pady=5)



tk.Label(
    formulario,
    text="Tipo",
    bg="#F4F6F8"
).grid(row=0, column=2, sticky="w")

tipo_selecionado = tk.StringVar(value="Despesa")

opcao_tipo = ttk.Combobox(
    formulario,
    textvariable=tipo_selecionado,
    values=["Receita", "Despesa"],
    state="readonly",
    width=12
)

opcao_tipo.grid(row=1, column=2, padx=(0, 15), pady=5)




tk.Label(
    formulario,
    text="Categoria",
    bg="#F4F6F8"
).grid(row=0, column=3, sticky="w")

categoria_selecionada = tk.StringVar(value="Outros")

opcao_categoria = ttk.Combobox(
    formulario,
    textvariable=categoria_selecionada,
    values=[
        "Alimentação",
        "Transporte",
        "Salário",
        "Lazer",
        "Moradia",
        "Outros"
    ],
    state="readonly",
    width=15
)

opcao_categoria.grid(row=1, column=3, pady=5)




def atualizar_dashboard():

    saldo = total_receitas - total_despesas

    valor_saldo.config(
        text=f"R$ {saldo:.2f}".replace(".", ",")
    )

    valor_receitas.config(
        text=f"R$ {total_receitas:.2f}".replace(".", ",")
    )

    valor_despesas.config(
        text=f"R$ {total_despesas:.2f}".replace(".", ",")
    )




def adicionar_movimentacao():

    global total_receitas, total_despesas

    descricao = campo_descricao.get()
    valor_digitado = campo_valor.get().strip()

    tipo = tipo_selecionado.get()
    categoria = categoria_selecionada.get()

    if not descricao.strip() or not valor_digitado:
        messagebox.showwarning(
            "Atenção",
            "Preencha a descrição e o valor."
        )
        return

    try:
        valor = float(valor_digitado.replace(",", "."))

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite um valor numérico válido."
        )
        return

    if valor <= 0:
        messagebox.showwarning(
            "Atenção",
            "O valor deve ser maior que zero."
        )
        return

    movimentacao = {
        "descricao": descricao,
        "valor": valor,
        "tipo": tipo,
        "categoria": categoria
    }

    movimentacoes.append(movimentacao)

    if tipo == "Receita":
        total_receitas += valor

    else:
        total_despesas += valor

    tabela.insert(
        "",
        "end",
        values=(
            descricao,
            f"R$ {valor:.2f}".replace(".", ","),
            tipo,
            categoria
        )
    )

    atualizar_dashboard()

    campo_descricao.delete(0, tk.END)
    campo_valor.delete(0, tk.END)



botao_adicionar = tk.Button(
    janela,
    text="Adicionar movimentação",
    command=adicionar_movimentacao,
    bg="#2563EB",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    padx=15,
    pady=8
)

botao_adicionar.pack(pady=15)



titulo_historico = tk.Label(
    janela,
    text="Histórico de movimentações",
    font=("Arial", 16, "bold"),
    bg="#F4F6F8",
    fg="#222222"
)

titulo_historico.pack(anchor="w", padx=50, pady=(15, 10))


tabela = ttk.Treeview(
    janela,
    columns=("descricao", "valor", "tipo", "categoria"),
    show="headings",
    height=10
)

tabela.heading("descricao", text="Descrição")
tabela.heading("valor", text="Valor")
tabela.heading("tipo", text="Tipo")
tabela.heading("categoria", text="Categoria")

tabela.column("descricao", width=300)
tabela.column("valor", width=150)
tabela.column("tipo", width=150)
tabela.column("categoria", width=200)

tabela.pack(padx=50, fill="x")




janela.mainloop()
