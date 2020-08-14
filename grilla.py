import tkinter

ventana = tkinter.Tk()
ventana.geometry('400x300')
ventana.title('Ejemplo de grilla')
ventana.configure(bg='lavender')

# width=15 : ancho
# height=10 : alto
botoncito1 = tkinter.Button(ventana, text='Boton 1', width=7, height=2, bg='gold')
botoncito2 = tkinter.Button(ventana, text='Boton 2', width=7, height=2, bg='purple2', fg='white')
botoncito3 = tkinter.Button(ventana, text='Boton 3', width=7, height=2, bg='turquoise')

botoncito1.grid(row=0, column=0)
botoncito2.grid(row=1, column=1)
botoncito3.grid(row=2, column=2)


ventana.mainloop()