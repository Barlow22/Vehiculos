class Vehiculo():
    def __init__(self, color, marca, velocidad_max):
        self.color = color
        self.marca = marca
        self.velocidad_max = velocidad_max
        self.velocidad_actual = 0
        self.encendido = False

    def encender_auto(self):
        self.encendido = True
    def apargar_auto(self):
        self.encendido = False
    def mostar_velocimetro(self):
        print('La velocidad actual es de ' + str(self.velocidad_actual) + ' de ' + str(self.velocidad_max))
    def acelerar(self, velocidad):
        if self.encendido == True:
            if self.velocidad_actual + velocidad >= self.velocidad_max:
                self.velocidad_actual = 180
            else:
                self.velocidad_actual = self.velocidad_actual + velocidad
        else:
            print('Para acelerar hay que encender el auto.')
        self.mostar_velocimetro()
    def frenar(self, velocidad):
        if self.velocidad_actual - velocidad < 0:
            self.velocidad_actual = 0
        else:
            self.velocidad_actual = self.velocidad_actual - velocidad
        self.mostar_velocimetro()




class Camion(Vehiculo):
    def __init__(self, carga_max,color,marca,velocidad_max):
        self.carga_max = carga_max
        self.carga_actual = 0
        Vehiculo.__init__(self,color,marca,velocidad_max)

    def cargar(self, carga):
        self.carga_actual = self.carga_actual + carga
    def mostar_velocimetro(self):
        print('La velocidad actual es de ' + str(self.velocidad_actual) + ' de ' + str(self.velocidad_max) +' y la carga es de ' +str(self.carga_actual))


        

class Automovil(Vehiculo):
    #constructor
    def __init__(self, nro_puertas,color,marca,velocidad_max):
        #Propiedades
        self.nro_puertas = nro_puertas
        Vehiculo.__init__(self,color,marca,velocidad_max)
    def abir_puertas(self, nro_puertas):
        print('Se abren las pueras')
    
    #Metodos



#Creacion del objeto mi auto con las propiedades

mi_camion = Camion(2000,'Verde', 'Scania', 200)
mi_camion.encender_auto()
mi_camion.cargar(1000)
mi_camion.acelerar(100)

mi_auto = Automovil(4, 'rojo', 'Ford', 250)
mi_auto.encender_auto()
mi_auto.acelerar(180)
mi_auto.frenar(100)
mi_auto.apargar_auto()