class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
        
    def cambiarColor(self, color):
        validos = ["rojo", "verde", "amarillo", "blanco", "negro"]
        for i in validos:
            if color == i:
                self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro 
    def asignarTipo(self, tipo):
        tipos = ["electrico", "gasolina"]
        for i in tipos:
            if tipo == i:
                self.tipo = tipo

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        c = 0
        for i in  self.asientos:
            if i != None:
                c+=1
        return c
    def verificarIntegridad(self):
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"
        for i in range(len(self.asientos)):
            if self.asientos[i] != None:
                if (self.asientos[i].registro != self.registro):
                    return "Las piezas no son originales"
        return "Auto original"
