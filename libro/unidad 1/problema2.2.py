"""
Problema 2.2
Los daños en molinos de papel(en miles de dólares) debido a roturas se dividen de acuerdo con el producto 
fabricado.

a) Dibuje un diagrama de Pareto
b) ¿Qué porcentaje de la pérdida ocurre al fabricar:
1) Papel sanitario?
42 porciento
2) Papel sanitario  o toallas para las manos?
70 por ciento
"""
from function import get_data
from function import pareto


if __name__ == "__main__":
    df = get_data("2.2.csv")
    pareto(df, "Producto", "Cantidad")
