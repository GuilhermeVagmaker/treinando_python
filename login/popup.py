def popup(app, titulo, mensagem):

    import customtkinter as ctk

    janela = ctk.CTkToplevel()
    janela.title(titulo)
    janela.geometry("320x160")
    janela.resizable(False, False)

    janela.attributes("-topmost", True)
   

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

    janela.after(50, janela.grab_set)

def popLogin(app):
    popup(app, "Login", "Login Efetuado com sucesso!!")
def popErroSenha(app):
    popup(app,"Erro", "Senha ou usuario errado!!")
def popErroUsuario(app):
    popup(app,"Erro", "Usuario não encontrado!!")
def popUsuarioExistente(app):
    popup(app,"Criar Login", "Já existe um usuario com esse gmail!!")
def popUsuarioCriado(app):
    popup(app,"Criar Login", "Usuario criado com sucesso!!")
def popPreenchaOsCampos(app):
    popup(app,"Erro", "Preencha todos os campos corretamentes")


