import os
import shutil

pasta_origem = os.listdir("coisas")

for pasta in pasta_origem:
  
  nome, extensao = os.path.splitext(pasta)
  
  if extensao == "":
    continue
  
  arquivo_extensao = extensao.replace(".", "").upper()
  caminho_pasta = os.path.join("coisas", arquivo_extensao)
  
  if not os.path.exists(caminho_pasta):
    os.mkdir(caminho_pasta)
  
  caminho_dentro_do_coisas = os.path.join("coisas", pasta)
  caminho_dentro_das_novas_pastas = os.path.join(caminho_pasta, pasta)
  
  shutil.move(caminho_dentro_do_coisas, caminho_dentro_das_novas_pastas)
  
  