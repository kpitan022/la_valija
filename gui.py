from os import listdir, remove
import pathlib
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, font
import cv2
from PIL import Image

xI, yI, xF, yF = 0, 0, 0, 0
interruptor = False
# img=cv2.imread('Qwe.jpeg')


def dibujar_rectangulo(event, x, y, flags, param):
    global xI, yI, xF, yF, interruptor
    if event == cv2.EVENT_LBUTTONDOWN:
        xI, yI = x, y
        interruptor = False
    elif event == cv2.EVENT_LBUTTONUP:
        xF, yF = x, y
        interruptor = True
        recorte = img[yI:yF, xI:xF]
        if 'recorte.jpg' in listdir('./'):
            remove('recorte.jpg')
        cv2.imwrite("recorte.jpg", recorte)
        # cv2.imshow('imagen',recorte)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


def recorte():
    global img
    filename = filedialog.askopenfilename(
        title="Seleccione la imagen a recortar",
        filetypes=(("all files", "*.*"), ("jpeg files", "*.jpeg"),
                   ("jpg files", "*.jpg"), ("png files",
                                            "*.png"), ("bmp files", "*.bmp")))
    foto_path.set(filename)
    # img=cv2.imread('Qwe.jpeg')
    img = cv2.imread(str(foto_path.get()))
    if len(foto_path.get()) != 0:
        cv2.namedWindow('Pulse Esc para aceptar')
        cv2.setMouseCallback('Pulse Esc para aceptar', dibujar_rectangulo)
        while True:
            img = cv2.imread(str(foto_path.get()))
            if interruptor == True:
                cv2.rectangle(img, (xI, yI), (xF, yF), (0, 0, 0), 2)
            cv2.imshow('Pulse Esc para aceptar', img)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break

        cv2.destroyAllWindows()


def ruta_descarga():
    filename = filedialog.askdirectory(
        title="Seleccione la ruta de descarga ", )
    carpeta.set(filename)


def nueva_credencial(nombre, domicilio, numero_socio, dni, anio):
    if len(nombre.get()) == 0 or len(domicilio.get()) == 0 or len(
            numero_socio.get()) == 0 or len(dni.get()) == 0:
        messagebox.showerror("Error", "No puede dejar campos vacios")
        return

    # preguntar ruta de descarga
    #Leer imagen
    img = cv2.imread('credencial.jpeg')

    #Características del texto
    # nombre = no
    ubicacion_nombre = (327, 116)
    # domicilio = "Calle falsa 123"
    ubicacion_domicilio = (346, 147)
    # numero_socio = "123456789"
    ubicacion_numero_socio = (358, 189)
    # dni= "12345678"
    ubicacion_dni = (300, 227)
    ubicacion_anio = (296, 252)
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    tamañoLetra = 0.9
    colorLetra = (0, 0, 0)
    grosorLetra = 1

    #Escribir texto
    cv2.putText(img, dni.get(), ubicacion_dni, font, tamañoLetra, colorLetra,
                grosorLetra)
    cv2.putText(img,
                nombre.get().title(), ubicacion_nombre, font, tamañoLetra,
                colorLetra, grosorLetra)
    cv2.putText(img,
                domicilio.get().title(), ubicacion_domicilio, font,
                tamañoLetra, colorLetra, grosorLetra)
    cv2.putText(img, numero_socio.get(), ubicacion_numero_socio, font,
                tamañoLetra, colorLetra, grosorLetra)
    cv2.putText(img, anio.get(), ubicacion_anio, font, tamañoLetra, colorLetra,
                grosorLetra)
    # preguntar si la imagen existe

    if len(carpeta.get()) != 0:
        carpeta_guardado = pathlib.Path(carpeta.get(),
                                        nombre.get().title() + ".jpeg")
        # comprueba si la credencial ya existe y si existe la borra
        if carpeta_guardado.exists():
            remove(str(carpeta_guardado))
        #Guardar imagen
        cv2.imwrite(
            str(carpeta_guardado),
            img,
        )
        if 'recorte.jpg' in listdir('./'):
            cred = Image.open(str(carpeta_guardado))
            foto = Image.open('recorte.jpg')
            foto_resize = foto.resize((180, 180))
            cred.paste(foto_resize, (30, 20))
            cred.save(str(carpeta_guardado))
            cred.close()
            foto.close()
            remove('recorte.jpg')

        # borrar campos
        nombre.set("")
        domicilio.set("")
        numero_socio.set("")
        dni.set("")
        anio.set("")
        messagebox.showinfo("Credencial",
                            "Credencial guardada en " + str(carpeta_guardado))

    else:
        messagebox.showerror("Error", "No selecciono la ruta de descarga")
    #Mostrar imagen
    # cv2.imshow('imagen',img)
    # cv2.waitKey(0)
    cv2.destroyAllWindows()


# crear ventana
ventana = tk.Tk()
ventana.title("Credenciales")
# ventana.geometry("300x200")
ventana.resizable(0, 0)
# fuente de la letra
fuente = font.Font(family='Helvetica', size=12, weight='bold')

# crear variables tkinter
nombre_var = tk.StringVar()
domicilio_var = tk.StringVar()
socio_var = tk.StringVar()
dni_var = tk.StringVar()
carpeta = tk.StringVar()
foto_path = tk.StringVar()
anio_var = tk.StringVar()

# crear etiquetas
etiqueta_nombre = ttk.Label(ventana, font=fuente, text=str("Nombre"))
etiqueta_domicilio = ttk.Label(ventana, font=fuente, text="Domicilio:")
etiqueta_socio = ttk.Label(ventana, font=fuente, text="N socio:")
etiqueta_dni = ttk.Label(ventana, font=fuente, text="D.N.I:")
etiqueta_anio = ttk.Label(ventana, font=fuente, text="Año:")

# empaquetar etiquetas
etiqueta_nombre.grid(row=1, column=0)
etiqueta_domicilio.grid(row=2, column=0)
etiqueta_socio.grid(row=3, column=0)
etiqueta_dni.grid(row=4, column=0)
etiqueta_anio.grid(row=5, column=0)

# crear entradas
nombre = ttk.Entry(ventana, font=fuente, textvariable=nombre_var)
domicilio = ttk.Entry(ventana, font=fuente, textvariable=domicilio_var)
socio = ttk.Entry(ventana, font=fuente, textvariable=socio_var)
dni = ttk.Entry(ventana, font=fuente, textvariable=dni_var)
anio = ttk.Entry(ventana, font=fuente, textvariable=anio_var)

# grilla de entradas
nombre.grid(row=1, column=1)
domicilio.grid(row=2, column=1)
socio.grid(row=3, column=1)
dni.grid(row=4, column=1)
anio.grid(row=5, column=1)

# guardar datos en variables de tkinter

nombre_var.set(nombre.get())
domicilio_var.set(domicilio.get())
socio_var.set(socio.get())
dni_var.set(dni.get())

#  boton para mostrar datos

crear_boton = ttk.Button(ventana,
                         text="Crear credencial",
                         command=lambda: nueva_credencial(
                             nombre_var,
                             domicilio_var,
                             socio_var,
                             dni_var,
                             anio_var,
                         ))
crear_boton.grid(row=8, column=0, columnspan=2, sticky="ew")

# boton cargar imagen
boton_cargar = ttk.Button(ventana,
                          text="Cargar imagen",
                          command=lambda: recorte())
boton_cargar.grid(row=7, column=0, columnspan=2, sticky="ew")

# boton filepath
button_explore = ttk.Button(
    ventana,
    text="Ruta de descarga",
    command=ruta_descarga,
)
button_explore.grid(row=6, column=0, columnspan=2, sticky="ew")
# msg = ttk.Label(ventana, font=fuente, textvariable=carpeta)

ventana.mainloop()