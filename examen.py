from tkinter import ttk
from tkinter import *

import sqlite3

class Product:

    dt = "examen.db"

    def __init__(self, window):
        self.wind = window
        self.wind.title("Lengua Española")

        frame = LabelFrame(self.wind, text = "")
        frame.grid(row = 1, column = 0, pady = 10, sticky = W + E)

        Label(self.wind, text = "Bienvenidos al nuevo examen de Lengua Española (2020)").grid(row = 0, columnspan = 2)
        #name
        self.name = Label(frame, text = "Inserte su nombre y su apellido: ").grid(row = 1, column = 0, columnspan = 1)
        self.name = Entry(frame)
        self.name.grid(row = 1, column = 1, sticky = W + E)

        #edad
        self.edad = Label(frame, text = "Edad: ").grid(row = 1, column = 2)
        self.edad = Entry(frame)
        self.edad.grid(row = 1, column = 3)

        #Fecha
        self.fecha = Label(frame, text = "Fecha: ").grid(row = 1, column = 4)
        self.fecha = Entry(frame)
        self.fecha.grid(row = 1, column = 5)

        self.mensaje = Label(frame, text = "Ahora conteste las siguientes prguntas")
        self.mensaje.grid(row = 5, columnspan = 10)

         #preguntas
        self.one = Label(frame, text = "Cual es el nombre de la Capital de Republica Dominicana? ").grid(row = 6, column = 1)
        self.one = Entry(frame)
        self.one.grid(row = 7, column = 1, sticky = W + E)

        self.two = Label(frame, text = "Que dia se Libro la independencia en Republica Dominicana? ").grid(row = 8, column = 1)
        self.two = Entry(frame)
        self.two.grid(row = 9, column = 1, sticky = W + E)

        self.three = Label(frame, text = "Cuales son los padres de la patria de Republica Dominicana? ").grid(row = 10, column = 1)
        self.three = Entry(frame)
        self.three.grid(row = 13, column = 1, sticky = W + E)

        self.four = Label(frame, text = "Cual es el prisidente actual de Republica Dominicana? ").grid(row = 14, column = 1)
        self.four = Entry(frame)
        self.four.grid(row = 15, column = 1, sticky = W + E)

        self.five = Label(frame, text = "Cual es la privincia mas grande de Republica Dominicana? ").grid(row = 16, column = 1)
        self.five = Entry(frame)
        self.five.grid(row = 17, column = 1, sticky = W + E)

        #falso y verdadero
        self.II = Label(frame, text ="Escribe V si la pregunta es verdadera, o escribe F si la pregunta es falsa").grid(row = 18, columnspan = 5)
        
        self.uno = Label(frame,  text = "La bandera de la Republica Dominicana es azul? ").grid(row = 19, column = 1, sticky = W + E)
        self.uno = Entry(frame)
        self.uno.grid(row = 19, column = 2)

        self.dos = Label(frame, text = "La Republica Dominicana tiene 31 privincias? ").grid(row = 20, column = 1)
        self.dos = Entry(frame)
        self.dos.grid(row = 20, column = 2)

        self.tres = Label(frame, text = "La tierra es redonda? ").grid(row = 21, column = 1) 
        self.tres = Entry(frame)
        self.tres.grid(row = 21, column = 2)

        #Finalizar
        Button(self.wind, text = "Finalizar").grid(row = 20, columnspan = 2, sticky = W + E)

if __name__ == "__main__":
    window = Tk()
    aplication = Product(window)
    window.mainloop()