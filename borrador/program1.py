from mip import Model, xsum, BINARY, INTEGER

n = 1000  # maximum number of bars
L = 13500  # bar length
m = 3  # number of requests
w = [4800, 5200, 3750]  # size of each item
b = [18, 3, 42]  # demand for each item

# creating the model
model = Model()
x = {(i, j): model.add_var(obj=0, var_type=INTEGER, name="x[%d,%d]" % (i, j))
     for i in range(m) for j in range(n)}
y = {j: model.add_var(obj=1, var_type=BINARY, name="y[%d]" % j)
     for j in range(n)}

# constraints
for i in range(m):
    model.add_constr(xsum(x[i, j] for j in range(n)) >= b[i])
for j in range(n):
    model.add_constr(xsum(w[i] * x[i, j] for i in range(m)) <= L * y[j])

# additional constraints to reduce symmetry
for j in range(1, n):
    model.add_constr(y[j - 1] >= y[j])

# optimizing the model
model.optimize()

# printing the solution
print('')
print('Objective value: {model.objective_value:.3}'.format(**locals()))
print('Solution: ', end='')
for v in model.vars:
    if v.x > 1e-5:
        print('{v.name} = {v.x}'.format(**locals()))
        print('          ', end='')



n_barras_estandar=0
for j in y:
    n_barras_estandar+=y[j].x
print(f'El numero de barras estandar minimo es: {n_barras_estandar}')
n_piezas1=0
n_piezas2=0
n_piezas3=0
for barra in range(int(n_barras_estandar)):
    print(f'Para la barra {barra} las piezas de cada tipo que se extraen son: {x[0,barra].x} piezas4800,{x[1,barra].x} piezas5200,{x[2,barra].x} piezas3750' )
    n_piezas1+=x[0,barra].x
    n_piezas2+=x[1,barra].x
    n_piezas3+=x[2,barra].x
print(f'Tras cortar el numero de piezas totales de cada tipo es: {n_piezas1} piezas4800,{n_piezas2} piezas5200, {n_piezas3} piezas3750')




#######################################################################################
#######################################################################################


from mip import Model, xsum, BINARY, INTEGER

n1 = 1000  # maximum number of bars
n2 = 1000  # maximum number of bars
L1 = 13500  # bar length
L2 = 12000  # bar length
m = 3  # number of requests
w = [480500000, 5205, 3755]  # size of each item
b = [18, 3, 42]  # demand for each item

# creating the model
model = Model()
x1 = {(i, j): model.add_var(obj=0, var_type=INTEGER, name="x1[%d,%d]" % (i, j))
     for i in range(m) for j in range(n1)}
x2 = {(i, j): model.add_var(obj=0, var_type=INTEGER, name="x2[%d,%d]" % (i, j))
     for i in range(m) for j in range(n2)}

y1 = {j: model.add_var(obj=1, var_type=BINARY, name="y1[%d]" % j)
     for j in range(n1)}
y2 = {j: model.add_var(obj=1, var_type=BINARY, name="y2[%d]" % j)
     for j in range(n2)}

# constraints
for i in range(m):
    model.add_constr(xsum(x1[i, j] for j in range(n1))+xsum(x2[i, j] for j in range(n2)) >= b[i])
for j in range(n1):
    model.add_constr(xsum(w[i] * x1[i, j] for i in range(m)) <= L1 * y1[j])

for j in range(n2):
    model.add_constr(xsum(w[i] * x2[i, j] for i in range(m)) <= L2 * y2[j])

# additional constraints to reduce symmetry
for j in range(1, n1):
    model.add_constr(y1[j - 1] >= y1[j])

for j in range(1, n2):
    model.add_constr(y2[j - 1] >= y2[j])

# optimizing the model
model.optimize()

# printing the solution
print('')
print('Objective value: {model.objective_value:.3}'.format(**locals()))
print('Solution: ', end='')
for v in model.vars:
    if v.x > 1e-5:
        print('{v.name} = {v.x}'.format(**locals()))
        print('          ', end='')



n_barras_estandar1=0
for j in y1:
    n_barras_estandar1+=y1[j].x
print(f'El numero de barras estandar 13500 minimo es: {n_barras_estandar1}')
n_barras_estandar2=0
for j in y1:
    n_barras_estandar2+=y2[j].x
print(f'El numero de barras estandar 12000 minimo es: {n_barras_estandar2}')
n_piezas1=0
n_piezas2=0
n_piezas3=0
for barra in range(int(n_barras_estandar1)):
    print(f'Para la barra 13500, {barra} las piezas de cada tipo que se extraen son: {x1[0,barra].x} piezas4800,{x1[1,barra].x} piezas5200,{x1[2,barra].x} piezas3750' )
    n_piezas1+=x1[0,barra].x
    n_piezas2+=x1[1,barra].x
    n_piezas3+=x1[2,barra].x
print(f'Tras cortar el numero de piezas totales, sacadas de barras 13500, de cada tipo es: {n_piezas1} piezas4800,{n_piezas2} piezas5200, {n_piezas3} piezas3750')
c1=n_piezas1
c2=n_piezas2
c3=n_piezas3


n_piezas1=0
n_piezas2=0
n_piezas3=0
for barra in range(int(n_barras_estandar2)):
    print(f'Para la barra 12000, {barra} las piezas de cada tipo que se extraen son: {x2[0,barra].x} piezas4800,{x2[1,barra].x} piezas5200,{x2[2,barra].x} piezas3750' )
    n_piezas1+=x2[0,barra].x
    n_piezas2+=x2[1,barra].x
    n_piezas3+=x2[2,barra].x
print(f'Tras cortar el numero de piezas totales, sacadas de barras 13500, de cada tipo es: {n_piezas1} piezas4800,{n_piezas2} piezas5200, {n_piezas3} piezas3750')

print(f'El numero de barras estandar 13500 minimo es: {n_barras_estandar1}\n.El numero de barras estandar 12000 minimo es: {n_barras_estandar2}')
print(f'El total de piezas es {n_piezas1+c1} piezas4800,{n_piezas2+c2} piezas5200, {n_piezas3+c3} piezas3750')


def f():
    return [1,2],3,[5,1]








