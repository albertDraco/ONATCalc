#! /usr/bin/env python

from tkinter import *
import math
from tkinter import messagebox
from tkinter.filedialog import SaveAs, asksaveasfile
import tkinter.font as tkFont
import os, errno, sys, re
from os import path
""" import csv, openpyxl, getpass
from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.utils import get_column_letter """


# funciones -------------------

def resource_path(relative_path): # funcion imprescindible para guardar las imagenes en el ejecutable
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def borrar_campos():
    ingreso_bruto.set("")
    retenciones.set("")
    representacion.set("")
    lista.delete(0, END)
    checkbox_1.deselect()
    checkbox_2.deselect()
    
def salir():
    valor=messagebox.askokcancel("Salir", "Desea salir de la Aplicación?")
    if valor:
        root.destroy()
        
def guardar():
    archivos=[('Documento de texto', '*.txt')]
    
    file=asksaveasfile(filetypes=archivos, defaultextension=archivos)
    
    contenido=lista.get(0, END)
    
    file.writelines(contenido)
    file.close()
    
    
def borrar_item():
    lista.delete(ANCHOR)
    
def borrar_lista():
    lista.delete(0, END)
    
def acerca_de():
    messagebox.showinfo("Cálculo impuestos ONAT", "Versión 1.0.1 (beta)\n19 de enero 2022\nPython 3.10.2\nDiseño y programación: Alberto Hernández Cáceres\nALyS Design Group\n\nEn memoria de Lourdes, que trató de enseñarme cómo funcionaban los impuestos y no lo aprendí hasta ahora que tuve la necesidad.")

def licencia():
    messagebox.showinfo("Licencia", "Software totalmente gratuito")
    
     

def calcular():
    
    
      
    
    try:
        ing_bruto=int(ingreso_bruto.get())                 
        
            
        ret=int(retenciones.get())
        
        porciento_representacion=int(representacion.get())      
                
        while ing_bruto>=0:            
         
            break   
                  
        while ret>=0:
        
            break
        
        while porciento_representacion>=0:
        
            break
        
    except:
        messagebox.showerror("Error", "Llene todos los campos con un número mayor o igual a cero")
 
    calculo_representacion=ing_bruto*porciento_representacion/100
    lista.insert(END, f"Ingreso bruto: {ing_bruto}")
    lista.insert(END, f"Representación del {porciento_representacion}%: {calculo_representacion}")    
    
    deducido=ing_bruto - calculo_representacion
    lista.insert(END, f"Deducido: {deducido:.2f}")
    #print(f"deducido: {deducido}")        
        
    ret_tributaria=math.ceil(deducido*ret/100)
    lista.insert(END, f"Retención tributaria del {ret}%: {ret_tributaria}")       
   
    total_a_pagar=int(deducido - ret_tributaria)
    lista.insert(END, f"Total a pagar: {total_a_pagar}")
    
    ingresos_obtenidos=total_a_pagar
    lista.insert(END, f"Ingresos obtenidos: {ingresos_obtenidos}")
    
    
    min_exento=39120    
       
    gastos_actividad=math.floor(ingresos_obtenidos*.20)    
       
    base_imponible=ingresos_obtenidos - gastos_actividad - min_exento        
    
    #lista.insert(END, f"Total retenciones: {ret_tributaria}")
    
    lista.insert(END, f"Mínimo exento: {min_exento}")
    
    lista.insert(END, f"Gastos deducibles por actividad: {gastos_actividad}")
    
    if base_imponible>0:
        lista.insert(END, f"Base imponible: {base_imponible}")       
        
    else:
        lista.insert(END, "No debe nada")
    
    #-- Tramo de 0 a 10000-----------
    
    if base_imponible>=0 and base_imponible<=10000:
        modulo1=math.ceil(base_imponible)
        lista.insert(END, f"Base imponible de 0 a 10000: {modulo1}")
        
        importe_1=math.floor(modulo1*.15)
        lista.insert(END, f"Importe de 0 a 10000: {importe_1}")
        
        importe_total_1=importe_1
        lista.insert(END, f"Importe total segun escala progresiva: {importe_total_1}")
        
    
        impuesto_total_1=importe_total_1 - ret_tributaria
        #lista.insert(END, f"el total a pagar es: {impuesto_total_1}")
        if impuesto_total_1<0:
            lista.insert(END, "No debe nada")
        else:
          lista.insert(END, f"El total a pagar es: {impuesto_total_1}")       
          
        
    if base_imponible<0:
        #lista.insert(END, f"La ONAT le debe: {base_imponible*-1}")
        messagebox.showinfo(message=f"La ONAT te debe {base_imponible*-1} pesos, pero creo que no lo van a devolver", title="informacion")
          
        
        
        #--- Tramo de 10000 a 20000---------
    
    if base_imponible>=10000 and base_imponible<=20000:
        lista.insert(END, "El importe de 0 a 10000 es: 1500")        
        
        modulo2=math.ceil(base_imponible-10000)
        lista.insert(END, f"Base imponible de 10000 a 20000: {modulo2}")
            
        importe_2=math.floor(modulo2*.20)
        lista.insert(END, f"Importe de 10000 a 20000: {importe_2}")
        
        importe_total_2=importe_2 + 1500
        lista.insert(END, f"Importe según escala progresiva: {importe_total_2}")
        
        
        impuesto_total_2=importe_total_2 - ret_tributaria
        
        #----bonificaciones de 10000 a 20000-------------------
        
        if (x.get()==1) & (y.get()==0):
            check=int(impuesto_total_2*.05)
            if check<0:
                lista.insert(END, "No debe nada")
            else:            
                lista.insert(END, f"Bonificado con 5% por pronto pago: {check:.2f}")
                lista.insert(END, f"El total a pagar es: {impuesto_total_2-check}")
                
                ingreso_neto=ingresos_obtenidos - impuesto_total_2 - check
                lista.insert(END, f"El ingreso neto es: {ingreso_neto}")
        
        elif (x.get()==0) & (y.get()==1):
            check=float(impuesto_total_2*.03)
            if check<0:
                lista.insert(END, "No debe nada")
            else:            
                lista.insert(END, f"Bonificado con 3% por pago online: {check:.2f}")
                lista.insert(END, f"El total a pagar es: {impuesto_total_2-check}")
                
                ingreso_neto=ingresos_obtenidos - impuesto_total_2 - check
                lista.insert(END, f"El ingreso neto es: {ingreso_neto}")       
        
        elif (x.get()==1) & (y.get()==1):
            check=int(impuesto_total_2*.08)
            if check<0:
                lista.insert(END, "No debe nada")
            else:            
                lista.insert(END, f"Bonificado con 8% por pronto pago y pago online: {check}")
                lista.insert(END, f"El total a pagar es: {impuesto_total_2-check}")
                
                ingreso_neto=ingresos_obtenidos - impuesto_total_2 - check
                lista.insert(END, f"El ingreso neto es: {ingreso_neto}")        
        
        else:
            if impuesto_total_2<0:
                lista.insert(END, "No debe nada")
            else:
            
                ingreso_neto=ingresos_obtenidos - impuesto_total_2
                lista.insert(END, f"El total a pagar es: {impuesto_total_2}")
                lista.insert(END, f"El ingreso neto es: {ingreso_neto}")
            
        #----bonificaciones de 10000 a 20000------------------- 
        
               
        
                      
        #-- Tramo de 20000 a 30000----------

    if base_imponible>=20000 and base_imponible<=30000:        
        lista.insert(END, "El importe de 0 a 10000 es: 1500")
        lista.insert(END, "El importe de 10000 a 20000 es: 2000")
                    
        modulo3=math.ceil(base_imponible-20000)
        
           
        importe_3=math.floor(modulo3*.30)
        lista.insert(END, f"El importe de 20000 a 30000 es {importe_3}")
        lista.insert(END, f"La base imponible de 20000 a 30000 es {modulo3}")
        
        importe_total_3=importe_3 + 1500 + 2000
        lista.insert(END, f"Importe total según escala progresiva: {importe_total_3}")
        
        
        impuesto_total_3=importe_total_3 - ret_tributaria
        
        
        #----bonificaciones de 20000 a 30000-------------------
        
        if (x.get()==1) & (y.get()==0):
            check=int(impuesto_total_3*.05)
            if check<0:
                lista.insert(END, "No debe nada")
            else:            
                lista.insert(END, f"Bonificado con 5% por pronto pago: {check:.2f}")
                lista.insert(END, f"El total a pagar es: {impuesto_total_3-check}")
                
                ingreso_neto=ingresos_obtenidos - impuesto_total_3 - check
                lista.insert(END, f"El ingreso neto es: {ingreso_neto}")
        
        elif (x.get()==0) & (y.get()==1):
            check=float(impuesto_total_3*.03)
            if check<0:
                lista.insert(END, "No debe nada")
            else:            
                lista.insert(END, f"Bonificado con 3% por pago online: {check:.2f}")
                lista.insert(END, f"El total a pagar es: {impuesto_total_3-check}")
                
                ingreso_neto=ingresos_obtenidos - impuesto_total_3 - check
                lista.insert(END, f"El ingreso neto es: {ingreso_neto}")       
        
        elif (x.get()==1) & (y.get()==1):
            check=int(impuesto_total_3*.08)
            if check<0:
                lista.insert(END, "No debe nada")
            else:            
                lista.insert(END, f"Bonificado con 8% por pronto pago y pago online: {check:.2f}")
                lista.insert(END, f"El total a pagar es: {impuesto_total_3-check}")
                
                ingreso_neto=ingresos_obtenidos - impuesto_total_3 - check
                lista.insert(END, f"El ingreso neto es: {ingreso_neto}")        
        
        else:
            if impuesto_total_3<0:
                lista.insert(END, "No debe nada")
            else:
            
                ingreso_neto=ingresos_obtenidos - impuesto_total_3
                lista.insert(END, f"El total a pagar es: {impuesto_total_3}")
                lista.insert(END, f"El ingreso neto es: {ingreso_neto}")
            
        #----bonificaciones de 20000 a 30000-------------------
        
        
        
                
        #-- Tramo de 30000 a 50000----------

    if base_imponible>=30000 and base_imponible<=50000:        
        lista.insert(END, "El importe de 0 a 10000 es: 1500")
        lista.insert(END, "El importe de 10000 a 20000 es: 2000")
        lista.insert(END, "El importe de 20000 a 30000 es: 3000")
            
        modulo4=math.ceil(base_imponible-30000)
        lista.insert(END, f"La base imponible de 30000 a 50000 es {modulo4}")
        #print(f"la base imponible de 30000 a 50000 es {modulo4}")    
        importe_4=math.floor(modulo4*.40)
        lista.insert(END, f"El importe de 30000 a 50000 es {importe_4}")
        #print(f"el importe de 30000 a 50000 es {importe_4}")
        importe_total_4=importe_4 + 1500 + 2000 + 3000
        lista.insert(END, f"Importe total según escala progresiva: {importe_total_4}")
        #print(f"importe total segun escala progresiva: {importe_total_4}")
        
        impuesto_total_4=importe_total_4 - ret_tributaria
        
        
        #----bonificaciones de 30000 a 50000-------------------
        
        if (x.get()==1) & (y.get()==0):
            check=int(impuesto_total_4*.05)
            if check<0:
                lista.insert(END, "No debe nada")
            else:            
                lista.insert(END, f"Bonificado con 5% por pronto pago: {check:.2f}")
                lista.insert(END, f"El total a pagar es: {impuesto_total_4-check}")
                
                ingreso_neto=ingresos_obtenidos - impuesto_total_4 - check
                lista.insert(END, f"El ingreso neto es: {ingreso_neto}")
        
        elif (x.get()==0) & (y.get()==1):
            check=int(impuesto_total_4*.03)
            if check<0:
                lista.insert(END, "No debe nada")
            else:            
                lista.insert(END, f"Bonificado con 3% por pago online: {check:.2f}")
                lista.insert(END, f"El total a pagar es: {impuesto_total_4-check}")
                
                ingreso_neto=ingresos_obtenidos - impuesto_total_4 - check
                lista.insert(END, f"El ingreso neto es: {ingreso_neto}")       
        
        elif (x.get()==1) & (y.get()==1):
            check=int(impuesto_total_4*.08)
            if check<0:
                lista.insert(END, "No debe nada")
            else:            
                lista.insert(END, f"Bonificado con 8% por pronto pago y pago online: {check:.2f}")
                lista.insert(END, f"El total a pagar es: {impuesto_total_4-check}")
                
                ingreso_neto=ingresos_obtenidos - impuesto_total_4 - check
                lista.insert(END, f"El ingreso neto es: {ingreso_neto}")        
        
        else:
            if impuesto_total_4<0:
                lista.insert(END, "No debe nada")
            else:
            
                ingreso_neto=ingresos_obtenidos - impuesto_total_4
                lista.insert(END, f"El total a pagar es: {impuesto_total_4}")
                lista.insert(END, f"El ingreso neto es: {ingreso_neto}")
            
        #----bonificaciones de 30000 a 50000-------------------
        
        

        #-- Tramo mayor de 50000----------

    if base_imponible>=50000:        
        lista.insert(END, "El importe de 0 a 10000 es: 1500")
        lista.insert(END, "El importe de 10000 a 20000 es: 2000")
        lista.insert(END, "El importe de 20000 a 30000 es: 3000")
        lista.insert(END, "El importe de 30000 a 50000 es: 8000")
                    
        modulo5=math.ceil(base_imponible-50000)
        lista.insert(END, f"La base imponible de mas de 50000 es: {modulo5}")
        #print(f"La base imponible de mas de 50000 es: {modulo5}")    
        importe_5=math.ceil(modulo5*.50)
        lista.insert(END, f"El importe de mayor que 50000 es {importe_5}")
        #print(f"el importe de mayor que 50000 es {importe_5}")
        importe_total_5=importe_5 + 1500 + 2000 + 3000 + 8000
        lista.insert(END, f"Importe total según escala progresiva: {importe_total_5}")
        #print(f"importe total segun escala progresiva: {importe_total_5}")
        
        impuesto_total_5=importe_total_5 - ret_tributaria
        
        #----bonificaciones mayor 50000-------------------
        
        if (x.get()==1) & (y.get()==0):
            check=int(impuesto_total_5*.05)
            if check<0:
                lista.insert(END, "No debe nada")
            else:            
                lista.insert(END, f"Bonificado con 5% por pronto pago: {check:.2f}")
                lista.insert(END, f"El total a pagar es: {impuesto_total_5-check}")
                
                ingreso_neto=ingresos_obtenidos - impuesto_total_5 - check
                lista.insert(END, f"El ingreso neto es: {ingreso_neto}")
        
        elif (x.get()==0) & (y.get()==1):
            check=int(impuesto_total_5*.03)
            if check<0:
                lista.insert(END, "No debe nada")
            else:            
                lista.insert(END, f"Bonificado con 3% por pago online: {check:.2f}")
                lista.insert(END, f"El total a pagar es: {impuesto_total_5-check}")
                
                ingreso_neto=ingresos_obtenidos - impuesto_total_5 - check
                lista.insert(END, f"El ingreso neto es: {ingreso_neto}")       
        
        elif (x.get()==1) & (y.get()==1):
            check=int(impuesto_total_5*.08)
            if check<0:
                lista.insert(END, "No debe nada")
            else:            
                lista.insert(END, f"Bonificado con 8% por pronto pago y pago online: {check}")
                lista.insert(END, f"El total a pagar es: {impuesto_total_5-check}")
                
                ingreso_neto=ingresos_obtenidos - impuesto_total_5 - check
                lista.insert(END, f"El ingreso neto es: {ingreso_neto}")        
        
        else:
            if impuesto_total_5<0:
                lista.insert(END, "No debe nada")
            else:
            
                ingreso_neto=ingresos_obtenidos - impuesto_total_5
                lista.insert(END, f"El total a pagar es: {impuesto_total_5}")
                lista.insert(END, f"El ingreso neto es: {ingreso_neto}")
            
        #----bonificaciones mayor que 50000-------------------
        
           

    
# contruccion de GUI -------------------------

root=Tk()

root.title("Cálculo de impuestos ONAT")
#root.iconphoto(False, PhotoImage(file='ALyS.png'))
#root.iconbitmap(path)

path=resource_path("ALyS_logo.png")
fondo=PhotoImage(file=path)
path=resource_path("ALyS_1.ico")
root.iconbitmap(path)

""" fuente_ejemplo_1=tkFont.Font(family="VOXWIDE-SEMIBOLD", size=12, weight="bold", slant="roman")
fuente_ejemplo_2=tkFont.Font(family="VOX-BOLDITALIC", size=12, weight="bold", slant="roman") """

fuente_ejemplo_1=tkFont.Font(family="arial", size=12, weight="bold")
fuente_ejemplo_2=tkFont.Font(family="arial", size=12, weight="bold")


#imagen=PhotoImage(file="img/ALyS_3.png")


# MENU -----------------

barra_menu=Menu(root)
root.config(menu=barra_menu, width=300, height=300)

archivo=Menu(barra_menu, tearoff=0)
archivo.add_command(label="Guardar como", command=guardar)
archivo.add_command(label="Borrar campos", command=borrar_campos)
archivo.add_command(label="Salir", command=salir)

ayuda=Menu(barra_menu, tearoff=0)
ayuda.add_command(label="Licencia", command=licencia)
ayuda.add_command(label="Acerca de...", command=acerca_de)

barra_menu.add_cascade(label="Archivo", menu=archivo)
barra_menu.add_cascade(label="Ayuda", menu=ayuda)


# FIN MENU -------------------------

root.config(bg="#282828")
root.resizable(False, False)
#root.geometry('500x500')

miFrame=Frame()
miFrame.pack()
miFrame.config(bg="#282828")



# campo de ingresar datos -------------------

ingreso_bruto = DoubleVar()
retenciones = DoubleVar()
representacion = IntVar()
ingreso_bruto.set("")  
retenciones.set("")  
representacion.set("") 
    
ingresosLabel=Label(miFrame, text="Ingreso bruto: ", anchor="w")
ingresosLabel.grid(row=0, column=0, pady=10, padx=30, sticky="w")
ingresosLabel.config(bg="#282828", fg="green", font=fuente_ejemplo_1)
ingresosEntrada=Entry(miFrame, textvariable=ingreso_bruto)
ingresosEntrada.grid(row=0, column=1, pady=10, padx=30, sticky="w", columnspan=3)
ingresosEntrada.config(justify="left", bg="#343434", fg="#00ea0b", width=50, font=fuente_ejemplo_2)

representacionLabel=Label(miFrame, text="Porciento de representación: ", anchor="w")
representacionLabel.grid(row=1, column=0, pady=10, padx=30, sticky="w")
representacionLabel.config(bg="#282828", fg="green", font=fuente_ejemplo_1)
representacionEntrada=Entry(miFrame, textvariable=representacion)
representacionEntrada.grid(row=1, column=1, pady=10, padx=30, sticky="w", columnspan=3)
representacionEntrada.config(justify="left", bg="#343434", fg="#00ea0b", width=50, font=fuente_ejemplo_2)

retencionesLabel=Label(miFrame, text="Porciento de retenciones: ", anchor="w")
retencionesLabel.grid(row=2, column=0, pady=10, padx=30, sticky="w")
retencionesLabel.config(bg="#282828", fg="green", font=fuente_ejemplo_1)
retencionesEntrada=Entry(miFrame, textvariable=retenciones)
retencionesEntrada.grid(row=2, column=1, pady=10, padx=30, sticky="w", columnspan=3)
retencionesEntrada.config(justify="left", bg="#343434", fg="#00ea0b", width=50, font=fuente_ejemplo_2)



# boton calcular-----------------------------

botonCalcular=Button(miFrame, text="Calcular", command=calcular)
botonCalcular.grid(row=3, column=3, padx=30, pady=10, sticky='w')
botonCalcular.config(cursor="hand2", font=fuente_ejemplo_1, bg="green", fg="white", width=10)

# boton borrar lista-----------------------------

botonBorrar=Button(miFrame, text="Borrar lista", command=borrar_lista)
botonBorrar.grid(row=5, column=1, padx=30, pady=5)
botonBorrar.config(cursor="hand2", font=fuente_ejemplo_1, bg="red", fg="white", width=10)

# boton borrar campos-----------------------------

botonBorrar=Button(miFrame, text="Borrar todo", command=borrar_campos)
botonBorrar.grid(row=5, column=2, padx=30, pady=5)
botonBorrar.config(cursor="hand2", font=fuente_ejemplo_1, bg="red", fg="white", width=10)

# boton borrar item-----------------------------

botonBorrar=Button(miFrame, text="Borrar item", command=borrar_item)
botonBorrar.grid(row=5, column=3, padx=30, pady=5)
botonBorrar.config(cursor="hand2", font=fuente_ejemplo_1, bg="red", fg="white", width=10)



# checkbox --------------------

x=IntVar()

checkbox_1=Checkbutton(miFrame, text="pronto pago", variable=x, onvalue=1, offvalue=0, anchor="w")
checkbox_1.config(justify="left", bg="#282828", fg="green", width=10, font=fuente_ejemplo_1)
checkbox_1.grid(row=3, column=1, pady=0, padx=25, sticky="w")

y=IntVar()

checkbox_2=Checkbutton(miFrame, text="pago online", variable=y, onvalue=1, offvalue=0, anchor="w")
checkbox_2.config(justify="left", bg="#282828", fg="green", width=10, font=fuente_ejemplo_1)
checkbox_2.grid(row=3, column=2, pady=0, sticky="w")

# Listbox -----------------

lista = Listbox(miFrame, width=10, height=20, highlightcolor="#00ea0b", selectmode=EXTENDED, activestyle=NONE)

lista.grid(row=6, padx=30, pady=30, columnspan=4, sticky="nsew")

lista.config(font=fuente_ejemplo_2, bg="#282828", fg="grey", bd=0)

#---------imagen------------------

imagen=Label(miFrame, image=fondo, bd=0)
imagen.grid(row=3, column=0, rowspan=3, sticky='w', padx=30, pady=5)

mainloop()