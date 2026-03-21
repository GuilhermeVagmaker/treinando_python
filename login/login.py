import customtkinter as ctk
import json
import os

arquivos = "usuarios.json"
if not os.path.exists(arquivos):
    with open(arquivos, "w") as f:
       json.dump({}, f)

def loginUsuario():
  usuario = campo_usuario.get()
  senha = campo_senha.get()

  with open(arquivos, "r") as arquivo:
    usuarios = json.load(arquivo)

  usuarios[usuario] = senha

  with open(arquivos, "w") as arquivo:
     json.dump(usuarios, arquivo, indent=4)

  for user, password in usuarios.items():
     print(f"Usuario: {user} | Senha: {password}")


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("500x400")
app.title("Titulo")

frame_principal = ctk.CTkFrame(app)
frame_principal.pack(expand=True)

frame_login = ctk.CTkFrame(frame_principal, width=300, height=250, corner_radius=15)
frame_login.pack(padx=20, pady=20)

titulo = ctk.CTkLabel(frame_login, text="Criar Usuario", font=("Arial", 24))
titulo.grid(row=0, column=0,columnspan=3, padx=10, pady=10)

label_usuario = ctk.CTkLabel(frame_login, text="Usuario:", font=("Arial", 16))
label_usuario.grid(row=1, column=0, padx=10, pady=10)

campo_usuario = ctk.CTkEntry(frame_login, width=200, placeholder_text="Guilherme@gmail.com")
campo_usuario.grid(row=1, column=1, padx=10, pady=10)

label_senha = ctk.CTkLabel(frame_login, text="Senha:", font=("Arial", 16))
label_senha.grid(row=2, column=0, padx=10, pady=10)

campo_senha = ctk.CTkEntry(frame_login, show="*", width=200, placeholder_text="123456")
campo_senha.grid(row=2, column=1, padx=10, pady=10)

botao = ctk.CTkButton(frame_login, text="Entrar", command=loginUsuario, font=("Arial", 18))
botao.grid(row=3, column=0,columnspan=3, pady=20)

app.mainloop()