import customtkinter as ctk
import json
import os
from popup import popLogin
from popup import popErroSenha
from popup import popErroUsuario
from criarUser import criar_user

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("500x450")
app.title("Login")

usuarios_arquivo = "usuarios.json"
if not os.path.exists(usuarios_arquivo):
    with open(usuarios_arquivo, "w") as f:
        json.dump({}, f)

def loginUsuario():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    
    with open(usuarios_arquivo, "r") as arquivo:
        usuarios = json.load(arquivo)
    
    # Apenas para teste: adiciona o usuário
    usuarios[usuario] = senha
    if usuario in usuarios:
      if usuarios[usuario] == senha:
        print("Login efetuado com sucesso")
        popLogin()
      else:
        print("Usuário ou senha incorretos")
        popErroSenha()
    else: 
       print("Usuario não criado")
       popErroUsuario()

frame_principal = ctk.CTkFrame(app, corner_radius=20)
frame_principal.pack(expand=True, fill="both", padx=40, pady=40)

frame_login = ctk.CTkFrame(frame_principal, width=400, height=350, corner_radius=20)
frame_login.place(relx=0.5, rely=0.5, anchor="center")  # centraliza no frame
frame_login.pack_propagate(False)

titulo = ctk.CTkLabel(frame_login, text="Bem-vindo!", font=("Arial", 26, "bold"))
titulo.pack(pady=(20, 30))

campo_usuario = ctk.CTkEntry(frame_login, width=300, placeholder_text="Digite seu email")
campo_usuario.pack(pady=10)


campo_senha = ctk.CTkEntry(frame_login, width=300, show="*", placeholder_text="Digite sua senha")
campo_senha.pack(pady=10)

frame_botoes = ctk.CTkFrame(frame_login, fg_color="transparent")
frame_botoes.pack(pady=15, fill="x")

botao_esqueceu_senha = ctk.CTkButton(
    frame_botoes,
    text="Esqueceu a senha?",
    fg_color="transparent",
    text_color="white",
    hover_color="gray30",
    border_width=0,
    font=("Arial", 14)
)
botao_esqueceu_senha.pack(side="left", expand=True, padx=10)

botao_criar_usuario = ctk.CTkButton(
    frame_botoes,
    command=criar_user,
    text="Criar usuário",
    fg_color="transparent",
    text_color="white",
    hover_color="gray30",
    border_width=0,
    font=("Arial", 14)
)
botao_criar_usuario.pack(side="right", expand=True, padx=10)


botao_entrar = ctk.CTkButton(
    frame_login,
    text="Entrar",
    command=loginUsuario,
    font=("Arial", 18),
    width=200,
    corner_radius=12
)
botao_entrar.pack(pady=25)

app.mainloop()