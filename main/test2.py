import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Formulario")
ventana.geometry("1920x1080")

# ventana.attributes("-fullscreen", True)

# --- Fondo con imagen ---
imagen_fondo = Image.open("main/fondo2.jpg")
imagen_fondo = imagen_fondo.resize((1920, 1080), Image.Resampling.LANCZOS)
fondo = ImageTk.PhotoImage(imagen_fondo)

canvas = tk.Canvas(ventana, width=1920, height=1080)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=fondo, anchor="nw")

# --- Frame con formulario encima del fondo ---
formulario = tk.Frame(ventana, bg="#43b0f6")
formulario.place(relx=0.5, rely=0.4, anchor="center")

# Fuente labels
fuente = ("Lato", 15, "bold")

# Variables de entrada

entry_var1 = tk.StringVar()
entry_var2 = tk.StringVar()

def guardar_datos():
    valor1 = entry_var1.get()
    valor2 = entry_var2.get()
    valoreseleccion = seleccion.get()

    if valor1 == "" or valor2 == "":
        mostrar_mensaje_temporal("Faltan datos")
    else:
        print(valor1," ", valor2, " ", valoreseleccion)
        mostrar_mensaje_temporal("Datos guardados correctamente")
        # aca se puede almacenar/ crear objeto/
        entry_var1.set("")
        entry_var2.set("")
        selector.current(0)

    
    
    

# Pruebas seleccion de opciones

opciones = ["Opcion 1", "Opcion 2", "Opcion 3", "Opcion 4", "Opcion 5", "Opcion 6"]

seleccion = tk.StringVar() # variable que almacena la selección
selector = ttk.Combobox(formulario, textvariable=seleccion, values=opciones, width=29, font=fuente)
selector.current(0)
selector.grid(row=3, column=3, padx=10, pady=5)

def mostrar():
    print("Elegiste:", seleccion.get())



# Prueba mensaje emergente

def mostrar_mensaje():
    messagebox.showinfo("Título del mensaje", "Este es un comentario emergente")


def mostrar_mensaje_temporal(Texto):
    popup = tk.Toplevel()
    popup.title("Aviso")
    popup.geometry("250x100")
    popup.configure(bg="white")

    mensaje = tk.Label(popup, text= Texto, bg="white", font=("Lato", 12))
    mensaje.pack(expand=True)

    # Cerrar después de 3 segundos (3000 milisegundos)
    popup.after(3000, popup.destroy)



# Crear etiquetas y entradas una por una
label1 = tk.Label(formulario, text="Etiqueta 1", bg="#43b0f6", fg="black", font= fuente)
entry1 = tk.Entry(formulario, font=fuente, width=30, textvariable= entry_var1)

label2 = tk.Label(formulario, text="Etiqueta 2", bg="#43b0f6", fg="black", font= fuente)
entry2 = tk.Entry(formulario, font=fuente, width=30, textvariable= entry_var2)

label3 = tk.Label(formulario, text="Etiqueta 3", bg="#43b0f6", fg="black", font= fuente)
entry3 = tk.Entry(formulario, font=fuente, width=30)

label4 = tk.Label(formulario, text="Etiqueta 4", bg="#43b0f6", fg="black", font= fuente)
entry4 = tk.Entry(formulario, font=fuente, width=30)

label5 = tk.Label(formulario, text="Etiqueta 5", bg="#43b0f6", fg="black", font= fuente)
entry5 = tk.Entry(formulario, font=fuente, width=30)

label6 = tk.Label(formulario, text="Etiqueta 6", bg="#43b0f6", fg="black", font= fuente)
entry6 = tk.Entry(formulario, font=fuente, width=30)

label7 = tk.Label(formulario, text="Etiqueta 7", bg="#43b0f6", fg="black", font= fuente)
entry7 = tk.Entry(formulario, font=fuente, width=30)

label8 = tk.Label(formulario, text="Etiqueta 8", bg="#43b0f6", fg="black", font= fuente)
#entry8 = tk.Entry(formulario, font=fuente, width=30)

# Organizar en 2 filas de 4 columnas
label1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry1.grid(row=1, column=0, padx=10, pady=5)

label2.grid(row=0, column=1, padx=10, pady=5, sticky="w")
entry2.grid(row=1, column=1, padx=10, pady=5)

label3.grid(row=0, column=2, padx=10, pady=5, sticky="w")
entry3.grid(row=1, column=2, padx=10, pady=5)

label4.grid(row=0, column=3, padx=10, pady=5, sticky="w")
entry4.grid(row=1, column=3, padx=10, pady=5)

label5.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry5.grid(row=3, column=0, padx=10, pady=5)

label6.grid(row=2, column=1, padx=10, pady=5, sticky="w")
entry6.grid(row=3, column=1, padx=10, pady=5)

label7.grid(row=2, column=2, padx=10, pady=5, sticky="w")
entry7.grid(row=3, column=2, padx=10, pady=5)

label8.grid(row=2, column=3, padx=10, pady=5, sticky="w")
#entry8.grid(row=3, column=3, padx=10, pady=5)

# Botón centrado
boton = tk.Button(ventana, text="Guardar", font=("Lato",50, "bold"), command= guardar_datos)
boton.place(relx=0.5, rely=0.9, anchor="center")

ventana.mainloop()


'''
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario")
ventana.configure(bg='gray')
ventana.geometry("1920x1080")  # Tamaño aproximado basado en la imagen

# Estilo para etiquetas y entradas
etiqueta_font = ("Lato", 15)
entrada_font = ("Lato", 15)

imagen_fondo = Image.open("fondo1.jpg")
fondo_tk = ImageTk.PhotoImage(imagen_fondo)

canvas = tk.Canvas(ventana)
canvas.pack(fill="both", expand=True)

canvas.create_image(0,0,image=fondo_tk, anchor="nw")

# Crear el frame central
frame = tk.Frame(ventana, bg='', highlightthickness=0)
frame.place(relx = 0.5, rely= 0.4, anchor="center")
#canvas.create_window(0, 0, anchor="nw", window=frame, width=1920, height=500)
#frame.pack(pady=0)

# Fila 1
label1 = tk.Label(frame, text="Etiqueta 1", font=etiq, font= fuenteueta_font)
label1.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="w")
entry1 = tk.Entry(frame, font=entrada_font, width=25, bd=3, relief="flat", justify="left")
entry1.grid(row=1, column=0, padx=20, pady=(0, 15), ipady=10)

label2 = tk.Label(frame, text="Etiqueta 2", bg='gray', font= fuente, fg='black', font=etiqueta_font)
label2.grid(row=0, column=1, padx=20, pady=(10, 0), sticky="w")
entry2 = tk.Entry(frame, font=entrada_font, width=25, bd=3, relief="flat", justify="left")
entry2.grid(row=1, column=1, padx=20, pady=(0, 15), ipady=10)

label3 = tk.Label(frame, text="Etiqueta 3", bg='gray', font= fuente, fg='black', font=etiqueta_font)
label3.grid(row=0, column=2, padx=20, pady=(10, 0), sticky="w")
entry3 = tk.Entry(frame, font=entrada_font, width=25, bd=3, relief="flat", justify="left")
entry3.grid(row=1, column=2, padx=20, pady=(0, 15), ipady=10)

label4 = tk.Label(frame, text="Etiqueta 4", bg='gray', font= fuente, fg='black', font=etiqueta_font)
label4.grid(row=0, column=3, padx=20, pady=(10, 0), sticky="w")
entry4 = tk.Entry(frame, font=entrada_font, width=25, bd=3, relief="flat", justify="left")
entry4.grid(row=1, column=3, padx=20, pady=(0, 15), ipady=10)

# Fila 2
label5 = tk.Label(frame, text="Etiqueta 5", bg='gray', font= fuente, fg='black', font=etiqueta_font)
label5.grid(row=2, column=0, padx=20, pady=(10, 0), sticky="w")
entry5 = tk.Entry(frame, font=entrada_font, width=25, bd=3, relief="flat", justify="left")
entry5.grid(row=3, column=0, padx=20, pady=(0, 15), ipady=10)

label6 = tk.Label(frame, text="Etiqueta 6", bg='gray', font= fuente, fg='black', font=etiqueta_font)
label6.grid(row=2, column=1, padx=20, pady=(10, 0), sticky="w")
entry6 = tk.Entry(frame, font=entrada_font, width=25, bd=3, relief="flat", justify="left")
entry6.grid(row=3, column=1, padx=20, pady=(0, 15), ipady=10)

label7 = tk.Label(frame, text="Etiqueta 7", bg='gray', font= fuente, fg='black', font=etiqueta_font)
label7.grid(row=2, column=2, padx=20, pady=(10, 0), sticky="w")
entry7 = tk.Entry(frame, font=entrada_font, width=25, bd=3, relief="flat", justify="left")
entry7.grid(row=3, column=2, padx=20, pady=(0, 15), ipady=10)

label8 = tk.Label(frame, text="Etiqueta 8", bg='gray', font= fuente, fg='black', font=etiqueta_font)
label8.grid(row=2, column=3, padx=20, pady=(10, 0), sticky="w")
entry8 = tk.Entry(frame, font=entrada_font, width=25, bd=3, relief="flat", justify="left")
entry8.grid(row=3, column=3, padx=20, pady=(0, 15), ipady=10)

# Crear el botón
boton = tk.Button(ventana, text="Boton", font=("Arial",, font= fuente 18, "bold"), bg='white', fg='black', padx=40, pady=10)
boton.pack(pady=30)

# Ejecutar la ventana
ventana.mainloop()
'''