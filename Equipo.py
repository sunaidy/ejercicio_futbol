from Partido import Partido
class Equipo:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.list_partido_con_quien_jugo = {}
        self.ganados = 0
        self.perdidos = 0
        self.empates = 0
        self.aFavor = 0
        self.enContra = 0
        self.diferencia = 0
        self.puntos = 0
    def result(self):
        return f' {self.nombre}   {self.ganados}  {self.perdidos}  {self.empates}  {self.aFavor}  {self.enContra}  {self.diferencia}  {self.puntos} '

    def save(self, ganados, perdidos, empates, aFavor, enContra, puntos, nombre_contrincante):
        self.ganados += ganados
        self.perdidos += perdidos
        self.empates += empates
        self.aFavor += aFavor
        self.enContra += enContra
        self.diferencia += aFavor - enContra
        self.puntos += puntos
        self.list_partido_con_quien_jugo[nombre_contrincante] = Partido(puntos,(aFavor - enContra),aFavor)
        