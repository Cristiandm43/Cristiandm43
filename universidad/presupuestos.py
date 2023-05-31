from abc import ABC, abstractmethod

class Subject(ABC):
    """
    Interfaz del sujeto, define los métodos que los observadores deben implementar para recibir actualizaciones
    """
    @abstractmethod
    def agregar_observador(self, observador):
        pass
    
    @abstractmethod
    def eliminar_observador(self, observador):
        pass
    
    @abstractmethod
    def notificar_observadores(self):
        pass

class Presupuesto(Subject):
    """
    Clase que representa el presupuesto que se va a controlar, implementa la interfaz de Subject
    """
    def __init__(self):
        self._ingresos = 0
        self._egresos = 0
        self._observadores = []
    
    def agregar_observador(self, observador):
        self._observadores.append(observador)
    
    def eliminar_observador(self, observador):
        self._observadores.remove(observador)
    
    def notificar_observadores(self):
        for observador in self._observadores:
            observador.actualizar(self)
    
    def actualizar_presupuesto(self, ingresos, egresos):
        self._ingresos = ingresos
        self._egresos = egresos
        self.notificar_observadores()

class Observador(ABC):
    """
    Interfaz del observador, define los métodos que deben implementar los objetos que quieren recibir actualizaciones
    """
    @abstractmethod
    def actualizar(self, sujeto):
        pass

class Estadisticas(Observador):
    """
    Clase que representa a un observador que realiza estadísticas sobre el presupuesto
    """
    def actualizar(self, sujeto):
        ingresos = sujeto._ingresos
        egresos = sujeto._egresos
        saldo = ingresos - egresos
        print(f"Estadísticas: Ingresos: {ingresos}, Egresos: {egresos}, Saldo: {saldo}")

class Alertas(Observador):
    """
    Clase que representa a un observador que envía alertas cuando el presupuesto está en riesgo
    """
    def actualizar(self, sujeto):
        ingresos = sujeto._ingresos
        egresos = sujeto._egresos
        saldo = ingresos - egresos
        if saldo < 0:
            print("ALERTA: El presupuesto está en riesgo de no ser suficiente para cubrir los gastos")
        elif saldo < 1000:
            print("ALERTA: El presupuesto está llegando a un límite peligroso")