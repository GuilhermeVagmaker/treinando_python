def criar_user():
  import customtkinter as ctk
  import json
  import os
  from popup import popUsuarioExistente
  from popup import popUsuarioCriado
  from popup import popPreenchaOsCampos

  ctk.set_appearance_mode("dark")
  ctk.set_default_color_theme("blue")

  app = ctk.CTkToplevel()
  app.geometry("500x450")
  app.title("Login")

  usuarios_arquivo = "usuarios.json"
  if not os.path.exists(usuarios_arquivo):
      with open(usuarios_arquivo, "w") as f:
          json.dump({}, f)
  def fechaJanela():
     app.destroy()

  def CriarUsuario():
      usuario = campo_usuario.get()
      senha = campo_senha.get()

      if not usuario or not senha:
        popPreenchaOsCampos()
        print("Preencha todos os campos")
        return
      
      with open(usuarios_arquivo, "r") as arquivo:
          usuarios = json.load(arquivo)

      if usuario in usuarios:
          print("Usuario ja existe")
          popUsuarioExistente()
      else: 
        usuarios[usuario] = senha
        with open(usuarios_arquivo, "w") as arquivo:
          json.dump(usuarios, arquivo, indent=4)
        print("Usuario criado")
        popUsuarioCriado()
        fechaJanela()

  frame_principal = ctk.CTkFrame(app, corner_radius=20)
  frame_principal.pack(expand=True, fill="both", padx=40, pady=40)

  frame_login = ctk.CTkFrame(frame_principal, width=400, height=350, corner_radius=20)
  frame_login.place(relx=0.5, rely=0.5, anchor="center")  # centraliza no frame
  frame_login.pack_propagate(False)

  titulo = ctk.CTkLabel(frame_login, text="Criar usuario", font=("Arial", 26, "bold"))
  titulo.pack(pady=(20, 30))

  campo_usuario = ctk.CTkEntry(frame_login, width=300, placeholder_text="Digite um email")
  campo_usuario.pack(pady=10)


  campo_senha = ctk.CTkEntry(frame_login, width=300, show="*", placeholder_text="Crie uma senha")
  campo_senha.pack(pady=10)

  frame_botoes = ctk.CTkFrame(frame_login, fg_color="transparent")
  frame_botoes.pack(pady=15, fill="x")

  botao_criar_conta = ctk.CTkButton(
      frame_botoes,
      text="Criar conta",
      command=CriarUsuario,
      font=("Arial", 18),
      width=200,
      corner_radius=12,
  )
  botao_criar_conta.pack(pady=25)

  app.mainloop()