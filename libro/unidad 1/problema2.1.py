"""
Descripción del problema:

Los accidentes en una planta de papas fritas se clasifican de acuerdo con el área lesionada.
Dibuje un diagrama de Pareto

"""
from function import get_data
from function import pareto


if __name__ == "__main__":
    df = get_data("2.1.csv")
    pareto(df, "Accidentes", "Numero")

"""
Observemos que de la gráfica aproximadamente el 90 por ciento de los accidentes son descritos por las lesiones en dedos y ojos, lo cual se tiene que sugerir medidas de seguridad
adecuadas en esa área de lesión.    
"""
