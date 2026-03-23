def criar_user():
  import customtkinter as ctk
  import json
  import os
  from popup import popUsuarioExistente
  from popup import popUsuarioCriado
  from popup import popPreenchaOsCampos
  import secrets
  import string
  from datetime import datetime
  import bcrypt

  ctk.set_appearance_mode("dark")
  ctk.set_default_color_theme("blue")

  app = ctk.CTkToplevel()
  app.geometry("700x700")
  app.title("Criar Login")

  usuarios_arquivo = "usuarios.json"
  if not os.path.exists(usuarios_arquivo):
      with open(usuarios_arquivo, "w") as f:
          json.dump({}, f)

  def token():
    caracteres = string.ascii_letters + string.digits
    token = "".join(secrets.choice(caracteres) for _ in range(6))
    label_token.configure(text="Token: "+token)
    return token
  
  def fechaJanela():
     app.destroy()

  def CriarUsuario():
      usuario = campo_usuario.get()
      email = campo_email.get()
      senha = campo_senha.get()

      senha_bytes = senha.encode("utf-8")

      senha_hash = bcrypt.hashpw(senha_bytes, bcrypt.gensalt())
      senha_hash = senha_hash.decode("utf-8")

      data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

      if not (usuario or email) or not senha:
        popPreenchaOsCampos(app)
        print("Preencha todos os campos")
        return
      
      with open(usuarios_arquivo, "r") as arquivo:
          usuarios = json.load(arquivo)

      if  usuario in usuarios:
          print("Usuario ja existe")
          popUsuarioExistente(app)
      else: 
        token_gerado = token()

        usuarios[usuario] = {
          "senha": senha_hash,
          "token": token_gerado,
          "email": email,
          "criado_em": data
          }
        with open(usuarios_arquivo, "w") as arquivo:
          json.dump(usuarios, arquivo, indent=4)
        print("Usuario criado")
        popUsuarioCriado(app)
        fechaJanela()

  frame_principal = ctk.CTkFrame(app, corner_radius=20)
  frame_principal.pack(expand=True, fill="both", padx=40, pady=40)

  frame_login = ctk.CTkFrame(frame_principal, width=600, height=500, corner_radius=20)
  frame_login.pack(expand=True)  # centraliza no frame
  frame_login.pack_propagate(False)

  titulo = ctk.CTkLabel(frame_login, text="Criar usuario", font=("Arial", 26, "bold"))
  titulo.pack(pady=(20, 30))

  campo_usuario = ctk.CTkEntry(frame_login, width=400,height=40 ,font=("Arial", 20), placeholder_text="Digite um nome para o usuario")
  campo_usuario.pack(pady=10,padx=40, fill="x")

  campo_email = ctk.CTkEntry(frame_login, width=400,height=40,font=("Arial", 20), placeholder_text="Digite um email")
  campo_email.pack(pady=10,padx=40, fill="x")

  campo_senha = ctk.CTkEntry(frame_login, width=400,height=40,font=("Arial", 20),show="*", placeholder_text="Crie uma senha")
  campo_senha.pack(pady=10,padx=40, fill="x")

  label_token = ctk.CTkLabel(frame_login, text="", font=("Arial", 24))
  label_token.pack(pady=10)

  botao_criar_conta = ctk.CTkButton(
    frame_login,
    text="Entrar",
    command=CriarUsuario,
    font=("Arial", 24),
    width=350,
    height=50,
    corner_radius=12
  )
  botao_criar_conta.pack(pady=25)

  app.mainloop()