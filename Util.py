from typing import Dict, List
from xmlrpc.client import Boolean

from Equipo import Equipo


 
def quick_sort( collection: List) -> List:
    
    if len(collection) < 2:
        return collection
    
    pivot = collection.pop()  # Uso el ultimo elemento como primer pivot
    mayor: list[Equipo] = []  # Todos los elementos mayores que el pivote
    menor: list[Equipo] = []  # Todos los elementos menores que el pivote
    for element in collection:

      menor, mayor= desempate(menor,mayor, element,pivot,['puntos','diferencia', 'aFavor'])
  
    return quick_sort(mayor) + [pivot] + quick_sort(menor)
 

def desempate(menor, mayor, elemnto, pivote, criterios: List):
    if  len(criterios) < 1:
        return  
    if getattr(pivote, criterios[0]) == getattr(elemnto, criterios[0])  :
        if len(criterios)==1:
           
            menor, mayor = desempatePartido(menor, mayor,elemnto, pivote, ['puntos', 'diferencia', 'goles_anotados'])
           
        criterios.pop(0)
        desempate(menor, mayor, elemnto, pivote, criterios)
    else:
        (menor if getattr(elemnto, criterios[0]) < getattr(pivote, criterios[0]) else mayor).append(elemnto)
    return menor, mayor

        
def desempatePartido(menor, mayor, elemento, pivote, criteriosC):
    elemento_partido = elemento.list_partido_con_quien_jugo[pivote.nombre]
    pivote_partido = pivote.list_partido_con_quien_jugo[elemento.nombre]
    if  len(criteriosC) < 1:
        return  
    if getattr(elemento_partido, criteriosC[0]) == getattr(pivote_partido, criteriosC[0])  :
        if len(criteriosC) == 1:
            menor.append(elemento)
        criteriosC.pop(0)    
        desempatePartido(menor, mayor, elemento, pivote, criteriosC)
    
    else:
        (menor if getattr(elemento_partido, criteriosC[0]) < getattr(pivote_partido, criteriosC[0])  else mayor).append(elemento)
    return menor, mayor   