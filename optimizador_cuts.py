from mip import Model, xsum, BINARY, INTEGER, minimize

def resolver_problema_cortes(n,L,m,w,b,):
    # creating the model
    model = Model()
    x = {(k, i, j): model.add_var(obj=0, var_type=INTEGER, name="x[%d,%d,%d]" % (k, i, j))
          for i in range(m) for k in range(len(n)) for j in range(n[k])}

    y = {(k, j): model.add_var(obj=0, var_type=BINARY, name="y[%d,%d]" % (k, j))
         for k in range(len(n)) for j in range(n[k])}

    model.objective = minimize(
        xsum( xsum(L[k] *y[k, j] for k in range(len(n)) for j in range(n[k])) for k in range(len(n)))

    )
    #le hemos puesto que ademas priorice coger las menores longitudes--> menor desperdicio!!

    # constraints
    for i in range(m):
        model.add_constr(xsum(xsum(x[k, i, j] for j in range(n[k])) for k in range(len(n))) >= b[i])

    for k in range(len(n)):
        for j in range(n[k]):
            model.add_constr(xsum(w[i] * x[k, i, j] for i in range(m)) <= L[k] * y[k, j])

    for k in range(len(n)):
        for j in range(1, n[k]):
            model.add_constr(y[k, j - 1] >= y[k, j])

    # optimizing the model
    model.optimize()

    # printing the solution
    l_solution = []

    materia_prima_total=''
    materia_prima_desglosada=[]
    materia_prima_y_resultado=[]
    materia_resultado_desglosada=[]

    s_t=0
    for k in range(len(n)):
        s_k=0
        for j in range(n[k]):
            if y[k, j].x!=None:
                s_k+=int(y[k, j].x)
                s_t+=int(y[k, j].x)
        l_solution.append(f'El numero de barras estandar {str(L[k])} utilizado es: {s_k}')

        materia_prima_desglosada.append({'tipo_materia_prima':str(L[k]),'numero_usado':str(s_k)})

    l_solution.append(f'---------El numero de barras totales usadas es: {s_t} ------------')
    materia_prima_total=str(s_t)



    l_solution.append('-------------------------------------------------------------------')
    l_solution.append('-------------------------------------------------------------------')
    l_solution.append('-----------A continuación los cortes por barra estandar-------------------------------')
    for k in range(len(n)):
        l_solution.append(f'-----------TIPO {str(L[k])}-------------------------------')
        for j in range(n[k]):
            for i in range(m):
                    if x[k, i,j].x != None and x[k, i,j].x > 1e-5:
                        l_solution.append(f'El numero de barras demandadas {str(w[i])} extraidas en barra {str(L[k])} ({str(j)}) es: {str(x[k, i,j].x)}')
                        materia_prima_y_resultado.append({'tipo_materia_prima':str(L[k]), 'numero_usado':str(j) ,'tipo_materia_resultado':str(w[i]),'numero_resultado':str(x[k, i,j].x)})
    l_solution.append('-------------------------------------------------------------------')
    l_solution.append('-------------------------------------------------------------------')
    for i in range(m):
        s_i=0
        for k in range(len(n)):
            for j in range(n[k]):
                if x[k, i,j].x!=None:
                    s_i+=int(x[k, i,j].x)
        l_solution.append(f'-----------El numero de barras demandadas {str(w[i])} extraidas total es: {str(s_i)}-------------------')
        materia_resultado_desglosada.append({'tipo_materia_resultado':str(w[i]),'numero_resultado':str(s_i)})



    return model.status.value ,l_solution,    materia_prima_total,   materia_prima_desglosada,    materia_prima_y_resultado,    materia_resultado_desglosada



# L= [13500, 12000]
# n= [100, 100]
# m= 3
# w= [4800, 5200, 3750]
# b= [18, 3, 42]
#
# resolver_problema(n,L,m,w,b,)




