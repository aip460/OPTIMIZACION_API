def comprobacion_enteros(arg):
    try:
        if int(arg)==float(arg):
            return True
        else:
            return False
    except:
        return False


def comprobacion_float(arg):
    try:
        float(arg)
        return True
    except:
        return False

