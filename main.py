
import tkinter as tk


janela = tk.Tk()

janela.title("Personal Finance Manager")
janela.geometry("1000x700")
janela.configure(bg="#F4F6F8")


titulo = tk.Label(
    janela,
    text="Personal Finance Manager",
    font=("Arial", 22, "bold"),
    bg="#F4F6F8",
    fg="#222222"
)

titulo.pack(pady=30)


area_cartoes = tk.Frame(
    janela,
    bg="#F4F6F8"
)

area_cartoes.pack(pady=20)


cartao_saldo = tk.Frame(
    area_cartoes,
    bg="#FFFFFF",
    width=280,
    height=150
)

cartao_saldo.pack(side="left", padx=10)
cartao_saldo.pack_propagate(False)


texto_saldo = tk.Label(
    cartao_saldo,
    text="SALDO TOTAL",
    font=("Arial", 12),
    bg="#FFFFFF",
    fg="#777777"
)

texto_saldo.pack(pady=(25, 10))

valor_saldo = tk.Label(
    cartao_saldo,
    text="R$ 2.500,00",
    font=("Arial", 24, "bold"),
    bg="#FFFFFF",
    fg="#222222"
)

valor_saldo.pack()


cartao_receitas = tk.Frame(
    area_cartoes,
    bg="#FFFFFF",
    width=280,
    height=150
)

cartao_receitas.pack(side="left", padx=10)
cartao_receitas.pack_propagate(False)

texto_receitas = tk.Label(
    cartao_receitas,
    text="RECEITAS",
    font=("Arial", 12),
    bg="#FFFFFF",
    fg="#777777"
)

texto_receitas.pack(pady=(25, 10))

valor_receitas = tk.Label(
    cartao_receitas,
    text="R$ 4.000,00",
    font=("Arial", 24, "bold"),
    bg="#FFFFFF",
    fg="#16A36A"
)

valor_receitas.pack()


cartao_despesas = tk.Frame(
    area_cartoes,
    bg="#FFFFFF",
    width=280,
    height=150
)

cartao_despesas.pack(side="left", padx=10)
cartao_despesas.pack_propagate(False)

texto_despesas = tk.Label(
    cartao_despesas,
    text="DESPESAS",
    font=("Arial", 12),
    bg="#FFFFFF",
    fg="#777777"
)

texto_despesas.pack(pady=(25, 10))

valor_despesas = tk.Label(
    cartao_despesas,
    text="R$ 1.500,00",
    font=("Arial", 24, "bold"),
    bg="#FFFFFF",
    fg="#DC4545"
)

valor_despesas.pack()

janela.mainloop()
