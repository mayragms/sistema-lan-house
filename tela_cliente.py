import tkinter as tk
from tkinter import ttk, messagebox
from cliente import Cliente
import dados

# --- PALETA DE CORES ---
BG_DARK = "#0b0b0b"        # Fundo geral
BG_CARD = "#161616"        # Fundo dos painéis
BG_INPUT = "#242424"       # Fundo dos campos de texto
BORDER_DARK = "#2e2e2e"    # Borda subtil dos cards e inputs
RED_PRIMARY = "#e61919"    # Vermelho principal
RED_HOVER = "#b31212"      # Vermelho escuro
TEXT_WHITE = "#ffffff"     # Texto branco
TEXT_GRAY = "#9e9e9e"      # Texto cinzento


class TelaLogin(tk.Frame):
    def __init__(self, parent, ao_logar_callback):
        super().__init__(parent, bg=BG_DARK)
        self.ao_logar_callback = ao_logar_callback
        self.senha_visivel = False
        self.criar_layout()

    def criar_layout(self):
        card = tk.Frame(
            self, bg=BG_CARD, padx=45, pady=40,
            highlightbackground=RED_PRIMARY, highlightthickness=2
        )
        card.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            card, text="LAN HOUSE SYSTEM", font=("Segoe UI", 22, "bold"),
            bg=BG_CARD, fg=RED_PRIMARY
        ).pack(pady=(0, 4))

        tk.Label(
            card, text="Acesso Restrito • Painel de Controle", font=("Segoe UI", 10),
            bg=BG_CARD, fg=TEXT_GRAY
        ).pack(pady=(0, 28))

        # Campo Usuário
        tk.Label(
            card, text="USUÁRIO ADMIN", font=("Segoe UI", 9, "bold"),
            bg=BG_CARD, fg=TEXT_WHITE, anchor="w"
        ).pack(fill="x")

        self.entry_user = tk.Entry(
            card, font=("Segoe UI", 12), bg=BG_INPUT, fg=TEXT_WHITE,
            insertbackground=TEXT_WHITE, relief="flat", width=28,
            highlightbackground=BORDER_DARK, highlightcolor=RED_PRIMARY, highlightthickness=1
        )
        self.entry_user.pack(pady=(6, 18), ipady=7, ipadx=6)
        self.entry_user.insert(0, "admin")

        # Cabeçalho Senha + Botão Mostrar/Ocultar
        frame_lbl_senha = tk.Frame(card, bg=BG_CARD)
        frame_lbl_senha.pack(fill="x")

        tk.Label(
            frame_lbl_senha, text="SENHA", font=("Segoe UI", 9, "bold"),
            bg=BG_CARD, fg=TEXT_WHITE
        ).pack(side="left")

        self.btn_olho = tk.Button(
            frame_lbl_senha, text="Mostrar", font=("Segoe UI", 8, "underline"),
            bg=BG_CARD, fg=TEXT_GRAY, activebackground=BG_CARD,
            activeforeground=TEXT_WHITE, relief="flat", cursor="hand2",
            bd=0, command=self.alternar_senha
        )
        self.btn_olho.pack(side="right")

        self.entry_pass = tk.Entry(
            card, font=("Segoe UI", 12), bg=BG_INPUT, fg=TEXT_WHITE,
            insertbackground=TEXT_WHITE, relief="flat", width=28, show="•",
            highlightbackground=BORDER_DARK, highlightcolor=RED_PRIMARY, highlightthickness=1
        )
        self.entry_pass.pack(pady=(6, 28), ipady=7, ipadx=6)
        self.entry_pass.insert(0, "1234")

        # Permitir login apertando Enter
        self.entry_user.bind("<Return>", lambda e: self.validar_login())
        self.entry_pass.bind("<Return>", lambda e: self.validar_login())

        btn_entrar = tk.Button(
            card, text="ACESSAR SISTEMA", font=("Segoe UI", 11, "bold"),
            bg=RED_PRIMARY, fg=TEXT_WHITE, activebackground=RED_HOVER,
            activeforeground=TEXT_WHITE, relief="flat", cursor="hand2",
            command=self.validar_login
        )
        btn_entrar.pack(fill="x", ipady=9)

        tk.Label(
            card, text="Credenciais padrão: admin / 1234", font=("Segoe UI", 8),
            bg=BG_CARD, fg=TEXT_GRAY
        ).pack(pady=(14, 0))

    def alternar_senha(self):
        self.senha_visivel = not self.senha_visivel
        if self.senha_visivel:
            self.entry_pass.config(show="")
            self.btn_olho.config(text="Ocultar")
        else:
            self.entry_pass.config(show="•")
            self.btn_olho.config(text="Mostrar")

    def validar_login(self):
        usuario = self.entry_user.get().strip()
        senha = self.entry_pass.get().strip()
        if usuario == "admin" and senha == "1234":
            self.ao_logar_callback()
        else:
            messagebox.showerror("Acesso Negado", "Usuário ou senha incorretos!")


class TelaCliente(tk.Frame):
    def __init__(self, parent, voltar_login_callback=None):
        super().__init__(parent, bg=BG_DARK)
        self.voltar_login_callback = voltar_login_callback
        self.configurar_estilo_tabela()
        self.criar_componentes()
        self.atualizar_tabela()

    def configurar_estilo_tabela(self):
        style = ttk.Style()
        style.theme_use("clam")
        
        # Remove a borda branca indesejada em volta da Treeview
        style.layout("Treeview", [("Treeview.treearea", {"sticky": "nswe"})])
        
        style.configure(
            "Treeview",
            background=BG_CARD,
            foreground=TEXT_WHITE,
            fieldbackground=BG_CARD,
            rowheight=34,
            borderwidth=0,
            font=("Segoe UI", 10)
        )
        style.configure(
            "Treeview.Heading",
            background=RED_PRIMARY,
            foreground=TEXT_WHITE,
            font=("Segoe UI", 10, "bold"),
            borderwidth=0,
            relief="flat",
            padding=(0, 6)
        )
        style.map(
            "Treeview",
            background=[("selected", "#3d1212")],
            foreground=[("selected", TEXT_WHITE)]
        )
        style.map(
            "Treeview.Heading",
            background=[("active", RED_HOVER)]
        )

    def criar_input(self, parent, largura):
        return tk.Entry(
            parent, font=("Segoe UI", 11), bg=BG_INPUT, fg=TEXT_WHITE,
            insertbackground=TEXT_WHITE, relief="flat", width=largura,
            highlightbackground=BORDER_DARK, highlightcolor=RED_PRIMARY, highlightthickness=1
        )

    def criar_componentes(self):
        # --- CABEÇALHO ---
        header = tk.Frame(
            self, bg=BG_CARD, pady=12, padx=20,
            highlightbackground=RED_PRIMARY, highlightthickness=1
        )
        header.pack(fill="x", padx=20, pady=(15, 10))

        tk.Label(
            header, text="PAINEL DE CLIENTES // LAN HOUSE",
            font=("Segoe UI", 14, "bold"), bg=BG_CARD, fg=RED_PRIMARY
        ).pack(side="left")

        if self.voltar_login_callback:
            tk.Button(
                header, text="Sair (Logout)", font=("Segoe UI", 9, "bold"),
                bg=BG_INPUT, fg=TEXT_WHITE, activebackground=RED_PRIMARY,
                activeforeground=TEXT_WHITE, relief="flat", cursor="hand2",
                padx=14, pady=5, command=self.voltar_login_callback
            ).pack(side="right")

        # --- BLOCO 1: FORMULÁRIO DE CADASTRO ---
        card_form = tk.Frame(
            self, bg=BG_CARD, padx=22, pady=18,
            highlightbackground=BORDER_DARK, highlightthickness=1
        )
        card_form.pack(fill="x", padx=20, pady=5)
        card_form.columnconfigure(1, weight=1)
        card_form.columnconfigure(3, weight=1)

        tk.Label(
            card_form, text="CADASTRAR NOVO CLIENTE",
            font=("Segoe UI", 11, "bold"), bg=BG_CARD, fg=TEXT_WHITE
        ).grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 14))

        # Linha 1: Nome e Data de Nascimento
        tk.Label(
            card_form, text="Nome Completo:", font=("Segoe UI", 10),
            bg=BG_CARD, fg=TEXT_GRAY
        ).grid(row=1, column=0, sticky="w", pady=6)

        self.entry_nome = self.criar_input(card_form, 34)
        self.entry_nome.grid(row=1, column=1, padx=(10, 25), pady=6, ipady=5, ipadx=5, sticky="we")

        tk.Label(
            card_form, text="Data Nasc. (DDMMAAAA):", font=("Segoe UI", 10),
            bg=BG_CARD, fg=TEXT_GRAY
        ).grid(row=1, column=2, sticky="w", pady=6)

        self.entry_nasc = self.criar_input(card_form, 20)
        self.entry_nasc.grid(row=1, column=3, padx=(10, 0), pady=6, ipady=5, ipadx=5, sticky="we")

        # Linha 2: CPF e Botão Cadastrar
        tk.Label(
            card_form, text="CPF (11 números):", font=("Segoe UI", 10),
            bg=BG_CARD, fg=TEXT_GRAY
        ).grid(row=2, column=0, sticky="w", pady=8)

        self.entry_cpf = self.criar_input(card_form, 24)
        self.entry_cpf.grid(row=2, column=1, padx=(10, 25), pady=8, ipady=5, ipadx=5, sticky="w")
        self.entry_cpf.bind("<Return>", lambda e: self.cadastrar_cliente())

        btn_salvar = tk.Button(
            card_form, text="+ CADASTRAR CLIENTE", font=("Segoe UI", 10, "bold"),
            bg=RED_PRIMARY, fg=TEXT_WHITE, activebackground=RED_HOVER,
            activeforeground=TEXT_WHITE, relief="flat", cursor="hand2",
            padx=22, pady=7, command=self.cadastrar_cliente
        )
        btn_salvar.grid(row=2, column=2, columnspan=2, sticky="e", pady=8)

        # --- BLOCO 2: CONSULTA E TABELA ---
        card_tabela = tk.Frame(
            self, bg=BG_CARD, padx=22, pady=18,
            highlightbackground=BORDER_DARK, highlightthickness=1
        )
        card_tabela.pack(fill="both", expand=True, padx=20, pady=(10, 20))

        # Barra de pesquisa e ações
        frame_busca = tk.Frame(card_tabela, bg=BG_CARD)
        frame_busca.pack(fill="x", pady=(0, 14))

        tk.Label(
            frame_busca, text="Pesquisar (Nome ou CPF):",
            font=("Segoe UI", 10, "bold"), bg=BG_CARD, fg=TEXT_WHITE
        ).pack(side="left")

        self.entry_busca = self.criar_input(frame_busca, 26)
        self.entry_busca.pack(side="left", padx=10, ipady=4, ipadx=5)
        self.entry_busca.bind("<Return>", lambda e: self.buscar_cliente())

        tk.Button(
            frame_busca, text="Buscar", font=("Segoe UI", 9, "bold"),
            bg=RED_PRIMARY, fg=TEXT_WHITE, activebackground=RED_HOVER,
            relief="flat", cursor="hand2", padx=14, pady=5,
            command=self.buscar_cliente
        ).pack(side="left", padx=4)

        tk.Button(
            frame_busca, text="Mostrar Todos", font=("Segoe UI", 9),
            bg=BG_INPUT, fg=TEXT_WHITE, activebackground="#383838",
            relief="flat", cursor="hand2", padx=12, pady=5,
            command=self.mostrar_todos
        ).pack(side="left", padx=4)

        # Botão de Remover e Contador à direita
        tk.Button(
            frame_busca, text="Excluir Selecionado", font=("Segoe UI", 9, "bold"),
            bg="#2b1111", fg="#ff6b6b", activebackground=RED_PRIMARY,
            activeforeground=TEXT_WHITE, relief="flat", cursor="hand2",
            padx=12, pady=5, command=self.excluir_cliente
        ).pack(side="right")

        self.lbl_contador = tk.Label(
            frame_busca, text="Total: 0 cliente(s)",
            font=("Segoe UI", 9, "bold"), bg=BG_CARD, fg=TEXT_GRAY
        )
        self.lbl_contador.pack(side="right", padx=15)

        # Contentor da tabela com borda escura elegante
        frame_tree = tk.Frame(
            card_tabela, bg=BG_CARD,
            highlightbackground=BORDER_DARK, highlightthickness=1
        )
        frame_tree.pack(fill="both", expand=True)

        colunas = ("id", "nome", "nascimento", "cpf")
        self.tabela = ttk.Treeview(frame_tree, columns=colunas, show="headings", height=8)

        self.tabela.heading("id", text="ID CLIENTE")
        self.tabela.heading("nome", text="NOME DO CLIENTE")
        self.tabela.heading("nascimento", text="DATA DE NASCIMENTO")
        self.tabela.heading("cpf", text="CPF")

        self.tabela.column("id", width=120, anchor="center")
        self.tabela.column("nome", width=320, anchor="w")
        self.tabela.column("nascimento", width=170, anchor="center")
        self.tabela.column("cpf", width=170, anchor="center")
        self.tabela.pack(fill="both", expand=True)

    def formatar_data(self, d):
        if len(d) == 8:
            return f"{d[:2]}/{d[2:4]}/{d[4:]}"
        return d

    def formatar_cpf(self, c):
        if len(c) == 11:
            return f"{c[:3]}.{c[3:6]}.{c[6:9]}-{c[9:]}"
        return c

    def cadastrar_cliente(self):
        nome = self.entry_nome.get().strip()
        data_nascimento = self.entry_nasc.get().strip()
        cpf = self.entry_cpf.get().strip()

        if not nome or not data_nascimento or not cpf:
            messagebox.showwarning("Atenção", "Preencha todos os campos do cliente!")
            return

        if not data_nascimento.isdigit() or len(data_nascimento) != 8:
            messagebox.showerror("Erro", "Digite a Data de Nascimento com 8 números (DDMMAAAA)!")
            return

        if not cpf.isdigit() or len(cpf) != 11:
            messagebox.showerror("Erro", "Digite o CPF com 11 números!")
            return

        for c in dados.clientes:
            if c.cpf == cpf:
                messagebox.showerror("Erro", "Já existe um cliente cadastrado com este CPF!")
                return

        novo_cliente = Cliente(nome, data_nascimento, cpf)
        dados.clientes.append(novo_cliente)

        self.atualizar_tabela()
        self.limpar_campos()
        self.entry_nome.focus_set()
        messagebox.showinfo("Sucesso", f"Cliente '{nome}' cadastrado no sistema!")

    def excluir_cliente(self):
        selecionado = self.tabela.selection()
        if not selecionado:
            messagebox.showwarning("Seleção", "Selecione um cliente na tabela para excluir!")
            return

        valores = self.tabela.item(selecionado[0], "values")
        id_curto_tabela = valores[0].replace("#", "").lower()

        for c in dados.clientes:
            if c.id_cliente.lower().startswith(id_curto_tabela):
                dados.clientes.remove(c)
                break

        self.atualizar_tabela()
        messagebox.showinfo("Removido", "Cliente removido com sucesso!")

    def atualizar_tabela(self, lista_filtrada=None):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        lista = lista_filtrada if lista_filtrada is not None else dados.clientes

        for c in lista:
            id_curto = f"#{c.id_cliente[:8].upper()}"
            data_fmt = self.formatar_data(c.data_nascimento)
            cpf_fmt = self.formatar_cpf(c.cpf)
            self.tabela.insert("", "end", values=(id_curto, c.nome, data_fmt, cpf_fmt))

        self.lbl_contador.config(text=f"Total: {len(lista)} cliente(s)")

    def buscar_cliente(self):
        termo = self.entry_busca.get().strip().lower()
        filtrados = [
            c for c in dados.clientes
            if termo in c.nome.lower() or termo in c.cpf
        ]
        self.atualizar_tabela(filtrados)

    def mostrar_todos(self):
        self.entry_busca.delete(0, tk.END)
        self.atualizar_tabela()

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_nasc.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)


class AppMaster(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lan House System - Admin & Clientes")
        self.geometry("920x620")
        self.configure(bg=BG_DARK)
        self.mostrar_login()

    def mostrar_login(self):
        self.limpar_janela()
        tela_login = TelaLogin(self, ao_logar_callback=self.mostrar_painel_clientes)
        tela_login.pack(fill="both", expand=True)

    def mostrar_painel_clientes(self):
        self.limpar_janela()
        tela_clientes = TelaCliente(self, voltar_login_callback=self.mostrar_login)
        tela_clientes.pack(fill="both", expand=True)

    def limpar_janela(self):
        for widget in self.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    app = AppMaster()
    app.mainloop()