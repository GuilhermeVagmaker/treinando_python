import customtkinter as ctk

def popup(titulo, mensagem):

    janela = ctk.CTkToplevel()
    janela.title(titulo)
    janela.geometry("320x160")
    janela.resizable(False, False)

    janela.attributes("-topmost", True)
    janela.grab_set()
    janela.focus_force()

    label = ctk.CTkLabel(
        janela,
        text=mensagem,
        font=("Arial", 20)
    )
    label.pack(pady=30)

    botao = ctk.CTkButton(
        janela,
        text="OK",
        command=janela.destroy
    )
    botao.pack(pady=10)

    janela.after(2000, popup.destroy())

def popLogin():
    popup("Login", "Login Efetuado com sucesso!!")
def popErroSenha():
    popup("Erro", "Senha ou usuario errado!!")
def popErroUsuario():
    popup("Erro", "Usuario não encontrado!!")
def popUsuarioExistente():
    popup("Criar Login", "Já existe um usuario com esse gmail!!")
def popUsuarioCriado():
    popup("Criar Login", "Usuario criado com sucesso!!")
def popPreenchaOsCampos():
    popup("Erro", "Preencha todos os campos corretamentes")


