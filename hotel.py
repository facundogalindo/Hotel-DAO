import csv

class Hotel:
    def __init__(self, archivo_csv):
        self.habitaciones = []
        self.archivo_csv = archivo_csv


        with open(archivo_csv, newline='') as archivo:
            lector = csv.reader(archivo)
            for linea in lector:
                tipo = int(linea[0])
                numero = int(linea[1])
                huesped = linea[2]
                costo_base = float(linea[3])
                noches = int(linea[4])
                extra = linea[5].lower() == "true"
                if tipo == 1:
                    habitacion = Estandar(numero,huesped,costo_base,noches,extra)
                elif tipo == 2:
                    habitacion = Suite(numero, huesped, costo_base, noches, extra)
                elif tipo == 3:
                    habitacion = SuitePremium(numero, huesped, costo_base, noches, extra)
                self.habitaciones.append(habitacion)


    def cantidad_habitaciones(self):
        return self.habitaciones

    def cantidad_por_tipo(self):
        cantidades= {"Estandar": 0, "Suite": 0, "SuitePremium": 0}

        for habitacion in self.habitaciones:
            if isinstance(habitacion, Estandar):
                cantidades["Estandar"] += 1
            elif isinstance(habitacion, Suite):
                cantidades["Suite"] += 1
            elif isinstance(habitacion, SuitePremium):
                cantidades["SuitePremium"] += 1
        return cantidades
    def calcular_ingreso_total(self):
        ingreso_total = 0
        for habitacion in self.habitaciones:
            ingreso_total += habitacion.calcular_costo()
        return ingreso_total

    def obtener_suma_reservas(self):
        suma = 0
        for habitacion in self.habitaciones:
            suma += habitacion.calcular_costo()
        return suma
    def contar_suites_vista_mar(self):
        suites_vista_mar = 0
        for habitacion in self.habitaciones:
            if (habitacion.tipo == 2):
                if (habitacion.vista_mar == True):
                    suites_vista_mar += 1
        return suites_vista_mar
    def contar_suites_premium_jacuzzi(self):
        suites_vista_mar = 0
        for habitacion in self.habitaciones:
            if (habitacion.tipo == 3):
                if (habitacion.jacuzzi == True):
                    suites_vista_mar += 1
        return suites_vista_mar

    def obtener_reserva_mas_cara(self):
        max_costo = 0
        reserva_cara = None

        for habitacion in self.habitaciones:
            costo = habitacion.calcular_costo()
            if costo > max_costo:
                max_costo = costo
                reserva_cara = habitacion

        return reserva_cara














class Habitacion:
    def __init__(self, tipo, numero, huesped, costo_base,noches,extra):
        self.tipo = tipo
        self.numero = numero
        self.huesped = huesped
        self.costo_base = costo_base
        self.noches = noches
        self.extra = extra
    def calcular_costo(self):
        return self.costo_base * self.noches

class Estandar(Habitacion):
    def __init__(self,numero, huesped, costo_base,noches,extra):
        self.tipo = 1
        self.numero = numero
        self.huesped = huesped
        self.costo_base = costo_base
        self.noches = noches
        self.extra = extra
    def calcular_costo(self):
        return self.costo_base * self.noches

    def calcular_costo_total(self):
        return self.calcular_costo()

class Suite(Habitacion):
    def __init__(self,numero, huesped, costo_base,noches, vista_mar):
        self.tipo = 2
        self.numero = numero
        self.huesped = huesped
        self.costo_base = costo_base
        self.noches = noches
        self.vista_mar = vista_mar
    def calcular_costo(self):
        if self.vista_mar == False:
            return super().calcular_costo()
        else:
            return super().calcular_costo() * 1.1

    def calcular_costo_total(self):
        return self.calcular_costo()

class SuitePremium(Habitacion):
    def __init__(self,numero, huesped, costo_base,noches, jacuzzi):
        self.tipo = 3
        self.numero = numero
        self.huesped = huesped
        self.costo_base = costo_base
        self.noches = noches
        self.jacuzzi = jacuzzi

    def calcular_costo(self):

        if self.jacuzzi == False:
            return super().calcular_costo()
        else:
            return super().calcular_costo() * 1.2

    def calcular_costo_total(self):
        return self.calcular_costo()


