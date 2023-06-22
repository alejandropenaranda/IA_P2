import tkinter as tk
import sys
# Crea la ventana principal
ventana = tk.Tk()
ventana.geometry("400x130")
ventana.resizable(False, False)
ventana.eval('tk::PlaceWindow . center')
ventana.title("Smart Horses (Elección de dificultad)")

# Crear una etiqueta con el texto"
etiqueta = tk.Label(ventana, text="Indique la dificultad en la que desea jugar")
etiqueta.pack()

# Crear una variable para almacenar la respuesta del usuario
var = tk.StringVar()
var.set(0)

# Crear dos botones de radio con las opciones de informada y no informada
radio1 = tk.Radiobutton(ventana, text="Principiante", variable=var, value="principiante")
radio2 = tk.Radiobutton(ventana, text="Amateur", variable=var, value="amateur")
radio3 = tk.Radiobutton(ventana, text="Experto", variable=var, value="experto")
radio1.pack()
radio2.pack()
radio3.pack()

def enviar():
            global dificultad
            dificultad = var.get()
            print(dificultad)
            if dificultad != 'principiante' and dificultad != 'amateur' and dificultad != 'experto':
                sys.exit()
            ventana.destroy()

# Crear un boton que llame a la funcion mostrar_opciones
boton = tk.Button(ventana, text="Continuar", command=enviar)
boton.pack()


# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()