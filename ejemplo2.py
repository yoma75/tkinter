import tkinter

ventana = tkinter.Tk()
ventana.geometry("400x300")
ventana.title('Segundo ejemplo')

# text='Hola Fredy': texto etiqueta
# bg='blue': color fondo
# fg="white: color texto 
etiqueta = tkinter.Label(ventana, text='Hola Fredy', bg='navy', fg="white", font='Helvetica 12')
etiqueta.pack(fill=tkinter.X, ipady=8) # (side=tkinter.RIGHT): ubicacion, (fill=tkinter.X): estirar color de relleno


# Funcion para interactar con botoncito
def saludo():
    print('Como estas..?')

# con parametro
# def saludo(nombre):
#     print('Como estas ..?' + nombre)

# padx=10: padding a lo ancho
# pady=5: padding a lo alto
# command=nombre_funcion: permite conectar el boton para interactuar
# con parametro: command=lambda:saludo('python')
botoncito1 = tkinter.Button(ventana, text='Presiona', padx=10, pady=5, bg='purple2', fg='white', command=saludo)
botoncito1.pack(side=tkinter.BOTTOM, pady=12)

# input
# font='Helvetica 14': tipo de letra y tamaño
cajaTexto = tkinter.Entry(ventana, font='Helvetica 14')
cajaTexto.pack(pady=12)

# Obtener el texto del input
def textoDeLaCaja():
    x = cajaTexto.get()
    etiqueta2['text'] = x # muestra la etiqueta en la ventana

botoncito2 = tkinter.Button(ventana, text='Enviar', bg='pale green', padx=10, pady=5, command=textoDeLaCaja)
botoncito2.pack()

# Mostrar una etiqueta en la ventana
etiqueta2 = tkinter.Label(ventana)
etiqueta2.pack(side=tkinter.BOTTOM)


ventana.mainloop()

