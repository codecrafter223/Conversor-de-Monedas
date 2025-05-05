from tkinter import *
from tkinter import ttk

# Crear la ventana principal
root = Tk()
root.geometry("350x350")
frame = Frame(root)
frame.pack()

# Variables para almacenar la opción seleccionada
moneda_origen = StringVar()
moneda_destino = StringVar()

# Función para convertir moneda
def convertir():
    try:
        cantidad = float(cantidad_entry.get())
        origen = moneda_origen.get()
        destino = moneda_destino.get()
        
        # Lógica de conversión
        if origen == "EUR" and destino == "USD":
            resultado = cantidad * 1.1  # Ejemplo: 1 EUR = 1.1 USD
        elif origen == "USD" and destino == "EUR":
            resultado = cantidad * 0.9  # Ejemplo: 1 USD = 0.9 EUR
        else:
            resultado = cantidad  # Si es la misma moneda
        
        resultado_entry.delete(0, END)  # Limpiar el resultado anterior
        resultado_entry.insert(0, str(resultado))  # Mostrar el nuevo resultado
    except ValueError:
        resultado_entry.delete(0, END)  # Limpiar el resultado en caso de error
        resultado_entry.insert(0, "Error")  # Mostrar mensaje de error

# Labels
origen_label = Label(frame, text="Moneda de origen")
origen_label.grid(row=1, column=1)

# Combobox para seleccionar la moneda de origen
combobox_origen = ttk.Combobox(frame, textvariable=moneda_origen)
combobox_origen['values'] = ("EUR", "USD")  # Opciones del Combobox
combobox_origen.grid(row=2, column=1)  # Colocar el Combobox debajo del Label

destino_label = Label(frame, text="Moneda de destino")
destino_label.grid(row=3, column=1)

# Combobox para seleccionar la moneda de destino
combobox_destino = ttk.Combobox(frame, textvariable=moneda_destino)
combobox_destino['values'] = ("EUR", "USD")  # Opciones del Combobox
combobox_destino.grid(row=4, column=1)  # Colocar el Combobox debajo del Label

# Label y Entry para ingresar la cantidad a convertir
cantidad_label = Label(frame, text="Cantidad a convertir")
cantidad_label.grid(row=5, column=1)

cantidad_entry = Entry(frame)
cantidad_entry.grid(row=6, column=1, pady=10)

resultado_label = Label(frame, text="Resultado")
resultado_label.grid(row=8, column=1, pady=10)

# Entry para mostrar la cantidad convertida
resultado_entry = Entry(frame)
resultado_entry.grid(row=9, column=1)

# Botón para convertir
convertir_button = Button(frame, text="Convertir", command=convertir)
convertir_button.grid(row=7, column=1, pady=10)

root.mainloop()
