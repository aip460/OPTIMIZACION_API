from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Progressbar
import time
from FullScreenApp import FullScreenApp
from ScrollableFrame import ScrollableFrame
import comprobaciones
from optimizador_cuts import resolver_problema_cortes
from optimizador_cuts_and_cost import resolver_problema_cortes_costos
from save import save

import sys
import subprocess
import conda.cli.python_api as Conda

def run():


    ##############################creacion de la ventana##################################################################
    window = Tk()
    window.config(bg="blue")          # color de fondo, background
    window.config(cursor="arrow")    # tipo de cursor (pirate por ejemplo, arrow por defecto)
    window.config(relief="sunken")    # relieve del root
    window.config(bd=25)              # tamaño del borde en píxeles

    window.title("Bienvenido al optimizador")
    window.geometry('1400x800')



    imagen1 = PhotoImage(file=f"images/serrucho.gif")
    Label(window, image=imagen1, bd=10).pack(side='right',fill="both")

    #############################creacion de tab en la ventana############################################################
    tab_control = ttk.Notebook(window)
    tab0 = ttk.Frame(tab_control)
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab3 = ttk.Frame(tab_control)


    tab_control.add(tab0,text='Portada')
    tab_control.add(tab1, text='Inicio')
    tab_control.add(tab2, text='Introducción de parámetros')
    tab_control.add(tab3, text='Resultados')

    ############################PORTADA ################################################################################
    lbl_portada = Label(tab0, text="""INDOP 4.0""", fg="brown", bg="green",
                            font=("Verdana", 20)).pack(anchor=NW,padx=20, pady=20)

    Label(tab0, text="""
    Planteamiento del problema: Antonio Madrazo.""").pack(anchor=NE)
    Label(tab0, text="""
    Resolución del problema: Alberto Irusta.""").pack(anchor=NE)

    Label(tab0, text="""
    Aplicación de escritorio encapsulada en el ámbito de INDUSTRY 4.0.""").pack(anchor=NW)
    Label(tab0, text="""
    Optimización de cortes de piezas. Minimización de la producción y maximización de los beneficios.\n                       
                                                """).pack(anchor=NW)
    Label(tab0, text="""
    INPUTS: stocks, longitudes tanto de materias primas como resultantes. Opcional añadir costos y precios.\n                       
                                                """).pack(anchor=NW)
    Label(tab0, text="""
    OUTPUTS: Secuencia de corte óptimo y rentabilidad óptima.\n                       
                                                """).pack(anchor=NW)

    Label(tab0, text="""
    Desarrollado en Python.\n                       
                                                """).pack(anchor=NW)
    Label(tab0, text="""
    Posibles mejoras: Introducir capacidades de almacenamiento en la rentabilidad para no coger todo el material...""").pack(anchor=SE)


    ###########################CONTENIDO DE TAB1=INICIO####################################################################
    bar = Progressbar(tab1, length=200)
    bar.pack(anchor=CENTER,padx=10, pady=10)

    lbl_description = Label(tab1, text="""Descripción del problema""",fg="brown",bg="green",font=("Verdana",20)).pack(anchor=NW)


    lbl = Label(tab1, text="""Se resuelve el problema de optimización siguiente:                                                       \n
                                            *Datos:                                                                                                  \n
                                            - Dadas n tipos de materias primas con sus respectivos
                                              valores de stock y sus longitudes.\n
                                                - Dadas m tipos de piezas resultantes con sus respectivos
                                                 valores minimos a extraer y sus longitudes.\n
                                            *Solcuión:                                                                                                \n
                                                Materias primas mínimas necesarias y
                                                 como distribuir las particiones, 
                                                 para extraer los valores minimos de las
                                                  distinas piezas resultantes.\n
                                            """).pack(anchor=NW)

    imagen2 = PhotoImage(file=f"images/Modelo_problema.gif")
    Label(tab1, image=imagen2, bd=0).pack(side='bottom',fill="both")


    ###############################CONTENIDO TAB2=INTRODUCCION DE PARAMETROS######################################################
    tab2_scrollbar=ScrollableFrame(tab2)
    tab2_scrollbar.scrollable_frame.grid_columnconfigure(2, minsize=300)


    bar = Progressbar(tab2_scrollbar.scrollable_frame, length=200)
    bar.grid(column=1, row=0,padx=10, pady=10)
    bar['value'] = 20
    lbl_desc = Label(tab2_scrollbar.scrollable_frame, text="""Introducción de parámetros y resolución""",fg="brown",bg="green",font=("Verdana",20)).grid(column=0, row=1)
    lbl_expl = Label(tab2_scrollbar.scrollable_frame, text= """A continuación, en 3 pasos se modelizará y resolverá el problema.           \n
                                        \t - En el primer paso, se introducirán las dimensiones del problema.           \n
                                        \t - En el segundo paso, se definirán los valores de longitudes y stock/demanda.\n
                                        \t - Opcionalmente se puede añadir minimzar y maximizar costos y beneficios. \n
                                        \t - Finalmente, se resolverá el problema planteado.                            \n""").grid(column=0, row=2)

    def clicked1():


        lbl1 = Label(tab2_scrollbar.scrollable_frame, text="......PASO 1.......").grid(column=0, row=4)
        lbl2 = Label(tab2_scrollbar.scrollable_frame, text="Introduzca el número de variedades de materias primas que se van a utilizar").grid(column=0, row=5)
        txt1 = Entry(tab2_scrollbar.scrollable_frame, width=10)
        txt1.grid(column=0, row=6)

        lbl3 = Label(tab2_scrollbar.scrollable_frame, text="Introduzca el número de variedades de materias resultantes").grid(column=0, row=7)
        txt2 = Entry(tab2_scrollbar.scrollable_frame, width=10)
        txt2.grid(column=0, row=8)
        lbl = Label(tab2_scrollbar.scrollable_frame, text="--------------------------------------------------------").grid(column=0, row=9)

        chk_state = BooleanVar()
        chk_state.set(False)  # set check state
        chk = Checkbutton(tab2_scrollbar.scrollable_frame, text='Min precios stock, Max precios productos', var=chk_state)
        chk.grid(column=1, row=9)


        txt1.focus()
        bar['value'] = 25


        def clicked2():

            if comprobaciones.comprobacion_enteros(txt1.get()) and comprobaciones.comprobacion_enteros(txt2.get()):
                txt1.config(state='disabled')
                txt2.config(state='disabled')
                chk.config(state='disabled')

                n1 = int(txt1.get())
                n2 = int(txt2.get())



                lbl4 = Label(tab2_scrollbar.scrollable_frame, text="......PASO 2.......").grid(column=0, row=11)
                lbl5_dimnesiones = Label(tab2_scrollbar.scrollable_frame, text="Introduzca las dimensiones de cada materia prima").grid(column=0, row=12)
                lbl5_stock = Label(tab2_scrollbar.scrollable_frame, text="Introduzca el stock o disponibilidad de cada materia prima").grid(column=1, row=12)
                l_n1_dimensiones=['txt1_dimensiones_'+str(i) for i in range(0,n1)]
                l_n1_stock=['txt1_stock_'+str(i) for i in range(0,n1)]
                if chk_state.get() == True:
                    lbl5_precio = Label(tab2_scrollbar.scrollable_frame,text="Introduzca el precio de cada materia prima").grid(column=2,row=12)
                    l_n1_precio = ['txt1_precio_' + str(i) for i in range(0, n1)]
                for i in range(0,n1):
                    l_n1_dimensiones[i] = Entry(tab2_scrollbar.scrollable_frame, width=10)
                    l_n1_dimensiones[i].grid(column=0, row= 13+i)
                    l_n1_stock[i] = Entry(tab2_scrollbar.scrollable_frame, width=10)
                    l_n1_stock[i].grid(column=1, row= 13+i)
                    if chk_state.get() == True:
                        l_n1_precio[i] = Entry(tab2_scrollbar.scrollable_frame, width=10)
                        l_n1_precio[i].grid(column=2, row=13 + i)

                fila_escribir=13+n1+1

                lbl6_dimnesiones = Label(tab2_scrollbar.scrollable_frame, text="Introduzca las dimensiones de cada materia resultante").grid(column=0, row=fila_escribir)
                lbl6_resultado_minimo = Label(tab2_scrollbar.scrollable_frame, text="Introduzca el stock minimo resultante de cada pieza resultante").grid(column=1, row=fila_escribir)
                l_n2_dimensiones=['txt2_dimensiones_'+str(i) for i in range(0,n2)]
                l_n2_stock=['txt2_stock_'+str(i) for i in range(0,n2)]
                if chk_state.get() == True:
                    lbl6_precio = Label(tab2_scrollbar.scrollable_frame,text="Introduzca el precio de cada materia resultante").grid(column=2,row=fila_escribir)
                    l_n2_precio = ['txt2_precio_' + str(i) for i in range(0, n2)]
                for i in range(0,n2):
                    l_n2_dimensiones[i] = Entry(tab2_scrollbar.scrollable_frame, width=10)
                    l_n2_dimensiones[i].grid(column=0, row= fila_escribir+i+1)
                    l_n2_stock[i] = Entry(tab2_scrollbar.scrollable_frame, width=10)
                    l_n2_stock[i].grid(column=1, row= fila_escribir+i+1)
                    if chk_state.get() == True:
                        l_n2_precio[i] = Entry(tab2_scrollbar.scrollable_frame, width=10)
                        l_n2_precio[i].grid(column=2, row=fila_escribir+i+1)
                fila_escribir=fila_escribir+n2+2
                lbl7 = Label(tab2_scrollbar.scrollable_frame, text="-------------------------------------------------------").grid(column=0, row=fila_escribir)


                l_n1_dimensiones[0].focus()
                bar['value'] = 50


                def clicked3():
                    res = messagebox.askokcancel('Info', '¿Desea continuar y resolver el problema?')

                    if res==True:

                        check1=True
                        for i in range(0, n1):
                            if comprobaciones.comprobacion_enteros(l_n1_dimensiones[i].get())==False or comprobaciones.comprobacion_enteros(l_n1_stock[i].get())==False:
                                check1=False
                                break
                        check2=True
                        for i in range(0, n2):
                            if comprobaciones.comprobacion_enteros(l_n2_dimensiones[i].get())==False or comprobaciones.comprobacion_enteros(l_n2_stock[i].get())==False:
                                check2=False
                                break

                        check3=True
                        if chk_state.get():
                            for i in range(0, n1):
                                if comprobaciones.comprobacion_float(l_n1_precio[i].get()) == False :
                                    check3 = False
                                    break
                            if check3:
                                for i in range(0, n2):
                                    if comprobaciones.comprobacion_float(l_n2_precio[i].get()) == False:
                                        check3 = False
                                        break


                        if check1 and check2 and check3:
                            for i in range(0, n1):
                                l_n1_dimensiones[i].config(state='disabled')
                                l_n1_stock[i].config(state='disabled')
                                if chk_state.get():
                                    l_n1_precio[i].config(state='disabled')

                            for i in range(0, n2):
                                l_n2_dimensiones[i].config(state='disabled')
                                l_n2_stock[i].config(state='disabled')
                                if chk_state.get():
                                    l_n2_precio[i].config(state='disabled')


                            L = [int(l_n1_dimensiones[i].get()) for i in range(0,n1)] # size of each item
                            print('L: '+str(L))
                            n = [int(l_n1_stock[i].get()) for i in range(0,n1)] # stock for each item
                            print('n: '+str(n))
                            cost=None
                            if chk_state.get():
                                cost = [float(l_n1_precio[i].get()) for i in range(0, n1)]

                            m = int(n2)  # number of requests
                            print('m: '+str(n2))
                            w = [int(l_n2_dimensiones[i].get()) for i in range(0,m)] # size of each item
                            print('w: '+str(w))
                            b = [int(l_n2_stock[i].get()) for i in range(0,m)] # demand for each item
                            print('b: '+str(b))

                            profit=None
                            if chk_state.get():
                                profit = [float(l_n2_precio[i].get()) for i in range(0, n2)]

                            t1 = time.time()
                            if chk_state.get():
                                sol=resolver_problema_cortes_costos(n, L, m, w, b,cost,profit)
                            else:
                                sol = resolver_problema_cortes(n, L, m, w, b)
                            t2 = time.time()
                            bar['value'] = 100

                            messagebox.showinfo('SOLUCION',f'El problema ha tardado en resolverse {str(t2-t1)} segundos')
                            lbl_sep=Label(tab2_scrollbar.scrollable_frame, text="""   """).grid(column=0, row=fila_escribir + 2)

                            lbl_resolution = Label(tab2_scrollbar.scrollable_frame, text="""Resolución""",fg="brown",bg="green",font=("Verdana",20)).grid(column=0, row=fila_escribir+3)

                            line=fila_escribir+4

                            if sol[0]==0 or sol[0]==3: #OPTIMAL(0),FEASIBLE(3)'

                                for idx,s in enumerate(sol[1]):
                                    lbl_name='lbl_sol_'+str(idx)
                                    lbl_name=Label(tab2_scrollbar.scrollable_frame, text=str(s)).grid(column=0, row=fila_escribir + 2+line)
                                    line+=1
                                # Si es optimo puedo exportar el resultado
                                btn_exportar = Button(tab3, text='Exportar resultados', command=lambda: save(sol,chk_state.get())).pack()

                            else:
                                messagebox.showerror('CUIDADO!',
                                                    f'El problema es infactible. No tiene solución')


                        else:
                            messagebox.showwarning('REVISA', f'Verifica los datos. Hay algún dato vacío y/o no entero.')

                btn3 = Button(tab2_scrollbar.scrollable_frame, text="Click para resolver", bg="green", fg="brown", command=clicked3).grid(column=0, row=fila_escribir+1)

            else:
                messagebox.showwarning('REVISA', f'Verifica los datos. Hay algún dato vacío y/o incorrecto.')

        btn2 = Button(tab2_scrollbar.scrollable_frame, text="Click para continuar", bg="green", fg="brown", command=clicked2).grid(column=0, row=10)

    btn1 = Button(tab2_scrollbar.scrollable_frame, text="Click para empezar",bg="green", fg="brown", command=clicked1).grid(column=0, row=3)

    def clicked_reset():
        for widget in tab2_scrollbar.scrollable_frame.winfo_children():
            widget.destroy()

        bar = Progressbar(tab2_scrollbar.scrollable_frame, length=200)
        bar.grid(column=1, row=0, padx=10, pady=10)
        bar['value'] = 20
        lbl_desc = Label(tab2_scrollbar.scrollable_frame, text="""Introducción de parámetros y resolución""",
                         fg="brown", bg="green", font=("Verdana", 20)).grid(column=0, row=1)
        lbl_expl = Label(tab2_scrollbar.scrollable_frame, text="""A continuación, en 3 pasos se modelizará y resolverá el problema.           \n
                                            \t - En el primer paso, se introducirán las dimensiones del problema.           \n
                                            \t - En el segundo paso, se definirán los valores de longitudes y stock/demanda.\n
                                            \t - Opcionalmente se puede añadir minimzar y maximizar costos y beneficios. \n
                                            \t - Finalmente, se resolverá el problema planteado.                            \n""").grid(
            column=0, row=2)

        def clicked1():

            lbl1 = Label(tab2_scrollbar.scrollable_frame, text="......PASO 1.......").grid(column=0, row=4)
            lbl2 = Label(tab2_scrollbar.scrollable_frame,
                         text="Introduzca el número de variedades de materias primas que se van a utilizar").grid(
                column=0, row=5)
            txt1 = Entry(tab2_scrollbar.scrollable_frame, width=10)
            txt1.grid(column=0, row=6)

            lbl3 = Label(tab2_scrollbar.scrollable_frame,
                         text="Introduzca el número de variedades de materias resultantes").grid(column=0, row=7)
            txt2 = Entry(tab2_scrollbar.scrollable_frame, width=10)
            txt2.grid(column=0, row=8)
            lbl = Label(tab2_scrollbar.scrollable_frame,
                        text="--------------------------------------------------------").grid(column=0, row=9)

            chk_state = BooleanVar()
            chk_state.set(False)  # set check state
            chk = Checkbutton(tab2_scrollbar.scrollable_frame, text='Min precios stock, Max precios productos',
                              var=chk_state)
            chk.grid(column=1, row=9)

            txt1.focus()
            bar['value'] = 25

            def clicked2():

                if comprobaciones.comprobacion_enteros(txt1.get()) and comprobaciones.comprobacion_enteros(txt2.get()):
                    txt1.config(state='disabled')
                    txt2.config(state='disabled')
                    chk.config(state='disabled')

                    n1 = int(txt1.get())
                    n2 = int(txt2.get())

                    lbl4 = Label(tab2_scrollbar.scrollable_frame, text="......PASO 2.......").grid(column=0, row=11)
                    lbl5_dimnesiones = Label(tab2_scrollbar.scrollable_frame,
                                             text="Introduzca las dimensiones de cada materia prima").grid(column=0,
                                                                                                           row=12)
                    lbl5_stock = Label(tab2_scrollbar.scrollable_frame,
                                       text="Introduzca el stock o disponibilidad de cada materia prima").grid(column=1,
                                                                                                               row=12)
                    l_n1_dimensiones = ['txt1_dimensiones_' + str(i) for i in range(0, n1)]
                    l_n1_stock = ['txt1_stock_' + str(i) for i in range(0, n1)]
                    if chk_state.get() == True:
                        lbl5_precio = Label(tab2_scrollbar.scrollable_frame,
                                            text="Introduzca el precio de cada materia prima").grid(column=2, row=12)
                        l_n1_precio = ['txt1_precio_' + str(i) for i in range(0, n1)]
                    for i in range(0, n1):
                        l_n1_dimensiones[i] = Entry(tab2_scrollbar.scrollable_frame, width=10)
                        l_n1_dimensiones[i].grid(column=0, row=13 + i)
                        l_n1_stock[i] = Entry(tab2_scrollbar.scrollable_frame, width=10)
                        l_n1_stock[i].grid(column=1, row=13 + i)
                        if chk_state.get() == True:
                            l_n1_precio[i] = Entry(tab2_scrollbar.scrollable_frame, width=10)
                            l_n1_precio[i].grid(column=2, row=13 + i)

                    fila_escribir = 13 + n1 + 1

                    lbl6_dimnesiones = Label(tab2_scrollbar.scrollable_frame,
                                             text="Introduzca las dimensiones de cada materia resultante").grid(
                        column=0, row=fila_escribir)
                    lbl6_resultado_minimo = Label(tab2_scrollbar.scrollable_frame,
                                                  text="Introduzca el stock minimo resultante de cada pieza resultante").grid(
                        column=1, row=fila_escribir)
                    l_n2_dimensiones = ['txt2_dimensiones_' + str(i) for i in range(0, n2)]
                    l_n2_stock = ['txt2_stock_' + str(i) for i in range(0, n2)]
                    if chk_state.get() == True:
                        lbl6_precio = Label(tab2_scrollbar.scrollable_frame,
                                            text="Introduzca el precio de cada materia resultante").grid(column=2,
                                                                                                         row=fila_escribir)
                        l_n2_precio = ['txt2_precio_' + str(i) for i in range(0, n2)]
                    for i in range(0, n2):
                        l_n2_dimensiones[i] = Entry(tab2_scrollbar.scrollable_frame, width=10)
                        l_n2_dimensiones[i].grid(column=0, row=fila_escribir + i + 1)
                        l_n2_stock[i] = Entry(tab2_scrollbar.scrollable_frame, width=10)
                        l_n2_stock[i].grid(column=1, row=fila_escribir + i + 1)
                        if chk_state.get() == True:
                            l_n2_precio[i] = Entry(tab2_scrollbar.scrollable_frame, width=10)
                            l_n2_precio[i].grid(column=2, row=fila_escribir + i + 1)
                    fila_escribir = fila_escribir + n2 + 2
                    lbl7 = Label(tab2_scrollbar.scrollable_frame,
                                 text="-------------------------------------------------------").grid(column=0,
                                                                                                      row=fila_escribir)

                    l_n1_dimensiones[0].focus()
                    bar['value'] = 50

                    def clicked3():
                        res = messagebox.askokcancel('Info', '¿Desea continuar y resolver el problema?')

                        if res == True:

                            check1 = True
                            for i in range(0, n1):
                                if comprobaciones.comprobacion_enteros(
                                        l_n1_dimensiones[i].get()) == False or comprobaciones.comprobacion_enteros(
                                        l_n1_stock[i].get()) == False:
                                    check1 = False
                                    break
                            check2 = True
                            for i in range(0, n2):
                                if comprobaciones.comprobacion_enteros(
                                        l_n2_dimensiones[i].get()) == False or comprobaciones.comprobacion_enteros(
                                        l_n2_stock[i].get()) == False:
                                    check2 = False
                                    break

                            check3 = True
                            if chk_state.get():
                                for i in range(0, n1):
                                    if comprobaciones.comprobacion_float(l_n1_precio[i].get()) == False:
                                        check3 = False
                                        break
                                if check3:
                                    for i in range(0, n2):
                                        if comprobaciones.comprobacion_float(l_n2_precio[i].get()) == False:
                                            check3 = False
                                            break

                            if check1 and check2 and check3:
                                for i in range(0, n1):
                                    l_n1_dimensiones[i].config(state='disabled')
                                    l_n1_stock[i].config(state='disabled')
                                    if chk_state.get():
                                        l_n1_precio[i].config(state='disabled')

                                for i in range(0, n2):
                                    l_n2_dimensiones[i].config(state='disabled')
                                    l_n2_stock[i].config(state='disabled')
                                    if chk_state.get():
                                        l_n2_precio[i].config(state='disabled')

                                L = [int(l_n1_dimensiones[i].get()) for i in range(0, n1)]  # size of each item
                                print('L: ' + str(L))
                                n = [int(l_n1_stock[i].get()) for i in range(0, n1)]  # stock for each item
                                print('n: ' + str(n))
                                cost = None
                                if chk_state.get():
                                    cost = [float(l_n1_precio[i].get()) for i in range(0, n1)]

                                m = int(n2)  # number of requests
                                print('m: ' + str(n2))
                                w = [int(l_n2_dimensiones[i].get()) for i in range(0, m)]  # size of each item
                                print('w: ' + str(w))
                                b = [int(l_n2_stock[i].get()) for i in range(0, m)]  # demand for each item
                                print('b: ' + str(b))

                                profit = None
                                if chk_state.get():
                                    profit = [float(l_n2_precio[i].get()) for i in range(0, n2)]

                                t1 = time.time()
                                if chk_state.get():
                                    sol = resolver_problema_cortes_costos(n, L, m, w, b, cost, profit)
                                else:
                                    sol = resolver_problema_cortes(n, L, m, w, b)
                                t2 = time.time()
                                bar['value'] = 100

                                messagebox.showinfo('SOLUCION',
                                                    f'El problema ha tardado en resolverse {str(t2 - t1)} segundos')
                                lbl_sep = Label(tab2_scrollbar.scrollable_frame, text="""   """).grid(column=0,
                                                                                                      row=fila_escribir + 2)

                                lbl_resolution = Label(tab2_scrollbar.scrollable_frame, text="""Resolución""",
                                                       fg="brown", bg="green", font=("Verdana", 20)).grid(column=0,
                                                                                                          row=fila_escribir + 3)

                                line = fila_escribir + 4

                                if sol[0] == 0 or sol[0] == 3:  # OPTIMAL(0),FEASIBLE(3)'

                                    for idx, s in enumerate(sol[1]):
                                        lbl_name = 'lbl_sol_' + str(idx)
                                        lbl_name = Label(tab2_scrollbar.scrollable_frame, text=str(s)).grid(column=0,
                                                                                                            row=fila_escribir + 2 + line)
                                        line += 1
                                    # Si es optimo puedo exportar el resultado
                                    btn_exportar = Button(tab3, text='Exportar resultados',
                                                          command=lambda: save(sol, chk_state.get())).pack()

                                else:
                                    messagebox.showerror('CUIDADO!',
                                                         f'El problema es infactible. No tiene solución')


                            else:
                                messagebox.showwarning('REVISA',
                                                       f'Verifica los datos. Hay algún dato vacío y/o no entero.')

                    btn3 = Button(tab2_scrollbar.scrollable_frame, text="Click para resolver", bg="green", fg="brown",
                                  command=clicked3).grid(column=0, row=fila_escribir + 1)

                else:
                    messagebox.showwarning('REVISA', f'Verifica los datos. Hay algún dato vacío y/o incorrecto.')

            btn2 = Button(tab2_scrollbar.scrollable_frame, text="Click para continuar", bg="green", fg="brown",
                          command=clicked2).grid(column=0, row=10)

        btn1 = Button(tab2_scrollbar.scrollable_frame, text="Click para empezar", bg="green", fg="brown",
                      command=clicked1).grid(column=0, row=3)

        btn_reset = Button(tab2_scrollbar.scrollable_frame, text="Click para resetear", bg="green", fg="brown",
                           command=clicked_reset).grid(column=1, row=3)

    btn_reset=Button(tab2_scrollbar.scrollable_frame, text="Click para resetear",bg="green", fg="brown", command=clicked_reset).grid(column=1, row=3)



    #
    #


    ##############################TAB3=EXPOTAR RESULTADOS#################################################################################
    lbl_descr = Label(tab3, text="""Exportar resultados""",fg="brown",bg="green",font=("Verdana",20)).pack(anchor=NW,padx=10, pady=10)
    lbl_explic = Label(tab3, text= """A continuación, seleccione el tipo de fichero (txt,csv) y un directorio donde guardar los resultados""").pack(anchor=NW,padx=10, pady=10)






    ###############################################################################################################################
    tab_control.pack(expand=1, fill='both')
    tab2_scrollbar.pack(expand=1, fill='both')
    app=FullScreenApp(window)

    window.mainloop()

if __name__=='__main__':


    # # implementar conda como un subproceso:
    #
    # subprocess.check_call([sys.executable, '-m', 'conda', 'install',
    #                        ' mip ','--yes'])




    run()

