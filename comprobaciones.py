def comprobacion_enteros(arg):
    try:
        if int(arg)==float(arg):
            return True
        else:
            return False
    except:
        return False

