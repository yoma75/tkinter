from tkinter import *
import requests

# key: b3b8f0eb4b0e5f1e235d74c338fcbae7
# api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}

def mostrar_respuesta(clima):
    nombre_ciudad = clima['name']
    desc = (clima['weather'][0]['description'])
    temp = (clima['main']['temp'])

    ciudad['text'] = nombre_ciudad
    temperatura['text'] = temp
    descripcion['text'] = desc


def clima_JSON(ciudad):
    API_key = 'b3b8f0eb4b0e5f1e235d74c338fcbae7'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    parametros = {'APPID' : API_key, 'q' : ciudad, 'units' : 'metric'}
    response = requests.get(URL, params=parametros)
    clima = response.json()
    
    print(clima['name'])
    print(clima['weather'][0]['description'])
    print(clima['main']['temp'])

    mostrar_respuesta(clima)

    
# Interfaz
ventana = Tk()
ventana.geometry('390x400')
ventana.title('Estado del tiempo')

texto_ciudad = Entry(ventana, font=('Courier', 20, 'normal'), justify='center')
texto_ciudad.pack(padx=30, pady=30)

obtener_clima = Button(ventana, text='Obtener clima', width=15, height=1, bg='light goldenrod', font=('Courier', 12, 'normal'), command= lambda: clima_JSON(texto_ciudad.get()))
obtener_clima.pack()

ciudad = Label(font=('Courier', 20, 'normal'))
ciudad.pack(padx=20, pady=20)

temperatura = Label(font=('Courier', 40, 'normal'))
temperatura.pack(padx=10, pady=10)

descripcion = Label(font=('Courier', 20, 'normal'))
descripcion.pack(padx=1, pady=10)

ventana.mainloop()