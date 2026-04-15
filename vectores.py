"""
Ainhoa Daniela Dumitru
TASCA 3: APA - CURS 2025-2026

Implementació d'una classe per a la manipulació de vectors i operacions algebraiques.

Tests unitaris:
>>> v1 = Vector([1, 2, 3])
>>> v2 = Vector([4, 5, 6])
>>> v1 * 2
Vector([2.0, 4.0, 6.0])

>>> v1 * v2
Vector([4.0, 10.0, 18.0])

>>> v1 @ v2
32.0

>>> v3 = Vector([2, 1, 2])
>>> v4 = Vector([0.5, 1, 0.5])
>>> v3 // v4
Vector([1.0, 2.0, 1.0])

>>> v3 % v4
Vector([1.0, -1.0, 1.0])
"""

class Vector:
    """
    Classe optimitzada per a l'àlgebra vectorial.
    Inclou suport per a producte d'Hadamard, producte escalar i descomposició ortogonal.
    """

    def __init__(self, elements):
        """Inicialitza el vector assegurant que les dades siguin de tipus flotant."""
        self._data = [float(item) for item in elements]

    def __repr__(self):
        """Representació de depuració de l'objecte."""
        return f"Vector({self._data})"

    def __str__(self):
        """Format de cadena simple per a l'usuari."""
        return str(self._data)

    def __len__(self):
        """Retorna el nombre de components del vector."""
        return len(self._data)

    def __getitem__(self, i):
        """Accés a un element per índex."""
        return self._data[i]

    def __setitem__(self, i, valor):
        """Assignació d'un valor a una posició concreta."""
        self._data[i] = float(valor)

    def __mul__(self, other):
        """
        Sobrecàrrega del producte (*). 
        Gestiona tant el producte per escalar com el producte d'Hadamard (element a element).
        """
        if isinstance(other, (int, float, complex)):
            return Vector([x * other for x in self._data])
        
        if len(self) != len(other):
            raise ValueError("La dimensió dels vectors no coincideix per al producte.")
        
        # Implementació alternativa mitjançant l'ús de zip
        return Vector([a * b for a, b in zip(self._data, other)])

    def __rmul__(self, other):
        """Permet operacions del tipus: escalar * Vector."""
        return self.__mul__(other)

    def __matmul__(self, other):
        """
        Producte escalar (dot product) utilitzant l'operador @.
        """
        if len(self) != len(other):
            raise ValueError("Dimensions incompatibles per al producte escalar.")
        
        return sum(x * y for x, y in zip(self._data, other))

    def __sub__(self, other):
        """Resta algebraica de dos vectors."""
        return Vector([a - b for a, b in zip(self._data, other)])

    def __floordiv__(self, base):
        """
        Projecció del vector sobre un altre (component paral·lela) amb //.
        Fórmula: (v · b / b · b) * b
        """
        # Calculem el factor escalar de la projecció
        escalar = (self @ base) / (base @ base)
        return escalar * base

    def __mod__(self, base):
        """
        Component ortogonal (normal) mitjançant l'operador %.
        S'obté restant la part paral·lela al vector original.
        """
        parallela = self // base
        return self - parallela

if __name__ == "__main__":
    import doctest
    # Executa els tests per validar el comportament segons l'enunciat
    doctest.testmod(verbose=True)