# Interfaz usuario

from base_conocimientos import *
from motor_inferencia import recomendar_ropa

def sistema_experto_ropa():
    print("Sistema Experto de Asesoramiento de Vestuario")
    
    ocasion = input(f"¿Para qué ocasión te vistes hoy? {ocasiones}: ")
    clima = input(f"¿Qué clima hace hoy? {climas}: ")
    presupuesto = input(f"¿Cuál es tu presupuesto aproximado? {presupuestos}: ")
    estilo = input(f"¿Cuál es tu estilo preferido? {estilos}: ")

    recomendaciones = recomendar_ropa(ocasion, clima, presupuesto, estilo)
    
    print("\nTe recomendamos usar:")
    for recomendacion in recomendaciones:
        print(f"- {recomendacion}")
