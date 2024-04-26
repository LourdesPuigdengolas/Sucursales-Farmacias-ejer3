from ventas import Ventas

class Gestor:
    __lista= [[]]

    def __init__(self):
        self.__lista=[]
        self.crearMatriz()  #ver como hacerlo privado para mayor seguridad
        
    def crearMatriz(self):
        filas = 5
        columnas = 7
         # Generar valores para cada celda
        contenido = 0  # Valor inicial
        for i in range(filas):
            fila = []            # Crear una nueva fila
            for j in range(columnas):
                fila.append(contenido)       # Agregar el valor del contador
                #contenido += 1           # Incrementar el contador
            self.__lista.append(fila)       # Agregar la fila a la matriz
        
        for fila in self.__lista:  # Imprimir la matriz
            print(fila)
    
    def agregarFactura(self, dia, suc, impor):
        self.__lista[suc-1][dia-1] += impor
        for fila in self.__lista:  # Imprimir la matriz
                 print(fila)
                 

    def calculaTotalSuc(self, suc):
        total=0
        j=0
        columnas = 7
        self.__lista[suc-1]
        for j in range(columnas):
              total += self.__lista[suc-1][j]      
        print("El total de facturación para la sucursal {} es de {} ".format(suc, total)) 


    def sucursalMasFac(self, day):
        max=0
        filas=5
        i=0
        factura= int
        for i in range(filas):
            if (self.__lista[i][day-1] > max):
                   factura = self.__lista[i][day-1]
                   max= factura
                   sucursal= i+1 
        print("La sucursal {} es la que más facturó para el día {} ".format (sucursal, day))    

     # -------ARREGLAR FUNCIONES DESDE ACÁ ----------------------

    def menorFacSemanal(self):  #Calcular la sucursal con menos facturación durante toda la semana
        min=99999
        filas=5
        columnas=7
        suc=0
        tot=0
        sumaFilas=[]
        i=0
        for i in range(filas):
            for j in range(columnas):
                tot+= self.__lista[i][j]  
            sumaFilas.append(tot)
            tot=0

        for i in range(filas):       
            if (sumaFilas[i] < min):
                    suc= i+1
                    min= sumaFilas[i]            
        print("La sucursal {} fué la que menos facturó por semana y facturó un total de $ {} ".format(suc,min))

    def calculaTotal(self):   #Calcular el total facturado por todas las sucursales durante toda la semana.
        filas=5
        columnas=7
        tot=0
        i=0
        for i in range(filas):
            for j in range(columnas):
                tot+= self.__lista[i][j]  
            
        print("El total facturado esta semana fue de $ {} ".format(tot))   