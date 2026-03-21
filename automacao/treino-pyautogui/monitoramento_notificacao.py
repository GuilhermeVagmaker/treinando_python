import tkinter as tk

x = 500
y = 300
largura = 400
altura = 200

janela = tk.Tk()

janela.overrideredirect(True)
janela.geometry(f"{largura}x{altura}+{x}+{y}")

janela.wm_attributes("-topmost", True)
janela.wm_attributes("-alpha", 0.3)

canvas = tk.Canvas(janela, width=largura, height=altura, bg="black")
canvas.pack()

canvas.create_rectangle(0, 0, largura, altura, outline="red", width=4)

janela.after(5000, janela.destroy)