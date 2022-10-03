# Importar o SimpleTK
from time import sleep
import SimpleTK

# Deixar o fundo azul
SimpleTK.setBackground("white")
# Criar um Texto

SimpleTK.createText(60, 50, "Clique para adicionar 1+1", "black", "white", ("Helvetica", 16), Center=True)

# Criar um Botão
SimpleTK.createButton(80, 100, "Adicionar", "black", "white", Center=True, Command=None)

# Botar um icon de ICO
# SimpleTK.setIconICO("icon/ico.ico")

# Botar um icon de PNG
SimpleTK.setIconPNG("icon/ico.png")

# Criar a janela
SimpleTK.createWindow("Example APP", None)

# Como usar os GET's

# Pegar todos os comandos para usar da janela
SimpleTK.getWindow()

# Pegar todos os comandos do tkinter
SimpleTK.getTkinter()
