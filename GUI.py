from tkinter import *
import tkinter
#enconding: utf-8

raiz = Tk()

raiz.title("BOT NEW COINS")

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

cuadroNombre=Entry(miFrame) 
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config()  #Configuración de parametros visuales

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=5, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=7, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=9, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=10, column=1, padx=10, pady=10)

# ----------------------------------------------------------------

apellidoLabel=Label(miFrame, text="COLOQUE SU API DE BINANCE AQUI:") #TITULO
apellidoLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame, text="API Key:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="API Secret:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="COLOQUE SU API DE TELEGRAM AQUI:") #TITULO
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Telegram Key:")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Telegram Secret:")
direccionLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="COLOQUE EL MONTO QUE DESEA UTILIZAR POR OPERACION:") #TITULO
apellidoLabel.grid(row=6, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Monto en BUSD (Min 20 BUSD):")
apellidoLabel.grid(row=7, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="COLOQUE LOS PARAMETROS DE SU GESTIÓN DEL RIESGO:") #TITULO
apellidoLabel.grid(row=8, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Take Profit:")
direccionLabel.grid(row=9, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Stop Loss:")
direccionLabel.grid(row=10, column=0, sticky="e", padx=10, pady=10)

submit_button = Button(raiz, text = "Submit").pack()


raiz.mainloop()
