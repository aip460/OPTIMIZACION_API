# which is used to save file in any extension
from  tkinter  import  filedialog
import pandas as pd
from tkinter import messagebox

# function to call when user press
# the save button, a filedialog will
# open and ask to save file
def save(data,type_solution):

    files = [
             ('CSV', '*.csv'),
             ]
    outfilename = filedialog.asksaveasfile(filetypes = files, defaultextension = files[0])  # obtener ubicación para guardar
    df=pd.DataFrame()
    ############valores de file###############################
    relleno='X'
    n_rows=max([len(data[2]),len(data[3]),len(data[4]),len(data[5])])

    col1=[relleno]*n_rows
    col1[0]=data[2]
    df['materia_prima_total_usada']=col1

    if type_solution:
        col2=[relleno]*n_rows
        col2[0]=data[6]
        df['materia_prima_coste_total']=col2

        col3=[relleno]*n_rows
        col3[0]=data[7]
        df['materia_resultado_beneficio']=col3

    tipo = [relleno]*n_rows
    n = [relleno]*n_rows
    if type_solution:
        cost=[relleno]*n_rows
    for idx,value in enumerate(data[3]):
        tipo[idx]=value['tipo_materia_prima']
        n[idx]=value['numero_usado']
        if type_solution:
            cost[idx] = value['coste']
    df['TIPO_materia_prima_desglosada'] = tipo
    df['N_materia_prima_desglosada'] = n
    if type_solution:
        df['materia_prima_coste_desglosado'] = cost


    tipo = [relleno]*n_rows
    n = [relleno]*n_rows
    if type_solution:
        profit = [relleno] * n_rows
    for idx,value in  enumerate(data[5]):
        tipo[idx]=value['tipo_materia_resultado']
        n[idx]=value['numero_resultado']
        if type_solution:
            profit[idx] = value['beneficio']

    df['TIPO_materia_resultado_desglosada']=tipo
    df['N_materia_resultado_desglosada'] = n
    if type_solution:
        df['materia_resultado_beneficio_desglosado'] = profit


    tipoPrima=[relleno]*n_rows
    numeroPrima=[relleno]*n_rows
    tipoResultado=[relleno]*n_rows
    numeroResultado=[relleno]*n_rows
    for idx,value in enumerate(data[4]):
        tipoPrima[idx]=value['tipo_materia_prima']
        numeroPrima[idx]=int(value['numero_usado'])+1 ########la pieza a cortar
        tipoResultado[idx]=value['tipo_materia_resultado']
        numeroResultado[idx]=value['numero_resultado']

    df['tipoPrima']=tipoPrima
    df['numeroPrima'] = numeroPrima
    df['tipoResultado'] = tipoResultado
    df['numeroResultado'] = numeroResultado

    df.to_csv(outfilename,index=False,sep=';',)

    outfilename.close()

    messagebox.showinfo('Proceso terminado', f'Exportación completada con éxito.')





#btn = ttk.Button(root, text='Save', command=lambda: save())