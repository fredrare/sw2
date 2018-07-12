import requests

def obtener_tiempo_actual():
    respuesta = requests.get('http://165.227.76.18:3000/tiempo')
    print respuesta.content
    return respuesta.content
def nuevo_tiempo(tiempo):
    requests.get('http://165.227.76.18:3000/time?time=' + tiempo )
