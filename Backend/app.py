import json

def cargardatos(ruta):
    with open(ruta) as activosd:
        depreciacion = json.load(activosd)
        for valor in depreciacion:
            valorint = valor.get('Costo')
            anual = int(valorint)*0.33
            mensual = anual/12
            depanual = int(valorint)-anual
            print("Depreciación anual es "+str(anual)+" y la mensual es "+str(mensual))
            print("El valor del activo después de un año es de "+str(depanual))

if __name__ == '__main__':
    ruta = 'Activos fijos.json'
    cargardatos(ruta)
