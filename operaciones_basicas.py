"""
Este módulo contiene clases para realizar operaciones matemáticas básicas como suma y resta,
así como para calcular el promedio de una lista de valores.
"""

from typing import List


class OperacionesBasicas:
    """Clase para realizar operaciones matemáticas básicas como suma y resta."""

    def __init__(self) -> None:
        """Inicializa el resultado en 0."""
        self.resultado: int = 0

    def sumar(self, a: int, b: int) -> None:
        """Suma dos números y almacena el resultado."""
        self.resultado = a + b

    def restar(self, a: int, b: int) -> None:
        """Resta dos números y almacena el resultado."""
        self.resultado = a - b

    def obtener_resultado(self) -> int:
        """Devuelve el resultado de la última operación."""
        return self.resultado


class CalculadoraPromedio:
    """Clase para calcular el promedio de una lista de valores."""

    def __init__(self, valores: List[float]) -> None:
        """Inicializa la clase con una lista de valores.

        Args:
            valores (List[float]): Lista de números a promediar.
        """
        self._valores = valores

    @property
    def valores(self) -> List[float]:
        """Obtiene la lista de valores."""
        return self._valores

    @valores.setter
    def valores(self, valores: List[float]) -> None:
        """Establece la lista de valores, asegurándose de que no esté vacía.

        Args:
            valores (List[float]): Lista de números a establecer.

        Raises:
            ValueError: Si la lista de valores está vacía.
        """
        if not valores:
            raise ValueError("La lista de valores no puede estar vacía.")
        self._valores = valores

    def calcular_promedio(self) -> float:
        """Calcula el promedio de los valores almacenados.

        Returns:
            float: Promedio de los valores.
        """
        suma = sum(self._valores)
        promedio_numeros = suma / len(self._valores)
        return promedio_numeros
