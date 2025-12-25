import os
import shutil

categorias = {
    "Imagens": [".jpg", ".png", ".jpeg", ".gif"],
    "Vídeos": [".mp4", ".avi", ".mkv"],
    "Documentos": [".pdf", ".txt", ".docx"],
    "Compactados": [".zip", ".rar"]
}

pasta_origem = os.listdir("coisas")

for arquivos in pasta_origem:
  nome, extensao = os.path.splitext(arquivos)
  if extensao == "":
    continue
  
  for categoria, extensoes in categorias.items():
    
    if extensao in extensoes:
      
      caminho_no_coisas = os.path.join("coisas", categoria)
      if not os.path.exists(caminho_no_coisas):
        os.mkdir(caminho_no_coisas)
     
  caminhoDentroDoCoisas = os.path.join("coisas", arquivos)
  caminhoDentroDasNovasPastas = os.path.join(caminho_no_coisas, arquivos)
  
  shutil.move(caminhoDentroDoCoisas, caminhoDentroDasNovasPastas)
     

