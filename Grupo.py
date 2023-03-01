from typing import List
from Equipo import Equipo
from Util import quick_sort
class Grupo:
   
    def __init__(self, listgrupos):
        self.listgrupos = {}
        self.puntos= {'empate':1,'gano':3,'perdio':0}
        if len(listgrupos) <= 0:
            return 'lista vacia'

        for x in listgrupos:
            self.listgrupos[x]=Equipo(x)

    def match(self, nombreEquipo1, score1, nombreEquipo2, score2):
        equipo1 = self.listgrupos[nombreEquipo1]
        equipo2 = self.listgrupos[nombreEquipo2]
        if self.listgrupos.get(nombreEquipo1) == None:
            raise Exception('El nombre no coincide')

        if self.listgrupos.get(nombreEquipo2) == None:
            raise Exception('El nombre no coincide')
      
        if nombreEquipo2 in equipo1.list_partido_con_quien_jugo.keys():
            raise Exception('Ya jugaron {} y {}'.format(nombreEquipo1,nombreEquipo2))         
        
        if score1 == score2:
            equipo1.save(0,0,1,score1,score2,self.puntos['empate'], equipo2.nombre)
            equipo2.save(0,0,1,score2,score1,self.puntos['empate'], equipo1.nombre)
            return

        if score1 > score2:     
            equipo1.save(1, 0, 0, score1, score2, self.puntos['gano'], equipo2.nombre)
            equipo2.save(0, 1, 0, score2, score1, self.puntos['perdio'], equipo1.nombre)
            return

        equipo2.save(1, 0, 0, score2, score1, self.puntos['gano'], equipo1.nombre)
        equipo1.save(0, 1, 0, score1, score2, self.puntos['perdio'],equipo2.nombre)

    def result(self):       
        dictlist: List = []
        for key, value in self.listgrupos.items():
            dictlist.append(value)
        dictlist = quick_sort(dictlist)
        
        print('nombre  ganados  perdidos empates aFavor enContra difenrencia puntos')
        for x in dictlist:
            print(x.result())

  
        