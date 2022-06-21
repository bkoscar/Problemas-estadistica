# Este programa obtiene el archivo csv de la carpeta
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter


def get_data(file: str):
    """Esta función lee un archivo csv de la carpeta dataset

    Args:
        file (str): Nombre del archivo que se encuentra en la carpeta dataset

    Returns:
        DataFrame: Archivo en formato DataFrame
    """
    path = "/home/bk17/Documents/Estadística/dataset/" + file
    df = pd.read_csv(path)
    return df


def pareto(df: str, *columnas: str):
    """_Está función recibe el dataframe  y el nombre de las columnas por el cual se realizara el análisis del
    diagrama de Pareto, la función ordena la columna de forma decendente.
    Args:
        df (str): _El dataframe al cual se le aplicara el diagrama de Pareto_
        columnas (str): El nombre de las columnas la cual se ordenara de forma decendente
    """
    df = df.sort_values(by=[columnas[1]], ascending=False)
    df["Porcentaje acumulado"] = df[columnas[1]].cumsum() / df[columnas[1]].sum() * 100
    fig, ax = plt.subplots()
    ax.bar(df[columnas[0]], df[columnas[1]], color="indigo")
    ax2 = ax.twinx()
    ax2.plot(df[columnas[0]], df["Porcentaje acumulado"], marker="D", color="olive")
    ax2.yaxis.set_major_formatter(PercentFormatter())
    plt.title("Diagrama Pareto")
    plt.show()
