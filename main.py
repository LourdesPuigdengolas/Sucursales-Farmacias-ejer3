from gestorVentas import Gestor
from ventas import Ventas

if __name__=='__main__':

        gestorLista= Gestor()  #gestorLista es un objeto de gestor, ahi teng mi clase manejadora

        print(f"--- MENU: ---")
        print(f"[1]. Acumular importe de una factura ")
        print(f"[2]. Calcular el total de facturación para la sucursal ")
        print(f"[3]. Ver sucursal que más facturó en el día ")
        print(f"[4]. Calcular la sucursal con menos facturación durante toda la semana ")
        print(f"[5]. Calcular el total facturado por todas las sucursales durante toda la semana ")
        print(f"[0]. Salir ")
        

        opcion= int(input("Ingrese el numero de opción que desea: "))
        while opcion != 0:
                if opcion == 1:
                        #caja.mostrarDatos()  # siempre llamar a un ojeto no a una clase, porque el que tiene atributos y metodos es el objeto
                        #lista.mostrarLista() #en caso de listas llamamos a la lista de objetos
                        diaa= int(input("Ingrese el día de la semana (empezando por 1 Lun)"))
                        numSu= int(input("Ingrese el numero de sucursal "))
                        impFac= float(input("Ingrese el importe de la factura "))
                        gestorLista.agregarFactura(diaa, numSu, impFac)
                elif opcion == 2: 
                        suc= int(input("Ingrese el numero de sucursal "))
                        pass
                elif opcion == 3: 
                        day= int(input("Ingrese el día de la semana "))
                        gestorLista.sucursalMasFac(day)
                        pass
                elif opcion == 4: 
                        pass
                elif opcion == 5: 
                        pass
                
                opcion= int(input("Ingrese el numero de opción que desea: "))